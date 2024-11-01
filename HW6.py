my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

print("Student IDs : ", end="")

for i in my_dict["students"]:
    print(i["id"],end=" ")

choice = int(input("\nSelect ID of student: "))
student = None
for i in my_dict["students"]:
    if i["id"] == choice:
        student = i
        break


print(f"stundet information\n"+
      f"ID: {choice}, Name: {student["name"]}, Age: {student["age"]}\n"+
      f"subject: Math, grade: {my_dict['subjects'][0]["grades"][str(choice)]}\n"+
      f"subject: Physics, grade: {my_dict['subjects'][1]["grades"][str(choice)]}\n"+
      f"subject: English, grade: {my_dict['subjects'][2]["grades"][str(choice)]}\n"+
      f"subject: Chemistry, grade: {my_dict['subjects'][3]["grades"][str(choice)]}\n"+
      f"subject: History, grade: {my_dict['subjects'][4]["grades"][str(choice)]}")