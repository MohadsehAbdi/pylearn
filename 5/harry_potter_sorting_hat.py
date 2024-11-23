import random


hagwarests_houses = ("Griffindor","Hufflepuff","Ravenclaw","Slytherin")

students = ["Hermaione Granger",
            "Harry potter",
            "Ron weasley",
            "Lord voldemort",
            "Draco Malfoy",
            "Professor Severus Snape",
            "Prifessor Albus Dumbeledore",
            "Mohadeseh Abdi"]

students_houses = []
for student in students:
    r = random.randint(0, 3)
    selected_house = hagwarests_houses[r]
    students_houses.append(selected_house)

print(students_houses)