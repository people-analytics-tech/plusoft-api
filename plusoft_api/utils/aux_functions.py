def remove_none_fields(data: dict):
        result = {}
        for key, value in data.items():
            if value is not None:
                result[key] = value
        return result
