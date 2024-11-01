import csv

#  FIRST RUN THIS!!!!


# with open('Folder/csv_file.csv','w',encoding='utf-8',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["id","name","age","grade","subject_name","mark"])



def read_csv_file(path,id=None):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        if not id:
            
            
            return list(reader)
        
        reader = list(reader)
        result = []

        for i in reader:
            if int(i[0]) == id:
                result.append(i)
            if int(i[0]) > id:
                return result

        return result
    



def insert_student(id,name,age,grade,subject_name,mark):
    data = read_csv_file('Folder/csv_file.csv')

    with open('Folder/csv_file.csv','w',encoding='utf-8',newline='') as file:
        writer = csv.writer(file)

        for student in data:

            # Case when we instert already existed student, but with different subject
            if id == int(student[0]) and name == student[1] and age == int(student[2]) and subject_name  != student[4]:
                data += [[id,name,age,grade,subject_name,mark]]
                data.sort(key= lambda x: (int(x[0]), x[4]) )
                data =[["id","name","age","grade","subject_name","mark"]] +data
                writer.writerows(data)
                return
            if id == int(student[0]):
                data =[["id","name","age","grade","subject_name","mark"]] +data
                writer.writerows(data)
                return
            
        data += [[id,name,age,grade,subject_name,mark]]
        data.sort(key= lambda x: (int(x[0]),x[4]))
        data =[["id","name","age","grade","subject_name","mark"]] +data
        writer.writerows(data)


def avg_subject(path,subject):
    with open(path,'r') as file:
        reader = csv.reader(file)
        next(reader)
        reader = list(reader)
        sum, count = 0, 0

        for i in reader:
            if i[4] == subject:
                count += 1
                sum += int(i[5])

        return sum/count
    

def update_student_mark(path,id,subject,newMark):
    reader = read_csv_file(path)
    with open(path,'w',encoding='utf-8',newline='') as file:
        writer = csv.writer(file)

        for i in reader:
            if int(i[0]) == id and i[4] == subject:
                i[5] = newMark
                reader = [["id","name","age","grade","subject_name","mark"]] + reader
                break 
        writer.writerows(reader)




# insert_student(4,"Nika",21,"B","Math",89)
# insert_student(2,"Luka",4,"A","Biology",96)
# insert_student(32,"Lado",33,"F","Art",32)