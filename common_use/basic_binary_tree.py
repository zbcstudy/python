class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display(tree):
    if tree is None:
        return
    if tree.left is not None:
        display(tree.left)
    print(tree.left)

    if tree.right is not None:
        display(tree.right)
    return


def depth_of_tree(tree):
    if tree is None:
        return 0
    else:
        dept_l_tree = depth_of_tree(tree.left)
        dept_r_tree = depth_of_tree(tree.right)
        if dept_l_tree > dept_r_tree:
            return 1 + dept_l_tree
        else:
            return 1 + dept_r_tree


def is_full_binary_tree(tree):
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return (is_full_binary_tree(tree.left)) and is_full_binary_tree(tree.right)
    else:
        return False


def main():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print(is_full_binary_tree(tree))
    print(depth_of_tree(tree))
    print("Tree is: ")
    display(tree)


if __name__ == '__main__':
    main()
