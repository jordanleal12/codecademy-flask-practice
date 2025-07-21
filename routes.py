from flask import Blueprint

bp_routes = Blueprint("bp_routes", __name__)


@bp_routes.route("/")
@bp_routes.route("/home")
def home():
    return "home message"
