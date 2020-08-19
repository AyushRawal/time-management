import sqlite3
import kronos


class DatabaseFacade:
    rows_in_table = 0
    table_name = "time_management"
    schema = {
        "id": "id",
        "date": "date",
        "note": "note",
        "complete_in_days": "complete_in_days",
        "is_complete": "is_complete",
    }

    def __init__(self, name=":memory:"):
        try:
            self.database_name = name
            self.connection = sqlite3.connect(self.database_name)
            self.cursor = self.connection.cursor()
            self.create_table()
            self.rows_in_table = self.count_rows()
        except ValueError:
            print("Unable to initialize or read from database")

    def create_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS {}
                            ({} int, {} text, {} text, {} text, {} text)""".format(
                self.table_name, *self.schema
            )
        )
        self.connection.commit()

    def update_table_with_note(self, note):
        self.rows_in_table = self.rows_in_table + 1
        self.cursor.execute(
            "INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(
                self.table_name, *self.schema
            ),
            (self.rows_in_table, kronos.get_date_time_as_string(), note, "NA", "NA"),
        )
        self.connection.commit()

    def count_rows(self):
        return len(
            self.cursor.execute("SELECT * FROM {}".format(self.table_name)).fetchall()
        )

    def update_table_with_task(self, note, completion_goal):
        self.rows_in_table = self.rows_in_table + 1
        self.cursor.execute(
            "INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(
                self.table_name, *self.schema
            ),
            (
                self.rows_in_table,
                kronos.get_date_time_as_string(),
                note,
                completion_goal,
                "false",
            ),
        )
        self.connection.commit()

    def update_completion(self, row_id):
        self.cursor.execute(
            f"UPDATE {self.table_name} SET {self.schema['is_complete']} = 'true' WHERE id = {row_id}"
        )
        self.connection.commit()

    def get_all_items(self):
        rows = []
        for row in self.cursor.execute("SELECT * FROM {}".format(self.table_name)):
            item = self.__format_row(row)
            rows.append(item)
        return rows

    def get_all_ids(self):
        ids = []
        for id in self.cursor.execute("SELECT id FROM {}".format(self.table_name)):
            ids.append(id[0])
        return ids

    def get_overdue_items(self):
        rows = []
        for row in self.cursor.execute("SELECT * FROM {}".format(self.table_name)):
            if row[3] != "NA" and row[4] == "false":
                if kronos.is_overdue(row[1], row[3]):
                    item = self.__format_row(row)
                    rows.append(item)
        return rows

    def get_last_days_items(self):
        rows = []
        for row in self.cursor.execute("SELECT * FROM {}".format(self.table_name)):
            if kronos.get_day_of_week(kronos.get_date_time()) == "Monday":
                if kronos.is_previous_friday(row[1]):
                    item = self.__format_row(row)
                    rows.append(item)
            if kronos.is_yesterday(row[1]):
                item = self.__format_row(row)
                rows.append(item)
        return rows

    def __format_row(self, row):
        item_no = row[0]
        date = row[1]
        note = row[2]
        days_to_complete = row[3]
        is_complete = row[4]
        record_type = "Task"
        if days_to_complete == "NA":
            record_type = "Note"
        return f"Item No: {item_no}, Date: {date}, {record_type}: {note}, Days to complete: {days_to_complete}, Completed: {is_complete}"

    def delete_history(self):
        self.cursor.execute("DROP TABLE {}".format(self.table_name))
        self.create_table()
        self.connection.commit()
        self.rows_in_table = 0

    def disconnect(self):
        self.connection.close()
