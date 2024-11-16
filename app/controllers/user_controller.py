from bson import ObjectId
from app.services.user_service import UserService

class UserController:
    user_service = UserService()

    @classmethod
    def create_user(cls, user_data):
        try:
            return cls.user_service.create_user(user_data)
        except ValueError as e:
            abort(400, message=str(e))

    @classmethod
    def get_users(cls):
        return cls.user_service.get_users()

    @classmethod
    def get_user(cls, user_id):
        try:
            return cls.user_service.get_user(ObjectId(user_id))
        except ValueError:
            abort(400, message="Invalid user ID")

    @classmethod
    def update_user(cls, user_id, user_data):
        try:
            return cls.user_service.update_user(ObjectId(user_id), user_data)
        except ValueError as e:
            abort(400, message=str(e))

    @classmethod
    def delete_user(cls, user_id):
        try:
            return cls.user_service.delete_user(ObjectId(user_id))
        except ValueError:
            abort(400, message="Invalid user ID")