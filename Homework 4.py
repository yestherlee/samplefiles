#Homework 4 by Ye Eun (Esther) Lee

#intro
print('This is a recipe scaler for serving large crowds! \n')

#input recipe
q= []
u = []
i = []
numLines = 0
print('Enter one ingredient per line, with a numeric value first.\n'
               'Indicate the end of input with an empty line.')
line = input()
while len(line) > 0:
    quant, unit, item = line.split(' ',2)
    q.append(quant)
    u.append(unit)
    i.append(item)
    numLines += 1
    line = input()
    
#confirm recipe
temp = q + u
colWidth = len (max(temp, key=len)) + 2
print('Here is the recipe that has been recorded')
for x in range(0, numLines):
    print(q[x], u[x], i[x], sep="\t")

#how many servings in recipe
servings = int(input('\nHow many does this recipe serve? '))

#how many people must be served
people = int(input('How many people must be served? '))

#determine factor by which recipe must be scaled
factor = people/servings
factor = round(factor + 0.5)
print('Multiplying the recipe by', factor, '\n')
#scale recipe, multiply all quantities
scaleQuant = []
for j in q:
    if '/' in j: 
        numer, slash, denom = j.partition('/')
        numer = int(numer) * factor
        denom = int(denom) * factor
        numer = str(numer)
        denom = str(denom)
        scaleQuant.append(numer+slash+denom)
    else:
        j = int(j)
        scaleQuant.append(j*factor)
scaleQuant = list(map(str, scaleQuant))

#print answer
for x in range(0, numLines):
    print(scaleQuant[x], u[x], i[x], sep="\t")

print('\nServes', servings*factor)
