import mysql.connector
from mysql.connector import Error


def conectar(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='Iwamamauro11!',
            database='projetobd',
        )
        print("Conexão com o banco de dados MySQL bem-sucedida!")
    except Error as e:
        print(f"O erro '{e}' ocorreu")

    return connection


def fechar_conexao(connection):

    if connection and connection.is_connected():
        connection.close()
        print("Conexão ao MySQL foi encerrada.")



if __name__ == '__main__':

    HOST = "localhost"
    USUARIO = "root"
    SENHA = "Iwamamauro11!"
    BANCO_DE_DADOS = "projetobd"


    conectar = conectar(HOST, USUARIO, SENHA, BANCO_DE_DADOS)

    if conectar is not None and conectar.is_connected():

        try:
            cursor = conectar.cursor()

            cursor.execute("SELECT DATABASE();")

            resultado = cursor.fetchone()
            print(f"Você está conectado ao banco de dados: {resultado[0]}")

            cursor.close()

        except Error as e:
            print(f"Erro ao executar o comando no banco: {e}")

        finally:
            fechar_conexao(conectar)
    else:
        print("Não foi possível conectar ao banco de dados.")

