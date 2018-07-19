import json


def get_dict_from_json(json_file):
    """
    Opens given json file and parse it as dictionary
    :param json_file: filename of *.json in json folder
    :return: json as dictionary
    """
    with open("json/{}.json".format(json_file)) as file:
        data = json.load(file)
        file.close()
    return data


def create_json(big_dict: dict):
    """
    Dumps given dictionary to output/out.json
    :param big_dict: the huge dictionary
    """
    with open('output/out.json', 'w') as file:
        file.write(json.dumps(big_dict))
        file.close()
