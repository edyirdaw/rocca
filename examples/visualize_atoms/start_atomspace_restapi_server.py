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

# Endpoint configuration
# To allow public access, set to 0.0.0.0; for local access, set to 127.0.0.1
IP_ADDRESS = '127.0.0.1'
PORT = 5000

atomspace = AtomSpace()
set_default_atomspace(atomspace)
scheme_eval(atomspace, "(use-modules (opencog))")
scheme_eval(atomspace, "(use-modules (opencog exec))")
scheme_eval(atomspace, "(use-modules (opencog pln))")
scheme_eval(atomspace, "(use-modules (opencog spacetime))")


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

    # """
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
    # """

    # """
    exp_2 = '''
    (BackPredictiveImplicationScopeLink
      (VariableSet)
      (SLink
        (ZLink))
      (BackSequentialAndLink
        (SLink
         (SLink        
          (ZLink)))
        (BackSequentialAndLink
          (SLink
            (ZLink))
          (BackSequentialAndLink
            (SLink 
             (SLink
              (SLink
               (SLink
                 (ZLink)))))
            (AndLink (stv 0.085 0.2)
              (EvaluationLink (stv 0.585 0.2)
                (PredicateNode "Pellet Position")
                (ConceptNode "Right Square"))
              (ExecutionLink
                (SchemaNode "Stay"))
              (EvaluationLink (stv 0.58 0.2)
                (PredicateNode "Agent Position")
                (ConceptNode "Left Square")))
            (ExecutionLink
              (SchemaNode "Go Right")))
          (ExecutionLink
            (SchemaNode "Go Left")))
        (ExecutionLink
          (SchemaNode "Stay")))
      (EvaluationLink (stv 0.585 0.2)
        (PredicateNode "Pellet Position")
        (ConceptNode "Right Square")))
    '''
    # """

    exp = read_from_file('sample_hypergraph_2_trunc')

    # scheme_eval(atomspace, exp)
    scheme_eval(atomspace, pre_process_atoms(exp))
    # scheme_eval(atomspace, pre_process_atoms(exp_2))

def read_from_file(file_to_read):
    with open(file_to_read, 'r') as f:
        content = f.read()
    return content

def pre_process_atoms(exp):


    # Processing empty variableset
    exp = re.sub(r'\(VariableSet\)', '', exp)

    # Processing szlinks
    exp = re.sub(r';.*\n', '\n', exp, re.MULTILINE)
    exp = re.sub(r'\(ZLink\s+','(ZLink',exp)
    exp = re.sub(r'\)\s+\)','))',exp)
    exp = re.sub(r'\)\s+\)','))',exp)

    starting_indices_slinks = [m.start() for m in re.finditer('SLink', exp)]
    starting_indices_zlinks = [m.start() for m in re.finditer('ZLink', exp)]

    print('-------------------')
    print('starting_indices_slinks\n{}'.format(starting_indices_slinks))
    print('starting_indices_zlinks\n{}'.format(starting_indices_zlinks))
    print('-------------------')

    for i in range(len(starting_indices_zlinks)):

        print('current zlink starts at {}'.format(starting_indices_zlinks[i]))

        # Get the index of its preceding zlink
        index_preceding_zlink = -1 if i==0 else starting_indices_zlinks[i-1]
        print('index_preceding_zlink={}'.format(index_preceding_zlink))

        # Count the number of its parent links and the index of the start of its parent slink
        parent_count = 0
        index_parent_slink = 0
        for p in starting_indices_slinks:
            if  p < starting_indices_zlinks[i] and p > index_preceding_zlink:
                parent_count += 1
                if parent_count == 1:
                    index_parent_slink = p
            if p > starting_indices_zlinks[i]:
                break
        print('parent_count = {} for zlink at index {}'.format(parent_count,starting_indices_zlinks[i]))
        print('index_parent_slink = {} for zlink at index {}'.format(index_parent_slink,starting_indices_zlinks[i]))

        # Form the new string
        len_szlinks = (starting_indices_zlinks[i]+4+1+parent_count+1-1) - (index_parent_slink-1) + 1
        len_time_node = len('(TimeNode "'+str(parent_count)+'")')
        exp = exp[0:index_parent_slink-1] + '(TimeNode "'+str(parent_count)+'")' + '`'*(len_szlinks-len_time_node) + exp[starting_indices_zlinks[i]+4+1+parent_count+1:]

    exp = exp.replace('`', "")
    print(exp)





    # exit(0)

    return exp


def count_sz_links(atom):


    return






if __name__ == "__main__":

    load_atoms()

    api = RESTAPI(atomspace)
    api.run(host=IP_ADDRESS, port=PORT)


