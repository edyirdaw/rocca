# Atoms visualizer

from graphviz import Source


def viz():

    temp = """
    digraph G{
    edge [dir=forward]
    node [shape=plaintext]
    
    0 [label="0 (None)"]
    0 -> 5 [label="root"]
    1 [label="1 (Hello)"]
    2 [label="2 (how)"]
    2 -> 1 [label="advmod"]
    3 [label="3 (are)"]
    4 [label="4 (you)"]
    5 [label="5 (doing)"]
    5 -> 3 [label="aux"]
    5 -> 2 [label="advmod"]
    5 -> 4 [label="nsubj"]
    }
    """
    s = Source(temp, filename="visualize_atoms/test.gv", format="svg")
    s.view()

def viz_2 ():
    from graphviz import Source
    # path = 'visualize_atoms/test.gv'
    # path = 'visualize_atoms/test_2.gv'
    path = 'visualize_atoms/atoms.gv'
    s = Source.from_file(path, format="jpg")
    s.view()

if __name__ == "__main__":

    viz_2()
    # viz()