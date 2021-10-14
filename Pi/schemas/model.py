from marshmallow import Schema, fields


class Error(Schema):
    code = fields.Int(required=True,)
    message = fields.String(required=True,)


class User(Schema):
    id = fields.Int(required=True,)
    name = fields.String(required=True,)
    tag = fields.String()
