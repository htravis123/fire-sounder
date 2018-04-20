import pyglet
import sys
import time

print("/-----------------\\")
print("|00000000000000000|")
print("|0               0|")
print("|0               0|")
print("|0     /---\     0|")
print("|0     |   |     0|")
print("|0     |   |     0|")
print("|0     \---/     0|")
print("|0               0|")
print("|0               0|")
print("|00000000000000000|")
print("\\-----------------/")
print("I'm a fire sounder!")
tone = pyglet.resource.media('sounder.wav')
tone.play()
time.sleep(10)
sys.exit()
