import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_variable(key, default=None):
    value = os.getenv(key, default)
    return value

OPENAI_API_KEY = get_env_variable('OPENAI_API_KEY')
