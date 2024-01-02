# import json

class ResponseDTO:
    def __init__(self, message = 'success', data = None) -> None:
        self.message = message
        self.data = data
        
    def __str__(self) -> str:
        return self.data
    
    def to_dict(self) -> dict:
        return {"message": self.message, "data": self.data}
    
    # def to_json_str(self) -> str:
    #     return json.dumps(self.to_dict())