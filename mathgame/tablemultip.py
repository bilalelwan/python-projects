print("Math Game!")
while True:
    numb = int(input("Name your multiples: "))
    if 1<= numb<=10:
        break
    else:
        print("please enter a number between 1 ans 10")
        continue
correct = 0
incorrect = 0
for i in range(1,11):
    answer= int(input(f"what is {numb} * {i} ? "))
    if answer == numb * i:
        print("right answer!")
        correct+=1
    else:
        print("Nope! the answer was", answer)
        incorrect +=1
print("your score is" , correct)



