# Experiments

import re


def reg_exp():

    p_1 = re.compile(';.*\\n')
    exp = ';;an\n'

    m_i = p_1.finditer(exp)
    print(m_i)

    for m in m_i:
        print(m.start())
        print(m.end())
        print(exp[m.start():m.end()])


def reg_ex_2():

    p_1 = re.compile(';.*\\n')
    p_2 = re.compile('\(ZLink\\s*\)')
    p_3 = re.compile('\)\\s*\)')
    exp = '''
        (BackSequentialAndLink
            (SLink
              (SLink
               (SLink
               (ZLink
              ) ; [800fbffffffe8ce4][3]
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

    new_str = p_1.sub('\n',exp)
    # print('new_str========================')
    # print(new_str)
    exp = new_str
    print('exp========================')
    print(exp)


    print('p_2-----------------------')

    # m_i = p_2.finditer(exp)
    #
    # for m in m_i:
    #     print(m.start())
    #     print(m.end())
    #     print(exp[m.start():m.end()])

    new_str = p_2.sub('(ZLink)',exp)
    # print(new_str)

    exp = new_str
    print('exp========================')
    print(exp)


    print('p_3-----------------------')

    # m_i = p_3.finditer(exp)

    # for m in m_i:
    #     print(m.start())
    #     print(m.end())
    #     print(exp[m.start():m.end()])

    while(True):
        new_str = p_3.sub('))',exp)
        if exp == new_str:
            break
        else:
            exp = new_str

    print('exp========================')
    print(exp)
    while(True):
        new_str = p_3.sub('))',exp)
        if exp == new_str:
            break
        else:
            exp = new_str

    print('exp========================')
    print(exp)

    while(True):
        new_str = p_3.sub('))',exp)
        if exp == new_str:
            break
        else:
            exp = new_str

    print('exp========================')
    print(exp)




if __name__ == '__main__':

    # reg_exp()
    reg_ex_2()