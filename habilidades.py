from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

# Exercício para praticar

# Acrescentar na API de habilidade (módulo habilidades) os métodos PUT, POST e DELETE

# O método POST deverá inserir uma nova habilidade na lista

# O método PUT a partir de um ID (identificação da posição) deverá alterar o nome da habilidade que está naquela posição

# O método DELETE deverá deletar uma habilidade que esteja na posição informado na requisição.


