# Assignment

A production-ready Flask REST API with MongoDB backend, using Docker for deployment.

## Prerequisites

- Docker and Docker Compose installed on your machine
- Git (optional, for cloning the repository)

## Project Structure
```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
├── config.py
├── database.py
├── routes.py
├── models/
│   └── user.py
├── resources/
│   └── user.py
├── schemas/
   └── user_schema.py

```

## Setup Instructions

1. Clone the repository (if using Git):
   ```bash
   git clone <https://github.com/tanishq507/CoRider.git>
   cd <Project>
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

The API will be available at `http://localhost:5000`

## API Endpoints

### Users Resource
- `GET /users` - Retrieve all users
- `POST /users` - Create a new user
- `GET /users/<id>` - Retrieve a specific user
- `PUT /users/<id>` - Update a specific user
- `DELETE /users/<id>` - Delete a specific user

## Testing the API

### Create a User
```bash
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tanish123",
    "email": "tanish@example.com",
    "password": "password123"
  }'
```

### Get All Users
```bash
curl http://localhost:3000/users
```

### Get a Specific User
```bash
curl http://localhost:3000/users/<user_id>
```

### Update a User
```bash
curl -X PUT http://localhost:3000/users/<user_id> \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Name"
  }'
```

### Delete a User
```bash
curl -X DELETE http://localhost:3000/users/<user_id>
```

## Running Tests
```bash
docker-compose exec api pytest
```

## Features Implemented
- ✅ Full CRUD operations for User resource
- ✅ MongoDB integration with Flask-MongoEngine
- ✅ RESTful API design
- ✅ Input validation using Marshmallow
- ✅ Docker containerization
- ✅ Environment variable configuration
- ✅ Modular project structure
- ✅ Unit tests with pytest
- ✅ Production-ready configuration

## Security Features
- Password hashing (implemented in User model)
- Input validation and sanitization
- Environment variable configuration
- Secure MongoDB connection

## Production Considerations
- Use proper secret management for production
- Implement rate limiting
- Add authentication middleware
- Set up proper logging
- Configure CORS if needed
- Use HTTPS in production
