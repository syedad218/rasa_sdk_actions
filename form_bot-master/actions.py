# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core.events import AllSlotsReset
from rasa_core_sdk import Action

class AllSlotsReset(Action):
    def name(self):
        return "action_slot_reset"

    def run(self, dispatcher, tracker, domain):
        return_slots = []
        items = ["aqua stomp","cantus gold","winterraps","artichoke","sonnenblume"]
        # entities = traker.get_latest_entity_values()
        # print("Entites extracted from sentence: ")
        # print(entities)
        for slot in tracker.slots:
            value = next(tracker.get_latest_entity_values(slot), None)
            if (value in items):
                return_slots.append(SlotSet(slot, value))
            else:
                return_slots.append(SlotSet(slot, None))

        return return_slots


class CropForm(FormAction):
    """Example of a custom form action"""
    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""
        return "crop_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["crop", "product"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
    	
        return {"crop": self.from_entity(entity="crop",
                                            intent=["basf", "inform"]),
                "product": self.from_entity(entity="product",
                                                intent=["basf","inform"])}

    @staticmethod
    def cuisine_db():
        # type: () -> List[Text]
        """Database of supported products and crops"""
        return ["aqua stomp",
                "cantus gold",
                "winterraps",
                "artichoke",
                "sonnenblume"]

    # @staticmethod
    # def is_int(string: Text) -> bool:
    #     """Check if a string is an integer"""
    #     try:
    #         int(string)
    #         return True
    #     except ValueError:
    #         return False

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'crop' or slot == 'product':
                if value.lower() not in self.cuisine_db():
                    dispatcher.utter_template('utter_wrong_cuisine', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            # elif slot == 'num_people':
            #     if not self.is_int(value) or int(value) <= 0:
            #         dispatcher.utter_template('utter_wrong_num_people',
            #                                   tracker)
            #         # validation failed, set slot to None
            #         slot_values[slot] = None

            # elif slot == 'outdoor_seating':
            #     if isinstance(value, str):
            #         if 'out' in value:
            #             # convert "out..." to True
            #             slot_values[slot] = True
            #         elif 'in' in value:
            #             # convert "in..." to False
            #             slot_values[slot] = False
            #         else:
            #             dispatcher.utter_template('utter_wrong_outdoor_seating',
            #                                       tracker)
            #             # validation failed, set slot to None
            #             slot_values[slot] = None

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []
