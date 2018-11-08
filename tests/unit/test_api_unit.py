async def test_models_user(user):
    """
    GIVEN a User object
    WHEN a new User is created
    THEN check the user has all fields
    """
    assert user.username == 'scott'
    assert user.email == 'scott@stoltzmanconsulting.com'
