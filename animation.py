from servo import Servo, servo2040
import easingfunctions as easing
import time

class EasedServo(Servo):
    """Subclass of Servo object to support easing functions."""

    # TODO: @property and @setter decorators work in Micropython now, I think?


    def __init__(self, pin, angle=090):
        """Basic constructor. Creates a Servo object and sets the angle to the given value, defaulting to 0.

        We're assuming that servos go -90/+90 in micropython land.
        TODO: Check this assumption
        """
        super().__init__(pin)
        self.enable()
        self.angle = angle
        self.value(angle)
        # Are we using underscores to indicate private variables?
        self._easing_function = easing.linear
        self.isMoving=True


    def ease_to(self, angle, duration, easing_function=easing.linear):
        """Sets the target angle and duration, and receives a function to use for easing."""
        self._start_angle = self.angle
        self._target_angle = angle
        self._easing_function = easing_function
        # Start a millisecond timer
        self._base_time = time.ticks_ms()
        self._duration = duration
        self.isMoving = True
        print(
            ">>> Starting move from: "
            + str(self._start_angle)
            + " to: "
            + str(angle)
            + " in "
            + str(duration)
            + "ms"
            + " using "
            + easing_function.__name__
            + " easing."
        )

    def value(self, angle):
        """Set the servo angle.

        Need to override the superclass method to update the angle property."""

        self.angle = angle

        # Uncomment this line to spew diagnostics to the console
        # print (">>> Setting angle to: " + str(angle))

        # Call the superclass method to actually set the servo angle
        super().value(angle)


    def update(self):
        """Handle servo angle updates."""
        # How far through the movement duration are we?
        proportion_complete = (time.ticks_ms() - self._base_time) / self._duration

        # Calculate the new angle
        self.angle = (
            self._easing_function(proportion_complete)
            * (self._target_angle - self._start_angle)
            + self._start_angle
        )

        # Set the servo position
        self.value(self.angle)

        # Are we done?
        if proportion_complete > 1:
            # Set the angle to the target angle, so we haven't overshot for the
            # start of the next movement.
            self.angle = self._target_angle
            # We're done!
            self.isMoving = False
