def convert_entities_to_string(data):
    result = ""
    for key, value in data.items():
        result += f"{key}: {value}\n"
    return result.strip()
