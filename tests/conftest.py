import pytest

from app import create_app
from app_extensions import db as _db
from models.models import Address, Parent, Child


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()


@pytest.fixture(scope='session')
def db(app):
    """
    Setup our database, this only gets executed once per session.

    :param app: Pytest fixture
    :return: database session
    """

    Parent.drop_collection()
    Child.drop_collection()

    return _db


@pytest.fixture(scope='function')
def users(db):
    """
    Create user fixtures. They reset per test.

    :param db: Pytest fixture
    :return: database session
    """

    Parent.drop_collection()
    Child.drop_collection()

    address = Address(street='440 Sundown Lane', city='Austin', state='Texas', zip='78701')
    parent_john = Parent(first_name='John', last_name='Doe')
    parent_john.address = address
    parent_john.save()

    parent_sarah = Parent(first_name='Sarah', last_name='Smith')
    parent_sarah.address = address
    parent_sarah.save()

    child_one = Child(first_name='1st', last_name='Child')
    child_one.parent = parent_john
    child_one.save()

    child_two = Child(first_name='2nd', last_name='Child')
    child_two.parent = parent_sarah
    child_two.save()

    return db
