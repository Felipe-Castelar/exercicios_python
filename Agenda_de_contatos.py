

def salvar_novo_contato(lista_telefonica,nome,telefone):
    contatos={"nome":nome,"telefone":telefone, "favorito":False}
    lista_telefonica.append(contatos)
    print(f"\nO contato {nome} foi salvo com sucesso")
    return

def Deletar_contato(lista_telefonica, indice):
    indice = int(indice) - 1  # transforma o número do usuário em índice real da lista

    if 0 <= indice < len(lista_telefonica):
        lista_telefonica.pop(indice)
        print("Contato removido com sucesso!")
    else:
        print("Número inválido!")

        return

def Ver_lista_telefonica(lista_telefonica):
    for indice, contatos in enumerate(lista_telefonica,start=1):
        favoritar = "⭐" if contatos["favorito"] else " "
        nome = contatos["nome"]
        telefone= contatos["telefone"]
        print(f"\n{indice}. [{favoritar}] {nome}: {telefone}")
    return

def Ver_lista_favoritos(lista_telefonica):
    lista_telefonica_favoritos=[]
    for contatos in lista_telefonica:
        
        if contatos["favorito"] == True:
            lista_telefonica_favoritos.append(contatos)
            print(f"{contatos['nome']} - {contatos['telefone']} ⭐")
    return

def Editar_nome_contato(lista_telefonica,indice_contato,novo_nome):
#passamos o dicionario e depois o indice e a key para poder mudar o nome
    indice_contato_ajustado = int(indice_contato) -1
    if indice_contato_ajustado >=0 and indice_contato_ajustado<len(lista_telefonica):
        contato=lista_telefonica[indice_contato_ajustado]
        contato["nome"] = novo_nome
        print(f"\nContato {indice_contato} atualizada para{novo_nome}")
    else:
        print("Índice de tarefa inválido.")
    return   
        
def Editar_numero_contato(lista_telefonica,indice_contato, novo_numero):
    indice_contato_ajustado = int(indice_contato) -1
    if indice_contato_ajustado >=0 and indice_contato_ajustado<len(lista_telefonica):
        contato=lista_telefonica[indice_contato_ajustado]
        contato["telefone"]= novo_numero
        print(f"\nNumero do contato {contato['nome']} atualizado para {novo_numero}")
        
    else:
        print("Índice de tarefa inválido.")    
    return
    
def Favoritar_contato(lista_telefonica,indice_contato):
    indice_contato_ajustado = int(indice_contato)-1
    contato =lista_telefonica[indice_contato_ajustado]
    contato['favorito']=True
    print(f"\nContato {contato['nome']} favoritado com sucesso!")
    return

def Desfavoritar_contato(lista_telefonica,indice_contato):
    indice_contato_ajustado = int(indice_contato)-1
    contato=lista_telefonica[indice_contato_ajustado]
    contato['favorito']=False
    print(f"\nContato {contato['nome']} foi removido dos favoritos")
    return



lista_telefonica=[]
while True:
    print("LISTA TELEFONICA\n")
    print("1. Salvar um novo numero")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Deletar um contato")
    print("5. Marcar ou Desmarcar contato como favoritos")
    print("6. Ver lista dos favoritos")
    print("7. Sair")
    escolha = input("\nEscolha uma opção:")

    if escolha == "1":
        telefone = int(input("digite o numero do seu contato:"))
        nome= input("digite o nome do seu contato:")
        salvar_novo_contato(lista_telefonica,nome,telefone)
        
    elif escolha == "2":
        Ver_lista_telefonica(lista_telefonica)
        
    elif escolha == "3":
        Ver_lista_telefonica(lista_telefonica)
        indice_contato =input("\nEscolha um contato:")
        
        print("1. Atualizar Nome")
        print("2. Atualizar Numero")
        
        opcao= input("\nEscolha uma opção:")
        
        if opcao =="1":
            novo_nome = input("Digite o novo nome do contato:")
            Editar_nome_contato(lista_telefonica,indice_contato,novo_nome)
            
        elif opcao == "2":
            novo_numero = int(input("Digite o novo numero do contato:"))
            Editar_numero_contato(lista_telefonica,indice_contato,novo_numero)
    
    elif escolha == "4":
        Ver_lista_telefonica(lista_telefonica)
        apagar_contato = input("Digite o número do contato que deseja excluir: ")
        Deletar_contato(lista_telefonica, apagar_contato)

        
    
    elif escolha == "5":
       
        Ver_lista_telefonica(lista_telefonica)
        indice_contato = input("Escolha um contato:")
        
        print("1. Marcar como favorito")
        print("2. Tirar dos favoritos")
        
        opcao = input("Digite a oppção desejada:")
        
        if opcao == "1":
            Favoritar_contato(lista_telefonica, indice_contato)  
        
        elif opcao =="2":
            Desfavoritar_contato(lista_telefonica, indice_contato)       
         
    elif escolha == "6":
        Ver_lista_favoritos(lista_telefonica)    

        
    elif escolha == "7":
        break
print("programa finalizado")