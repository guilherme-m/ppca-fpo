# Trabalho da Disciplina Fundamentos em Pesquisa Operacional

Este projeto foi desenvolvido durante a disciplina Fundamentos em Pesquisa Operacional
do Programa de Pós-graduação em Computação Aplicada da Universidade de Brasília.

Seu objetivo é a implementação do seguinte modelo de otimização para alocação de matrículas em programas de pós-graduação para alunos especiais:

$$
\begin{equation}
\begin{aligned}
\max & \sum_{(i,j) \in M} M_{ij} X_{ij} + \sum_{i \in A} 0.1\times Y_i\\
\textrm{s.t.} & \\
& X_{ij} \leq M_{ij}, \forall i \in A,\forall j \in D.\\
& \sum_{i \in A} X_{ij} \leq L_{j}, \forall j \in D,\\
& Y_{i} \leq \sum_{j \in D} X_{ij}, \forall i \in A,\\
& \sum_{j \in D|H_{j}= g} X_{ij} \leq 1, \forall g \in G, \forall i \in A,\\
& 0 \leq X_{ij} \leq 1, \forall (i,j) \in M,\\
& 0 \leq Y_{i} \leq 1, \forall i \in A
\end{aligned}
\end{equation}
$$

## Requisitos

Foram utilizados as seguintes configurações de ambiente:

- Python 3.11.9

Versões das bibliotecas:

- ortools==9.11.4210
- numpy==2.1.1
- pandas==2.2.2

## Forma de utilizar

Para executar o modelo, basta executar o arquivo main.py.

\> python main.py
