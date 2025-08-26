import os
import time
import uuid

from fastapi import Request, Response

from app.core.log import setup_logger

middleware_logger = setup_logger(__name__)
IS_DEBUG = os.getenv("LOG_LEVEL", "INFO").upper() == "DEBUG"


async def log_request(request: Request):
    """Log the incoming request details along with request_id."""
    request.state.request_id = str(uuid.uuid4())
    request.state.start_time = time.perf_counter()  # Use a high-resolution timer
    client_ip = request.client.host
    request_data = {
        "log_type": "request",
        "request_id": request.state.request_id,
        "method": request.method,
        "path": request.url.path,
        "query_params": dict(request.query_params),
        "client_ip": client_ip,
    }
    if IS_DEBUG:
        body = await request.body()
        request_data["request_body"] = body.decode("utf-8")
    middleware_logger.info("Request received", extra={"data": request_data})


async def log_response(request: Request, response: Response):
    """Log the outgoing response details along with request_id."""
    response_time_ms = (time.perf_counter() - request.state.start_time) * 1000
    response_data = {
        "log_type": "response",
        "request_id": request.state.request_id,
        "status_code": response.status_code,
        "response_time_ms": response_time_ms,
    }
    if IS_DEBUG:
        pass
        # response_data["response_body"] = (await response.data).decode("utf-8")
    middleware_logger.info("Response sent", extra={"data": response_data})
    return response
