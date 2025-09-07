task_list = []

task_list_break_point = 3

while len(task_list) != task_list_break_point:
  task_list.append(input("Enter a task: ").strip())


print(f"Final task list: {task_list}")
