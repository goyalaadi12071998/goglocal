def validate_request_data(payload):
    if payload.get("content") is None:
        raise Exception("Data Validation Error")