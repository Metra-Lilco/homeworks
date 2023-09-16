def parse_cookie(query: str) -> dict:
    cookie_data = {}
    parts = query.split(";")
    for part in parts:
        if "=" in part:
            key, value = part.strip().split("=", 1)
            if value == "":
                continue
            cookie_data[key] = value
    return cookie_data


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
