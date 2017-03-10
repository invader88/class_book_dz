print("Checking for the numbers to be prime")
number = int(input("enter a number: "))
def is_prime(a):
    if number>0:
        for i in range(2,number):
            if number % i == 0:
                print ("False")
                break
        else: print("True")
print(is_prime(number))
                    
    
