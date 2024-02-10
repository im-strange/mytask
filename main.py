
import csv
import sys
from texttable import Texttable

"""
[+] each task contains:
    - id
    - category
    - task
    - deadline
    - status
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
        id = len(self.list) + 1
        current_tasks = self.read_list()

        task_list.insert(0, id)
        current_tasks.insert(0, task_list)

    def remove(self):
        pass

    def display_table(self):
        table = Texttable()
        table.header(self.columns)
        for row in self.list:
            table.add_row(row)
        print(table.draw())

class cli:
    def __init__(self, args):
        self.args = args
        self.app = app()

    def display_help(self):
        help_msg = [
            "Usage: mytask [OPTIONS]\n",
            "Options:",
            "  -h, --help\t Display help",
            "  -a, --add\t Add a new task",
            "  -d, --drop\t Delete a task",
            "  -e, --edit\t Edit a task"
        ]
        for row in help_msg:
            print(row)

    def match(self, list1, list2):
        result = any(item in list1 for item in list2)
        return result

    def run(self):
        if self.match(["-h", "--help"], self.args):
            self.display_help()

        elif self.match(["-a", "--add"], self.args):
            print("you are adding a tasks")

        elif self.match(["-d", "--drop"], self.args):
            print("you are removing a task")

        elif self.match(["-e", "--edit"], self.args):
            print("you are editing a task")

        elif self.match(["--view"], self.args):
            self.app.display_table()

if __name__ == "__main__":
    args = sys.argv
    todo = app()
    cli = cli(args)
    cli.run()
