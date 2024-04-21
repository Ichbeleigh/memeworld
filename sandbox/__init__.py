from flask import Blueprint

blueprint = Blueprint(
    'sandbox_blueprint',
    __name__,
    url_prefix=''
)