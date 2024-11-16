# Assignment 

A production-ready Flask REST API with MongoDB backend, using Docker for deployment.

## Prerequisites

- Docker and Docker Compose installed on your machine
- Git (optional, for cloning the repository)

## Project Structure
```

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
│   └── user_schema.py
└── tests/
    └── test_user.py
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

## Testing the API with Postman

### Create a User
1. Open Postman.
2. Create a new `POST` request.
3. Set the URL to `http://localhost:3000/users`.
4. In the `Headers` section, add `Content-Type: application/json`.
5. In the `Body` section, select `raw` and enter the JSON data:
   ```json
   {
     "name": "Tanish",
     "email": "tanish@example.com",
     "password": "password123"
   }
   ```
6. Send the request.

### Get All Users
1. Create a new `GET` request.
2. Set the URL to `http://localhost:3000/users`.
3. Send the request.

### Get a Specific User
1. Create a new `GET` request.
2. Set the URL to `http://localhost:3000/users/<user_id>` (replace `<user_id>` with the actual user ID).
3. Send the request.

### Update a User
1. Create a new `PUT` request.
2. Set the URL to `http://localhost:3000/users/<user_id>` (replace `<user_id>` with the actual user ID).
3. In the `Headers` section, add `Content-Type: application/json`.
4. In the `Body` section, select `raw` and enter the JSON data:
   ```json
   {
     "name": "Updated Name"
   }
   ```
5. Send the request.

### Delete a User
1. Create a new `DELETE` request.
2. Set the URL to `http://localhost:3000/users/<user_id>` (replace `<user_id>` with the actual user ID).
3. Send the request.

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





