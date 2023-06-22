import json
import logging
import os

from twk_backend.router import app


def get_int_agent_data():
    data = {}

    tools = []
    with open(os.path.join("tests", "data", "test_datastore.json")) as f:
        tool = {}
        tool["toolType"] = "Datastore"
        tool["toolConfig"] = json.load(f)
        tools.append(tool)

    data["toolList"] = tools
    data["agent"] = {
        "name": "TestAgent",
        "personality": "You speak like a pirate",
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
            "/chatWithAgent", json={"sessionId": "test", "query": "What are the 48 Laws of power?"}
        )
        logging.info(f"{response}")
        assert response.status_code == 200
        assert len(response.text) > 0

