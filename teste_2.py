from typing import Any

LIVRO_EXEMPLO: dict[str, Any] = {
  "nome": "dicionário aurélio",
  "autor": "aurélio",
  "ano": 2024,
  "quantidade": 1,
}
CATALOGO: list[dict[str, Any]] = []


def criar_livro(nome: str, autor: str, ano: int, quantidade: int):
  livro = {
    "nome": nome,
    "autor": autor,
    "ano": ano,
    "quantidade": quantidade
  }
  return livro


def exibir_informacao_do_livro(livro: dict[str, Any]):
  print(f" - Nome: {livro['nome']} | Autor: {livro['autor']} | Quantidade: {livro['quantidade']}")


def cadastrar_livro(nome: str):
  autor = input("Insira o nome do autor do livro cadastrado: ")
  ano = int(input("Insira o ano de lançamento do livro: "))
  quantidade = int(input("Quantos livros serão disponíveis para retirada? "))

  livro = criar_livro(nome=nome, autor=autor, ano=ano, quantidade=quantidade)

  CATALOGO.append(livro)
  print("Livro cadastrado com sucesso.")


def buscar_livro_por_nome(nome: str):
  for livro in CATALOGO:
    if livro["nome"] == nome:
      return livro


def buscar_livro_por_autor(autor: str):
  livros = []
  for livro in CATALOGO:
    if livro["autor"] == autor:
      livros.append(livro)
  return livros


def listar_livros():
  if len(CATALOGO) == 0:
    print("O catálogo está vazio. Insira um livro para começar.")
  else:
    print("Lista de livros no catálogo:")
    for livro in CATALOGO:
      exibir_informacao_do_livro(livro=livro)



while True:
  escolha = input("Insira a opção que deseja: ")

  if escolha == "1":
    nome = input("Insira o nome do livro que quer cadastrar: ").strip().lower()
    if buscar_livro_por_nome(nome=nome) is None:
      cadastrar_livro(nome=nome)
    else:
      print("Livro já existente no cadastro.")

  elif escolha == "2":
    listar_livros()

  elif escolha == "3":
    criterio = input("Buscar livro em catálogo: (nome/autor) ").strip().lower()
    if criterio == "nome":
        termo = input("Digite o nome do livro: ").strip().lower()
        print(termo)
        livro = buscar_livro_por_nome(nome=termo)
        if livro is None:
          print("Livro não encontrado.")
        else:
          exibir_informacao_do_livro(livro=livro)
    elif criterio == "autor":
        termo = input("Digite o nome do autor: ").strip().lower()
        livros = buscar_livro_por_autor(autor=termo)
        if livros:
          print(f"Livros do autor '{termo}':")
          for livro in livros:
            exibir_informacao_do_livro(livro=livro)
        else:
          print("Nenhum livro de autor no catálogo.")
    else:
      print(f"Opção inválida: {criterio}.")
    
  elif escolha == "6":
    print("Volte sempre!")
    break

# print(CATALOGO)
