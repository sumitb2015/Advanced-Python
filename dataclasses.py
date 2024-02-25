import pandas as pd
from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int
    profession:str

people=[]
person1 = Person("Sumit",13,"Student")
person2 = Person("Dilip",42,"Doctor")

print(person1)
print(person2)
print(person1==person2)
people.append(person1)
people.append(person2)

for person in people:
    print(person.name)

    
df = pd.DataFrame(people)
print(df)