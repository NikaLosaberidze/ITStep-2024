# N1
import random
import re 
lst = []

while True:
    choice = input("-a- for append | -r- for remove | -e- for exit: ")

    if choice == "a":
        lst.append(random.randint(0,100))
    elif choice == "r":
        lst.pop(len(lst)-1)
    elif choice == "e":
        print(lst)
        print("Programme has stopped.")
        break
    else:
        print("Invalid Input! Try Again")



# N2

my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

print(my_list_1.index(210))
my_list_1[5].append("Hello")
my_list_1.pop(2)
print(my_list_1)

my_llist_2 = my_list_1
my_llist_2 = my_llist_2.clear()

print(f"First List: {my_list_1}, Second List: {my_llist_2} ")


# N3

tel = input("Enter telephone number: ")
pattern = r"\(\d{3}\) \d{3}-\d{3}"
    
    
if re.fullmatch(pattern, tel):
    print(tel)
else:
    print("Invalid format")