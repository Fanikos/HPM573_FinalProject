import DecisionTree_HW as Tree

# Create the terminal nodes

T1 = Tree.TerminalNode(name='T1', cost=0, health=1)   # Symptomatic DVT -> Diagnosed DVT -> Survive
T2 = Tree.TerminalNode(name='T2', cost=0, health=0)   # Symptomatic DVT -> Diagnosed DVT -> Dead
T3 = Tree.TerminalNode(name='T3', cost=0, health=1)   # Asymptomatic DVT -> PE -> Diagnosed PE -> Survive
T4 = Tree.TerminalNode(name='T4', cost=0, health=0)   # Asymptomatic DVT -> PE -> Diagnosed PE -> Dead
T5 = Tree.TerminalNode(name='T5', cost=0, health=1)   # Asymptomatic DVT -> PE -> Undiagnosed PE -> Survive
T6 = Tree.TerminalNode(name='T6', cost=0, health=0)   # Asymptomatic DVT -> PE -> Undiagnosed PE -> Die
T7 = Tree.TerminalNode(name='T6', cost=0, health=1)   # Asymptomatic DVT -> No PE -> Survive

# Create the chance nodes

# name, cost, future nodes, probs
# C2 = ChanceNode('C2', 35, [T1, T2], [0.7, 0.3])

C1 = Tree.ChanceNode(name="C1",
                     cost=100,
                     future_nodes=[T1, T2],
                     probs=[0.99, 0.01])        # Diagnosed, treated DVT -> Survived or Dead


C2 = Tree.ChanceNode(name="C2",
                     cost=1000,
                     future_nodes=[T3, T4],
                     probs=[0.92, 0.08])        # Diagnosed, treated PE -> Survived or Dead

C3 = Tree.ChanceNode(name="C3",
                     cost=0,
                     future_nodes=[T5, T6],
                     probs=[0.7, 0.3])        # Undiagnosed PE -> Survived or Dead

C4 = Tree.ChanceNode(name="C4",
                     cost=0,
                     future_nodes=[T7],
                     probs=[1])        # No PE -> Survived

C5 = Tree.ChanceNode(name="C5",
                     cost=0,
                     future_nodes=[C1],
                     probs=[1])        # Symptomatic DVT -> Diagnosed, treated DVT

C6 = Tree.ChanceNode(name="C6",
                     cost=0,
                     future_nodes=[C2, C3],
                     probs=[0.29, 0.71])        # Progression to PE -> Diagnosed PE, Undiagnosed PE

C7 = Tree.ChanceNode(name="C7",
                     cost=0,
                     future_nodes=[C6, C4],
                     probs=[0.12, 0.88])        # Asymptomatic DVT -> PE, No PE

C8 = Tree.ChanceNode(name="C8",
                     cost=0,
                     future_nodes=[C5, C7],
                     probs=[0.1, 0.9])        # DVT -> Symptomatic, Asymptomatic

print("The expected cost is:", C8.get_expected_cost())
print("The expected utility is:", C8.get_expected_health())
