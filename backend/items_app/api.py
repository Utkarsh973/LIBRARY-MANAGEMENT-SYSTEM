from ninja import NinjaAPI
from typing import List,Optional
from items_app.models import Item
from items_app.schemas import ItemSchema,NotFoundSchema

api = NinjaAPI()

@api.get("/books", response = List[ItemSchema])
def books(request, title : Optional[str] = None):
    if title:
        return Item.objects.filter(title__icontains = title)
    return Item.objects.all()

@api.get("/books/{book_id}", response={200: ItemSchema, 404: NotFoundSchema})
def get_by_id(request, book_id : int):
    try:
        book = Item.objects.get(pk = book_id)
        return book
    except Item.DoesNotExist as e:
        return 404, {"message" : "FUCK OFF"}
    
@api.post("/books", response={201: ItemSchema})
def create_book(request, book : ItemSchema):
    book = Item.objects.create(**book.dict())
    return book

@api.put("/books/{book_id}", response={200: ItemSchema, 404: NotFoundSchema})
def change_book(request, book_id : int, data : ItemSchema):
    try:
        book = Item.objects.get(pk = book_id)
        for attribute,value in data.dict().items():
            setattr(book,attribute,value)
        book.save()
        return 200, book
    except Item.DoesNotExist as e:
        return 404, {"message" : "FUCK OFF"}
    
@api.delete("/books/{book_id}", response={200: ItemSchema, 404: NotFoundSchema})
def delete_book(request, book_id : int, ):
    try:
        book = Item.objects.get(pk = book_id)
        book.delete()
        return 200, 
    except Item.DoesNotExist as e:
        return 404, {"message" : "FUCK OFF"}