import json
from models.SessionData.SessionData import SessionData

class SessionDataHandler:
    def __init__(self):
        self._file_path = "./result/session_data.json"

    def read_data(self):
        with open(self._file_path, "r") as json_file:
            data = json.loads(json_file.read())

            return data
        
    def write_data(self, data: SessionData):
        with open(self._file_path, "w") as json_file:
            json.dumps(data.toJSON(), json_file)
        