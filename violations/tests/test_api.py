import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_violation():
    client = APIClient()
    payload = {
        "license_plate": "TS09XY1234",
        "violation_type": "no_helmet",
        "violation_image_url": "https://cdn-icons-png.flaticon.com/512/61/61088.png",
        "violation_datetime": "2025-07-22T12:00:00Z",
        "location": "Hyderabad"
    }
    response = client.post("/violations/ingest/", payload, format='json')
    assert response.status_code == 201
