import math

class Node:
    def __init__(self, pair, ):
        self.pair = pair
        self.sum_child = None
        self.product_child = None
        self.concat_child = None

    def add_child_nodes(self, number, with_concat = False):
        self.sum_child = Node([sum(self.pair), number])
        self.product_child = Node([math.prod(self.pair), number])
        if with_concat:
            self.concat_child = Node([int(str(self.pair[0]) + str(self.pair[1])), number])

def add_children(node, number, with_concat = False):
    if node.sum_child is None:
        node.add_child_nodes(number, with_concat)
        return
    add_children(node.sum_child, number, with_concat)
    add_children(node.product_child, number, with_concat)
    if with_concat:
        add_children(node.concat_child, number, with_concat)

def build_tree(list_of_members: list[int], with_concat = False) -> Node:
    root_node = Node([list_of_members[0], list_of_members[1]])
    for member in list_of_members[2:]:
        if member == None:
            continue
        add_children(root_node, member, with_concat)

    return root_node

def get_totals(node: Node, totals, with_concat = False):
    if node.sum_child is None:
        totals.append(sum(node.pair))
        totals.append(math.prod(node.pair))
        if with_concat:
            totals.append(int(str(node.pair[0]) + str(node.pair[1])))
        return totals

    totals = get_totals(node.sum_child, totals, with_concat)
    totals = get_totals(node.product_child, totals, with_concat)
    if with_concat:
        totals = get_totals(node.concat_child, totals, with_concat)
    return totals

if __name__ == "__main__":
    total_calibration_result = 0
    with open("/home/fl/PycharmProjects/AOC2024/day_seven/input.txt") as file:
        for line in file.readlines():
            calibration_parts = line.split(" ")
            calibration_value = int(calibration_parts[0].replace(":", ""))
            calibration_equation_members = [int(member) for member in calibration_parts[1:]]

            if len(calibration_equation_members) == 2:
                if calibration_value == calibration_equation_members[0] + calibration_equation_members[1] or calibration_value == calibration_equation_members[0] * calibration_equation_members[1] or calibration_value == int(str(calibration_equation_members[0]) + str(calibration_equation_members[1])):
                    total_calibration_result += calibration_value
            else:
                root_node = build_tree(calibration_equation_members, True)

                totals = get_totals(root_node, [], True)
                if calibration_value in totals:
                    total_calibration_result += calibration_value

    print(total_calibration_result)




