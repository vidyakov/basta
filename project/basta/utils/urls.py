from basta.http import Response


def redirect(path: str) -> Response:
    return Response(status_code=301, headers={'Location': path})
