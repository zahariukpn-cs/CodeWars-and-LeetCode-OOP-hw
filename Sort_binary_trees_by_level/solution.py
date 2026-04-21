from collections import deque

def tree_by_levels(node):
    if node is None:
        return []
    process_queue = deque([node])
    result = []
    while len(process_queue) > 0:
        node = process_queue.popleft()
        if node.left:
            process_queue.append(node.left)
        if node.right:
            process_queue.append(node.right)
        result.append(node.value)

    return result
