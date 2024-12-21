class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree_from_string(s):
    if not s or len(s) == 0:
        return None

    stack = []
    current = None

    for char in s:
        if char.isdigit():
            node = TreeNode(int(char))

            # Если стек пуст, то это корневой узел
            if len(stack) == 0:
                current = node
                stack.append(current)
            else:
                parent = stack[-1]

                # Добавляем новый узел как левый потомок
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

                stack.append(node)

        elif char == '(':
            continue

        elif char == ')':
            stack.pop()

        elif char == ',':
            # Переходим к правому поддереву
            parent = stack[-1]
            while parent.right is not None and len(stack) > 0:
                stack.pop()
            if len(stack) > 0:
                parent = stack[-1]

    return current


def post_order_traversal(root):
    if root is None:
        return
    post_order_traversal(root.left)  # Обрабатываем левое поддерево
    post_order_traversal(root.right)  # Обрабатываем правое поддерево
    print(root.value, end=" ")  # Посещаем корень


def in_order_traversal(root):
    if root is None:
        return
    in_order_traversal(root.left)  # Обрабатываем левое поддерево
    print(root.value, end=" ")  # Посещаем корень
    in_order_traversal(root.right)  # Обрабатываем правое поддерево


def pre_order_traversal(root):
    if root is None:
        return
    print(root.value, end=" ")  # Посещаем корень
    pre_order_traversal(root.left)  # Обрабатываем левое поддерево
    pre_order_traversal(root.right)  # Обрабатываем правое поддерево


def iterative_pre_order_traversal(root):
    if root is None:
        return

    stack = [root]

    while stack:
        current_node = stack.pop()
        print(current_node.value, end=" ")
        if current_node.right:
            stack.append(current_node.right)

        if current_node.left:
            stack.append(current_node.left)


# Создаём дерево
tree_root = build_tree_from_string("1(2(4)(5))(3)")

print("Прямой обход: ", end="")
pre_order_traversal(tree_root)
print("\nКонцевой обход: ", end="")
post_order_traversal(tree_root)
print("\nЦентральный обход: ", end="")
in_order_traversal(tree_root)
print("\nНе рекурсивный прямой обход: ", end="")
iterative_pre_order_traversal(tree_root)
