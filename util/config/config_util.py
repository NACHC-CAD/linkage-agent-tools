import util.file.file_util as fu
import json


def get_config(file_name):
    file_name = fu.get_file_name(file_name)
    print("Getting config from:")
    print(file_name)
    with open(file_name) as file:
        config = json.load(file)
    print(pretty_print(config))


def pretty_print(json_obj):
    return json.dumps(json_obj, indent=2, sort_keys=False)

