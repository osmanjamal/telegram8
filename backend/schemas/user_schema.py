from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    telegram_id = fields.Int(required=True)
    username = fields.Str()
    name = fields.Str()
    phone = fields.Str()
    address = fields.Str()