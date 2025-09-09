student = {
  "name" : "John",
  "age" : 22,
  "major" : "Computer Science"
}

print(f"Major: {student.get("major")}")

student["age"] = 23

print(f"Updated student info: {student}")
