import requests

url = "https://raw.githubusercontent.com/aryanyadavcoder/lerning_JSON/main/result1.json"

name = input("Enter Name: ").strip().lower()
roll = input("Enter Roll No: ").strip()

response = requests.get(url)
data = response.json()

found = False

for student in data:
    student_name = str(student.get("name", "")).strip().lower()
    student_roll = str(student.get("rollno", "")).strip()

    print("Checking:", student_name, student_roll)  # debug line

    if student_name == name and student_roll == roll:
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