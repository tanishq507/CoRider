from app.database import Database
import bcrypt
from datetime import datetime

class UserService:
    def __init__(self):
        self.db = Database.get_db()
        self.collection = self.db.users

    def _hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def create_user(self, user_data: dict) -> dict:
        # Check if email already exists
        if self.collection.find_one({'email': user_data['email']}):
            raise ValueError('Email already registered')

        user_data['password'] = self._hash_password(user_data['password'])
        user_data['created_at'] = datetime.utcnow()
        user_data['updated_at'] = datetime.utcnow()

        result = self.collection.insert_one(user_data)
        return self.get_user(result.inserted_id)

    def get_users(self) -> list:
        users = list(self.collection.find())
        for user in users:
            user['_id'] = str(user['_id'])
        return users

    def get_user(self, user_id: str) -> dict:
        user = self.collection.find_one({'_id': user_id})
        if user:
            user['_id'] = str(user['_id'])
        return user

    def update_user(self, user_id: str, user_data: dict) -> dict:
        if 'password' in user_data:
            user_data['password'] = self._hash_password(user_data['password'])
        
        user_data['updated_at'] = datetime.utcnow()

        result = self.collection.update_one(
            {'_id': user_id},
            {'$set': user_data}
        )

        if result.modified_count:
            return self.get_user(user_id)
        return None

    def delete_user(self, user_id: str) -> bool:
        result = self.collection.delete_one({'_id': user_id})
        return result.deleted_count > 0