import sqlite3


class DBParser:
    def __init__(self, db_name, table='ISO'):
        self.sqlite_cursor = sqlite3.connect(db_name).cursor()
        self.table = table

    def get_from_db(self, values):
        v = ', '
        self.sqlite_cursor.execute('SELECT {0} from {1}'.format(v.join(values), self.table))

        data = {}
        for row in self.sqlite_cursor:
            if row[0] in data:
                zip(row[1:], data[row[0]])
            else:
                data[row[0]] = row[1:]

        return data

    def write_to_to_single_row(self, column_values, row):
        self.sqlite_cursor.execute('UPDATE {0} SET {1} WHERE {2}'.format(self.table, column_values, row))

    def write_to_db(self, column_values):
        self.sqlite_cursor.execute('UPDATE {0} SET {1}'.format(self.table, column_values))
