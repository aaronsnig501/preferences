from dataclasses import asdict
from sanic import Blueprint
from sanic.request import Request as SanicRequest
from sanic.response import json, BaseHTTPResponse as SanicResponse

from application.ping.entities import HealthStatusResponse
from application.ping.managers import PingManager

bp = Blueprint("ping", url_prefix="/api")


@bp.get("/ping")
async def ping(_: SanicRequest, ping_manager: PingManager) -> SanicResponse:
    """Ping

    Ping endpoint to check the health of the application

    Example Usage:
        ```sh
        curl http://127.0.0.1:8000/api/ping | jq
        ```

    Example Response:
        ```json
        {
            "is_healthy": true,
            "status": [
                {
                    "name": "application",
                    "is_healthy": true
                }
            ]
        }
        ```
    """
    health_checks = await ping_manager.get_health_status()
    is_healthy = all([health_check.is_healthy for health_check in health_checks])
    status = 200 if is_healthy else 500
    return json(
        asdict(HealthStatusResponse(is_healthy, health_checks)), status=status
    )
