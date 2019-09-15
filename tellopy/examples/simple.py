import tellopy
import av
from time import sleep



prev_flight_data = None


def handler(event, sender, data, **args):
    global prev_flight_data
    global flight_data
    global log_data
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        if prev_flight_data != str(data):
            print(data)
            prev_flight_data = str(data)
        flight_data = data
    elif event is drone.EVENT_LOG_DATA:
        log_data = data
    else:
        print('event="%s" data=%s' % (event.getname(), str(data)))




drone = tellopy.Tello()
drone.connect()
drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
drone.subscribe(drone.EVENT_LOG_DATA, handler)

sleep(3)

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
