import easingfunctions as easing

#Select any of the below easing function by user

def selectEasingFunction():

    # A dictionary to map function names to the actual function objects
    easing_functions = {
        "linear": easing.linear,
        "easeInSine": easing.easeInSine,
        "easeOutSine": easing.easeOutSine,
        "easeInOutSine": easing.easeInOutSine,
        "easeInQuad": easing.easeInQuad,
        "easeOutQuad": easing.easeOutQuad,
        "easeInOutQuad": easing.easeInOutQuad,
        "easeInCubic": easing.easeInCubic,
        "easeOutCubic": easing.easeOutCubic,
        "easeInOutCubic": easing.easeInOutCubic,
        "easeInQuart": easing.easeInQuart,
        "easeOutQuart": easing.easeOutQuart,
        "easeInOutQuart": easing.easeInOutQuart,
        "easeInQuint": easing.easeInQuint,
        "easeOutQuint": easing.easeOutQuint,
        "easeInOutQuint": easing.easeInOutQuint,
        "easeInExpo": easing.easeInExpo,
        "easeOutExpo": easing.easeOutExpo,
        "easeInOutExpo": easing.easeInOutExpo,
        "easeInCirc": easing.easeInCirc,
        "easeOutCirc": easing.easeOutCirc,
        "easeInOutCirc": easing.easeInOutCirc
    }

    print("Available easing functions:")
    for func_name in easing_functions.keys():
        print(func_name)

    selected_function = input("Select an easing function: ")

    # Check if the selected function is valid
    if selected_function in easing_functions:
        return selected_function
    else:
        return "Invalid Function, try again."
