car = {
  "brand" : "Ford",
  "model" : "Mustang"
}

print(f"Year: {car.get("year")}")
print(f"Year with default: {car.get("year", "Unknown")}")
