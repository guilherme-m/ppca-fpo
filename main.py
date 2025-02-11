from src.obter_dados import obter_dados
from src.criar_restricoes import criar_restricoes

from ortools.linear_solver import pywraplp
import numpy as np

solver = pywraplp.Solver('solver matriculas',
                         pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

A, D, alunos = obter_dados()

m, n = A.shape

X = np.array([
    solver.NumVar(0, 1, f"X{i}{j}")
    for i in range(m)
    for j in range(n)
]).reshape((m, n))

Y = np.array([
    solver.NumVar(0, 1, f"Y{i}")
    for i in range(m)
])

criar_restricoes(solver, X, Y, A, D)

solver.Maximize((A*X).sum() + 0.1*Y.sum())

res = solver.Solve()

X_val = np.array([
    [x.solution_value() for x in i] for i in X
]).reshape(X.shape)

if res == solver.OPTIMAL:
    print(f'Solução: {solver.Objective().Value()}')
    print('X = ', X_val)
    print(f'{int(X_val.sum())} matrículas.' +
          f'{(X_val.sum(axis=1) > 0).sum()} alunos matriculados')
