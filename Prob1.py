# To make a function to print sum of all no in a list

class Sum_List:
    list1 = [1,2,3,4,5]
    
    def cal_sum(list1):
        sum1 = 0
        for i in range(len(list1)):
            sum1 = sum1 + list1[i]
        print(sum1)
    
    cal_sum(list1)