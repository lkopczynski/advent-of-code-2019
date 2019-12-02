import os 


if __name__ == '__main__':
  dir_path = os.path.dirname(os.path.realpath(__file__))
  file_path = os.path.join(dir_path, 'input.txt')
  with open(file_path) as f:
    raw_values = f.readlines()

  raw_values = [x.strip() for x in raw_values]
  
  instructions = raw_values[0].split(',')
  curr_inst_pos = 0

  # restore state
  instructions[1] = 12
  instructions[2] = 2

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

  print(instructions[0])

# do stuff with values
