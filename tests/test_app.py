from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Basketball Team" in data

def test_signup_and_unregister():
    activity = "Basketball Team"
    email = "testuser@mergington.edu"
    # Ensure not already signed up
    client.delete(f"/activities/{activity}/unregister?email={email}")
    # Sign up
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    assert f"Signed up {email}" in response.json()["message"]
 
    # Duplicate signup should fail
    response2 = client.post(f"/activities/{activity}/signup?email={email}")
    assert response2.status_code == 400

    # # Unregister
    # response3 = client.delete(f"/activities/{activity}/unregister?email={email}")
    # assert response3.status_code == 200
    # assert f"Removed {email}" in response3.json()["message"]

    # Unregister again should fail
    response4 = client.delete(f"/activities/{activity}/unregister?email={email}")
    assert response4.status_code == 404
