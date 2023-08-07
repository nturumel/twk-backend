import json
import logging
import os

from twk_backend.router import app


def get_int_agent_data():
    data = {}

    tools = []
    with open(os.path.join("tests", "data", "test_datastore.json")) as f:
        tool = {}
        tool["toolType"] = "datastore"
        tool["toolConfig"] = json.load(f)
        tools.append(tool)

    data["toolList"] = tools
    data["agent"] = {
        "name": "TestAgent",
        "writingStyle": "You speak like a pirate",
        "description": "You are a test agent",
        "temperature": 0,
    }
    data["sessionId"] = "test"

    return data


def test_handle_init_and_chat_with_agent():
    data = get_int_agent_data()
    with app.test_client() as client:
        response = client.post("/initialiseAgent", json=data)
        assert response._status_code == 200

        response = client.post(
            "/chatWithAgent", json={"sessionId": "test", "query": "Hi"}
        )

        logging.info(f"{response}")
        assert response.status_code == 200
        assert len(response.text) > 0

        response = client.post(
            "/chatWithAgent",
            json={"sessionId": "test", "query": "What are the 48 Laws of power?"},
        )
        logging.info(f"{response}")
        assert response.status_code == 200
        assert len(response.text) > 0


def test_handle_initialize_samples():
    with app.test_client() as client:
        data = {"sessionId": "sample_test", "samples": ["example1", "example2"]}
        response = client.post("/initialiseSamples", json=data)
        assert response.status_code == 200


def test_handle_refine_response_with_samples():
    with app.test_client() as client:
        # First, initialise some samples
        samples = [
            {"prompt": "happy", "response": "sad"},
            {"prompt": "tall", "response": "short"}
        ]
        data = {"sessionId": "refine_test", "samples": samples}
        client.post("/initialiseSamples", json=data)

        # Now, refine a response
        refine_data = {
            "sessionId": "refine_test",
            "query": "Hello?",
            "response": "Hi there!",
        }
        response = client.post("/refineAnswer", json=refine_data)

        assert response.status_code == 200
        assert "response" in response.get_json()
