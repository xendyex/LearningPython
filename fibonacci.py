fibto = int(input("How many Fibonaccies should my code generate?: "))
prev = 0
current = 1
#Prepares and asks for how many fibs to generate.
if fibto < 0:
    print("Put a number that isn't 0 or under!")
    #Checks in case anything is under 0.
    
for i in range(fibto):
    print(current)
    next_num = current + prev
    prev = current
    current = next_num
    #Generates Fibonaccies!