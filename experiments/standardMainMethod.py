import object_sketch
import time
import selectEasing
from servo import Servo, servo2040
import easingfunctions as easing


#Taking input from user for Servo Pin number
servo_pin_number = input("Enter servo pin number: ")
servo_pin = "SERVO_"+str(servo_pin_number)

#Creating a object for EasedServo
my_servo = object_sketch.EasedServo(getattr(servo2040, servo_pin))


def main():
    while True:
        #Taking input from user for target angle and duration in milli seconds
        angle = float(input("Enter the target angle (-90 to 90 degrees): "))
        duration = float(input("Enter the duration in milliseconds: "))

        #Select easing function from selectEasing module
        easing_function_name = selectEasing.selectEasingFunction()
        if hasattr(easing, easing_function_name):
            easing_function = getattr(easing, easing_function_name)
            my_servo.ease_to(angle, duration, easing_function)

            while my_servo._isMoving:
                my_servo.update()
                time.sleep(0.01)
        else:
            print("Invalid function, try again.")
            break


if __name__ == "__main__":
    main()
