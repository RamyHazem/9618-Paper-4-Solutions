array_nodes = [[-1, -1, -1] for i in range(20)]

free_node = 6
root_pointer = 0

def SearchValue(root, value):
    if root == -1:
        return -1

    if array_nodes[root][1] == value:
        return root
    elif array_nodes[root][1] == -1:
        return -1

    if array_nodes[root][1] < value:
        return SearchValue(array_nodes[root][0], value)

    if array_nodes[root][1] > value:
        return SearchValue(array_nodes[root][2], value)
