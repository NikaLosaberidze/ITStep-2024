import json

class Address:

    def __init__(self,city,street) -> None:
        self.city = city
        self.street = street


class Student:
    row_id = 0

    def __init__(self, name, mark, address : Address) -> None:

        if not isinstance(address, Address):
            raise TypeError("Address value must be Addres class instance")

        self.name = name
        self.mark = mark
        self.address = address

        if mark >= 91:
            self.grade = "A"
        elif mark >= 81:
            self.grade = "B"
        elif mark >= 71:
            self.grade = "C"
        else:
            self.grade = "D"

        Student.row_id += 1
        self.row_id = Student.row_id


ad1 = Address("Kutaisi","Niko Mari")
ad2 = Address("Batumi","Anjafaridze Street")
ad3 = Address("Poti", "Abashidze Street")

st1 = Student("Nika",50,ad1)
st2 = Student("Lasha",24,ad2)
st3 = Student("Kaxa",100,ad3)

studentList = [st1, st2, st3]



class encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Address):
            return {"city": obj.city, "street": obj.street}
        elif isinstance(obj, Student):
            return {
                "row_id" : obj.row_id,
                "name" : obj.name,
                "mark" : obj.mark,
                "address" : obj.address,
                "grade" : obj.grade
            }

        return super().default(obj)



with open("students.json","w",encoding="utf-8") as file:
        json.dump(studentList, file, cls=encoder, indent=4)