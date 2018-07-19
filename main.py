#!/bin/python
# main.py

import db_parser
import json_handler
import utils

if __name__ == '__main__':
    db_dict = db_parser.get_from_db('iso.db', ('iso2', 'v1', 'v2', 'v3'), 'ISO')
    data = utils.fill_dict(db_dict)
    json_dict = json_handler.get_dict_from_json('worldHigh')
    new_json_dict = utils.replace_id(data, json_dict)
    json_handler.create_json(new_json_dict)
