# Start the restapi server.

from opencog.web.api.apimain import RESTAPI
from opencog.atomspace import AtomSpace
from opencog.utilities import initialize_opencog
from opencog.scheme import scheme_eval


def start_rest_api_server():

    atomspace = AtomSpace()
    initialize_opencog(atomspace)
    scheme_eval(atomspace, "(use-modules (opencog pln))")

    """
    EvaluationLink(
        PredicateNode ("hold"),
        ListLink(
            ConceptNode ("self"),
            ConceptNode ("Key")
        )
    )
    """

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

    scheme_eval(atomspace,exp)


    api = RESTAPI(atomspace)
    api.run(port=5000)


if __name__ == "__main__":

    start_rest_api_server()
