from ninja import NinjaAPI
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from items_app.controllers.user_controller import UserController
from typing import List,Optional
from items_app.models import Item
from items_app.schemas import ItemSchema,NotFoundSchema
from ninja_jwt.authentication import JWTAuth

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)

api.register_controllers(UserController)

@api.get("/books", response=List[ItemSchema], auth=JWTAuth())
def books(request, title: Optional[str] = None):
    """
    Retrieve books. Accessible only to authenticated users.
    """
    if title:
        return Item.objects.filter(title__icontains=title)
    return Item.objects.all()


@api.get("/books/{book_id}", response={200: ItemSchema, 404: NotFoundSchema}, auth=JWTAuth())
def get_by_id(request, book_id: int):
    """
    Retrieve a book by ID. Accessible only to authenticated users.
    """
    try:
        book = Item.objects.get(pk=book_id)
        return book
    except Item.DoesNotExist:
        return 404, {"message": "Book not found"}


@api.post("/books", response={201: ItemSchema}, auth=JWTAuth())
def create_book(request, book: ItemSchema):
    """
    Create a new book. Accessible only to authenticated users.
    """
    book = Item.objects.create(**book.dict())
    return book


@api.put("/books/{book_id}", response={200: ItemSchema, 404: NotFoundSchema}, auth=JWTAuth())
def change_book(request, book_id: int, data: ItemSchema):
    """
    Update a book by ID. Accessible only to authenticated users.
    """
    try:
        book = Item.objects.get(pk=book_id)
        for attribute, value in data.dict().items():
            setattr(book, attribute, value)
        book.save()
        return 200, book
    except Item.DoesNotExist:
        return 404, {"message": "Book not found"}


@api.delete("/books/{book_id}", response={200: ItemSchema, 404: NotFoundSchema}, auth=JWTAuth())
def delete_book(request, book_id: int):
    """
    Delete a book by ID. Accessible only to authenticated users.
    """
    try:
        book = Item.objects.get(pk=book_id)
        book.delete()
        return 200
    except Item.DoesNotExist:
        return 404, {"message": "Book not found"}