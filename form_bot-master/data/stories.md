## greet
* greet
    - utter_greet

## chitchat
* chitchat
    - utter_chitchat

## inform
* inform
    - crop_form
    - form{"name": "crop_form"}
    - form{"name": null}
    - utter_slots_values

## basf
* basf
    - action_slot_reset
    - crop_form
    - form{"name": "crop_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## Generated Story -701185228439142841
* basf{"product": "cantus gold"}
    - action_slot_reset
    - slot{"crop": null}
    - slot{"product": "cantus gold"}
    - slot{"requested_slot": null}
    - crop_form
    - form{"name": "crop_form"}
    - slot{"requested_slot": "crop"}
* form: inform{"crop": "sonnenblume"}
    - form: crop_form
    - slot{"crop": "sonnenblume"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* thankyou
    - utter_noworries
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story 7903736422402982991
* inform{"crop": "sonnenblume"}
    - crop_form
    - form{"name": "crop_form"}
    - slot{"crop": "sonnenblume"}
    - slot{"requested_slot": "product"}
* form: inform{"product": "cantus gold"}
    - form: crop_form
    - slot{"product": "cantus gold"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values

## Generated Story -4072494660485396973
* basf{"product": "aqua stomp"}
    - action_slot_reset
    - slot{"crop": null}
    - slot{"product": "aqua stomp"}
    - slot{"requested_slot": null}
    - crop_form
    - form{"name": "crop_form"}
    - slot{"requested_slot": "crop"}
* chitchat
    - utter_chitchat
    - utter_ask_continue
* affirm
    - crop_form
    - slot{"requested_slot": "crop"}
* form: inform{"crop": "sonenblume"}
    - form: crop_form
    - slot{"crop": null}
    - slot{"requested_slot": "crop"}
* form: inform{"crop": "sonnenblume"}
    - form: crop_form
    - slot{"crop": "sonnenblume"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values

## Generated Story -9030762538833806982
* inform{"crop": "winteraps"}
    - crop_form
    - form{"name": "crop_form"}
    - slot{"crop": null}
    - slot{"requested_slot": "crop"}
* form: inform{"crop": "winterraps"}
    - form: crop_form
    - slot{"crop": "winterraps"}
    - slot{"requested_slot": "product"}
* form: inform{"product": "cantus gold"}
    - form: crop_form
    - slot{"product": "cantus gold"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values

## Generated Story -7929791597230644943
* basf{"product": "aqua stomp"}
    - action_slot_reset
    - slot{"crop": null}
    - slot{"product": "aqua stomp"}
    - slot{"requested_slot": null}
    - crop_form
    - form{"name": "crop_form"}
    - slot{"requested_slot": "crop"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_slot_reset
    - slot{"crop": null}
    - slot{"product": null}
    - slot{"requested_slot": null}

## Generated Story -3793150912093116303
* basf{"product": "aqua stomp", "crop": "sonnenblume"}
    - action_slot_reset
    - slot{"crop": "sonnenblume"}
    - slot{"product": "aqua stomp"}
    - slot{"requested_slot": null}
    - crop_form
    - form{"name": "crop_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values

## Generated Story 5128718506720935769
* inform{"crop": "sonneblume"}
    - crop_form
    - form{"name": "crop_form"}
    - slot{"crop": null}
    - slot{"requested_slot": "crop"}
* chitchat
    - utter_chitchat
    - utter_ask_continue
* affirm
    - crop_form
    - slot{"requested_slot": "crop"}
* form: inform{"crop": "winterraps"}
    - form: crop_form
    - slot{"crop": "winterraps"}
    - slot{"requested_slot": "product"}
* form: inform{"product": "cantus gold"}
    - form: crop_form
    - slot{"product": "cantus gold"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values

