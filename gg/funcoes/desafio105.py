"""
-> Função para analisar notas e situações de vários alunos
:param n: uma ou mais notas dos alunos (aceita várias)
:param sit: valor opcional, indicando a situação do aluno
:return: dicionário com várias informações sobre a situação da turma
"""

def notas(*n, sit = False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'

    return r

resp = notas (5.5,2.5,1.5, sit = True)
print(resp)