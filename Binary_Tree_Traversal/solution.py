# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    left, right = pre_order(node.left), pre_order(node.right)
    return [node.data] + left + right

# In-order traversal
def in_order(node):
    if node is None:
        return []
    left, right = in_order(node.left), in_order(node.right)
    return left + [node.data] + right

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    left, right = post_order(node.left), post_order(node.right)
    return left + right + [node.data]

