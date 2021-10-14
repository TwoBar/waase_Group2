from flask import Blueprint, request
from webargs.flaskparser import parser
from marshmallow import Schema, fields
from ..schemas import model
from .. import impl

bp = Blueprint('user', __name__)


@bp.route('/user', methods=['get'])
def ListUser():

    options = {}
    options["id"] = request.args.get("id")

    return impl.user.ListUser(options)
