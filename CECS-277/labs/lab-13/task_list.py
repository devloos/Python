from task import Task
from typing import Self

FILE_NAME = 'tasklist.txt'


def read_file():  # this is to read file
    tasks = []
    with open(FILE_NAME, 'r') as file:
        content = file.readlines()

        for line in content:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) == 3:
                    desc, date, time = parts
                    tasks.append(Task(desc, date, time))

    tasks.sort()
    return tasks


class TaskList:
    def __init__(self):
        self._tasklist: list[Task] = read_file()
        self._n = 0

    def add_task(self, desc, date, time):
        self._tasklist.append(Task(desc, date, time))
        self._tasklist.sort()

    def get_current_task(self) -> Task | None:
        if self._tasklist:
            return self._tasklist[0]

        return None

    def mark_complete(self) -> Task | None:
        if not self._tasklist:
            return None

        completed_task = self._tasklist.pop(0)
        self._tasklist.sort()

        return completed_task

    def postpone_task(self, date, time):
        current_task = self.get_current_task()
        desc = current_task.get_description()

        self._tasklist.append(Task(desc, date, time))
        self._tasklist.sort()

    def save_file(self):
        with open(FILE_NAME, 'w') as file:
            for task in self:
                file.write(repr(task) + '\n')

    def __iter__(self) -> Self:
        self._n = 0

        return self

    def __next__(self) -> Task:
        try:
            idx = self._n
            self._n += 1
            return self._tasklist[idx]
        except:
            raise StopIteration()

    def __len__(self) -> int:
        return len(self._tasklist)
