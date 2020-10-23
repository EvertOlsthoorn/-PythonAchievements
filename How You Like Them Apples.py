import math



trees = 333
shadedTrees = math.ceil((trees/3)*2) # Het antwoord is 222
sunnyTrees = (trees-shadedTrees) # Het antwoord is 111

shadeOutputModifier = 80

sunnyTreeOutput = 146
shadedTreeOutput = (sunnyTreeOutput%shadeOutputModifier) #Het antwoord is 117

sunnyOutput = (sunnyTrees*shadedTreeOutput) #Het antwoord
shadedOutput = (shadedTrees*shadedTreeOutput)
totalOutput = (trees*sunnyTreeOutput)

owners = 3

eatCount = 1
sellableOutput = (sunnyOutput*shadedOutput)
cut = (sellableOutput/owners)

print(cut)
