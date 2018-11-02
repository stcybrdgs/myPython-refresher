#
# Example file for working with conditional statements
#

# demo 1 of IF evaluations ---------------------------
def ifDemo1():
  # you may declare vars in a comma delimited list 
  x, y = 100, 100
  
  # conditional flow uses if, elif, else
  if ( x < y ):
    st = "x is less than y"
  elif ( x > y ):
    st = "x is greater than y"
  else:
    st = "x = y"
  print(st)

# demo 2 of IF evaluations ---------------------------
def ifDemo2():
  x, y = 100, 2
  st = "x is less than y" if (x < y) else "x is greater than or same as y"
  print(st)

# demo of a SWITCH evaluation in Python --------------
def week(i):
  switcher={
    0:'Sunday',
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday'
  }
  return switcher.get(i,"Invalid day of week")

# function calls -------------------------------------
ifDemo1()
ifDemo2()
print(week(2))

#if __name__ == "__main__":
#  main()
