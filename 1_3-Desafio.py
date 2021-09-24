N = int(input())
algoz = input()
persons = algoz.split(' ')
lowest_pos = 0
lowest = int(persons[0])
if N > 1:
  for i in range(1, N):
    if lowest > int(persons[i]):
      lowest = int(persons[i])
      lowest_pos = i + 1
else:
  lowest_pos = 1
print(lowest_pos)
