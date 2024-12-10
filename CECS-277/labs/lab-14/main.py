'''
Written by: Israel Fausto, Carlos Aguilera
Date: 12/02/24

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
from task_list import TaskList


def main_menu() -> int:
    print('1. Display all tasks')
    print('2. Display current task')
    print('3. Mark current task complete')
    print('4. Postpone current task')
    print('5. Add new task')
    print('6. Search tasks by date')
    print('7. Save and quit')

    return get_int_range('Enter choice: ', 1, 7)


def get_date() -> str:
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


def print_current_task(tasks: TaskList):
    current_task = tasks.get_current_task()

    if current_task:
        print('Current task is: ')
        print(current_task)
    else:
        print('There are no tasks to display.')


def main():
    tasks = TaskList()

    while True:
        print('-Tasklist-')

        if len(tasks) > 0:
            print('You have', len(tasks), 'tasks.')
        else:
            print('You have no tasks.')

        choice = main_menu()

        match choice:
            case 1:
                print('Tasks to complete:')

                for idx, task in enumerate(tasks):
                    print(f'{idx + 1}. {task}')
            case 2:
                print_current_task(tasks)

            case 3:
                completed_task = tasks.mark_complete()

                if not completed_task:
                    print('There are no tasks to complete.')
                    break

                print('Marking current task as complete: ')

                print(completed_task)
                print_current_task(tasks)

            case 4:
                current_task = tasks.get_current_task()

                if not current_task:
                    print('There are no tasks to postpone.')
                    break

                print('Postponing task: ')
                print(current_task)

                print('-Enter Due Date-')
                new_date = get_date()
                new_time = get_time()

                tasks.postpone_task(new_date, new_time)
            case 5:
                desc = input('Enter a task: ')
                print('-Enter Due Date-')
                due_date = get_date()
                due_time = get_time()
                tasks.add_task(desc, due_date, due_time)
            case 6:
                print('Search by Date:')
                date = get_date()

                tasks_found: list[Task] = []

                for task in tasks:
                    if task.date == date:
                        tasks_found.append(task)

                for idx, task in enumerate(tasks_found):
                    print(f'{idx + 1}. {task}')

            case 7:
                tasks.save_file()
                print('Saving and exiting.')
                exit()


main()
