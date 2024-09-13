from typing import List



def get_kwarg_values(kwargs:dict, keys:List[str])-> List:
    '''returns the values of kwargs keys in a list'''
    return [kwargs.get(key) for key in keys]
