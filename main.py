
import csv
from texttable import Texttable

"""
[+] each task contains:
    - category
    - task
    - time
    - deadline
"""

class app:
    def __init__(self):
        self.data_file = "data.csv"
        self.list = list(csv.reader(open(self.data_file)))
        self.columns = self.list[0]
        self.list = self.list[1:]

    def read_list(self):
        current_list = list(csv.reader(open(self.data_file)))[1:]
        return current_list

    def add(self, task_list):
        current_tasks = self.read_list()
        current_tasks.insert(0, task_list)

    def remove(self):
        pass

    def cli(self):
        pass

    def display_table(self):
        table = Texttable()
        table.header(self.columns)
        for row in self.list:
            table.add_row(row)
        print(table.draw())

if __name__ == "__main__":
    todo = app()
    todo.display_table()
