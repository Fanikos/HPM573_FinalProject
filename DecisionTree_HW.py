class Node:
    """ base (master) class for nodes """
    def __init__(self, name, cost):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        """

        self.name = name
        self.cost = cost

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """

    def get_expected_health(self):
        """

        :return: expected health of nodes
        """


class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        :param future_nodes: (list) future nodes connected to this node
        :param probs: (list) probability of future nodes
        """

        Node.__init__(self, name, cost)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        E[cost] = (cost of visiting this node)
                  + sum_{i}(probability of future node i)*(E[cost of future node i])
        """

        # expected cost initialized with the cost of visiting the current node
        exp_cost = self.cost

        # go over all future nodes
        i = 0
        for node in self.futureNodes:
            # increment expected cost by
            # (probability of visiting this future node) * (expected cost of this future node)
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1

        return exp_cost

    def get_expected_health(self):
        exp_health = 0
        i = 0
        for node in self.futureNodes:
            exp_health += self.probs[i]*node.get_expected_health()
            i += 1
        return exp_health


class TerminalNode(Node):

    def __init__(self, name, cost, health):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        """

        Node.__init__(self, name, cost)
        self.health = health

    def get_expected_cost(self):
        """
        :return: cost of this visiting this terminal node
        """
        return self.cost

    def get_expected_health(self):
        return self.health


class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        :param future_nodes: (list) future nodes connected to this node
        (assumes that future nodes can only be chance or terminal nodes)
        """

        Node.__init__(self, name, cost)
        self.futureNode = future_nodes

    def get_expected_costs(self):
        """ returns the expected costs of future nodes
        :return: a dictionary of expected costs of future nodes with node names as dictionary keys
        """

        # a dictionary to store the expected cost of future nodes
        exp_costs = dict()
        # go over all future nodes
        for node in self.futureNode:
            # add the expected cost of this future node to the dictionary
            exp_costs[node.name] = self.cost + node.get_expected_cost()

        return exp_costs

    def get_expected_health(self):
        exp_healths = dict()
        for node in self.futureNode:
            exp_healths[node.name] = node.get_expected_health()


#######################
# See figure DT3.png (from the project menu) for the structure of this decision tree
########################

# create the terminal nodes
T1 = TerminalNode('T1', 10, 0.5)
T2 = TerminalNode('T2', 20, 0.6)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.8)
T5 = TerminalNode('T5', 50, 0.9)

# create C2
# C2 = ChanceNode('C2', 35, [T1, T2], [0.7, 0.3])
C2 = ChanceNode('C2', 35, [T1], [0.7])

# create C1
C1 = ChanceNode('C1', 25, [C2, T3], [0.2, 0.8])
# create C3
C3 = ChanceNode('C3', 45, [T4, T5], [0.1, 0.9])

# The above is updated based on the Piazza notes. I think I got the numbers right?
#
# print("The expected cost of node C1 is ", C1.get_expected_cost(), ".",
#       "The expected health of node C1 is ", C1.get_expected_health())
#
# print("The expected cost of node C3 is ", C3.get_expected_cost(), ".",
#       "The expected health of node C3 is ", C3.get_expected_health())
#
# print("Incremental cost effectiveness is equal to the delta cost over the delta benefit. ")
# print("The expected cost of Arm 1 is ", C1.get_expected_cost(), ". ",
#       "The expected cost of Arm 2 is ", C3.get_expected_cost(), ". ")
# print("The expected benefit of Arm 1 is ", C1.get_expected_health(), ". ",
#       "The expected benefit of Arm 2 is ", C3.get_expected_health(), ". ")
#
# deltaC = (C3.get_expected_cost() - C1.get_expected_cost())
#
# print("Delta C = ", C3.get_expected_cost() - C1.get_expected_cost())
#
# deltaB = (C3.get_expected_health() - C1.get_expected_health())
#
# print("Delta B = ", C3.get_expected_health() - C1.get_expected_health())
# print("Delta C/Delta B = ", deltaC/deltaB)
