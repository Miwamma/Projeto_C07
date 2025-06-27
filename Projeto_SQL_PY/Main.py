from DAO.usuario_dao import UsuarioDAO, Carro_PilotoDAO, Equipamento_Seguranca
from DAO.usuario_dao import MarcaDAO, CarroDAO, PilotoDAO

usuario = UsuarioDAO()
usuario.test_connection()


def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Marca")
        print("2 - Carro")
        print("3 - Piloto")
        print("4 - Carro_Piloto")
        print("5 - Equipamento_Seguranca")
        print("0 - Sair")

        opcao = input("Escolha uma tabela: ")

        if opcao == "1":
            menu_marca()
        elif opcao == "2":
            menu_carro()
        elif opcao == "3":
            menu_piloto()
        elif opcao == "4":
            menu_carro_piloto()
        elif opcao == "5":
            menu_equipamento_seguranca()

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# ========== MENU MARCA ==========
def menu_marca():
    dao = MarcaDAO()
    while True:
        print("\n--- Tabela Marca ---")
        print("1 - Inserir")
        print("2 - Atualizar")
        print("3 - Deletar")
        print("4 - Buscar todos")
        print("5 - Buscar por ID")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")
        if op == "1":
            nome = input("Nome da marca: ")
            dao.inserir(nome)
        elif op == "2":
            id_marca = int(input("ID da marca: "))
            novo_nome = input("Novo nome: ")
            dao.atualizar(id_marca, novo_nome)
        elif op == "3":
            id_marca = int(input("ID da marca para deletar: "))
            dao.deletar(id_marca)
        elif op == "4":
            for m in dao.buscar_todos():
                print(m)
        elif op == "5":
            id_marca = int(input("ID da marca: "))
            print(dao.buscar_por_id(id_marca))
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ========== MENU CARRO ==========
def menu_carro():
    dao = CarroDAO()
    while True:
        print("\n--- Tabela Carro ---")
        print("1 - Inserir")
        print("2 - Atualizar")
        print("3 - Deletar")
        print("4 - Buscar todos")
        print("5 - Buscar por ID")
        print("6 - Buscar com JOIN (marca)")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")
        if op == "1":
            nome = input("Nome do carro: ")
            id_marca = int(input("ID da marca: "))
            dao.inserir(nome, id_marca)
        elif op == "2":
            id_carro = int(input("ID do carro: "))
            novo_nome = input("Novo nome: ")
            nova_marca = int(input("Novo ID da marca: "))
            dao.atualizar(id_carro, novo_nome, nova_marca)
        elif op == "3":
            id_carro = int(input("ID do carro para deletar: "))
            dao.deletar(id_carro)
        elif op == "4":
            for c in dao.buscar_todos():
                print(c)
        elif op == "5":
            id_carro = int(input("ID do carro: "))
            print(dao.buscar_por_id(id_carro))
        elif op == "6":
            for c in dao.buscar_com_join():
                print(c)
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ========== MENU PILOTO ==========
def menu_piloto():
    dao = PilotoDAO()
    while True:
        print("\n--- Tabela Piloto ---")
        print("1 - Inserir")
        print("2 - Atualizar")
        print("3 - Deletar")
        print("4 - Buscar todos")
        print("5 - Buscar por ID")
        print("6 - Buscar com JOIN (carro)")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")

        if op == "1":
            nome = input("Nome do piloto: ")
            dao.inserir(nome)

        elif op == "2":
            id_piloto = int(input("ID do piloto: "))
            novo_nome = input("Novo nome: ")
            dao.atualizar(id_piloto, novo_nome)
        elif op == "3":
            id_piloto = int(input("ID do piloto para deletar: "))
            dao.deletar(id_piloto)
        elif op == "4":
            for p in dao.buscar_todos():
                print(p)
        elif op == "5":
            id_piloto = int(input("ID do piloto: "))
            print(dao.buscar_por_id(id_piloto))
        elif op == "6":
            for p in dao.buscar_com_join():
                print(p)
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ========== MENU CARRO_PILOTO ==========

def menu_carro_piloto():
    dao = Carro_PilotoDAO()

    while True:
        print("\n--- Tabela Carro_Piloto ---")
        print("1 - Inserir relação Carro ↔ Piloto")
        print("2 - Deletar relação")
        print("3 - Buscar todos")
        print("4 - Buscar com JOIN (nomes)")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")
        if op == "1":
            id_carro = int(input("ID do carro: "))
            id_piloto = int(input("ID do piloto: "))
            dao.inserir_em_CarroPiloto(id_carro, id_piloto)
        elif op == "2":
            id_carro = int(input("ID do carro: "))
            id_piloto = int(input("ID do piloto: "))
            dao.deletar_em_Carropiloto(id_carro, id_piloto)
        elif op == "3":
            for rel in dao.buscar_todos_emCarropiloto():
                print(rel)
        elif op == "4":
            for rel in dao.buscar_com_join_em_Carropiloto():
                print(f"Carro: {rel[0]} | Piloto: {rel[1]}")
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ========== MENU EQUIPAMENTO_SEGURANCA ==========


def menu_equipamento_seguranca():
    dao = Equipamento_Seguranca()
    while True:
        print("\n--- Tabela Equipamento_Seguranca ---")
        print("1 - Inserir")
        print("2 - Atualizar")
        print("3 - Deletar")
        print("4 - Buscar todos")
        print("5 - Buscar por ID")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")
        if op == "1":
            nome = input("Nome do equipamento: ")
            dao.inserir_em_Equipamento_Seguranca(nome)
        elif op == "2":
            id_eq = int(input("ID do equipamento: "))
            novo_nome = input("Novo nome: ")
            dao.atualizar_em_Equipamento_Seguranca(id_eq, novo_nome)
        elif op == "3":
            id_eq = int(input("ID do equipamento: "))
            dao.deletar_em_Equipamento_Seguranca(id_eq)
        elif op == "4":
            for e in dao.buscar_todos_em_Equipamento_Seguranca():
                print(e)
        elif op == "5":
            id_eq = int(input("ID do equipamento: "))
            print(dao.buscar_por_id_em_Equipamento_Seguranca(id_eq))
        elif op == "0":
            break
        else:
            print("Opção inválida.")

# ========== INICIAR ==========
if __name__ == "__main__":
    menu_principal()

