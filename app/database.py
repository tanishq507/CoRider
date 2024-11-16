from pymongo import MongoClient
from app.config import Config

class Database:
    client = None
    db = None

    @classmethod
    def initialize(cls):
        if not cls.client:
            cls.client = MongoClient(Config.MONGO_URI)
            cls.db = cls.client.get_database()
        return cls.db

    @classmethod
    def get_db(cls):
        if not cls.db:
            return cls.initialize()
        return cls.db
