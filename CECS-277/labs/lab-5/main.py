'''
Written by: Israel Fausto, Carlos Aguilera
Date: 09/25/24

Description:
    This program allows users to manage their tasks by providing a simple, menu-driven interface.
    Upon starting, it displays how many tasks are currently on the list, along with the option to
    view the most urgent task. Users can mark tasks as complete, at which point the task is removed
    from the list, and the next task automatically becomes the focus. If a task cannot be completed
    right away, users can postpone it by entering a new due date and time. The program also allows
    for adding new tasks with descriptions, due dates, and times, which are sorted in order of urgency.
    Progress is saved to a file so users can easily pick up where they left off the next time they run
    the program. Overall, it's a straightforward tool for task organization, helping users prioritize
    and keep track of their responsibilities.
'''
from task import Task
from check_input import get_int_range

FILE_NAME = 'tasklist.txt'


def main_menu() -> int:
    print('1. Display current task')
    print('2. Mark current task complete')
    print('3. Postpone current task')
    print('4. Add new task')
    print('5. Save and quit')

    return get_int_range('Enter choice: ', 1, 5)


def display_task(tasks: list[Task]):
    if tasks:
        print('Current task is: ')
        print(tasks[0])
    else:
        print('There are no tasks to display.')


def complete_task(tasks: list[Task]):
    if not tasks:
        print('There are no tasks to complete.')
        return

    print('Marking current task as complete: ')

    completed_task = tasks.pop(0)
    print(completed_task)

    if tasks:
        tasks.sort()

        print('New current task is: ')
        print(tasks[0])
    else:
        print('There are no more tasks.')


def postpone_task(tasks: list[Task]):
    if not tasks:
        print('There are no tasks to postpone.')
        return

    print('Postponing task: ')
    task = tasks.pop(0)

    new_date = get_date()
    new_time = get_time()

    tasks.append(Task(task.get_description(), new_date, new_time))
    tasks.sort()


def add_task(tasks: list[Task]):
    desc = input('Enter a task: ')

    due_date = get_date()
    due_time = get_time()

    tasks.append(Task(desc, due_date, due_time))

    tasks.sort()


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


def write_file(tasks):  # this is to write in new tasks
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(repr(task) + '\n')


def get_date() -> str:
    print('-Enter Due Date-')

    month = get_int_range('Enter month: ', 1, 12)
    day = get_int_range('Enter day: ', 1, 31)
    year = get_int_range('Enter year: ', 2000, 2100)
    date = f'{month:02}/{day:02}/{year}'

    return date


def get_time() -> str:
    print('-Enter Time-')

    hour = get_int_range('Enter hour: ', 0, 23)
    minute = get_int_range('Enter minute: ', 0, 59)
    time = f'{hour:02}:{minute:02}'

    return time


def save_quit(tasks: list[Task]):
    write_file(tasks)
    print('Saving and exiting.')
    exit()


def main():
    tasks = read_file()

    while True:
        print('-Tasklist-')

        if len(tasks) > 0:
            print('You have', len(tasks), 'tasks.')
        else:
            print('You have no tasks.')

        choice = main_menu()

        match choice:
            case 1:
                display_task(tasks)
            case 2:
                complete_task(tasks)
            case 3:
                postpone_task(tasks)
            case 4:
                add_task(tasks)
            case 5:
                save_quit(tasks)


main()
