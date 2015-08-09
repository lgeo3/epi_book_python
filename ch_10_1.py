from tree import BinaryTree

def is_balanced(a_tree):
    """
    return true if for each node in the tree, difference in height of left and right subtree is at most one

    :param a_tree:
    :return:
    """

    # brute force .. using recursion

    if a_tree.is_empty:
        return True

    return is_balanced(a_tree.left) and is_balanced(a_tree.right) and abs(a_tree.right.height() - a_tree.left.height())<=1

def is_balanced_(a_tree):
    """
    ok the complexity is O(n) and the space complexity is O(h)
    :param a_tree:
    :return:
    """
    def check_balanced(a_tree):
        if a_tree.is_empty:
            return True, -1

        left_res = check_balanced(a_tree.left)
        if left_res[0] is False:
            return False, 0

        right_res = check_balanced(a_tree.right)
        if right_res[0] is False:
            return False, 0

        is_balanced = abs(right_res[1] - left_res[1]) <= 1
        height = max(right_res[1], left_res[1]) + 1
        return is_balanced, height

    res, height = check_balanced(a_tree)
    return res



LeftLeftLeft = BinaryTree(28)
LeftLeftRight = BinaryTree(0)
LeftLeft = BinaryTree(271, LeftLeftLeft, LeftLeftRight)
LeftRightRight = BinaryTree(3, BinaryTree(17))
LeftRight = BinaryTree(561, None, LeftRightRight)
RightRight = BinaryTree(271)
RightLeft = BinaryTree(2)
Left = BinaryTree(6, LeftLeft, LeftRight)
Right = BinaryTree(6, RightLeft, RightRight)
A = BinaryTree(314, Left, Right)

print(is_balanced(A))
assert(False == is_balanced(A))
assert(False == is_balanced_(A))
