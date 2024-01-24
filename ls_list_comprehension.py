x = 2
n = 2

res = [[i, n] for i in range(x) for j in range(n)]
# print(res)

arr = [2, 3, 6, 6, 5]
first_runner = max(arr)
print(first_runner)
print(max(filter(lambda _x: _x < first_runner, arr)))

# students = {"Harry": 37.21, "Berry": 37.21, "Tina": 37.2, "Akriti": 41, "Harsh": 39}
students = {"Harsh": 20, "Beria": 20, "Varun": 19, "Kakunami": 19, "Vikas": 21}

sorted_students = sorted(students.values())
lowest = sorted_students[0]
while lowest in sorted_students:
    sorted_students.remove(lowest)
second_lowest = sorted_students[0]
for name, score in students.items():
    if score == second_lowest:
        print(name)
