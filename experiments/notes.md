# Notes and links on potentially useful bits of Python

## Interrupts

Micropython has a `Timer` module: [docs](https://docs.micropython.org/en/latest/library/machine.Timer.html). On RP2 (RP2040 / Pico) ([docs](https://docs.micropython.org/en/latest/rp2/quickref.html#timers)) this is currently a software timer, but it may work well enough. Use something like:

```python
from machine import Timer

def updateServosCallback() {
    servo_controller.update()
}

my_timer = Timer(period=50, mode=Timer.PERIODIC, callback=updateServosCallback)
```

If we had a ServoController object with which QueueServos/EasedServos registered themselves, we could call a central `update()` method on a 50Hz timer using something like this.

Caveats: you're not supposed to allocate memory in a Timer callback. So no pushing to an array, for example. Hmm.

There's also a `micropython.schedule()` call, which is a bit mysterious to me at present. [Micropython docs](https://docs.micropython.org/en/latest/reference/isr_rules.html#isr-rules) [Forum thread](https://forum.micropython.org/viewtopic.php?t=8745)

