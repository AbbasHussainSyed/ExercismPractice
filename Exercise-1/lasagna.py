"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40
EACH_LAYER_TIME = 2

def bake_time_remaining(actual_minutes):
    """
    Returns the remaining bake time.
    This function takes the time already in the oven and calculates the 
    remaining time needed to bake the lasagna.
    """
    return EXPECTED_BAKE_TIME - actual_minutes


def preparation_time_in_minutes(number_of_layers):
    """ Returns lasagna preparation time.
    This function takes the number of layers and calculates the 
    time needed to prepare them all
    """
    return number_of_layers * EACH_LAYER_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Returns elapsed cooking time.
    This function takes two numbers representing the number of layers & the time 
    already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
