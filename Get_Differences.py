from dict_builder import * #Runs dict_builder, variables cube and canon now available

differences = {}

for instance in cube:
    if instance in canon:
        difference = cube[instance] - canon[instance]
        differences[instance] = difference

for x in differences:
    print(x,"   ",differences[x])
