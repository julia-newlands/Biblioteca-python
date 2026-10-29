livro_ex = {
    "nome": "Nome do Livro",
    "autor": "Nome do Autor",
    "ano": "Ano de lançamento",
    "quantidade": 0
}
catalogo = []


def busca_nome(nome):
    for livro in catalogo:
        if livro["nome"] == nome:
            print("Livro já cadastrado")
            return True
        else:
            print("não é o livro")

    print("terminamos o loop")
    print("livro não existe")
    return False


def cadastrado():
  novo_livro = livro_ex.copy()
  novo_livro["nome"] = cadastro
  autor = input("Insira o nome do autor do livro cadastrado: ")
  novo_livro["autor"] = autor
  ano = int(input("Insira o ano de lançamento do livro: "))
  novo_livro["ano"] = ano
  quantidade = int(input("Quantos livros serão disponíveis para retirada? "))
  novo_livro["quantidade"] = quantidade
  catalogo.append(novo_livro)
  print("Livro cadastrado com sucesso.")

def listagem():
  print("Lista de livros no catálogo:\n")
  for livro in cadastro:
    print("- ", livro["nome"])

while True:
  escolha = input("Insira a opção que deseja: ")
  if escolha == "1":
    cadastro = input("Insira o nome do livro que quer cadastrar: ").strip().lower()
    if cadastro in catalogo:
      print("Livro já existente no cadastro.")
    else:
      cadastrado()
  elif escolha == "2":
    listagem()

  elif escolha == "3":
    criterio = input("Buscar livro em catálogo: (nome/autor) ").strip().lower()
    if criterio == "nome":
        termo = input("Digite o nome do livro: ").strip().lower()
        for livro in criterio:
            if livro["nome"] == termo:
                print("Livro encontrado:", livro)
                continue
            else:
              print("Livro não encontrado.")
    elif criterio == "autor":
        termo = input("Digite o nome do autor: ").strip().lower()
        resultados = []
        for livro in catalogo:
          if livro["autor"] == termo:
            resultados.append(livro)
        if resultados:
          print("Livros de autor: ", resultados)
        else:
          print("Nenhum livro de autor no catálogo.")
  
  elif escolha == "6":
    print("Volte sempre!")
    break
print(catalogo)