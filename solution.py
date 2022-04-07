# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, N):
    # write your code in Python 3.6
    #bitwise xor prodyct is the biwise xor of all itegers from M to N

    #k&l are integeres
    #binary a&b

    #xor operaiton 0^1
    M = DecimalToBinary(M)
    N = DecimalToBinary(N)


    arr=[]

    for i in range (M, N-1):
        arr.append[i]
    
    print(arr)
       

    for index,ele in enumerate(arr):


        if index+1==arr.length: #no more index+1
            break

        num1 = arr[index]
        num2 = arr[index+1]
        #BitwiseXor(arr[index], arr[index+1], index+1)
        #replace 
        arr[index+1] = (num1 | num2) & (~num1 | ~num2)
    

    return arr[-1]


    

# def BitwiseXor(num1, num2, index):
#     #store result in index
#     arr[index] = (num1 | num2) & (~num1 | ~num2)
#     return 


def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    return(num % 2)