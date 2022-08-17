list_of_lists = [10, [20,30], [[40,50,60]], [[[70]]], [[[[[[[80]]]]]]]]

flat_list = []

def flatten_list(list_of_lists):

    for item in list_of_lists:

        # if type(item) == list:

        if isinstance(item, list):

            flatten_list(item)

        else:

            flat_list.append(item)

   

    return flat_list

flatten_list(list_of_lists)

print(flat_list)