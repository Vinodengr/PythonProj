import random
import time

operators =["+","-","*"]
min_operand =3
max_operand =12
total_problems  = 10

def generate_problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)

    expr = str(left) + " "+ operator + " "+str(right)
    
    ans = eval(expr)
    return expr, ans

wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(total_problems):
    exp, answer = generate_problem()
    while True:
        guess = input( "Problem No: " + str(i+1) + ":- " + exp + " = ")
        if guess == str(answer):
            break
        wrong +=1

end_time  = time.time()
time_diff =  end_time - start_time


print("-----------------------")
print("Nice Work You finishted in ", time_diff , "seconds! ")