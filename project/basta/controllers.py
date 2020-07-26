from .utils import get_path


def code_404(request) -> (str, list, bytes):
    return '404 Page not found', [], b'Page not found'


def redirect(path) -> (str, list, bytes):
    return '301 Moved Permanently', [('Location', path)], b''


def redirect_without_slash(request) -> (str, list, bytes):
    new_path = get_path(request) + '/'
    return '301 Moved Permanently', [('Location', new_path)], b''
