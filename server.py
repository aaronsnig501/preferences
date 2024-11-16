from dataclasses import asdict
from sanic import Sanic
from sanic.log import logger, LOGGING_CONFIG_DEFAULTS
from sanic.request import Request as SanicRequest
from sanic.response import BaseHTTPResponse as SanicResponse
from tortoise.contrib.sanic import register_tortoise

from application.ping.controllers import bp as ping_blueprint

from application.ping.managers import PingManager
from config.loader import load_config

app = Sanic("nlp")
config = load_config()
app.config.update(asdict(config))

LOGGING_CONFIG_DEFAULTS["formatters"] = {
    "generic": {
        "class": "sanic.logging.formatter.JSONFormatter"
    },
    "access": {
        "class": "sanic.logging.formatter.JSONFormatter"
    }
}

app.config.FALLBACK_ERROR_FORMAT = "json"

app.blueprint(ping_blueprint)
app.ext.dependency(PingManager())


@app.middleware("request")
async def callback_request(request: SanicRequest) -> None:
    logger.info(f"Request {request.path} received")


@app.middleware("response")
async def callback_response(request: SanicRequest, _: SanicResponse) -> None:
    logger.info(f"Request {request.path} processing finished")


register_tortoise(
    app,
    db_url=app.config["database"]["uri"],
    modules={
        "models": [
            "application.ping.models",
            "application.preferences.models",
        ]
    },
    generate_schemas=False
)
