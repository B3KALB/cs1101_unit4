import math

# EXAMPLE 1 hypotenuse

leg_x = float(input("leg X = "))# this sets our input x as a variable

leg_y = float(input("leg Y = "))#this sets our input y as a variable

def hypotenuse(x, y):# this creates our function and passes in the two arguments 
    z = math.sqrt(x**2 + y**2)# this does the heavy lifting by finding the sqr root of our two variables to the second power and added together
    print(f"The hypotenuse of leg Z = {round(z, 2)}")# this prints the value of variable z and i have rounded that to the nearest hundredth

hypotenuse(leg_x, leg_y)# this calls our function and passes in the two live variables as arguments

# inputs and outputs

# leg X = 3
# leg Y = 4
# The hypotenuse of leg Z = 5.0
# >
# leg X = 5
# leg Y = 5.5
# The hypotenuse of leg Z = 7.43
# > 
# leg X = 10
# leg Y = 12
# The hypotenuse of leg Z = 15.62


# EXAMPLE 2 make_a_function_up

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # the variable nums holds our list

target_value = int(input("Enter a target value 1-20: "))#this lets you enter a target value and stores it to a variable

def which_add_up(nums, target):#this is our function that passes in two arguments

    print(f"The numbers are {nums}")# this displays our var nums for the user to see
    
    for i in range(len(nums)):#in for loop 1 it holds the first index of 0 then moves through the list one at a time as our next loop returns
    
        for b in range(len(nums)):# in for loop 2 it holds index 0 and loopes through the list one at a time, in between the indexes of the first loop
    
            if nums[i]+nums[b] == target:#this is wher we set our conditional to check if loop_1 plus loop_2 equals our target value
    
                print("index "+ str(i) + " and index " + str(b) + f" equal {target}.")# this prints our two indexes if the equal the target value
    
                print(f"{nums[i]} + {nums[b]} = {target}")# this prints the values of each index that adds up to our target and the target value

which_add_up(nums, target_value)#this calls the function and passes in our two arguments

# inputs and outputs 
# Enter a target value 1-20: 3
# The numbers are [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index 0 and index 1 equal 3.
# 1 + 2 = 3
# index 1 and index 0 equal 3.
# 2 + 1 = 3
# > 
# Enter a target value 1-20: 9
# The numbers are [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index 0 and index 7 equal 9.
# 1 + 8 = 9
# index 1 and index 6 equal 9.
# 2 + 7 = 9
# index 2 and index 5 equal 9.
# 3 + 6 = 9
# index 3 and index 4 equal 9.
# 4 + 5 = 9
# index 4 and index 3 equal 9.
# 5 + 4 = 9
# index 5 and index 2 equal 9.
# 6 + 3 = 9
# index 6 and index 1 equal 9.
# 7 + 2 = 9
# index 7 and index 0 equal 9.
# 8 + 1 = 9
# > 
# Enter a target value 1-20: 17
# The numbers are [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index 6 and index 9 equal 17.
# 7 + 10 = 17
# index 7 and index 8 equal 17.
# 8 + 9 = 17
# index 8 and index 7 equal 17.
# 9 + 8 = 17
# index 9 and index 6 equal 17.
# 10 + 7 = 17
# > 