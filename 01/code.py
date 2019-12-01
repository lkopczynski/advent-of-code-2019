import math




def fuel_required(mass):
  mass = int(mass)
  fuel_req = math.floor(mass/3) - 2
  if fuel_req > 0:
    return fuel_req + fuel_required(fuel_req)
  else: 
    return 0


raw_values = []
module_sum = 0

with open('./input.txt') as f:
  raw_values = f.readlines()

raw_values = [x.strip() for x in raw_values]

for v in raw_values:
  module_sum = module_sum + fuel_required(v)

print(module_sum)
  
