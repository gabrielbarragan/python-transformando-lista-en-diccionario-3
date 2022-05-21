def convert_list_to_dict(nested_list: list= []) -> dict:
    """get a nested list and return a dict
    input-> nested_list: list
    output-> dict"""

    my_dict = {key[0]:key[1] for key in nested_list }
    
    return my_dict
