print("List generator")
start = int(input("start at: "))
end = int(input("end before: "))
increment = int(input("increment between values: "))
for value in range(start, end, increment):
    print(value)