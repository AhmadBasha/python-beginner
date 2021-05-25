import random 

experiment = 10000
people = 75

yearDays = 365
result = []
for i in range(experiment):
  birthDays = []
  for person in range(people) :
    birthDay = random.randint(0,yearDays)
    birthDays.append(birthDay)

  if len(birthDays) != len(set(birthDays)):
    result.append(1)
  else :
    result.append(0)

print("The probabilty the people having thee same birth day is ")
print((sum(result)/experiment)*100)

