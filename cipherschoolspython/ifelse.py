# In 'if'  'else' statements if one condition is true the other one will be false.There
#  wont be two outcomes for single problem
# 'elif' conditions are between 'if' and 'else' and if 'elif' satisifies else statement doesnt work



age=int(input("Enter your age"))
if 0<age<=5:
    print("No cost")
elif 5<age<=12:
    print("Half of the cost") 
else:
    print("Full cost")       
