def fill_dict(country_dict: dict):
    help_dict = {
        (0, 0, 0): "c1",
        (0, 0, 1): "c2",
        (0, 1, 0): "c3",
        (0, 1, 1): "c4",
        (1, 0, 0): "c5",
        (1, 0, 1): "c6",
        (1, 1, 0): "c7",
        (1, 1, 1): "c8"
    }

    data = {}
    for country in country_dict:
        data[country] = country + help_dict.get(country_dict.get(country))

    # or maybe as single line for loop:
    # data_dict = {country: country + help_dict.get(country_dict.get(country)) for country in country_dict}
    # data_dict = {country: country + help_dict[country_dict[country]] for country in country_dict}

    id_list = []
    for country_id in country_dict:
        id_list.append(data.get(country_id))

    # I like single line for loops
    # id_list = [data.get(country_id) for country_id in country_dict]

    return data


def replace_id(db_dict: dict, json_dict: dict):
    g_path = json_dict['svg']['g']['path']

    for i in range(len(g_path)):
        if g_path[i]['id'] in db_dict:
            json_dict['svg']['g']['path'][i]['id'] = db_dict[g_path[i]['id']]

    return json_dict
