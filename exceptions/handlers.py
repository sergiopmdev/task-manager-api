from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse


def exception_409_handler(request: Request, exception: HTTPException) -> JSONResponse:
    """
    Handle conflict errors with 409
    code by specifying the URL and
    the error message generated

    Parameters
    ----------
    request : Request
        Details of the request
    exception : HTTPException
        Details of the exception

    Returns
    -------
    JSONResponse
        Object which contains the
        details of the conflict error
    """

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"url": request.url.path, "message": exception.detail},
    )
