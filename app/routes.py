from flask import render_template
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from app.controllers.user_controller import UserController
from app.schemas import UserCreateSchema, UserUpdateSchema, UserResponseSchema

# Home page blueprint
main_bp = Blueprint(
    'main',
    __name__,
    description='Main pages',
    template_folder='templates'
)

@main_bp.route('/')
def home():
    """Home page"""
    return render_template('home.html')

# API blueprint
api_bp = Blueprint(
    'api', 
    __name__, 
    # url_prefix='/api/v1',
    description='Operations on users'
)

@api_bp.route('/users')
class UserList(MethodView):
    @api_bp.response(200, UserResponseSchema(many=True))
    def get(self):
        """List all users"""
        return UserController.get_users()

    @api_bp.arguments(UserCreateSchema)
    @api_bp.response(201, UserResponseSchema)
    def post(self, user_data):
        """Create a new user"""
        return UserController.create_user(user_data)

@api_bp.route('/users/<user_id>')
class User(MethodView):
    @api_bp.response(200, UserResponseSchema)
    def get(self, user_id):
        """Get a user by ID"""
        user = UserController.get_user(user_id)
        if not user:
            abort(404, message="User not found")
        return user

    @api_bp.arguments(UserUpdateSchema)
    @api_bp.response(200, UserResponseSchema)
    def put(self, user_data, user_id):
        """Update a user"""
        user = UserController.update_user(user_id, user_data)
        if not user:
            abort(404, message="User not found")
        return user

    @api_bp.response(204)
    def delete(self, user_id):
        """Delete a user"""
        if not UserController.delete_user(user_id):
            abort(404, message="User not found")
        return ''