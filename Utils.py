def sort_sub_list_by_index(sub_li, index, reverse=True): 
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of 
    # sublist lambda has been used 
    sub_li.sort(key = lambda x: x[index], reverse=reverse) 
    return sub_li
    # fonte: https://stackoverflow.com/questions/65679123/sort-nested-list-data-in-python