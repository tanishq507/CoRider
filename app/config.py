import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/admin')
    SECRET_KEY = os.getenv('SECRET_KEY')
    # DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    PORT = 3000
    
    # API Documentation
    API_TITLE = 'User Management API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = ''
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    
    # Swagger UI Configuration
    API_SPEC_OPTIONS = {
        'info': {
            'description': 'A RESTful API for managing users with MongoDB',
        },
        'components': {
            'securitySchemes': {
                'Bearer': {
                    'type': 'http',
                    'scheme': 'bearer',
                    'bearerFormat': 'JWT'
                }
            }
        }
    }