import os
import pytest
import hopsapp.routes
import hopsapp.models
import tempfile
import unittest

@pytest.fixture
def app(request):

    db_fd, temp_db_location = tempfile.mkstemp()
    config = {
        'DATABASE': temp_db_location,
        'TESTING': True,
        'DB_FD': db_fd
    }

    app = create_app(config=config)

    with app.app_context():
        init_db()
        yield app


@pytest.fixture
def client(request, app):

    client = app.test_client()

    def teardown():
        os.close(app.config['DB_FD'])
        os.unlink(app.config['DATABASE'])
    request.addfinalizer(teardown)

    return client



