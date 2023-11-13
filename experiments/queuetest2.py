# Brazen cheat from ChatGPT 3.5
from collections import deque


class SomeObject:
    def some_method(self, param):
        print(f"Some method called with parameter: {param}")


class AnotherObject:
    def another_method(self, param):
        print(f"Another method called with parameter: {param}")


# Create a deque to store object-reference-and-method-parameter pairs
my_queue = deque()

# Define objects, methods, and parameters
object1 = SomeObject()
method1 = object1.some_method
param1 = "Parameter 1"

object2 = AnotherObject()
method2 = object2.another_method
param2 = "Parameter 2"

# Queue the object, method, and parameter as a tuple
my_queue.append((object1, method1, param1))
my_queue.append((object2, method2, param2))

# To dequeue and execute the methods on the objects with parameters
while my_queue:
    obj, method, param = my_queue.popleft()
    method(param)  # Call the method on the object with the provided parameter

# Here, we call the methods with their respective parameters in the order they were added to the queue.

# We're not using the reference to the object obj above, so it can be removed:
my_queue.append((method1, param2))
my_queue.append((method2, param1))
while my_queue:
    method, param = my_queue.popleft()
    method(param)  # Call the method on the object with the provided parameter


# Implications for our servo queueing system:
# def queueEaseTo(angle, time, easing):
#     ._self.queue.append((self, self._servo.easeTo, angle, time, easing))

# method, param_angle, param_time, param_easing = _self.queue.popleft()
# method(param_angle, param_time, param_easing)
