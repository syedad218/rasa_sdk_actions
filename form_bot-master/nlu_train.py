from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer

training_data = load_data('data/nlu_data.md')
trainer = Trainer(config.load('nlu_tensorflow.yml'))
interpreter = trainer.train(training_data)
model_directory = trainer.persist('models/nlu', fixed_model_name="current")

print(model_directory)