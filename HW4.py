import string

# N1

str = input("შეიყვეანეთ ტექსტი: ")
str = str.encode("utf-8")

print(str)


# N2

txt = input("შეიყვანეთ ტექსტი:")

txt = txt.strip()
txt = txt.lower()
txt += " Python"

if "python" in txt:
    txt = txt.replace("python","Python")

print(txt)


# N3

txt = input("შეიყვანეთ ტექსტი: ")

print(txt[:len(txt)//2])


# N4


txt = set(input("შეიყვანეთ ტექსტი: "))

strSet = set(string.ascii_letters)
digSet = set(string.digits)
puncSet = set(string.punctuation)


if txt & strSet != {} and txt & digSet != {} and txt & puncSet == set():
    print("ვალიდურია")
else:
    print("არ არის ვალიდური")

# N5


txt = input("შეიყვანეთ ტექსტი: ")

txt = txt.encode("utf-8")
print(txt)

txt = txt.decode("utf-8")
print(txt)