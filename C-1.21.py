#Write a Python program that repeatedly reads lines from stadard input until an EOFError is raised, and then outputs
those lines in reverse order (a user can indicate end of inpuht by typing ctrl-D).


lines=[]



try:
  while True:
    line=input()
    lines.append(line)
except:
  EOFerror
  for line in reversed(lines):
    print(line)
