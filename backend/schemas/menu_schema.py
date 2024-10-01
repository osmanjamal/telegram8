from marshmallow import Schema, fields

class MenuItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    image_url = fields.Str()
    category = fields.Str()