import os 

def process_intcode(code, noun, verb):
  instructions = code.split(',')
  curr_inst_pos = 0

  # restore state
  instructions[1] = noun
  instructions[2] = verb

  while curr_inst_pos < len(instructions):
    curr_inst = int(instructions[curr_inst_pos])
        
    if curr_inst == 99:
      break
  
    inst_set = [int(x) for x in instructions[curr_inst_pos:curr_inst_pos+4]] # get next 4 ints to determine operation
    a = int(instructions[inst_set[1]])
    b = int(instructions[inst_set[2]])
    target = int(inst_set[3])

    if curr_inst == 1:
      output = a + b
    elif curr_inst == 2:
      output = a * b

    instructions[target] = output
    curr_inst_pos += 4
  
  return instructions[0]


if __name__ == '__main__':
  dir_path = os.path.dirname(os.path.realpath(__file__))
  file_path = os.path.join(dir_path, 'input.txt')
  with open(file_path) as f:
    raw_values = f.readlines()

  raw_values = [x.strip() for x in raw_values]
  for noun in range(0, 100):
    for verb in range(0, 100):
      if process_intcode(raw_values[0], noun, verb) == 19690720:
        print(f'found! noun={noun}, verb={verb}')


