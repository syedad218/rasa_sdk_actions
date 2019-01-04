from rasa_nlu.model import Interpreter
import json

# where model_directory points to the model folder
interpreter = Interpreter.load('models/nlu/default/current')
while (True):

    a = input("Enter your query: ")
    if a == 'stop':
        break
    result = interpreter.parse(a)
    print(json.dumps(result, indent=2))