# Atomspace restapi service

'''

Once https://github.com/opencog/atomspace-restful is installed (tested with sha ca0fc3722568ebaeb30f0bd970bd7a5e3034b14c),
the restapi service worked after
1. Installing with pip flask-restful-swagger==0.20.2
2. Commenting out references to the attention bank used by atomspace-restful in the python bindings installed in the system files.
   The references are easily apparent when this restapi service is launched.

'''


from opencog.web.api.apimain import RESTAPI
from opencog.atomspace import AtomSpace
from opencog.type_constructors import set_default_atomspace
from opencog.scheme import scheme_eval

import re
import traceback

# Endpoint configuration
# To allow public access, set to 0.0.0.0; for local access, set to 127.0.0.1
IP_ADDRESS = '127.0.0.1'
PORT = 5000

atomspace = AtomSpace()
set_default_atomspace(atomspace)
scheme_eval(atomspace, "(use-modules (opencog))")
scheme_eval(atomspace, "(use-modules (opencog exec))")
scheme_eval(atomspace, "(use-modules (opencog pln))")

# atomspace_2 to hold TimeNodes instead of S/Zlinks
atomspace_2 = AtomSpace()
scheme_eval(atomspace_2, "(use-modules (opencog))")
scheme_eval(atomspace_2, "(use-modules (opencog exec))")
scheme_eval(atomspace_2, "(use-modules (opencog pln))")

def load_atoms():

    """
    exp = '''
    (EvaluationLink
        (PredicateNode "hold")
        (ListLink
            (ConceptNode "self")
            (ConceptNode "Key")
        )
    )
    '''
    """


    """
    exp = '''
       (ListLink
            (ConceptNode "self")
            (ConceptNode "Key")
        )
    '''
    """


    exp = '''
    (BackSequentialAndLink
        (SLink
          (ZLink
          ) ; [800fbffffffe8ce4][3]
        ) ; [da5f815ba9d4009f][3]
        (AndLink (stv 0.02 0.2)
          (EvaluationLink (stv 0.39 0.2)
            (PredicateNode "Pellet Position") ; [56e6ab0f525cb504][3]
            (ConceptNode "Right Square") ; [6dd382acb6aa376e][3]
          ) ; [bfafa25da890c502][3]
          (ExecutionLink
            (SchemaNode "Go Right") ; [51c7a48fd94d12d8][3]
          ) ; [c29bf0559d1ad8ec][3]
          (EvaluationLink (stv 0.495 0.2)
            (PredicateNode "Agent Position") ; [3fdca752fd5e5335][3]
            (ConceptNode "Right Square") ; [6dd382acb6aa376e][3]
          ) ; [c9fcc2094e0150df][3]
        ) ; [c7d4e3c83331c030][3]
        (ExecutionLink
          (SchemaNode "Eat") ; [3fe4e22345c3679f][3]
        ) ; [9efce1dc8918c209][3]
      ) ; [969510428e2996c2][3]
    '''

    """
    exp = '''
    (BackSequentialAndLink
        (SLink
          (SLink
          (ZLink (ConceptNode "Time")
          )
         ) ; [800fbffffffe8ce4][3]
        ) ; [da5f815ba9d4009f][3]
        (AndLink (stv 0.02 0.2)
          (EvaluationLink (stv 0.39 0.2)
            (PredicateNode "Pellet Position") ; [56e6ab0f525cb504][3]
            (ConceptNode "Right Square") ; [6dd382acb6aa376e][3]
          ) ; [bfafa25da890c502][3]
          (ExecutionLink
            (SchemaNode "Go Right") ; [51c7a48fd94d12d8][3]
          ) ; [c29bf0559d1ad8ec][3]
          (EvaluationLink (stv 0.495 0.2)
            (PredicateNode "Agent Position") ; [3fdca752fd5e5335][3]
            (ConceptNode "Right Square") ; [6dd382acb6aa376e][3]
          ) ; [c9fcc2094e0150df][3]
        ) ; [c7d4e3c83331c030][3]
        (ExecutionLink
          (SchemaNode "Eat") ; [3fe4e22345c3679f][3]
        ) ; [9efce1dc8918c209][3]
      ) ; [969510428e2996c2][3]
    '''
    """

    # exp = read_from_file('sample_hypergraph_2_trunc')


    scheme_eval(atomspace,exp)


def read_from_file(file_to_read):
    with open(file_to_read, 'r') as f:
        content = f.read()
    return content

def atoms_exp():

    print(type(atomspace))
    print('Printing atomspace\n---------')
    for atom in atomspace:

        print(atom)
        print(type(atom))
        print('Atom type is {}'.format(atom.type_name))
        print('==========')
        try:
            print(len(atom.out))
            print(type(atom.out[0]))
        except Exception as e:
            print(e)
            print('No outgoing set')
        print('==========')
        print('---------')

        if atom.type_name == 'SLink':
            print('SLink found')
            count_sz_links(atom)

        atomspace_2.add_atom(atom)

    print('Number of atoms is',atomspace.size())

    print_atomspace(atomspace_2)

    exit(0)

def count_sz_links(atom):



    return


def print_atomspace(aspace):

    print('\n************************************************\nPrinting atomspace {}\n'.format(get_argument_name()))
    print('Type of atomsapce is {} \n'.format(type(aspace)))
    for atom in aspace:
        print(atom)
        print(type(atom))
        print('==========')
        try:
            print(type(atom.out[0]))
        except:
            print('No outgoing set')
        print('==========')
        print('---------')

    print('Number of atoms is',atomspace.size())
    print('************************************************')


def get_argument_name():

    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-3]
    vars_name = re.compile(r'\((.*?)\).*$').search(code).groups()[0]
    return vars_name






if __name__ == "__main__":

    load_atoms()

    atoms_exp()

    api = RESTAPI(atomspace)
    api.run(host=IP_ADDRESS, port=PORT)


