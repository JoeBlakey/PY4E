def arithmetic_arranger(x, sol=False):
  #Initialise Variables
  count = 0
  y = 0
  underline = ""
  top_line = ""
  bottom_line = ""
  solution_line = ""
  #Checks number of problems
  if len(x) < 6:
    #Loops for number of problems
    while count is not len(x):
      #Splits the problem into numbers and operator
      splitprob = x[count].split()
      width = max(len(splitprob[0]), len(splitprob[2])) + 2
      #Checks length of numbers
      if max(len(splitprob[0]), len(splitprob[2])) > 4:
        return("Error: Numbers cannot be more than four digits.")
      #Checks numbers are not strings
      if splitprob[0].isdigit() is False or splitprob[2].isdigit() is False:
        return("Error: Numbers must only contain digits.")
      #Sets up each line of the output
      line_top = splitprob[y].rjust(width)
      operand = splitprob[y + 1]
      line_bot = splitprob[y + 2].rjust(width - 2)
      #Checks operator is either + or -
      if operand != "+" and operand != "-":
        return ("Error: Operator must be '+' or '-'.")
      #Generates underline for each of the problems based on width
      line = ""
      z = 0
      while z is not width:
        line = line + "-"
        z = z + 1
      #Calculated solution to problem
      solution = str(eval(x[count])).rjust(width)
      #Adds problem to each line.
      space = "    "
      top_line = top_line + line_top + space
      bottom_line = bottom_line + operand + " " + line_bot + space
      underline = underline + line + space
      solution_line = solution_line + solution + space
      count = count + 1
    #Strips white space from end of each line
    top_line = top_line.rstrip()
    bottom_line = bottom_line.rstrip()
    underline = underline.rstrip()
    solution_line = solution_line.rstrip()
    #Adds solution_line if sol=True
    if sol:
      arranged_output = top_line + "\n" + bottom_line + "\n" + underline + "\n" + solution_line
    else:
      arranged_output = top_line + "\n" + bottom_line + "\n" + underline
    #Returns output
    return arranged_output
  else:
    return ("Error: Too many problems.")
  
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43"], True))