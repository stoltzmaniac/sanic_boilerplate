import pytest
from my_app import create_app
from my_app.models import User

@pytest.yield_fixture
def app():
    test_app = create_app()
    yield test_app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))


@pytest.fixture
def user():
    user = User(username='scott', email='scott@stoltzmanconsulting.com')
    return user