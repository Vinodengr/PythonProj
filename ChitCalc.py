init_amount = 20000
monthly_amount = 14000
tenure = 30
acc_amount = 0
Final_amount = 588000
for i in range(tenure):
    monthly_amount = monthly_amount+200
    acc_amount = acc_amount + monthly_amount
    print(i,monthly_amount)

print("-------")
print(acc_amount)
print("The total amount paid is ", acc_amount+ init_amount)

#Calc ROI
roi = (Final_amount- (acc_amount+init_amount))/(acc_amount+init_amount)* 100
print(roi)
