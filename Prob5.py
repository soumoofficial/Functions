# Function to print even no from a given list

class Even_show:
    input1 = [1,4,2,3,6,10,12,7,19,20]

    def even_check(input1):
        for i in range(len(input1)):
            if input1[i]%2==0:
                print(input1[i])
            else:
                pass
    
    print("The even no are :")
    even_check(input1)