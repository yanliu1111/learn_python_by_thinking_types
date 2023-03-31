subjects: tuple = ("Math", "English", "Science")
print (f"No. of subjects: {len(subjects)}")

#different between tuple and list
#tuple is immutable, list is mutable

for subject in subjects:
    print(f"Boo is signing up for: {subject}")

print(subjects[1])

addl_subjects = ("History", "Python", "Physics")
total_subjects = subjects + addl_subjects
print(f"All subjects: {total_subjects}")

if "Python" in total_subjects:
    print("Yayy, Boo is going to learn Python!!")
else:
    print("Oh ho, no Python for Boo")