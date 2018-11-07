import pytest
from my_app import create_app

@pytest.yield_fixture
def app():
    test_app = create_app()
    yield test_app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))
