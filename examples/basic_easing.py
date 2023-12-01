from animation import EasedServo, easing, servo2040
import time

# my_servo = EasedServo(2)
my_servo = EasedServo(servo2040.SERVO_1)

print ("Testing servo movement")
print ("Standard movement")

print ("Move to -90")
my_servo.value(-90)
time.sleep_ms(1000)

print ("Move to 90")
my_servo.value(90)
time.sleep_ms(1000)

print ("Move to 0")
my_servo.value(0)
time.sleep_ms(1000)

print("ease in-out movement")
my_servo.ease_to(-90, 2000, easing.easeInOutCubic)

while my_servo.isMoving:
    my_servo.update()
    time.sleep(0.01)

time.sleep_ms(1000)
print("ease out movement")
my_servo.ease_to(90, 5000, easing.easeOutExpo)

while my_servo.isMoving:
    my_servo.update()
    time.sleep(0.01)

time.sleep_ms(1000)
print("ease in movement")
my_servo.ease_to(-90, 2000, easing.easeInExpo)

while my_servo.isMoving:
    my_servo.update()
    time.sleep(0.01)

time.sleep_ms(1000)
print("return home")
my_servo.ease_to(0, 500, easing.easeInOutCubic)
while my_servo.isMoving:
    my_servo.update()
    time.sleep(0.01)

print("Done!")

