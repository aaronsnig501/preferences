from sanic import Blueprint, json
from sanic.request import Request as SanicRequest
from sanic.response import BaseHTTPResponse as SanicResponse
from sanic_ext import validate

from .manager import PreferencesManager
from .validators import PreferencesRequestBody

bp = Blueprint("preferences", url_prefix="/api/preferences")



@bp.post("/create")
@validate(json=PreferencesRequestBody)
async def create_preferences(
    _: SanicRequest,
    body: PreferencesRequestBody,
    preferences_manager: PreferencesManager
) -> SanicResponse:
    await preferences_manager.set_preferences(body)
    return json({"message": "SUCCESS"}, status=200)
