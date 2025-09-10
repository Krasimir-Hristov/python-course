saturday_tasks = {"clean room", "buy groceries", "read book"}
sunday_tasks = {"read book", "go to gym", "meet friends"}

weekend_tasks = saturday_tasks.union(sunday_tasks)

# or => weekend_tasks = saturday_tasks | sunday_tasks

print(weekend_tasks)
