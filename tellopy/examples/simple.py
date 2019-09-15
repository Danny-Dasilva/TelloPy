import tellopy
import av
from time import sleep
from handler import handler


# setup
drone = tellopy.Tello()
drone.connect()
drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
drone.subscribe(drone.EVENT_LOG_DATA, handler)

# need sleep at the beginning to wait for command
sleep(2)

drone.takeoff()
sleep(2)
drone.counter_clockwise(30)
sleep(2)
drone.counter_clockwise(0)
drone.clockwise(30)
sleep(2)
drone.clockwise(0)
drone.forward(10)
sleep(2)
drone.forward(0)
drone.backward(10)
sleep(2)
drone.backward(0)
drone.left(10)
sleep(2)
drone.left(0)
drone.right(10)
sleep(2)
drone.right(0)
drone.up(20)
sleep(2)
drone.down(20)
sleep(2)
drone.land()
