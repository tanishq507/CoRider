from marshmallow import Schema, fields, validate

class UserBaseSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6), load_only=True)

class UserCreateSchema(UserBaseSchema):
    pass

class UserUpdateSchema(Schema):
    name = fields.Str(validate=validate.Length(min=2, max=100))
    email = fields.Email()
    password = fields.Str(validate=validate.Length(min=6), load_only=True)

class UserResponseSchema(UserBaseSchema):
    id = fields.Str(attribute="_id")
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    
    class Meta:
        exclude = ("password",)