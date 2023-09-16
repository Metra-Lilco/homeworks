def parse(query: str) -> dict:
    query_params = {}
    parts = query.split("?")
    if len(parts) > 1:
        params = parts[1].split("&")
        for param in params:
            key_value = param.split("=")
            if len(key_value) == 2:
                key, value = key_value
                query_params[key] = value
    return query_params


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    