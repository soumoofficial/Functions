# To check whether a no is prime or not

class Check:

    n = int(input("Enter a no :"))

    def Prime(n):
        flag = False
        for i in range(2,n):
            if n%i == 0:
                flag = True
                break

        if flag :
            print("Not Prime")
        else :
            print("Prime")        
    Prime(n)