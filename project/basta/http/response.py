from basta.config import ENCODING
from .common import CODES


class Response:
    def __init__(self, body: str = '', status_code: int = 200, headers=None):
        self._body = body
        self.status_code = status_code
        self._headers = headers if headers else {}

    @property
    def headers(self) -> [(), ]:
        return [(key, value) for key, value in self._headers.items()]

    @property
    def body(self) -> (bytes, ):
        return self._body.encode(ENCODING),

    @property
    def status(self) -> str:
        return CODES.get(self.status_code)

    def add_headers(self, new_headers: dict) -> None:
        self._headers.update(new_headers)
