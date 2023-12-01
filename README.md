# Animation

Working repository for micropython-based servo (and LED?) animation system.

As of 2023-12-01 this is in no way ready for anyone else to use, but:

## Objectives

MicroPython lacks a smoothed servo library like the excellent [ServoEasing](https://github.com/ArminJo/ServoEasing) on Arduino. In one application of ServoEasing, we've also found it useful to have the concept of servo _queues_, where multiple sequential movements are stacked up. The servo can then play through an animation sequence semi-automatically. Our (unpublished, because it's horribly scrappy) Arduino implementation also includes queuable commands which allow one servo to 'wait for' a signal from another, which allows relatively complex multi-servo animation sequences to be coded with a reasonably natural syntax.

In this project, we're exploring something similar for MicroPython.

## Target hardware

We're going to build on the excellent [Servo class](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/servo) developed by Pimoroni for their [Servo2040](https://shop.pimoroni.com/products/servo-2040?variant=39800591679571) board, though we also intend that our code works on a plain Raspberry Pi Pico board, so long as it's running [Pimoroni's Micropython distribution](https://github.com/pimoroni/pimoroni-pico/releases).

## Other notes

This is all a bit nascent and we may not get very far, but the plan goes something like:

1. Subclass Servo with an EasedServo class, which allows eased movement
(this is at least partly functional as of this writing).

2. Subclass EasedServo with a QueueServo class, which adds animation sequence queue handling
(this is also partly functional)

3. Tidy everything up, remove early experiments
4. Documentation and examples
5. Work out we've done it all really badly, and either give up or go back to step 0.

This is the first time we've written a python module which might be intended for use by others. We've only a limited idea of what we're doing. But we have AI assistance now, what could possibly go wrong?

## Timescale

We're working in November/December 2023 with the hope of getting something at least visible before the end of the teaching term. Efforts will doubtless continue into 2024.

## Acknowledgments

Our thanks to Northumbria University for supporting a short-term studentship to get this project started.

## Contact

Jonathan Sanderson, Northumbria University. [jonathan.sanderson@northumbria.ac.uk](mailto:jonathan.sanderson@northumbria.ac.uk).
