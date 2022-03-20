# Function to print factorial of a number 

class Cal_Fact :
    num = int(input("Enter a no :"))

    def factorial_cal(num):
        fact = 1
        if(num != 0):
            for i in range(1,num+1):
                fact = fact*i
        print(fact)
    
    factorial_cal(num)