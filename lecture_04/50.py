python_club = {"Abhi", "Rahul", "Aman", "Priya"}
cyber_club = {"Priya", "Aman", "Riya", "Karan"}

both = python_club.intersection(cyber_club)

only_python = python_club.difference(cyber_club)

either = python_club.union(cyber_club)

print("Both:", both)
print("Only Python:", only_python)
print("Either:", either)
