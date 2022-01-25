# Atoms visualizer with graphviz/dot

'''

You will need to have the graphviz graph drawing software installed: sudo apt install graphviz
Also, pip install graphviz==0.19.1

'''

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
    s = Source(temp, filename="test.gv", format="svg")
    s.view()

def viz_2 ():

    # path = 'test.gv'
    # path = 'test_2.gv'
    path = 'atoms.gv'
    s = Source.from_file(path, format="jpg")
    s.view()

if __name__ == "__main__":

    viz_2()
    # viz()