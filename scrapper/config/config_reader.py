import json


class ConfigReader:
    def __init__(self):
        self.filepath = 'scrapper/config/scrapping.cfg'
        self.config = {}

    def load_config(self):
        with open(self.filepath) as f:
            self.config = json.load(f)

    def get(self, key, default=None):
        if not key:
            raise Exception(f"Invalid key: {key}")
        return self.config.get(key, default)
