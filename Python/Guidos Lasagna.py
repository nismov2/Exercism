"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

   

def bake_time_remaining(elapsed_time_in_minutes):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_time = EXPECTED_BAKE_TIME - elapsed_time_in_minutes
    return remaining_time
    



def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes 

    :param number of layer: int - the number of layers in the lasagna
    :param time_for_layer: int - the estimated time for a single layer (here 2 min)
    :return: int - total preparation time

    This function takes two integers and multiply them according to the numbers of layers then give us the result of the total prep time."""
    time_for_layer = 2
    total_preparation_time = time_for_layer * number_of_layers
    
    return total_preparation_time

    
    





def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ calculate the elapsed cooking time in minutes 

    :param number of layer: int - the number of layers in the lasagna
    :param elapsed_bake_time int - elapsed cooking time
    :return: int - total time elapsed (in minutes) preparing and cooking

    This function takes two integers representing the lasagna layers and the time already spent baking and calculate the total elapsed time since."""
    prep_time = preparation_time_in_minutes(number_of_layers)
    total_elapsed_time = prep_time + elapsed_bake_time
    return total_elapsed_time
