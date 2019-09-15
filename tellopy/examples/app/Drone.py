
from time import sleep
import tellopy
import time
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


class Drone():
    def __init__(self):
        self.drone = tellopy.Tello()
        self.drone.connect()
        self.drone.subscribe(self.drone.EVENT_FLIGHT_DATA, handler)
        self.drone.subscribe(self.drone.EVENT_LOG_DATA, handler)
        
    def counter_clockwise(self, speed):
        self.drone.counter_clockwise(speed)
    def clockwise(self, speed):
        self.drone.clockwise(speed)
    def forward(self, speed):
        self.drone.forward(speed)
    def backward(self, speed):
        self.drone.backward(speed)
    def left(self, speed):
        self.drone.left(speed)
    def right(self, speed):
        self.drone.right(speed)
    def up(self, speed):
        self.drone.up(speed)
    def down(self, speed):
        self.drone.down(speed)
        
    def takeoff(self):
        time.sleep(.5)
        self.drone.takeoff()
    def land(self):
        time.sleep(.5)
        self.drone.land()
    def sleep(self, sec):
        print("before")
        time.sleep(sec)
        print("after")
        drone.counter_clockwise(0)
        drone.clockwise(0)
        drone.forward(0)
        drone.backward(0)
        drone.left(0)
        drone.right(0)
        drone.up(0)
        drone.down(0)

