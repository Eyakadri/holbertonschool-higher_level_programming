
def class_to_json(obj):
    serializable_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
    return serializable_dict
