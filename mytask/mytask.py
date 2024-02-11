
import os
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
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.data_file = file1_path = os.path.join(self.data_dir, 'data.csv')
        self.list = list(csv.reader(open(self.data_file)))
        self.columns = self.list[0]
        self.list = self.list[1:]

    def read_list(self):
        current_list = list(csv.reader(open(self.data_file)))[1:]
        return current_list

    def write(self, data):
        data.insert(0, self.columns)
        with open(self.data_file, "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def add(self, task_list):
        id = len(self.list) + 1
        current_tasks = self.read_list()

        task_list.insert(0, id)
        current_tasks.insert(0, task_list)

        self.write(current_tasks)
        print(f"[+] Task added!")

    def remove(self, id):
        auth = input("[!] Are you sure you want to remove the task? (y/n): ")
        if auth.lower() == "y":
            pass
        else:
            print(f"[!] Deletion cancelled")
            exit()

        tasks = self.read_list()
        tasks = [task for task in tasks if int(task[0]) != int(id)]
        self.write(tasks)

        print("[+] Task removed!")

    def edit(self, id, new_data):
        tasks = self.read_list()
        to_edit = [task for task in tasks if int(task[0]) == int(id)][0]
        to_edit_index = to_edit[0]
        tasks.remove(to_edit)

        new_data.insert(0, to_edit_index)
        new_data = [i if len(i.split()) > 0 else to_edit[new_data.index(i)] for i in new_data]
        tasks.insert(0, new_data)

        self.write(tasks)
        print("[+] Task updated!")

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
            "  -e, --edit\t Edit a task",
            "  --view\t View task"
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
            category = input("[+] Enter category: ")
            task = input("[+] Enter task: ")
            deadline = input("[+] Enter deadline: ")
            status = "added"

            data = [category, task, deadline, status]
            data = [i.lower() for i in data]

            self.app.add(data)
        elif self.match(["-d", "--drop"], self.args):
            try:
                id = int(input("[+] Enter task id: "))
                self.app.remove(id)
            except:
                print("[!] Error")
                exit()

        elif self.match(["-e", "--edit"], self.args):
            id = int(input("[+] Enter id to edit: "))
            category = input("[+] Enter category: ")
            task = input("[+] Enter task: ")
            deadline = input("[+] Enter deadline: ")
            status = input("[+] Enter status: ")

            new_data = [category, task, deadline, status]
            new_data = [i.lower() for i in new_data]
            self.app.edit(id, new_data)

        elif self.match(["--view"], self.args):
            self.app.display_table()

        else:
            self.display_help()
            print("\n[!] unknown command")

def main():
    args = sys.argv
    cl = cli(args)
    cl.run()

if __name__ == "__main__":
    main()
