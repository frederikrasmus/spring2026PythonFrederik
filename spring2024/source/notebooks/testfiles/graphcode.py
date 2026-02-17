# These 2 functions are not super important for you to look at right now. The fokus should be on the Value class. 
# But basicly what the 2 functions do are to produce the graph below with its nodes and edges. 
# If you later look through the code step by step, you should by now be able to understand what it does. 
# If not it is a good exercise to do so. 

# In order for this to work you have to install graphviz on your laptop. 
# Install graphviz on you computer: https://graphviz.org/download/

# Then install graphviz in the environment 'pip install graphviz'

from graphviz import Digraph


def trace(root):
    # builds a set of all nodes and edges in a graph
    nodes, edges = set(), set()
    
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    
    build(root)
    
    return nodes, edges

def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'}) # LR = left to right
    
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # for any value in the graph, create a rectangular ('record') node for it
        dot.node(name=uid, label=f"{{ {n.label} | data {n.data:.1f} }}", shape='record')
        if n._op:
            # if this value is a result of some operation, create an op node for it
            dot.node(name=uid + n._op, label=n._op)
            # and connect this node to it
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        # connect n1 to the op node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot