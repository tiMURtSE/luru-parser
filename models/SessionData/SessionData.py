import json

class SessionData:
    def __init__(self, queue, visited):
        self.queue = queue
        self.visited = visited

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                          sort_keys=True, indent=4)
    