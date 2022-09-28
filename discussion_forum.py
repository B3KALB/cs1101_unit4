# Function issue - precondition
pre = nope #the issue. precondition, if you want to use that value you havve to use a string " "

def funk_one(issue):# the function with the issue passed in as the argument

    print(f"precondition {issue}")# we are trying to print the issue, but it is in the function which is already experinceing the issue

funk_one(pre)#calling the function with the issue passed in as the argument



# Function issue _ postcondition
pre_two = 2#nothing wrong with this precondition

def funk_two(arg):#the function with the precondition passed in
    print("postcondition" + {arg} + "issue")# the post condition issue lies here, it shoud read print(f"postcondition {arg} issue")

funk_two(pre_two) # this is calling the function with the precondition passed in as the argument

# Returpostssue - value or as used
pre_three = 3#nothing wrong with this precondition

def funk_three(arg):# a happy little function with a good precondition passed in
   post = print(f"returpostssue times {arg}")#our good postcondition featuring a handsom print statement
return post# the return issue, it is being used incorrectly. It is being used outside the function, it needs to be indented correctly to work.

funk_three(pre_three)   # calling the function with a good precondition and post condition