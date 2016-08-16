import time
from termcolor import colored

print(chr(27) + "[2J")

print '\n'.join([
  'Welcome to the clock-hands program.',
  'Give it the time in integer format',
  'and get the number of degrees in',
  'between the hour and minute hands!',
  'Fail to input the time correctly,', 
  'and your head might explode!','\n\n\n'
])

def magic_time(hour, minute):
    degrees = abs((hour * 30 + minute * 0.5) - (minute * 6))
    print(degrees) 

hour   = int( input("Input the hour: ") )
minute = int( input("Input the minute: ") )

print colored('Oh, I usually have tea at that time!', 'yellow')
print colored('The degrees between your clock hands equals... ', 'red')
time.sleep(5)
 
magic_time(hour, minute)
