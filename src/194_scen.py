#Sorting a Python list by two criteria


There is no built-in function in Python to sort by two criteria, but the following code will accomplish what you want:

def sort_by_two_criteria(lst, key1, key2):
    """
    Sort a list of tuples by two criteria.
    
    Parameters
    ----------
    lst : list
        A list of tuples.
    key1 : function
        A function that takes a tuple and returns a value to sort by.
    key2 : function
        A function that takes a tuple and returns a value to sort by.
        
    Returns
    -------
    list
        The sorted list.
    """