from marshmallow import Schema, fields

class OrderItemSchema(Schema):
    id = fields.Int(dump_only=True)
    menu_item_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    status = fields.Str()
    total = fields.Float()
    created_at = fields.DateTime(dump_only=True)
    items = fields.Nested(OrderItemSchema, many=True)