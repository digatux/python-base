#!/usr/bin/env python3

"""Exibe relatorio de crianças por atividades

Imprimir as lista de ciranças agruapas por sala 
que frequentas casa uma das atividades

"""

__version__ = "0.1.0"
__autor__ = "Edgar Silva"


# Dados das Salas
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

# Dados das Aulas
aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]


atividades = [("Ingles", aula_ingles),
              ("Musica", aula_musica),
              ("Dança", aula_danca)]

for nome_atividade, atividade in atividades:
    print("-" * 40)
    print(f"Alunos da ativide {nome_atividade}\n")
    
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(atividade_sala1)
    print(atividade_sala2)

