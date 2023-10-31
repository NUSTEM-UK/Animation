from collections import deque

queue = deque()


class TestObject():
    def __init__(self):
        # Give ourselves some attributes
        self._property1 = 1
        self._property2 = 2
        self._property3 = 3


    def method_to_call(thing):
        print(thing)


    def method_to_call_2(thing):
        print(thing, thing)


object1 = TestObject()


message_to_append = (object1, object1.method_to_call, "Hello, world!")
queue.append(message_to_append)

# queue.append(object1.method_to_call_2, "This seems to work")
# queue.append(message_to_append)
# queue.append(object1.method_to_call_2("This seems to work"))


target_object, target_method, target_value = queue.popleft()
print (target_method, target_value)

target_object.target_method(target_value)

# target_method, target_value = queue.popleft()
# target_method(target_value)


