from dataclasses import asdict
from sanic import Sanic, json
from sanic.log import logger, LOGGING_CONFIG_DEFAULTS
from sanic.request import Request as SanicRequest
from sanic.response import BaseHTTPResponse as SanicResponse
from tortoise.contrib.sanic import register_tortoise

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


@app.middleware("request")
async def callback_request(request: SanicRequest) -> None:
    logger.info(f"Request {request.path} received")


@app.middleware("response")
async def callback_response(request: SanicRequest, response: SanicResponse) -> None:
    logger.info(f"Request {request.path} processing finished")


@app.get("/")
async def hello(request):
    return json({"hello": "world"})


register_tortoise(
    app,
    db_url=app.config["database"]["uri"],
    modules={"models": ["application.preferences.models"]},
    generate_schemas=True
)
