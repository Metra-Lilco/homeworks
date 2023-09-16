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
    assert parse('https://example.com/?age=22&gender=female') == {'age': '22', 'gender': 'female'}
    assert parse('https://example.com/?age=30&gender=male') == {'age': '30', 'gender': 'male'}
    assert parse('https://example.com/?category=books&genre=fiction') == {'category': 'books', 'genre': 'fiction'}
    assert parse('https://example.com/?name=Andrii&age=25&city=Tokmak') == {'name': 'Andrii', 'age': '25', 'city': 'Tokmak'}
    assert parse('https://example.com/?product=laptop&brand=Apple&price=58000') == {'product': 'laptop', 'brand': 'Apple', 'price': '58000'}
    assert parse('https://example.com/?type=cryptocyrrency&name=waves') == {'type': 'cryptocyrrency', 'name': 'waves'}
    assert parse('https://example.com/?type=NFT&name=boredape') == {'type': 'NFT', 'name': 'boredape'}
    assert parse('https://example.com/?id=12345&size=medium') == {'id': '12345', 'size': 'medium'}
    assert parse('https://example.com/?crypto=BTC&amount=0.05') == {'crypto': 'BTC', 'amount': '0.05'}
    assert parse('https://example.com/?crypto=ETH&price=2500&exchange=Binance') == {'crypto': 'ETH', 'price': '2500', 'exchange': 'Binance'}
