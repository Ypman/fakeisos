import sqlite3


def get_from_db(db_name, values, table):
    """
    Get a dictionary from the database
    :param db_name: name of the *.db file
    :param values: column names as tuples or list, first element will be the key in the dictionary
    :param table: which table of the database
    :return: dictionary with first column value as key and tuples as value
    """
    raise NotImplemented


def write_to_db_single_row(db_name, table, column_values, row):
    """
    Write something to database in specific row(s)
    :param db_name: name of the *.db file
    :param table: which table of the database
    :param column_values: which columns of the database
    :param row: which row of the database
    """
    raise NotImplemented


def write_to_db(db_name, table, column_values):
    """
    Write something to database in each row
    :param db_name: name of the *.db file
    :param table: which table of the database
    :param column_values: which columns of the database
    """
    raise NotImplemented


def __check_if_exists(db_name, values, table):
    """
    Not sure if this will work
    :param db_name: name of the *.db file
    :param values: which values of the database
    :param table: which table of the database
    :return: if column exists in table return true else false
    """
    cursor = sqlite3.connect(db_name).cursor()
    cursor.execute('SELECT {} FROM {}'.format(values, table))
    if cursor.fetchone() is None:
        return False
    return True
