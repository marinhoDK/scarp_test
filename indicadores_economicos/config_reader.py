import json

class ConfigReader:
    """ Class to read configuration from a JSON file. """
    def __init__(self, filepath):
        self.filepath = filepath

    def read_config(self):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
        return data['pages']
