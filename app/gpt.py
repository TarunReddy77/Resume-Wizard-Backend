from openai import OpenAI

import os
import yaml
from dotenv import load_dotenv

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the config.yaml file
config_path = os.path.join(current_dir, 'config.yaml')

# Load the config.yaml file
with open(config_path) as f:
    config = yaml.safe_load(f)

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()
model = config['model']


def get_content(prompt, job_desc, response_format):
    return client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": job_desc},
        ],
        response_format=response_format
    ).choices[0].message.parsed
