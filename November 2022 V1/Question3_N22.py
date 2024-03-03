array_nodes = [[-1, -1, -1] for i in range(20)]

array_nodes = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]

free_node = 6
root_pointer = 0


def SearchValue(root, value):
    if root == -1:
        return -1

    if array_nodes[root][1] == value:
        return root
    elif array_nodes[root][1] == -1:
        return -1

    if array_nodes[root][1] > value:
        return SearchValue(array_nodes[root][0], value)

    if array_nodes[root][1] < value:
        return SearchValue(array_nodes[root][2], value)


def post_order_traversal(root):
    if array_nodes[root][0] != -1:
        post_order_traversal(array_nodes[root][0])
    if array_nodes[root][2] != -1:
        post_order_traversal(array_nodes[root][2])
    print(array_nodes[root][1])


answer = SearchValue(root_pointer, 15)
if answer == -1:
    print("Value not found in the tree")
else:
    print(f"Value was found at index: {answer}")
post_order_traversal(root_pointer)
