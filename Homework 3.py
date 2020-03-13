#Homework 3 by Ye Eun (Esther) Lee

#Establish Monopoly property group data
psize = {'purple':2, 'light blue':3,'maroon':3, 'orange':3, 'red':3, 'yellow':3, 'green':3, 'dark blue':2}
pcost = {'purple':50, 'light blue':50,'maroon':100, 'orange':100, 'red':150, 'yellow':150, 'green':200, 'dark blue':200}

#Input color block user is building on
color = input('Which color block will you be building on? ' )


#Prompt again if invalid entry for color
while color not in ('purple', 'light blue', 'maroon', 'orange', 'red', 'yellow', 'green', 'dark blue'):
    if color == 'blue':
        color = input('Light blue or dark blue? ')
    else:
        print('Color not valid. Please try again.')
        color = input('Which color block will you be building on? ' )

#Input money user has to spend
money = input('How much money do you have to spend? ' )
money = int(money)

#Retrieve cost of houses on property from dictionary
cost = pcost[color]

#Calculate number of houses that can be built
houses = money // cost
    
#Retrieve size of property (number of properties in group) from dictionary
size = psize[color]

#Calculate evenly distributed number of houses on each property, and remainder to be distributed
num_equal_houses = houses//size
remainder = houses%size

#Identify how many properties will receive extra houses
extra_houses = remainder

#Identify how many properties will receive equal distribution of houses
equal_houses = size - extra_houses

#Determine how many houses those properties with more will receive
num_extra_houses = num_equal_houses + 1

#Output result
if houses == 0:
    print('You cannot afford even one house.')
elif num_equal_houses >= 5 and extra_houses == 0:
    num_equal_houses = 'a hotel'
    print('There are',size, color,'properties and each house costs', cost)
    print('You can build',houses,'houses --', equal_houses, 'will have', num_equal_houses)
elif num_equal_houses >= 5 and num_extra_houses >= 5:
    print('There are',size, color,'properties and each house costs', cost)
    print('You can build',houses,'houses --', equal_houses+extra_houses, 'will have a hotel')
elif num_equal_houses >= 5:
    num_equal_houses = 'a hotel'
    print('There are',size, color,'properties and each house costs', cost)
    print('You can build',houses,'houses --', equal_houses, 'will have', num_equal_houses, 'and', extra_houses, 'will have', num_extra_houses)
elif num_extra_houses >= 5:
    num_extra_houses = 'a hotel'
    print('There are',size, color,'properties and each house costs', cost)
    print('You can build',houses,'houses --', equal_houses, 'will have', num_equal_houses, 'and', extra_houses, 'will have', num_extra_houses)
elif extra_houses == 0:
    print('There are',size, color,'properties and each house costs', cost)
    print('You can build',houses,'houses --', equal_houses, 'will have', num_equal_houses)
else:
    print('There are',size, color,'properties and each house costs', cost)
    print('You can build',houses,'houses --', equal_houses, 'will have', num_equal_houses, 'and', extra_houses, 'will have', num_extra_houses)
