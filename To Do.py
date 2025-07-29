import os
lista_tarefas = []
menu = 1
while menu == 1:
    print("Bem vindo ao seu To Do!")
    print("Escolha oque você deseja fazer:\n 1- Adicionar tarefas\n 2- Lista das suas tarefas\n 3- Remover alguma tarefa\n 4- Sair do To Do.")
    escolha = int(input("Oque deseja fazer? Digite o numero a seguir\n -->"))
    if escolha == 1:
        addtarefa="Continuar"
        while addtarefa!="Parar":
            trf=input("Digite sua Tarefa a seguir\n -->")
            lista_tarefas.append(trf)
            addtarefa=input("Você deseja adicinar mais tarefas? Digite Continuar ou Parar --> ")
            while addtarefa != "Continuar" and  addtarefa != "Parar":
                print("Comando invalido, digite novamente...")
                addtarefa=input("Adicionar mais tarefas? Digite Continuar ou Parar: ")
                print("Suas tarefas foram adicionadas com sucesso!")
                os.system("cls")
                os.system("pause")
    if escolha == 2: 
        if lista_tarefas == []:
            print("Você ainda não adicionou nenhuma tarefa. Adicione-as")
        else:
            print("As tarefas suas tarefas são:\n ")
            print(lista_tarefas)
        os.system("pause")
    if escolha == 3:
        os.system("cls")
        remover = int(input("Digite o número da tarefa para remove-la: "))
        if remover == 1:    
            a=None
            print ("Tarefa 1 Excluida!")
        elif remover == 2:    
            b=None
            print ("Tarefa 2 Excluida!")
        elif remover == 3:    
            c=None
            print ("Tarefa 3 Excluida!")
        elif remover == 4:    
            d=None
            print ("Tarefa 4 Excluida!")
        elif remover == 5:    
            e=None
            print ("Tarefa 5 Excluida!")
        elif remover == 6:    
            f=None
            print ("Tarefa 6 Excluida!")
        elif remover == 7:    
            g=None
            print ("Tarefa 7 Excluida!")
        elif remover == 8:    
            h=None
            print ("Tarefa 8 Excluida!")
        elif remover == 9:    
            i=None
            print ("Tarefa 9 Excluida!")
        elif remover == 10:    
            j=None
            print ("Tarefa 10 Excluida!")
        else:
            print ("Número de Tarefa inválido")
        print ("\n\nRetornando ao MENU")
        os.system("pause")
    elif escolha == 4:
        os.system("cls")
        print("Saindo...")
        sair = 4
        os.system("pause")
        sair = 0
