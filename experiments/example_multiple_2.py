from object_sketch import EasedServo, easing, time, servo2040
import random
from plasma import WS2812


# LED config
SPEED = 5
BRIGHTNESS = 0.4
UPDATES_PER_SECOND = 100
SLEEP_TIME = 1.0 / UPDATES_PER_SECOND

led_bar = WS2812(servo2040.NUM_LEDS, 1, 0, servo2040.LED_DATA)
led_bar.start()
offset = 0.0

# Servo config
servo_config = [
    {"pin": servo2040.SERVO_1,  "init_angle": -13, "min_angle": -52, "max_angle": 26},
    {"pin": servo2040.SERVO_3,  "init_angle":  -3, "min_angle": -36, "max_angle": 30},
    {"pin": servo2040.SERVO_4,  "init_angle": -17, "min_angle": -54, "max_angle": 20},
    {"pin": servo2040.SERVO_5,  "init_angle":  -9, "min_angle": -32, "max_angle": 14},
    {"pin": servo2040.SERVO_18, "init_angle": -15, "min_angle": -50, "max_angle": 20},
]

# Choose some easing functions
easing_functions = [
    easing.easeInCubic,
    easing.easeOutCubic,
    easing.easeInOutQuad,
    easing.easeInOutQuart,
    easing.easeInExpo,
    easing.easeOutExpo,
    easing.easeInOutCubic,
    easing.easeInOutCubic,
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

# Move the servos to random angles within their ranges, over random time period
# using random easing functions
for servo in servos:
    servo.ease_to(
        random.randint(servo._min_angle, servo._max_angle),
        random.randint(500, 3000),
        random.choice(easing_functions)
    )

# Now loop, checking if any servo has stopped moving

while True:
    # Update the servos
    for servo in servos:
        if servo._isMoving:
            servo.update()
        else:
            print("Servo at pin " + str(servo._servo.pin) + " has stopped moving.")
            # Move the servo to a new random angle within its range
            servo.ease_to(
                random.randint(servo._min_angle, servo._max_angle),
                random.randint(500, 3000),
                random.choice(easing_functions)
            )

    # Update the LED bar
    offset += SPEED / 1000.0
    for i in range(servo2040.NUM_LEDS):
        hue = float(i) / servo2040.NUM_LEDS
        led_bar.set_hsv(i, hue + offset, 1.0, BRIGHTNESS)

    # Pause for a moment to allow the servos to move
    time.sleep(SLEEP_TIME)
