# Accept a string and display the no of uppercase letters and lower case letters

class String_Dis:
    input1 = input("Enter a string :")

    def Counting(input1):
        u_count=l_count = 0

        l = len(input1)

        for i in range(l):
             
            if(input1[i]>='A' and input1[i]<='Z'):
                u_count += 1
            elif(input1[i]>='a' and input1[i]<='z'):
                l_count += 1

        print(f"Upper Case = {u_count}")
        print(f"Lower Case = {l_count}")

    Counting(input1)
            