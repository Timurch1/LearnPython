# Алгоритм обхода бинарного дерева в ширину

while v:
    vn = []
    for x in v:
        print(x.data)
        if x.left:
            vn += [x.left]
        if x.right:
            vn += [x.right]
    v = vn

# Алгоритм обхода бинарного дерева в глубину

def show_tree(self, node):
    if node is None:
        return

    self.show_tree(node.left)
    print(node.data)
    self.show_tree(node.right)