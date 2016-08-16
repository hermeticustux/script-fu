import time
from termcolor import colored

#OCD dicates the screen be cleared on first run
print(chr(27) + "[2J")

#always follow the six aristotelian elements of play
print '\n'.join([
  'Welcome to the clock-hands program.',
  'Give it the time in integer format',
  'and get the number of degrees in',
  'between the hour and minute hands!',
  'Fail to input the time correctly,', 
  'and your head might explode!','\n\n\n'
])

#main function that takes two arguments
def magic_time(hourhand, minutehand):
    #formulate the distance in between clock hands by reducing and calculating the difference
    degrees = abs((hourhand * 30 + minutehand * 0.5) - (minutehand * 6))
    print(degrees) 

#necessary variables
hourhand   = int( input("Input the hour: ") )
minutehand = int( input("Input the minute: ") )

#more elements of play...
print colored('Oh, I usually have tea at that time!', 'yellow')
print colored('The degrees between your clock hands equals... ', 'red')
time.sleep(3)

#result 
magic_time(hourhand, minutehand)
