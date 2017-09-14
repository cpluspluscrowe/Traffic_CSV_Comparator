from dict_builder import * #Runs dict_builder, variables cube and canon now available

differences = []

class Difference():
    def __init__(self,key,difference):
        spl = key.split("-")
        self.A = spl[0]
        self.B = spl[1]
        self.type = spl[2]
        self.time = spl[3]
        self.difference = difference

for instance in cube:
    if instance in canon:
        difference = cube[instance] - canon[instance]
        diff = Difference(instance,difference)
        differences.append(diff)


