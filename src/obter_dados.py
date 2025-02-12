import pandas as pd

def obter_dados():
    df_A = pd.read_csv('data/matriculas.csv', 
                    sep=',')
    
    A = df_A.iloc[:, 1:].replace(0, -999).to_numpy()
    
    alunos = df_A['aluno']
    
    D = pd.read_csv('data/disciplinas.csv', 
                    sep=',')
    
    D = D.set_index('disciplina', drop=True)
    
    disciplinas = df_A.columns[1:]
    
    D = D.loc[disciplinas,:]
    
    D['index'] = range(len(disciplinas))
    
    D = D.reset_index()
    
    return A, D, alunos