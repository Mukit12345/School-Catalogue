"""
Use this if you have a prior version of python 3.9 and change list[str] to List[str] in HighSchool class's constructor 'def __init__'
from typing import List
"""

class School:
  def __init__(self, name: str, level: str, numberOfStudents: int):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

    #getters
  def getName(self):
    return self.name
  def getLevel(self):
    return self.level
  def getNumberOfStudents(self):
    return self.numberOfStudents

    #setters
  def setNumberOfStudents(self, value: int):
    self.numberOfStudents = value

def __repr__(self):
  return f'A {level} school named {name} with {numberOfStudents} students'

#TEST:
'''
a = School("Coding", "high", 100)
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(200)
print(a.getNumberOfStudents())
'''

class PrimarySchool(School):
  def __init__(self, name: str, numberOfStudents: int, pickupPolicy: str):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy
    #getter
  def getPickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f"The pickup policy is {self.pickupPolicy}"

#TEST:
'''
b = PrimarySchool("Coding", 300, "Pickup Allowed")
print(b.getPickupPolicy())
print(b)
'''

class HighSchool(School):
  def __init__(self, name: str, numberOfStudents: int, sportsTeams: list[str]):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  #getter
  def getSportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f". The sports teams are {self.sportsTeams}"

#TEST:
'''
c = HighSchool("Coding High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)

'''
