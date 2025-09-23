chickenThigh: int = 25
egg: int = 5
proteinPoweder = 25
bean = 10
oneDayIntakeProtein = chickenThigh*3 + egg*4 + proteinPoweder + bean

proteinToBodyWeightFactor = 1.8
bodyWeight = 79
proteinIntakeTarget = bodyWeight * proteinToBodyWeightFactor

print(oneDayIntakeProtein)
print(proteinIntakeTarget)