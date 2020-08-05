
import json
import logging
import pytest
import urllib.parse

from server import app

LOG = logging.getLogger(__name__)


@pytest.fixture
def app_client():
    app_client = app.test_client()
    app_client.testing = True
    yield(app_client)


def test_root_endpoint(app_client):
    response = app_client.get('/')
    assert response.status_code == 200
    response.close()


def test_health_endpoint(app_client):
    result = json.loads(app_client.get('/v1/health').data)
    LOG.debug('/v1/health : ' + str(result))
    assert result['status'] == 'UP'