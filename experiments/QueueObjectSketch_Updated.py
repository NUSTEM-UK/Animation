from servo import Servo, servo2040
import easingfunctions as easing
import time
from object_sketch import *
import time
from collections import deque

class QueueServo(EasedServo):
    def __init__(self, pin, angle=90):
        super().__init__(pin, angle)
        self.angle_queue = deque((),1000)  # Using deque with max length 1000

    def queue_angle(self, angle, duration, easing_function):
        """Queue up angles to move sequentially."""
        self.angle_queue.append((angle, duration, easing_function)) # Adding Eased Servo Paramenters to anle_queue

    def process_queue(self):
        while self.angle_queue:
            angle, duration, easing_function = self.angle_queue.popleft()  # Using popleft() to remove from the left end
            self.ease_to(angle, duration, easing_function)
            while self._isMoving:
                self.update()
                time.sleep(0.01)
            time.sleep_ms(200)

        #Go to home after all queue servo execution
        self.go_home()

        # Detach the Servo
        self.detach_servo()


    def flush_queue(self):
        self._queue.clear()

    def pause_queue(self):
        self._isMoving = False

    def resume_queue(self):
        self._isMoving = True

    def queue_wait_for(self, other_servo):
        pass  # TODO: Implement synchronization with another servo

    def go_home(self):
        self.ease_to(90,4000,easing.linear)
        while self._isMoving:
                self.update()
                time.sleep(0.01)
        pass

    def detach_servo(self):
        # TODO: Implement detaching the servo
        pass




if __name__ == '__main__':

    queue_servo = QueueServo(servo2040.SERVO_1)
    queue_servo.queue_angle(-90, 4000, easing.linear)
    queue_servo.queue_angle(90, 4000, easing.easeOutExpo)
    queue_servo.queue_angle(-90, 4000, easing.easeInExpo)
    queue_servo.process_queue()
    print("Done!")
