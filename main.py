from src.obter_dados import obter_dados
from src.criar_restricoes import criar_restricoes

from ortools.linear_solver import pywraplp
import numpy as np

solver = pywraplp.Solver('solver matriculas',
                         pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# obter dados de matrículas (A), disciplinas (D) e lista de alunos
M, D, alunos = obter_dados()

# definir matriz de variáveis de decisão X (m x n)
m, n = M.shape # dimensões: m = alunos, n = disciplinas

# X[i][j]: se o aluno i se matricula (1) ou não (0) na disciplina j
X = np.array([
    solver.NumVar(0, 1, f"X{i}{j}")
    for i in range(m)
    for j in range(n)
]).reshape((m, n))

# definir vetor de variáveis de decisão Y
# Y[i]: se o aluno i foi atendido (1) ou não (0)
Y = np.array([
    solver.NumVar(0, 1, f"Y{i}")
    for i in range(m)
])

# passar restrições do problema para o solver
criar_restricoes(solver, X, Y, D, M)

# definir função objetivo para maximizar
# soma total das matrículas efetivadas (A * X)
# peso de 0.1 para a soma das variáveis Y, incentivando a matrícula de alunos
solver.Maximize((M*X).sum() + 0.1*Y.sum())

# resolver
res = solver.Solve()

# extrair os valores de solução da matriz X
X_val = np.array([
    [x.solution_value() for x in i] for i in X
]).reshape(X.shape)


if res == solver.OPTIMAL:
    print(f'Solução: {solver.Objective().Value()}')
    for i, a in enumerate(X_val):
        disciplinas_aceitas = D.loc[(a.astype(np.int32) > 0), 'disciplina'].tolist()
        print(f'{alunos[i]} = {disciplinas_aceitas}')
    print(f'{int(X_val.sum())} matrículas aceitas de um total de ' +
          f'{(M>0).sum()}. ' +
          f'{(X_val.sum(axis=1) > 0).sum()} alunos matriculados de '  +
          f'um total de {X_val.shape[0]}.')
