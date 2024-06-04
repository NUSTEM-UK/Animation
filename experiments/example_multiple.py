from object_sketch import EasedServo, easing, time, servo2040
import random

servo_config = [
    {"pin": servo2040.SERVO_1, "init_angle": 0, "min_angle": -30, "max_angle": 30},
    {"pin": servo2040.SERVO_2, "init_angle": 0, "min_angle": -30, "max_angle": 30},
    {"pin": servo2040.SERVO_3, "init_angle": 0, "min_angle": -30, "max_angle": 30},
]

# Initialise the servos
servos = []
for servo in servo_config:
    servos.append(
        EasedServo(
            servo["pin"],
            angle=servo["init_angle"],
            min_angle=servo["min_angle"],
            max_angle=servo["max_angle"],
        )
    )

# Move the servos to random angles within their ranges. over random time period
for servo in servos:
    servo.ease_to(
        random.randint(servo._min_angle, servo._max_angle),
        random.randint(500, 3000),
        easing.easeInOutCubic,
    )

# Now loop, checking if any servo has stopped moving

while True:
    for servo in servos:
        if servo._isMoving:
            servo.update()
        else:
            print("Servo at pin " + str(servo._servo.pin) + " has stopped moving.")
            # Move the servo to a new random angle within its range
            servo.ease_to(
                random.randint(servo._min_angle, servo._max_angle),
                random.randint(500, 3000),
                easing.easeInOutCubic,
            )
    # Pause for a moment to allow the servos to move
    time.sleep(0.01)
