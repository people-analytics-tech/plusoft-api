# This module contains auxiliary functions to use in library


def remove_none_fields(data: dict) -> dict:
    """Remove keys with none values from dictionary

    Args:
        data (dict, mandatory): Dictionary with data to filter

    return: dictionary with filtred data
    """
    result = {}
    for key, value in data.items():
        if value is not None:
            if isinstance(
                value, dict
            ):  # If value is dict, use recursive call to iterate all data
                result[key] = remove_none_fields(data=value)

            result[key] = value

    return result
