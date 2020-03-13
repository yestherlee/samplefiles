#Homework 2 by Ye Eun (Esther) Lee

#Establish Monopoly property group data
psize = {'purple':2, 'light blue':3,'maroon':3, 'orange':3, 'red':3, 'yellow':3, 'green':3, 'dark blue':2}
pcost = {'purple':50, 'light blue':50,'maroon':100, 'orange':100, 'red':150, 'yellow':150, 'green':200, 'dark blue':200}

#Establish number to word dictionary
wordform = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve'}

#Input color block user is building on
color = input('Which color block will you be building on?' )

#Input money user has to spend
money = input('How much money do you have to spend?' )
money = int(money)

#Retrieve cost of houses on property from dictionary
cost = pcost[color]

#Calculate number of houses that can be built
houses = money // cost

#Retrieve size of property from dictionary
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

#Convert output numbers to words
word_size = wordform[size]
word_houses = wordform[houses]
word_eqhouses = wordform[equal_houses]
word_num_equal_houses = wordform[num_equal_houses]
word_extra_houses = wordform[extra_houses]
word_num_extra_houses = wordform[num_extra_houses]

#Output result
print('There are',word_size,'properties and each house costs', cost)
print('You can build',word_houses,'houses --', word_eqhouses, 'will have', word_num_equal_houses, 'and', word_extra_houses, 'will have', word_num_extra_houses)
