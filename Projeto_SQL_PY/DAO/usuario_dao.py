from Database.conexao import conectar


class UsuarioDAO:
    def __init__(self):
        self.conexao = conectar(host_name='localhost', user_name='root', user_password='Iwamamauro11!', db_name='projetobd')

    def test_connection(self):
        try:
            if self.conexao.is_connected():
                print("Conectou")
            else:
                print("Nao foi")

        except Exception as e:
            print(f"Erro ao testar conexão {e}")

#===================================================================#

class MarcaDAO:
    def __init__(self):
        self.conexao = conectar(host_name='localhost', user_name='root', user_password='Iwamamauro11!', db_name='projetobd')

    def tabela_Marca(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Marca (
            id_marca INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL
        )
        """)

    def inserir(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Marca (nome) VALUES (%s)", (nome,))
        self.conexao.commit()
        cursor.close()

    def atualizar(self, id_marca, novo_nome):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE Marca SET nome=%s WHERE id_marca=%s", (novo_nome, id_marca))
        self.conexao.commit()
        cursor.close()

    def deletar(self, id_marca):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM Marca WHERE id_marca=%s", (id_marca,))
        self.conexao.commit()
        print("Deletado")

    def buscar_todos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Marca")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def buscar_por_id(self, id_marca):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Marca WHERE id_marca=%s", (id_marca,))
        resultado = cursor.fetchone()
        cursor.close()
        self.conexao.commit()
        cursor.close()
        return resultado

#===================================================================#

class CarroDAO:
    def __init__(self):
        self.conexao = conectar(host_name='localhost', user_name='root', user_password='Iwamamauro11!', db_name='projetobd')

    def tabela_Carro(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Carro (
            id_carro INT PRIMARY KEY AUTO_INCREMENT,
            id_marca INT,
            nome VARCHAR(100) NOT NULL,
            FOREIGN KEY (id_marca) REFERENCES Marca(id_marca)
        )
        """)

    def inserir(self, nome, id_marca):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Carro (nome, id_marca) VALUES (%s, %s)", (nome, id_marca))
        self.conexao.commit()
        cursor.close()

    def atualizar(self, id_carro, novo_nome, nova_marca):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE Carro SET nome=%s, id_marca=%s WHERE id_carro=%s", (novo_nome, nova_marca, id_carro))
        self.conexao.commit()
        cursor.close()

    def deletar(self, id_carro):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM Carro WHERE id_carro=%s", (id_carro,))
        self.conexao.commit()
        cursor.close()

    def buscar_todos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Carro")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def buscar_por_id(self, id_carro):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Carro WHERE id_carro=%s", (id_carro,))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado

    def buscar_com_join(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
            SELECT Carro.nome, Marca.nome 
            FROM Carro 
            JOIN Marca ON Carro.id_marca = Marca.id_marca
        """)
        resultado = cursor.fetchall()
        cursor.close()
        self.conexao.commit()
        cursor.close()
        return resultado


#===================================================================#

class PilotoDAO:
    def __init__(self):
        self.conexao = conectar(host_name='localhost', user_name='root', user_password='Iwamamauro11!', db_name='projetobd')

    def tabela_Piloto(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Piloto (
            id_piloto INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL
        )
        """)

    def inserir(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Piloto (nome) VALUES (%s)", (nome,))
        self.conexao.commit()
        cursor.close()

    def atualizar(self, id_piloto, novo_nome,):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE Piloto SET nome=%s WHERE id_piloto=%s", (novo_nome, id_piloto))
        self.conexao.commit()
        cursor.close()

    def deletar(self, id_piloto):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM Piloto WHERE id_piloto=%s", (id_piloto,))
        self.conexao.commit()
        cursor.close()

    def buscar_todos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Piloto")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def buscar_por_id(self, id_piloto):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Piloto WHERE id_piloto=%s", (id_piloto,))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado

    def buscar_com_join(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
            SELECT Piloto.nome, Carro.nome
            FROM Piloto
            JOIN Carro_Piloto ON Piloto.id_piloto = Carro_Piloto.id_piloto
            JOIN Carro ON Carro.id_carro = Carro_Piloto.id_carro
        """)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

#===================================================================#

class Carro_PilotoDAO:
    def __init__(self):
        self.conexao = conectar(host_name='localhost', user_name='root', user_password='Iwamamauro11!', db_name='projetobd')

    def tabela_Carro_Piloto(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Carro_Piloto (
            id_carro INT,
            id_piloto INT,
            PRIMARY KEY (id_carro, id_piloto),
            FOREIGN KEY (id_carro) REFERENCES Carro(id_carro),
            FOREIGN KEY (id_piloto) REFERENCES Piloto(id_piloto)
        )
        """)

    def inserir_em_CarroPiloto(self, id_carro, id_piloto):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Carro_Piloto (id_carro, id_piloto) VALUES (%s, %s)", (id_carro, id_piloto))
        self.conexao.commit()
        cursor.close()

    def deletar_em_Carropiloto(self, id_carro, id_piloto):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM Carro_Piloto WHERE id_carro=%s AND id_piloto=%s", (id_carro, id_piloto))
        self.conexao.commit()
        cursor.close()

    def buscar_todos_emCarropiloto(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Carro_Piloto")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def buscar_com_join_em_Carropiloto(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
            SELECT Carro.nome, Piloto.nome 
            FROM Carro_Piloto
            JOIN Carro ON Carro.id_carro = Carro_Piloto.id_carro
            JOIN Piloto ON Piloto.id_piloto = Carro_Piloto.id_piloto
        """)
        resultado = cursor.fetchall()
        cursor.close()
        self.conexao.commit()
        cursor.close()
        return resultado

#===================================================================#

class Equipamento_Seguranca:
    def __init__(self):
        self.conexao = conectar(host_name='localhost', user_name='root', user_password='Iwamamauro11!', db_name='projetobd')


    def tabela_Equipamento_Seguranca(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Equipamento_Seguranca (
            id_equipamento INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL
        )
        """)

    def inserir_em_Equipamento_Seguranca(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Equipamento_Seguranca (nome) VALUES (%s)", (nome,))
        self.conexao.commit()
        cursor.close()

    def atualizar_em_Equipamento_Seguranca(self, id_equipamento, novo_nome):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE Equipamento_Seguranca SET nome=%s WHERE id_equipamento=%s",
                       (novo_nome, id_equipamento))
        self.conexao.commit()
        cursor.close()

    def deletar_em_Equipamento_Seguranca(self, id_equipamento):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM Equipamento_Seguranca WHERE id_equipamento=%s", (id_equipamento,))
        self.conexao.commit()
        cursor.close()

    def buscar_todos_em_Equipamento_Seguranca(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Equipamento_Seguranca")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def buscar_por_id_em_Equipamento_Seguranca(self, id_equipamento):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Equipamento_Seguranca WHERE id_equipamento=%s", (id_equipamento,))
        resultado = cursor.fetchone()
        cursor.close()
        self.conexao.commit()
        cursor.close()
        return resultado

#===================================================================#

    def tabela_Piloto_Equipamento(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Piloto_Equipamento (
            id_piloto INT,
            id_equipamento INT,
            PRIMARY KEY (id_piloto, id_equipamento),
            FOREIGN KEY (id_piloto) REFERENCES Piloto(id_piloto),
            FOREIGN KEY (id_equipamento) REFERENCES Equipamento_Seguranca(id_equipamento)
        )
        """)
        self.conexao.commit()
        cursor.close()

#===================================================================#

    def tabela_Patrocinador(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patrocinador (
            id_patrocinador INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL
        )
        """)
        self.conexao.commit()
        cursor.close()

#===================================================================#
    def tabela_Marca_Patrocinador(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Marca_Patrocinador (
            id_marca INT,
            id_patrocinador INT,
            PRIMARY KEY (id_marca, id_patrocinador),
            FOREIGN KEY (id_marca) REFERENCES Marca(id_marca),
            FOREIGN KEY (id_patrocinador) REFERENCES Patrocinador(id_patrocinador)
        )
        """)
        self.conexao.commit()
        cursor.close()