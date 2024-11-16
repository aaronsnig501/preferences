from sanic import Sanic, json
from sanic.log import logger, LOGGING_CONFIG_DEFAULTS
from sanic.request import Request as SanicRequest
from sanic.response import BaseHTTPResponse as SanicResponse

app = Sanic("nlp")

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
