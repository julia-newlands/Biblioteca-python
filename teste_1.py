livro_ex = {
    "nome": "Nome do Livro",
    "autor": "Nome do Autor",
    "quantidade": 0
}
catalogo = []

def livro_existe(nome):
  # checar cada livro em catalogo se existe livro que "nome do livro" == nome
  print("checando se livro existe... nome = ", nome)
  print("checando catalogo...")
  for livro in catalogo:
    print("checando livro: ", livro)
    if livro["nome"] == nome:
      print("Livro já cadastrado")
      return True
    else:
      print("não é o livro")

  print("terminamos o loop")
  print("livro não existe")  
  return False  

while True:
  escolha = input("Insira a opção que deseja: ")
  if escolha == "1":
    cadastro = input("Insira o nome do livro que quer cadastrar: ")
    if livro_existe(cadastro):
      print("Livro já existente no cadastro.")
    else:
      def cadastrado():
        novo_livro = livro_ex.copy()
        novo_livro["nome"] = cadastro
        autor = input("Insira o nome do autor do livro cadastrado: ")
        novo_livro["autor"] = autor
        quantidade = int(input("Quantos livros serão disponíveis para retirada? "))
        novo_livro["quantidade"] = quantidade
        catalogo.append(novo_livro)
        print("Livro cadastrado com sucesso.")
      cadastrado()


      
  elif escolha == "6":
    print("Volte sempre!")
    break
print(catalogo)