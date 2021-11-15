#
# The first version of our function!
# Write doc strings 
#
def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities or tuples
    Intensities are defined as local maxima if the
    intensities of the elements in the list before and after
    are smaller than the peak we want to determine.

    For example given a list:
        [1, 5, 6, 4, 1, 2, 3, 2]

    We expect 6 and 3 to be returned.
    

    Args:
        list_of_intensities (list of floats, ints or tuple of ints): a list of
            numeric values

    Returns:
        list of floats or tuples: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)

    """
    maxima = []
    
    for pos in range(1, len(list_of_intensities)):

        if list_of_intensities[pos]>list_of_intensities[pos-1] and list_of_intensities[pos]>list_of_intensities[pos+1]:
            maxima.append(list_of_intensities[pos])

    return maxima
