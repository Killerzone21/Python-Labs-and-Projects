nums = [1,2,3,4,5,6,7,8,9,10]
go = 'y'
while go == 'y':
    userNum = int(input("put in an integer"))
    
    if userNum in nums:
        print('yes')
    else:
        print("reeeee")
    go = input("continue? y or n")
