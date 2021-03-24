def arithmetic_arranger(problems, solve = False):
  if len(problems) > 5:
    return "Error: Too many problems."

  simplified_prob = []
  for problem in problems:
    prob_list = problem.split(' ')
    if ('+' in prob_list) or ('-' in prob_list):
      if prob_list[0].isdigit() and prob_list[2].isdigit():
        if (len(prob_list[0]) > 4) or (len(prob_list[2]) > 4):
          return 'Error: Numbers cannot be more than four digits.'
        else:
          simplified_prob.append(prob_list)
      else:
        return 'Error: Numbers must only contain digits.'
    else:
      return "Error: Operator must be '+' or '-'."

  n = 0
  line = ""
  while True:
    for problem in simplified_prob:
      if len(problem[0]) > len(problem[2]):
        problemSpace = len(problem[0]) + 2
      else:
        problemSpace = len(problem[2]) + 2

      if n == 0:
        line = line + (problemSpace - len(problem[0])) * " " + problem[0] + (4 * " ")
        continue
      elif n == 1:
        line = line + problem[1] + (problemSpace - len(problem[2]) - 1) * ' ' + problem[2] + (4 * ' ')
        continue
      elif n == 2:
        line = line + (problemSpace * '-') + (4 * ' ')
        continue

      if solve == True:
        if problem[1] == '+':
          solution = int(problem[0]) + int(problem[2])
        else:
          solution = int(problem[0]) - int(problem[2])

        line = line + ((problemSpace - len(str(solution))) * ' ') + str(solution) + (4 * ' ')

        
    line = line + '\n'
    n += 1
    if n == 4:
      break
    
  return line
