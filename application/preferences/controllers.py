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
    """Create preferences

    Store a user's preferences in the database

    Example Usage:
        ```sh
            curl --header "Content-Type: application/json" \
                --request POST \
                --data \
                    '{ \
                        "to_language": "en", \
                        "from_language": "en", \
                        "part_of_speech_tagger": "aws", \
                        "client_id": "d807e048-d118-4331-a8e6-d59cbe62cbd4"\
                    }' http://localhost:8002/api/preferences/create | jq
        ```

    Example Response:
        ```json
        {
            "message": "SUCCESS"
        }
        ```
    """
    await preferences_manager.set_preferences(body)
    return json({"message": "SUCCESS"}, status=200)
