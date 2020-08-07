def _make_dict_from_query(query: str) -> dict:
    return dict(map(lambda elem: elem.split('='), query.split('&')))


def get_data_from_query_string(request) -> dict:
    if data := request.query_string:
        return _make_dict_from_query(data)
    return {}


def get_post_data(request) -> dict:
    if data := request.form:
        return _make_dict_from_query(data)
    return {}
