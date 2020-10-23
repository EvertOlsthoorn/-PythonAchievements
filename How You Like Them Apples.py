import math



trees = 333
shadedTrees = math.ceil((trees/3)*2)
sunnyTrees = (trees-shadedTrees)

shadeOutputModifier = 80

sunnyTreeOutput = 146
shadedTreeOutput = (sunnyTreeOutput%shadeOutputModifier)

sunnyOutput = (sunnyTrees*shadedTreeOutput)
shadedOutput = (shadedTrees*shadedTreeOutput)
totalOutput = (trees*sunnyTreeOutput)

owners = 3

eatCount = 1
sellableOutput = (sunnyOutput*shadedOutput)
cut = (sellableOutput/owners)

print(cut)
