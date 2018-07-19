#!/bin/python
# main_obj.py

import json_handler
import utils
from db_parser_obj import DBParser

if __name__ == '__main__':
    db_parser = DBParser('iso.db')
    db_dict = db_parser.get_from_db(('iso2', 'v1', 'v2', 'v3'))
    data = utils.fill_dict(db_dict)
    json_dict = json_handler.get_dict_from_json('worldHigh')
    new_json_dict = utils.replace_id(data, json_dict)
    json_handler.create_json(new_json_dict)
