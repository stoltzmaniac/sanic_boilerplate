async def test_index_page(test_cli):
    """
    GIVEN a Sanic application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    resp = await test_cli.get('/')
    assert resp.status == 200
