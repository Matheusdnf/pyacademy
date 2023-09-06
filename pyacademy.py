#código de matheus diniz fernandes
import pickle # salvando arquivos
import os

usi={}
maquinas={}
series={}
dias = ["2", "3", "4", "5", "6", "7"]   #checagem para ver se o usuário digitou os dias válidos
try:   #recuperar os dados
  arqinfo = open("info.dat", "rb")
  dados = pickle.load(arqinfo)
  usi = dados[1]
  maquinas = dados[2]
  series = dados[3]
  arqinfo.close()
except:
  arqinfo = open("info.dat", "wb")
def apresentacao():
  print("|==============================================================|")
  print("|            Nome do Projeto:Pyacademy                         |")
  print("|Este projeto busca simular a gestão de treinos de uma academia|")
  print("|                   UFRN-CERES                                 |")
  print("|  Separado em 3 módulos,usuários,máquinas/exercícios e séries |")
  print("|           Feito por:Matheus Diniz Fernandes                  |")
  print("|==============================================================|")
  continuar = input('Tecle ENTER para sair:')
  os.system("clear||cls")
def menu():  #menu principal
  os.system("clear||cls")
  print("=" * 7, "Menu Principal", "=" * 7)
  print("1-Cadastrar usuário")
  print("2-Cadastrar exercícios/máquina")
  print("3-Cadastrar séries")
  print("4-Listar série do usuário")
  print("5-Sobre o projeto")
  print("0-Encerrar Programa")
  print("=" * 30)
  opn = input("O que deseja fazer:")
  return opn
def menuusuario():    #menu de usuário
  print("\n=======Área De Cadastro=======")
  print("1-Cadastrar usuário")
  print("2-Apagar usuário")
  print("3-Listar usuários")
  print("4-Procurar usuário")
  print("5-Atualizar usuário")
  print("0-voltar")
  print("=" * 30)
  while True:
      opn1 = input("O que deseja fazer:")
      if opn1 != "1" and opn1 != "2" and opn1 != "3" and opn1 != "4" and opn1 != "5" and opn1 != "0":
        print("Opção inválida")
      return opn1
def cadastroexercicio(): #menu de máquinas/exercícios
  print("\n=========","Menu cadastro de Máquina/exercício","===========")
  print("1-Cadastrar máquina/exercício:")
  print("2-Excluir máquina/exercício")
  print("3-Procurar por grupo muscular")
  print("4-Atualizar máquina")
  print("0-Voltar")
  print("=" * 56)
  while True:
      caex = input("qual opção escolher:")
      if caex != "1" and caex != "2" and caex != "3" and caex != "4" and caex != "5" and caex != "0":
          print("opção inválido")
      return caex
def serie():       #menu de séries
  print("\n=======Menu De Séries=======")
  print("1-Cadastrar Séries")
  print("2-Apagar Séries")
  print("3-Listar Séries")
  print("4-Atualizar série")
  print("0-voltar")
  print("=" * 27)
  while True:
    opn1 = input("O que deseja fazer:")
    if opn1 != "1" and opn1 != "2" and opn1 != "3" and opn1 != "4" and opn1 != "5" and opn1 != "0":
      print("opção inválido")
    return opn1
def partemuscular():     #menu de escolha da parte muscular
  print("\n==========", "Grupo muscular", "==========")
  print("1-Peito")
  print("2-Perna")
  print("3-Braço")
  print("0-voltar")
  print("====================================\n")
  while True:
    partm = input("Qual parte muscular:")
    if partm != "1" and partm != "2" and partm != "3" and partm != "0":
      print("opção inválido")
    return partm
def semana():    #menu para escolher os dias da semana
  print("\nDias da semana")
  print("2-Segunda")
  print("3-Terça")
  print("4-Quarta")
  print("5-Quinta")
  print("6-Sexta")
  print("7-Sábado\n")
  print("Caso queira adicionar mais de um dia,coloque uma [,]\n")
  dia = input("Digite o número atrelado aos dia da semana em que deseja práticar:")
  return dia
def salvar(): #salvar os arquivos dos usis
  dados = {1: usi, 2: maquinas, 3: series}
  arqinfo = open("info.dat", "wb")  
  pickle.dump(dados, arqinfo)
  arqinfo.close()
def explicacao():    #explicação da datação para o usuário
  print("\nPrimeiro [número]=id cadastrado")
  print("Segundo [número]=Dia da semana cadastrada")
  print("Terceiro [número]=máquinas/exercício atrelado a Quantidade de repetições\n")
def explicacaommaq():  #explicação da datação para o usuário
  print("\nPrimeiro [número]=id cadastrado")
  print("Segundo [número]=Parte muscular cadastrada")
  print("Terceiro [número]=Nome da máquina\n")
def listarmaq(partm):   #listar máquinas/exercícios cadastrados
  if veri(partm)==False:
    print("Nada cadastrado nessa parte muscular!")
  else:
    print("Máquinas;")
    for chave in maquinas:
      if maquinas[chave][0] == partm:    #irá mostrar apenas o grupo muscular escolhido, separando dos demais
        print(chave,"-",maquinas[chave][0], "-", maquinas[chave][1])
def listarserie(vn):  #função para exibir as séries
    print("\nSéries;")
    for chave in series:
      if series[chave][0] == partm:    #irá separar por grupo muscular mostrado apenas o que o usuário selecionou 
        if series[chave][3]==vn:  #além de separar por músculo irá também separar pelo nível do usuário
          print(chave, "-", series[chave][1], series[chave][2],series[chave][3])
    return chave
def verificaremail(email):  # autória de matheus diniz e maria eloisa ##
  l=['!' , " ", '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '[', ']', '{', '}', '|', ',', '/', ':', ';', '"', "'", ',', '<', '>', '?', '_', '~']
  for e in email:
      if e in l:
          return False
  fat=(email.split("@"))
  if len(fat)<2:
      return False
  elif len(fat)>2:
      return False
  else:
      antesArroba=fat[0]
      y=len(antesArroba)
      if y > 64:
        return False
      posArroba=fat [ 1]
      qtPonto=posArroba.count('.')
      if posArroba[0].isalnum() and qtPonto!=0:
          fatPonto=posArroba.split('.')
          if "" not in fatPonto:
              ultPont=fatPonto[len(fatPonto)-1]
              if ultPont.isalpha() and len(ultPont)>1:
                  return True
def validaCPF(cpf):   #fornecido por Flavius Gorgônio
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0
    if tam != 11:
        return False
    for i in range(11):
        if (cpf[i] < '0') or (cpf[i] > '9'):
            return False
    for i in range(9):
        soma += (int(cpf[i]) * (10 - i))
    d1 = 11 - (soma % 11)
    if (d1 == 10 or d1 == 11):
        d1 = 0
    if d1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += (int(cpf[i]) * (11 - i))
    d2 = 11 - (soma%11 )
    if (d2 == 10 or d2 == 11):
        d2 = 0
    if d2 != int(cpf[10]):
        return False
    return True
def validanome(nome):     #validar nome do usi
    l = ['!', '#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '[', ']', '{', '}', '|', ',', '/', ':', ';', '"', "'",',', '<', '>', '?', '_', '~']
    if nome.isdigit() == True:    #verifica se não é um número 
        return False
    for letra in nome:
        if letra in l:   #verificar se não tem nenhum caracter especial
            return False
    partes = nome.split(" ")  #verficia se após o espaço existe pelo ao menos um caracter
    for procura in partes: 
        if not procura.isalpha():
            return False
    return True
def cpfFV(cpf):    #verifica se no programa principal se ele é válido ou falso
  while True:  # Executa o loop indefinidamente até que o resultado seja True
    if validaCPF(cpf) == False:
        print("CPF inválido!")
    else:
        print("CPF válido")
        return cpf  # Retorna True quando o CPF for válido
    cpf = input("Digite um CPF válido:")  # Solicita que o usuário insira um novo CPF
def emailFV(email):    #verifica se no programa principal se ele é válido ou falso
  while True:
    if verificaremail(email) == False:
      print("Email inválido!")
    else:
      print("Email válido!")
      return email
    email=input("Digite um email válido!:").replace(".", "").replace("-", "").replace(" ", "")
def inusie(): #saber qual a chave das máquinas 
  ind=[]
  for inusie in maquinas:
    ind.append(inusie)
  return ind
def veri(partm):     #procurando se o grupo muscular foi cadastrado 
  cont=0       #se verificar que está em série ele conta mais um, cada vez que tiver um um iten de acordo com o if ele entra no contador caso não, não irá funcionar
  for i in maquinas:
    for j in maquinas[i]:
      if partm in maquinas[i][0]:
        cont+=1
  if cont==0:
    return False
  else:
    return True
def veri2(partm):
  cont=0
  for i in series:
    for j in series[i]:
      if partm in series[i][0]:
        cont+=1
  if cont==0:
    return False
  else:
    return True
def criar_id(lista):  #maria eloisa,criação de id
    id = len(lista)
    if id == 0:
      id = id + 1
    else:
        listChaves = list(lista.keys())
        listChaves.sort()
        id = listChaves[id - 1] + 1
    return id
def nivel():   #atrelar o nível de treinamento ao usuário
  print("\nNível de treinamento\n")
  print("I-Iniciante")
  print("M-Moderado")
  print("A-Avançado\n")
  while True:
    nv = input("Em qual nível o usuário se enquandra:").upper()
    if nv != "I" and nv != "M" and nv != "A":
      print("Opção inválida!\n")
    else:
      return nv
def veri3(vn):     #verificar se o no nível do usuário tem algo cadastrado, caso não retorna false
  cont=0
  for i in series:
    for j in series[i]:
      if vn in series[i][3]:
        cont+=1
  if cont==0:
    return False
  else:
    return True
def cadastroUsi():    #cadastro de usuário
  vnome = True
  while vnome:  # validar o nome,enquanto o nome não for válido o código não para
    nome = input("Digite o nome:").lower().title()
    validanome(nome)
    if validanome(nome) == False:
      print("Errado")
      continue
    else:
      print("Certo")
      vnome = False
      cpf = input("Digite o CPF:").replace(".", "").replace("-", "").replace(" ", "")
      if cpf in usi:
        print("Cpf já cadastrado!")
      else:
        cpfv=cpfFV(cpf)
        email = input("Digite o Email:")
        emailv=emailFV(email)
        nv=nivel()
        usi[criar_id(usi)] = [nome, emailv, nv,cpfv]
        salvar()
        print("Cadastrado!")
      vnome=False
def listausi():  #listar todos os usuários cadastrados
  if usi=={}:
    print("Nenhum usuário cadastrado!")
  else:
    for usuarios in usi:
      print("********************************")
      print("Id de usuário:",usuarios)
      print("Nome do usuário:", usi[usuarios][0])
      print("Email:", usi[usuarios][1])
      print("CPF:", usi[usuarios][3])
      print("Nível do usuário:", usi[usuarios][2])
def excluirusi():  #excluir usuário
  if usi == {}:
    print()
  else:
    listausi()
    apagar=True
    while apagar:
      try:
        apagar =int(input("\nDigite o id do usuário:"))
        if apagar in usi:
          usi.pop(apagar)
          print("Usuário apagado!")
          apagar=False
          salvar()
      except ValueError:    #tratar do tipo da string/o tipo atribuido,tratando de seus erros
        print("Digite um número inteiro!")   
def proqpor1usi():  #procurar por um usi em específico, a parte de como listar todos os usi com o mesmo nome foi fonecido pelo Chat Gpt
  if usi == {}:
    print("Nenhum usuário cadastrado!\n")
  else:
    procusi = True
    encontrado = False
    while procusi:
      procusi = input("\nNome do usuário que deseja buscar?").lower().title()
      for usuarios in usi:
        if procusi == usi[usuarios][0]:
          print("********************************")
          print("Nome do usuário:", usi[usuarios][0])
          print("Email:", usi[usuarios][1])
          print("CPF:", usi[usuarios][3])
          print("Nível do usuário:", usi[usuarios][2])
          print()
          encontrado=True
      if not encontrado:
        print("Nenhum usuário encontrado!")
      procusi = False
def menuattusuario(): #menu de atualização das informações do usuário
  print("\nO que deseja atualizar?")
  print("1-Atualizar Email")
  print("2-Atualizar nível de usuário ")
  print("0-Sair\n")
  attmenusi=True
  while attmenusi:
    attusu=input("O que deseja atualizar?")
    if attusu!="1" and attusu!="2" and attusu!="0":
      print("Opção errada!")
    else:
      return attusu
def atualizarusi():  #atualizar info de usi já existente
  if usi=={}:
    print()
  else:
    procura=True
    while procura:
      try:
        atusi=int(input("\nDigite o id do usuários referente em que deseja atualizar:"))
        if atusi in usi:
          att_usi=menuattusuario()
          if att_usi=="1":
            email = input("\nNovo Email:")
            emailFV(email)
            usi[atusi][1] = email
            print("\nAtualizado!")
            salvar()
            procura=False
          elif att_usi=="2":
            nv=nivel()
            usi[atusi][2]= nv
            procura=False
            salvar()
            print("\nAtualizado!")
            procura=False
          elif att_usi=="0":
            procura=False
        else:
          print("Errado!")
      except ValueError:
        print("Digite um número inteiro!")
def cadastromaq(partm):   #função de cadastrar as máquinas/exercícios
  cadmaq = True
  while cadmaq:
      quant = input("Quantas máquinas/exercício?")
      if quant.isdigit():
          quant = int(quant)
          cadmaq = False
      else:
          print("Digite apenas números!")
  for quandm in range(quant):
      nae = input(f"\nNome da máquina/exercício de N° {quandm + 1} : ")
      maquinas[criar_id(maquinas)] = [partm, nae]
      salvar()
  print("\nCadastrado!")
  cadmaq=False
def cadastroexer():   #escolher em qual parte muscular cadastrar
  procura=True
  while procura:
      partm=partemuscular()
      if partm =="1" or partm=="2" or partm=="3":
        cadastromaq(partm)
      elif partm=="0":
        procura=False
def remomaq():   #excluir máquinas/exercício
  if veri(partm)==False:
    print()
  else:
    explicacaommaq()
    remover = True
    while remover:
      remove = int(input("Qual deseja remover?"))
      maquinas.pop(remove)
      salvar()
      remover=False
      print("Apagado!")
def attmaq():  #atualizar o nome da máquinas/exercício
  if veri(partm)==False:
    print()
  else:
    attp=True
    explicacaommaq()
    while attp:  # while para atualizar
      att = input("Qual deseja atualizar (digite seu id) ?")
      print()
      att3=att.isdigit()
      if att3==True:
        attp=False
      try:
        att=int(att)
        for i in inusie():
          if att!= i:
            print("Errado")
            attp=False
          else:
            att2 = input("Digite o nome da nova máquina/exercício:")
            maquinas[att] = [partm, att2]
            salvar()
            att=False
            print("Atualizado!") 
      except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
def cadastroserie():  #cadastrar as séries
  if veri(partm)==False:
    print()
  else:
    nv=nivel()
    escdia = True
    while escdia: #escolher dia
      dia=semana()
      if validadia(dia):    
        escdia = False
      else:
        print("Não é possível cadastrar uma série nesse dia!\n")
    listarmaq(partm)
    valida=True
    while valida:
      cadaserie = input("Digite o número atrelado ao exercício/máquinas:\n")
      cadaserie2=cadaserie.isdigit()     #verificar se o que foi digitado é um núemro
      if cadaserie2==True:
        valida=False
      try:
        cadaserie=int(cadaserie)    #tranforma essa variável em um valor int
        for i in inusie():
          if cadaserie!= i:
            valida=False
          else:
            formas=True  # formato de como as séries devem ser
            while formas:
              print("Digite o número atrelado ao exercício e atribua a série.\nFormato (número atrelado ao exercício - Série X Repetições\n")
              quantidadedereps = input("reps:")
              if "x" not in quantidadedereps:
                print("Formatação Errada!\n Digite novamente")
              else:
                print("Cadastrado!\n")
              series[criar_id(series)] = [partm, dia, quantidadedereps,nv]
              formas = False
      except ValueError:
            print("Entrada inválida, digite um número inteiro.")
def apagserie():   #apagar as séries
  if maquinas == {}:
    print("Nenhum exercíco cadastrado!")
  if veri(partm)==False:
    print()
  else:
    lists=True
    while lists:
        listarserie(vn)
        explicacao()
        print("DIGITE APENAS NÚMEROS:")
        remove = int(input("Qual série deseja remover?"))
        if remove not in series:    #se o id da série não estiver cadastrado ele falará que não existe nenhuma série com o id 
            print("Não existe nenhuma série atrelada a isso!")
            lists=False
        series.pop(remove)
        lists = False
        salvar()
        print("Série removida!")
def listserie():   #listar as séries cadastradas
  if maquinas == {}:
    print("Nenhum exercíco cadastrado!")
  if veri(partm)==False:
    print()
  else:
    explicacao()   #explicara  formatação das séries
    listarserie(vn)
def menattserie(): #menu atualizar serie
  print("\n1-Atualizar dia da semana")
  print("2-Atualizar quantidade de repetições")
  print("0-Sair\n")
  attser=True
  while attser:
    atseri=input("O que deseja atualizar?")
    if atseri!="1" and atseri!="2" and atseri!="0":
      print("Opção errada!")
    else:
      return atseri
def attserie(vn):    #atualizar os dados das séries cadastradas
  if maquinas == {}:
    print("Nenhum exercíco cadastrado!")
  if veri(partm)==False:
    print()
  else:
    explicacao()
    listarserie(vn)
    apenasn=True
    while apenasn:
      try:
        print("\nDigite apenas os IDS das séries apresentadas!")   
        att = int(input("Qual série deseja atualizar?"))
        escdia = True
        att_serie=menattserie()
        if att_serie=="1":
          while escdia: #escolher dia
            dia=semana()
            if validadia(dia):    
              series[att][1]=dia
              salvar()
              print("Atualizado!")
              escdia = False
              apenasn=False
            else:
              print("Não é possível cadastrar uma série nesse dia!\n")
        elif att_serie=="2":
          quantidadedereps = input("\nDigite a máquinas máquina/exercício e sua nova quantidade de repetição:")
          series[att][2] = quantidadedereps
          salvar()
          print("\nAtualizado!")
          apenasn=False
        elif att_serie=="0":
          apenasn=False
      except ValueError:
        print("Digite um valor inteiro!")
def validadia(dia):   #função para validar o dia do usuários,para cadastrar apenas os dias válidos
    contar = dia.count(",")      #após selecionar o dia escolhido é necessário colocar outra vírgula para adicionar mais dias, 2,3 segunda e terça
    if contar == 0:
        if dia not in dias:
            return False
        return dia
    if contar > 6:   #só podera colocar vírgular 6 vezes pois bate com a quantidade de dias
        return False
    partes = dia.split(",")
    for procura in partes:
        if not procura.isdigit() or procura not in dias:      #verificar se os dígitos escrtios batem com os que estão disponíveis 
            return False
    return dia
def vericpfinusi():   #listar séries de usuários
  try:
    digid = int(input("Digite o ID do usuário: "))
    for procuraid in usi:
      if digid == procuraid:
          print("\nAcesso autorizado!") #caso esteja cadastrado,retornará o valor do cpf para exibir as séries atrelada a pessoa cadastrada
          return digid
    return False   #verificiar se o usi está no dic, caso não esteja ele envia um valor falso, para assim informar para não prosseguir
  except ValueError:
    return False
def procurando(partm, digid):    #fornecido pelo chat gpt  #parte destinada para mostrar as séries atralado ao nível do usuário
  listarmaq(partm)
  print("Séries:")
  for nv in series:
    if partm == series[nv][0] and usi[digid][2] == series[nv][3]: #meu erro era que eu estáva usando foi if ao invés de apenas um, a qual foi ajustada pelo gpt
      print("Dia da semana:", series[nv][1], "- Máquinas/exercício e repetições:", series[nv][2])
      print()
#programa principal
comeco=True
while comeco:
    menup = menu()
    if menup == "1":
        nada=True
        while nada:   #ficar repetindo as opções de cadastro de usi
            menuusi = menuusuario()
            if menuusi == "1":   
                cadastroUsi()    #cadastrar usuário
            elif menuusi == "2":  
              excluirusi()     #apagar usuários
            elif menuusi == "3":   
              listausi()       #listar usi
            elif menuusi == "4":   
              proqpor1usi()     #procurar por 1 usi específico
            elif menuusi == "5":    
              listausi()
              atualizarusi()   #atualizar usuário
            if menuusi=='0':
              nada=False   #fecha a opção de usi e vai para o menu principal
    elif menup == "0":
      print("Programa Encerrado!")   #fechar o programa
      comeco=False
    elif menup == "2": 
      inicio=True
      while inicio:      #primeiro while para quando no menu de cadastro o usuário digitar 0 ele retornar para o menu principal 
        nd=True
        while nd:       #segundo while para rodar as opções do menu de cadastro de exercício
            cadm = cadastroexercicio() 
            if cadm=="1":    
              cadastroexer()  #cadastrar  exercício/máquinas
            elif cadm=="2":    
              if maquinas=={}:
                print("Nenhum exercíco cadastrado!")
              else:
                partm=partemuscular()    #quando chamar o menu de grupo muscular e o usuário digitar 0, ele sair desse menu e voltar para o menu de cadastro de máquina
                if partm=="0":
                  nd=False
                else:     #caso ele continue com esse processo ele irá continuar a realizar o que a opção escolhida realizará
                  listarmaq(partm)
                  remomaq()   #remover máquinas/exercício cadastrado
            elif cadm=="3" :    
              if maquinas=={}:
                print("Nenhum exercíco cadastrado!")
              else:
                partm = partemuscular()
                if partm=="0":
                  nd=False
                else:
                  listarmaq(partm)        #listar as máquinas/exercícios cadastradas 
            elif cadm=="4" :   
              if maquinas=={}:
                print("Nenhum exercíco cadastrado!")
              else:
                partm=partemuscular()
                if partm=="0":
                  nd=False
                else:
                  listarmaq(partm)     
                  attmaq()    #atualizar máquina/exercício
            if cadm=="0":      
              nd=False
              inicio=False
    elif menup=="3":
      serie1=True
      while serie1:
        nd2=True
        while nd2:
          opn1 = serie()
          if opn1 == "1":    #cadastrar séries
            partm=partemuscular()
            if partm=="0":
              nd2=False
            else:
              cadastroserie()
          elif opn1 == "2":    #apagar série
            if series=={}:
              print("Nenhuma série foi cadastrada!")
              nd2=False
            else:
              partm=partemuscular()
              if partm=="0":
                nd2=False
              else:
                if veri2(partm)==False:
                  print("Nenhuma série cadastrada!")
                else:
                  vn=nivel()
                  if veri3(vn)==False:
                    print("Nada foi cadastrado nesse nível!")
                  else:
                    listarmaq(partm)
                    apagserie()
          elif opn1 == "3":  #listar série
            if series=={}:
              print("Nenhuma série foi cadastrada!")
              nd2=False
            else:
              partm=partemuscular()
              if partm=="0":
                nd2=False
              else:
                if veri2(partm)==False:
                  print("Nenhuma série cadastrada!")
                else:
                  vn=nivel()
                  if veri3(vn)==False:
                    print("Nada foi cadastrado nesse nível!")
                  else:
                    listarmaq(partm)
                    listserie()    
          elif opn1=="4":     #atualizar série
            if series=={}:
              print("Nenhuma série foi cadastrada!")
              nd2=False
            else:
              partm=partemuscular()
              if partm=="0":
                nd2=False
              else:
                if veri2(partm)==False:
                  print("Nenhuma série cadastrada!")
                else:
                  vn=nivel()
                  if veri3(vn)==False:
                    print("Nada foi cadastrado nesse nível!")
                  else:
                    listarmaq(partm)
                    attserie(vn)
          if opn1=="0":
              nd2=False
              serie1=False
    elif menup=="4":
      if usi=={}:
        print()
      else:
        digcpf=vericpfinusi()
        if digcpf==False:
          print()
        else:
          oi=True
          while oi:
            partm=partemuscular()
            if partm=="0":
              oi=False
            if veri2(partm)==False:
              print("Nenhuma série cadastrada!")
            else:
              procurando(partm,digcpf)
              input("Aperte ENTER para sair:")
    elif menup=="5":
      apresentacao()