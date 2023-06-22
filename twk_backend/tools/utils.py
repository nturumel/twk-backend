import logging
from typing import Dict

from langchain.tools import Tool

from twk_backend.tools.calculator_tool import get_calculator_tool
from twk_backend.tools.datastore_query.datastore_query_tool import \
    get_datastore_query_tool


def get_tool(tool_type: str, tool_config: Dict) -> Tool:
    match tool_type:
        case "Calculator":
            return get_calculator_tool()
        case "Datastore":
            datastore_id: str = tool_config["id"]
            datastore_name: str = tool_config["name"]
            datastore_description: str = tool_config.get("description")

            return get_datastore_query_tool(
                datastore_id=datastore_id,
                datastore_name=datastore_name,
                datastore_description=datastore_description
            )
        case _:
            logging.error("Incorrect Data Type")
            raise Exception("Incorrect Data Type")

