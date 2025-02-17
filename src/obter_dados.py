import pandas as pd

def obter_dados():
    # dados de matrículas
    df_A = pd.read_csv('data/matriculas.csv', sep=',')
    
    # colunas de escolha de materias (substitui valores 0 por -999)
    A = df_A.iloc[:, 1:].replace(0, -999).to_numpy()
    
    # separa a coluna aluno
    alunos = df_A['aluno']
    
    # dados de disciplinas
    D = pd.read_csv('data/disciplinas.csv', sep=',')
    D = D.set_index('disciplina', drop=True)
    
    # lista de disciplinas escolhidas
    disciplinas = df_A.columns[1:]
    
    # filtra apenas disciplinas que tiveram alunos interessados
    D = D.loc[disciplinas, :]
    
    # cria coluna 'index'
    D['index'] = range(len(disciplinas))
    D = D.reset_index()

    return A, D, alunos