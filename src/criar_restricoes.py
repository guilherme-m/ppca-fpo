import numpy as np

"""
Função responsável por criar e adicionar as restrições do problema de alocação de matrículas ao solver

Parâmetros:
- solver
- X: matriz de variáveis de decisão (m x n), onde X[i][j] indica se o aluno i se matricula (1) ou não (0) na disciplina j
- Y: vetor de variáveis de decisão (m), onde Y[i] indica se o aluno i foi atendido (1) ou não (0)
- D: DataFrame contendo informações sobre as disciplinas:
        - 'limite': limite máximo de matrículas permitidas em cada disciplina
        - 'horario': horário das disciplinas (usado para evitar conflitos)
        - 'index': índice numérico de cada disciplina
"""

def criar_restricoes(solver, X, Y, D, M):
    num_alunos, num_disciplinas = X.shape
    
    # 1) restrição de limite de vagas por disciplina
    for j in range(num_disciplinas):
        solver.Add(X[:, j].sum() <= D['limite'][j])
    
    # 2) Maximização do número de alunos matriculados
    for i in range(num_alunos):
        solver.Add(Y[i] <= X[i, :].sum())
    
    # 3) restrição de conflito de horários
    for g, df in D.groupby('horario'):
        if len(df) > 1:
            for i in range(num_alunos):
                solver.Add(X[i, df['index']].sum() <= 1)
                
    # 4) aluno não pode ser matriculado em matéria que não solicitou
    for i in range(num_alunos):
        for j in range(num_disciplinas):
            solver.Add(X[i, j] <= M[i, j])