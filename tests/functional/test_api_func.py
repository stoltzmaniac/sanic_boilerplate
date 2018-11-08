async def test_index_pages(test_cli):
    """
    GIVEN a Sanic application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    resp = await test_cli.get('/')
    assert resp.status == 200

    resp = await test_cli.get('/api')
    assert resp.status == 200

    resp = await test_cli.get('/users')
    assert resp.status == 200


async def test_json_pages(test_cli):
    """
    GIVEN a Sanic application
    WHEN the '/___/json' page is requested (GET)
    THEN check the response is valid
    """
    resp = await test_cli.get('/api/json')
    assert resp.status == 200

    resp = await test_cli.get('/users/json')
    assert resp.status == 200


async def test_text_pages(test_cli):
    """
    GIVEN a Sanic application
    WHEN the '/___/text' page is requested (GET)
    THEN check the response is valid
    """
    resp = await test_cli.get('/api/text')
    assert resp.status == 200

    resp = await test_cli.get('/users/text')
    assert resp.status == 200