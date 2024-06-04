from object_sketch import EasedServo, easing, time, servo2040
import random

servo_config = [
    {"pin": servo2040.SERVO_1,  "init_angle": -13, "min_angle": -52, "max_angle": 26},
    {"pin": servo2040.SERVO_3,  "init_angle":  -3, "min_angle": -36, "max_angle": 30},
    {"pin": servo2040.SERVO_4,  "init_angle": -17, "min_angle": -54, "max_angle": 20},
    {"pin": servo2040.SERVO_5,  "init_angle":  -9, "min_angle": -32, "max_angle": 14},
    {"pin": servo2040.SERVO_18, "init_angle": -15, "min_angle": -50, "max_angle": 20},
]

# Leftover while testing servo jitter, which seemed to be ... weird. Picking the right
# five servo channels cured it, in this case. WIth SERVO_2 in use, SERVO_18 also jittered.
# servo_config = [
#     {"pin": servo2040.SERVO_1,  "init_angle": -13, "min_angle": -52, "max_angle": 26},
#     # {"pin": servo2040.SERVO_2,  "init_angle":  -3, "min_angle": -36, "max_angle": 30},
#     {"pin": servo2040.SERVO_3,  "init_angle":  -3, "min_angle": -36, "max_angle": 30},
#     {"pin": servo2040.SERVO_4,  "init_angle":  -3, "min_angle": -36, "max_angle": 30},
#     {"pin": servo2040.SERVO_5,  "init_angle":  -3, "min_angle": -36, "max_angle": 30},
#     # {"pin": servo2040.SERVO_6,  "init_angle": -17, "min_angle": -54, "max_angle": 20},
#     # {"pin": servo2040.SERVO_7,  "init_angle":  -9, "min_angle": -32, "max_angle": 14},
#     # {"pin": servo2040.SERVO_8,  "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_9,  "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_10, "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_11, "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_12, "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_13, "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_14, "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_15, "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_16, "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     # {"pin": servo2040.SERVO_17, "init_angle": -15, "min_angle": -50, "max_angle": 20},
#     {"pin": servo2040.SERVO_18, "init_angle": -15, "min_angle": -50, "max_angle": 20},
# ]

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
    # time.sleep(0.01)
