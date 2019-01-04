from rasa_core.policies import KerasPolicy

from rasa_core.policies import MemoizationPolicy, FormPolicy
from rasa_core.agent import Agent
import ruamel
import warnings
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy(), FormPolicy()])
training_data = agent.load_data('data/stories.md')
agent.train(
        training_data,
        validation_split=0.0
)

agent.persist('models/dialogue')
