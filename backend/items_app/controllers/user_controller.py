from django.contrib.auth.models import User
from ninja_extra import api_controller, http_post
from items_app.schemas import RegisterSchema  # Import your schema

@api_controller
class UserController:
    @http_post('/register')
    def register_user(self, data: RegisterSchema):
        if User.objects.filter(username=data.username).exists():
            return {"message": "Username already exists"}
        User.objects.create_user(username=data.username, password=data.password)
        return {"message": "User registered successfully"}