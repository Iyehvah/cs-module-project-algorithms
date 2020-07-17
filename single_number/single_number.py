'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    for i in range(0, len(arr)):
        if arr.count(i) == 1:
            return i    

        
my_array = [1,1,2,2,3,4,4,5,5,6,6]
print(single_number(my_array))
            



# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

#     print(f"The odd-number-out is {single_number(arr)}")