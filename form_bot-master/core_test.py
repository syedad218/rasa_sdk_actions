from rasa_core.agent import Agent
import warnings
import ruamel
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

agent = Agent.load('models/dialogue', interpreter='models/nlu/default/current',
action_endpoint='endpoints.yml')

import logging, io, json, warnings
logging.basicConfig(level="INFO")
warnings.filterwarnings('ignore')

print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_text(a)
    for response in responses:
        print(response["text"])