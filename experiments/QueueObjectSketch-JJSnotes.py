# Object heirarchy sketch for QueueServo class

from servo import Servo, servo2040
import easingfunctions as easing
import time
from object_sketch import *
from collections import deque

# Subclass of EasedServo
class QueueServo():
    # TODO: Should this be a subclass of EasedServo?
    def __init__(self, pin, angle=90):
        """Basic constructor. Creates a QueueServo object and calls the EasedServo class."""
        self._servo = EasedServo(pin)
        print("called QueueServo Constructor")

        # TODO: Needs an instance of a queue container class
        #       Look in collections? Dequeue? https://docs.micropython.org/en/latest/library/collections.html
        self._queue = deque()

        # TODO: add home position (or should that be in EasedServo? -- no, probably here)
        # TODO: Add flags for end-of-animation-sequence options:
        #       - Queue emptied, queue pause at end of sequence
        #       - Queue emptied, pause has happened, queue to home position
        #       - Queue emptied, pause has happened, gone home, so now detach servo to prevent jitter/buzz

        # TODO: Register this servo with a global queue controller object?
        #       Then could call update() on that global object, in our loop?


    def queue_ease_to(self, angle, duration, easing=easing.linear):
        self._servo.ease_to(angle=-90, duration=4000, easing_function=easing)


    def update(self):
        self._servo.update()
        # TODO: Check if this is duplicated?
        if self._servo.proportion_complete > 1:
            self._servo._isMoving = False
        if self._servo._isMoving == False:
            # Ended a movement, so check if there's anything else in the queue:
            if len(self._queue) > 0:
                # TODO: Pop the next item off the queue and start it
                ### TODO: Depends how you encode data in the queue, but however we do it, we'll call it here
                pass
            else:
                # Start the pause / go home / detach sequence
                # (note flags in constructor)
                pass


    def flush_queue(self):
        """Empty the queue."""
        pass


    def pause_queue(self):
        """Pause the animation queue."""
        pass


    def resume_queue(self):
        """Resume the animation queue."""
        pass


    def queue_wait_for(self, other_servo):
        """Queue a wait for another servo to signal us to restart."""
        pass



    def queue_animation_sequence(self, animation_type, start_angle, end_angle, speed):

        if animation_type == 'waves':
            print("called Queue Animation Sequence")
            # Calculate the number of steps based on the speed
            num_steps = abs(end_angle - start_angle) // speed

            # Define the easing function based on the animation type
            if start_angle < end_angle:
                easing_function = easing.easeInOutCubic
            else:
                easing_function = easing.easeInOutCubic

            # Queue the animation steps
            for step in range(num_steps):
                # Calculate the current angle for this step
                angle = start_angle + (end_angle - start_angle) * (step / num_steps)

                # Queue the angle with the calculated easing function and speed
                self.queue_ease_to(angle, speed, easing_function)

        else:
            # Handle other animation types here
            pass


if __name__ == '__main__':

    # servo_gulls = QueueServo(servo2040.SERVO_1)
    # servo_gulls.queue_ease_to(-90, 3000, easing.easeInExpo)
    # while servo_gulls._servo._isMoving:
    #     servo_gulls.update()
    #     time.sleep(0.01)

    servo_waves = QueueServo(servo2040.SERVO_1)
    servo_waves.queue_animation_sequence('waves', 30, 90,250)




    # time.sleep_ms(2000)
    # servo_waves = QueueServo(servo2040.SERVO_1)
    # servo_waves.queue_ease_to(-90, 3000, easing.linear)
    # #print(servo_gulls._servo.proportion_complete)
    # while servo_waves._servo._isMoving:
    #     servo_waves.update()
    #     time.sleep(0.01)


    # time.sleep_ms(2000)
    # servo_life_boats = QueueServo(servo2040.SERVO_1)
    # servo_life_boats.queue_ease_to(-90, 3000, easing.easeOutSine)
    # #print(servo_gulls._servo.proportion_complete)
    # while servo_life_boats._servo._isMoving:
    #     servo_life_boats.update()
    #     time.sleep(0.01)

