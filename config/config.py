import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        self.model_name = os.getenv("MODEL_NAME", "mistral:latest")
        self.model_temperature = float(os.getenv("MODEL_TEMPERATURE", "0.7"))
