
class Frogs:

    class Node:

        def __init__(self, data, parent=None, children=[]):
            self.data = data
            self.parent = parent
            self.children = children

    def __init__(self, root):
        self.root = root

    def add_item(self, value, parent):
        stack = [self.root]
        current_height, max_height = 0, 0

        while stack:
            current = stack.pop()
            current_height += 1
            for child in current.children:
                stack.append(child)

            if not current.children:
                if current_height > max_height:
                    max_height = current_height
                current_height -= 1

    def generate_possible_moves(self, position):
        # >>>_<<<
        moves = []
        for i in range(len(position) - 2):
            if position[i] == '>':
                new_move = list(position)
                new_move[i] = "_"
                new_move[i + 2] = ">"
                moves.append(''.join(new_move))
            elif position[i + 1] == "_":
                new_move = list(position)
                new_move[i] = "_"
                new_move[i + 2] = ">"
                moves.append(''.join(new_move))
            elif position[i + 2] == "<"



    # def number_of_frogs(self, n):
    #     return n * ">" + "_" + n * "<"

    def can_move(self, root):
        pass


# def permutations():
#     list2Perm = ['>1', '>2', '>3', '_', '1<', '2<', '3<']
#     listPerm = [[a, b, c, d, e, f]
#                 for a in list2Perm
#                 for b in list2Perm
#                 for c in list2Perm
#                 if(a != b and b != c and a != c)
#                 ]
#     return listPerm

print(permutations())

