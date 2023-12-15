from servo import Servo, servo2040
import easingfunctions as easing
import time
from collections import deque

class QueueServo(EasedServo):
    def __init__(self, pin, angle=90):
        super().__init__(pin, angle)
        self._queue = deque((),1000)
        self._at_home = False
        self._detach_after_sequence = False
        

    def queue_ease_to(self, angle, duration, easing_function=easing.linear):
        self._queue.append((angle, duration, easing_function))
        self._servo.ease_to(angle=-90, duration=4000, easing_function=easing)

    def update(self):
        super().update()
        if not self._isMoving:  # Check if the servo is not moving
            if self._queue:
                next_angle, next_duration, next_easing = self._queue.popleft()
                self.ease_to(next_angle, next_duration, next_easing)
            elif not self._at_home:
                self.go_home()
                if self._detach_after_sequence:
                    self.detach_servo()

    def flush_queue(self):
        self._queue.clear()

    def pause_queue(self):
        self._isMoving = False

    def resume_queue(self):
        self._isMoving = True

    def queue_wait_for(self, other_servo):
        pass  # Implement synchronization with another servo

    def go_home(self):
        # Implement going to home position
        pass

    def detach_servo(self):
        # Implement detaching the servo
        pass


if __name__ == '__main__':
    servo_waves = QueueServo(servo2040.SERVO_1)
    servo_waves.queue_ease_to(-90, 3000, easing.easeInExpo)
    print("Done")
    servo_waves.queue_ease_to(90, 3000, easing.easeInExpo)
    print("Done")

    servo_waves.queue_ease_to(-90, 3000, easing.easeInExpo)
    print("Done")

    while servo_waves._isMoving:
        servo_waves.update()
        time.sleep(0.01)