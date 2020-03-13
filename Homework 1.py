#Homework 1 by Ye Eun (Esther) Lee

#Input how many people are sharing pizza

ppl = input('How many people are sharing pizza?')
ppl = int(ppl)

#Input how many pizzas will be ordered

numpiz = input('How many pizzas will be ordered?')
numpiz = int(numpiz)

#Input how many will limit themselves to two slices

twosliceppl = input('How many will limit themselves to two slices?')
twosliceppl = int(twosliceppl)

#Calculate number of total slices

totalslices = numpiz * 8

#Calculate number of slices to reserve to two slice people

reservedslices = twosliceppl * 2

#Calculate number of slices available for everyone else

slices = (numpiz * 8) - reservedslices

#Assign variable and value to "everyone else"

everyone = ppl - twosliceppl

#Divide slices equally among everyone else, with remainder

eqshare = slices // everyone
remainder = slices % everyone

#Identify how many people will receive extra slices

extra_ppl = remainder

#Identify how many people will receive equal slices

equal_ppl = everyone - extra_ppl

#Determine how many slices those people with more will receive

extra_ppl_slices = eqshare + 1

#Print answer

print("You will divide", totalslices, "slices.")
if twosliceppl > 0:
    print(twosliceppl, "will have 2")
print(equal_ppl, "will have", eqshare,)
if extra_ppl > 0:
    print("and", extra_ppl, "will have", extra_ppl_slices)







