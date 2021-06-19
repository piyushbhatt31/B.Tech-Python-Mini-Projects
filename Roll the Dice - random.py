import random 
while True:     
     user = input('Press 1 to roll the dice: ')    
     if user=="1":         
        number = random.randint(1,6)         
        print(number)     
     else:         
        break
