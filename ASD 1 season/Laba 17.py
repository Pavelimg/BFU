from graphviz import Digraph


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


tree_root = build_tree_from_string("1(2(4)(5))(3)")


def add_node(root, node):
    if root is None:
        return TreeNode(node)

    if node < root.value:
        root.left = add_node(root.left, node)

    elif node > root.value:
        root.right = add_node(root.right, node)

    return root


def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, key):
    if root is None:
        return root

    # Ищем узел с заданным ключом
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Нашли узел, который нужно удалить
        # Случай 1: Нет детей
        if root.left is None and root.right is None:
            root = None
        # Случай 2: Есть только правое поддерево
        elif root.left is None:
            root = root.right
        # Случай 3: Есть только левое поддерево
        elif root.right is None:
            root = root.left
        # Случай 4: Есть оба поддерева
        else:
            temp = find_min_node(root.right)
            root.val = temp.val
            root.right = delete_node(root.right, temp.val)

    return root


def print_tree(node, level=0):
    if node is None:
        return "-" * 4 * level + "None\n"
    result = "-" * 4 * level + f"({node.value})\n"
    result += print_tree(node.left, level + 1)
    result += print_tree(node.right, level + 1)
    return result

# Пример
print(print_tree(tree_root))
delete_node(tree_root, 3)
print(print_tree(tree_root))
add_node(tree_root, 7)
print(print_tree(tree_root))

# Далее можно вписывать свои команды вида "add 5" или "del 4"
while True:
    command = input()
    if command.startswith("add"):
        add_node(tree_root, int(command.split()[1]))
    elif command.startswith("del"):
        delete_node(tree_root, int(command.split()[1]))
    elif command.startswith("out"):
        print(print_tree(tree_root))
    else:
        break
