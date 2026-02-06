import json
import os

DB = "pets.json"

# -------- carregar / salvar --------
def carregar():
    if not os.path.exists(DB):
        return []
    with open(DB, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []


def salvar(lista):
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=2, ensure_ascii=False)


# -------- operações CRUD --------
def listar(lista):
    if not lista:
        print("Nenhum pet cadastrado.")
        return
    for pet in lista:
        print(
            f"id={pet['id']} | nome={pet['nome_pet']} | "
            f"espécie={pet['especie']} | raça={pet['raca']} | dono={pet['dono']}"
        )


def criar(lista, nome_pet, especie, raca, dono):
    novo_id = len(lista) + 1 
    pet = {
        "id": novo_id,
        "nome_pet": nome_pet,
        "especie": especie,
        "raca": raca,
        "dono": dono
    }
    lista.append(pet)
    salvar(lista)
    return pet


def ler(lista, pet_id):
    return next((p for p in lista if p["id"] == pet_id), None)


def atualizar(lista, pet_id, nome_pet=None, especie=None, raca=None, dono=None):
    for pet in lista:
        if pet["id"] == pet_id:
            if nome_pet:
                pet["nome_pet"] = nome_pet
            if especie:
                pet["especie"] = especie
            if raca:
                pet["raca"] = raca
            if dono:
                pet["dono"] = dono
            salvar(lista)
            return pet
    return None


def deletar(lista, pet_id):
    for pet in lista:
        if pet["id"] == pet_id:
            lista.remove(pet)
            salvar(lista)
            return True
    return False


# ------------------ menu ------------------
def menu():
    lista = carregar()
    while True:
        print("\n=== PETSHOP ===")
        print("1 - Listar pets")
        print("2 - Cadastrar pet")
        print("3 - Ler pet por ID")
        print("4 - Atualizar pet")
        print("5 - Deletar pet")
        print("0 - Sair")
        op = input("> ").strip()

        if op == "1":
            listar(lista)

        elif op == "2":
            nome_pet = input("Nome do pet: ").strip()
            especie = input("Espécie: ").strip()
            raca = input("Raça: ").strip()
            dono = input("Nome do dono: ").strip()

            if not nome_pet or not especie or not dono:
                print("Nome do pet, espécie e dono são obrigatórios.")
                continue

            criado = criar(lista, nome_pet, especie, raca, dono)
            print("Pet cadastrado:", criado)

        elif op == "3":
            try:
                pet_id = int(input("ID: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            print(ler(lista, pet_id) or "Pet não encontrado.")

        elif op == "4":
            try:
                pet_id = int(input("ID: ").strip())
            except ValueError:
                print("ID inválido.")
                continue

            nome_pet = input("Novo nome (Enter para manter): ").strip()
            especie = input("Nova espécie (Enter para manter): ").strip()
            raca = input("Nova raça (Enter para manter): ").strip()
            dono = input("Novo dono (Enter para manter): ").strip()

            resultado = atualizar(
                lista,
                pet_id,
                nome_pet or None,
                especie or None,
                raca or None,
                dono or None
            )
            print(resultado or "Pet não encontrado.")

        elif op == "5":
            try:
                pet_id = int(input("ID: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            print("Pet deletado." if deletar(lista, pet_id) else "Pet não encontrado.")

        elif op == "0":
            print("Saindo.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()