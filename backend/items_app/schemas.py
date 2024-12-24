from ninja import Schema

class ItemSchema(Schema):
    title : str
    description : str
    price : float
    stock : int
    
class NotFoundSchema(Schema):
    message : str