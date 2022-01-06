from typing import List, Tuple
import itertools



def flatten(strings: List[List[Tuple[str]]]) -> List[str]:
    """flatten the List[List[Tuple[str]]] from sqlalchemy"""
    flatten_list = itertools.chain.from_iterable(strings)
    return flatten_list

