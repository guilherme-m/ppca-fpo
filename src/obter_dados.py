import pandas as pd

def obter_dados():
    df_A = pd.read_csv('data/matriculas.csv', 
                    sep=',')
    
    A = df_A.iloc[:, 1:].replace(0, -999).to_numpy()
    
    alunos = df_A['aluno']
    
    M = pd.read_csv('data/disciplinas.csv', 
                    sep=',')
    
    return A, M, alunos