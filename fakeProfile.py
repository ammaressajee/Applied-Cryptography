from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout


password = raw_input()
timings = raw_input()
#print "password = {}".format(password)
#print "timings = {}".format(timings)

password = password.split(",")
password = password[:len(password)/2 + 1]
password = "".join(password)

print "password = {}".format(password)

timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings)/2 + 1]
keyinterval = timings[len(timings)/2 + 1:]

print "key press times = {}".format(keypress)
print "key intervals = {}".format(keyinterval)

keyboard = Controller()

for i in range(len(password)):
    keyboard.press(password[i])
    sleep(keypress[i])
    keyboard.release(password[i])
    if i == range(len(password) -1):
        sleep(keyinterval[i])


tcflush(stdout, TCIFLUSH)
print
