capitals = {
  "Bulgaria" : "Sofia",
  "Germany" : "Berlin",
  "France" : "Paris"
}

# Вместо една променлива 'item', дефинираме две: 'country' и 'capital'
for country, capital in capitals.items():
   # Python автоматично ще присвои първия елемент от кортежа на 'country',
   # а втория - на 'capital' при всяка итерация.
   print(f"The capital of {country} is {capital}")