import json
import os

# Nome do arquivo para persistência
ARQUIVO_JSON = 'plantas.json'

def carregar():
    """Lê o arquivo JSON e retorna a lista de plantas."""
    if not os.path.exists(ARQUIVO_JSON):
        return []
    try:
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, Exception):
        return []

def salvar(lista):
    """Salva a lista de plantas no arquivo JSON."""
    try:
        with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def listar(lista):
    """Exibe todos os registros de plantas."""
    if not lista:
        print("\nNenhuma planta cadastrada.")
        return
    print("\n--- LISTA DE PLANTAS ---")
    for planta in lista:
        print(f"ID: {planta['id']} | Nome: {planta['nome']} | tipo:{planta['tipo']} | Local:{planta['local']} | frequencia_rega: {planta['frequencia_rega']}")

def criar(lista):
    """Cria um novo registro de planta."""
    print("\n--- CADASTRAR NOVA PLANTA ---")
    nome = input("Nome da planta: ").strip()
    tipo = input("tipo(ornamental, frutifera, remedio): ").strip()
    local = input("local:").strip()
    frequencia_rega = input("frequencia_rega: ").strip()
    
    if not nome or not tipo:
        print("Erro: Nome e tipo são obrigatórios!")
        return

    # ID Automático conforme Requisito 3.4
    novo_id = len(lista) + 1
    
    nova_planta = {
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "local": local,
        "frequencia_rega": frequencia_rega,
    }
    
    lista.append(nova_planta)
    salvar(lista)
    print(f"Planta '{nome}' adicionada com sucesso!")

def ler(lista, id_busca):
    """Busca e retorna um item pelo ID."""
    for planta in lista:
        if planta['id'] == id_busca:
            return planta
    return None

def atualizar(lista, id_busca):
    """Modifica os campos de uma planta existente."""
    planta = ler(lista, id_busca)
    if not planta:
        print(f"Erro: Planta com ID {id_busca} não encontrada.")
        return

    print(f"\nEditando: {planta['nome']}")
    nome = input(f"Novo nome (deixe vazio para manter '{planta['nome']}'): ").strip()
    tipo = input(f"Tipo(deixe vazio para manter '{planta['tipo']}'): ").strip()
    local = input(f"local(deixe vazio para manter'{planta['local']}'): ").strip()
    frequencia_rega = input(f"frequencia_rega (deixe vazio para manter '{planta['frequencia_rega']}'): ").strip()

    if nome: planta['nome'] = nome
    if tipo: planta['tipo'] = tipo
    if local: planta['local'] = local
    if frequencia_rega: planta['frequencia_rega'] = frequencia_rega

    salvar(lista)
    print("Dados atualizados com sucesso!")

def deletar(lista, id_busca):
    """Exclui um item da lista pelo ID."""
    planta = ler(lista, id_busca)
    if not planta:
        print(f"Erro: Planta com ID {id_busca} não encontrada.")
        return

    lista.remove(planta)
    salvar(lista)
    print(f"Planta ID {id_busca} removida com sucesso!")

def menu():
    plantas = carregar()
    
    while True:
        print("\n========== MENU CONTROLE DE PLANTAS ==========")
        print("1 - Listar Plantas")
        print("2 - Cadastrar Planta")
        print("3 - Buscar por ID")
        print("4 - Atualizar Planta")
        print("5 - Deletar Planta")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        try:
            if opcao == '1':
                listar(plantas)
            elif opcao == '2':
                criar(plantas)
            elif opcao == '3':
                id_digito = int(input("Digite o ID da planta: "))
                p = ler(plantas, id_digito)
                if p:
                    print(f"\nEncontrado: {p}")
                else:
                    print("ID não encontrado.")
            elif opcao == '4':
                id_digito = int(input("Digite o ID para atualizar: "))
                atualizar(plantas, id_digito)
            elif opcao == '5':
                id_digito = int(input("Digite o ID para deletar: "))
                deletar(plantas, id_digito)
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Erro: Por favor, digite um número válido para o ID.")

if __name__ == "__main__":
    menu()