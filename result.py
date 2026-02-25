import requests

url = "https://yourusername.github.io/repositoryname/result.json"

name = input("Enter Name: ")
roll = input("Enter Roll No: ")

response = requests.get(url)
data = response.json()

found = False

for student in data:
    if student["name"].lower() == name.lower() and student["rollno"] == roll:
        print("\nResult Found ✅")
        print("Math:", student["math"])
        print("Science:", student["science"])
        print("English:", student["english"])
        total = student["math"] + student["science"] + student["english"]
        print("Total:", total)
        found = True
        break

if not found:
    print("Student Not Found ❌")