# Experiments

import re
from requests import post
import json


def reg_exp():

    exp = ';;an\n'

    m_i = re.finditer(r';.*\n',exp,re.MULTILINE)
    print(m_i)

    for m in m_i:
        print(m.start())
        print(m.end())
        print(exp[m.start():m.end()])
    print('Finished')

def reg_exp_1_2():

    exp = 'cccc\nccc'
    print(exp)
    # exp = re.sub(r'(\s)+','d',exp,re.MULTILINE)
    exp = re.sub(r'\n','d',exp,flags=re.MULTILINE)
    print(exp)

    exp = 'thIngs'
    print(exp)
    exp = re.sub(r'ing', '', exp,flags=re.IGNORECASE)
    print(exp)

    print('Finished')


def reg_ex_2():

    exp = '''
        (BackSequentialAndLink
            (SLink
              (SLink
               (SLink
                (SLink
                 (SLink
               (ZLink
               ) ; [800fbffffffe8ce4][3]
             ) ; [da5f815ba9d4009f][3]
           ) ; [da5f815ba9d4009f][3]
          ) ; [da5f815ba9d4009f][3]
           ) ; [da5f815ba9d4009f][3] 
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

    print('p_1-----------------------')

    # m_i = p_1.finditer(exp)
    #
    # for m in m_i:
    #     print(m.start())
    #     print(m.end())
    #     print(exp[m.start():m.end()])

    exp = re.sub(r';.*\n','\n',exp,flags=re.MULTILINE)
    # print('new_str========================')
    # print(new_str)
    print('exp========================')
    print(exp)

    print('p_2-----------------------')

    # m_i = p_2.finditer(exp)
    #
    # for m in m_i:
    #     print(m.start())
    #     print(m.end())
    #     print(exp[m.start():m.end()])

    exp = re.sub(r'\(ZLink\s+','(ZLink',exp)


    print('exp========================')
    print(exp)

    print('p_3-----------------------')

    # m_i = p_3.finditer(exp)

    # for m in m_i:
    #     print(m.start())
    #     print(m.end())
    #     print(exp[m.start():m.end()])

    exp = re.sub(r'\)\s+\)','))',exp)
    print('exp========================')
    print(exp)
    exp = re.sub(r'\)\s+\)','))',exp)
    # exp = re.sub(r'\)\s*\)','))',exp)
    # exp = re.sub(r'\)\s*\)','))',exp)

    print('exp========================')
    print(exp)


def post_to_restapi():

    # Define the API Endpoint - replace 127.0.0.1 with the server IP address if
    # necessary
    IP_ADDRESS = '127.0.0.1'
    PORT = '5000'
    uri = 'http://' + IP_ADDRESS + ':' + PORT + '/api/v1.1/'
    headers = {'content-type': 'application/json'}

    ####################################################################
    # Example POST and GET requests to create and read nodes and links #
    ####################################################################
    # POST a new node
    truthvalue = {'type': 'simple', 'details': {'strength': 0.08, 'count': 0.2}}
    atom = {'type': 'ConceptNode', 'name': 'new_atom', 'truthvalue': truthvalue}
    post_response = post(uri + 'atoms', data=json.dumps(atom), headers=headers)
    print(json.dumps(atom))
    post_result = post_response.json()
    print(post_result)


if __name__ == '__main__':

    # reg_exp()
    # reg_exp_1_2()
    # reg_ex_2()
    post_to_restapi()