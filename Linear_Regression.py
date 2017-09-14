from Get_Differences import * #Run all, get differences list
from scipy import stats

counts = [x for x in differences if x.type is 'V']
speeds = [x for x in differences if x.type is 'S']

cubes_count = [x.cube for x in counts]
canons_count = [x.canon for x in counts]

gradient, intercept, r_value, p_value, std_err = stats.linregress(cubes_count,canons_count)
print("Counts: ")
print("\tGradient: {0}".format(gradient))
print("\tIntercept: {0}".format(intercept))
print("\tR^2 Value: {0}".format(r_value))

cubes_speed = [x.cube for x in speeds]
canons_speed = [x.canon for x in speeds]

gradient, intercept, r_value, p_value, std_err = stats.linregress(cubes_speed,canons_speed)
print("Speeds: ")
print("\tGradient: {0}".format(gradient))
print("\tIntercept: {0}".format(intercept))
print("\tR^2 Value: {0}".format(r_value))
