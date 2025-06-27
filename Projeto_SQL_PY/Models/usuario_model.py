class Usuario:
    def __init__(self, nome, cpf, id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf

class Marca:
    def __init__(self, id_marca=None, nome=''):
        self.id_marca = id_marca
        self.nome = nome

class Carro:
    def __init__(self, id_carro=None, id_marca=None, nome=''):
        self.id_carro = id_carro
        self.id_marca = id_marca
        self.nome = nome

class Piloto:
    def __init__(self, id_piloto=None, nome = ''):
        self.id_piloto = id_piloto
        self.nome = nome

class CarroPiloto:
    def __init__(self, id_carro=None, id_piloto=None):
        self.id_carro = id_carro
        self.id_piloto = id_piloto

class Equipamento_Seguranca:
    def __init__(self, id_equipamento=None, nome=''):
        self.id_equipamento = id_equipamento
        self    .nome = nome

class Piloto_Equipamento:
    def __init__(self, id_piloto, id_equipamento):
        self.id_piloto = id_piloto
        self.id_equipamento = id_equipamento

class Patrocinador:
    def __init__(self, id_patrocinador=None, nome=''):
        self.id_patrocinador = id_patrocinador
        self.nome = nome

class Marca_Patrocinador:
    def __init__(self, id_mrca, id_patrocinador):
        self.id_marca = id_mrca
        self.id_patrocinador = id_patrocinador