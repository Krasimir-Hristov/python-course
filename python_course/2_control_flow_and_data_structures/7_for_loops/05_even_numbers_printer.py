# Solution variant A

start = 2
stop = 21
step = 2

for number in range(start, stop, step):
  print(number)


# Solution variant B

start = 2
stop = 21

for number in range(start, stop):
  if number % 2 == 0:
    print(number)
