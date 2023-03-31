# Dictionary makes it easy to have key-value pairs

marks: dict [str, int] = {"Math": 80,
    "Science": 82,
    "History": 78,
    "English": 35,
    "Python": 98,
    "Physics": 63}

print(f"Marks: {marks}")
#Boo wants to check out all the subjects(keys), keys() is a method of dictionary
for subject in marks.keys():
    print(f"Subject: {subject}")

#Boo wants to check out all the marks(values), values() is a method of dictionary
for score in marks.values():
    print(f"Mark: {score}")
#Boo wants to check out all the subjects and marks together
for subject, score in marks.items():
    print(f"Subject: {subject} - Mark: {score}")

for subject, score in marks.items():
    if score >= 50:
        print(f"{subject} - Pass")
    else:
        print(f"{subject} - Fail")

# update
marks["English"] = 70
print(f"Boo scored {marks['English']} in English")

# add Geography
marks["Geography"] = 78
for subject, score in marks.items():
    if score >= 50:
        print(f"{subject} - Pass")
    else:
        print(f"{subject} - Fail")

python_score = marks.get("Python")
#python_score = marks["Python"]
print(f"Boo scored {python_score} in Python")

java_score: int | None = marks.get("Java")

if java_score is None:
    print("Louis did not study Java")
else:
    print(f"Louis scored {java_score} in java")

# delete
del marks["English"]

print(f"Marks: {marks}")