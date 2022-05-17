from djitellopy import tello
from time import sleep

# drone takes off
me = tello.Tello()
me.connect()
me.takeoff()
me.move_up(120)
# Forward
me.move_forward(500)
me.move_forward(300)
sleep(.25)
me.rotate_counter_clockwise(90)
sleep(.25)
#sidways shuffle
me.move_forward(400)
sleep(.25)

me.rotate_counter_clockwise(90)
sleep(.25)
#goin home
me.move_forward(500)
me.move_forward(300)
sleep(.25)
me.rotate_counter_clockwise(90)
sleep(.25)
#going to bed
me.move_forward(400)
sleep(.25)
me.rotate_counter_clockwise(90)
sleep(.25)
#shleep
me.land()
# drone moves forward, rotates, waits, and lands.
