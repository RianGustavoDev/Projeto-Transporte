import os
 
rotas = [{'nome':'Rota 1', 'bairro':'Alvorada, Bairro da Paz, Redenção', 'modalidade':'W8', 'fornecedor':'Transsilvestre', 'ativo':False},
         {'nome':'Rota 2', 'bairro':'Compensa, Nova Esperança, Planalto', 'modalidade':'V8', 'fornecedor':'Transsilvestre', 'ativo':True},
         {'nome':'Rota 3', 'bairro':'Coroado, Mauazinho, Novo Aleixo', 'modalidade':'VAN', 'fornecedor':'Transsilvestre', 'ativo':False }]


def exibir_nome_do_programa():
    print("""
████████╗██████╗░░█████╗░███╗░░██╗░██████╗██████╗░░█████╗░██████╗░████████╗███████╗
╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
░░░██║░░░██████╔╝███████║██╔██╗██║╚█████╗░██████╔╝██║░░██║██████╔╝░░░██║░░░█████╗░░
░░░██║░░░██╔══██╗██╔══██║██║╚████║░╚═══██╗██╔═══╝░██║░░██║██╔══██╗░░░██║░░░██╔══╝░░
░░░██║░░░██║░░██║██║░░██║██║░╚███║██████╔╝██║░░░░░╚█████╔╝██║░░██║░░░██║░░░███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝

            ████████╗███████╗░█████╗░████████╗░█████╗░██╗░░░██╗
            ╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗╚██╗░██╔╝
            ░░░██║░░░█████╗░░██║░░╚═╝░░░██║░░░██║░░██║░╚████╔╝░
            ░░░██║░░░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║░░╚██╔╝░░
            ░░░██║░░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝░░░██║░░░
            ░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░ 
""")
 
def exibir_opcoes():
    print('1. Cadastro de Rotas')
    print('2. Listar Rotas')
    print('3. Alternar estado das Rotas')
    print('4. Editar rota')
    print('5. Sair \n')
 
def finalizar_app():
    exibir_subtitulo('Finalizar app')
 
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()
 
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha) 
    print(texto)
    print(linha)
    print()
 
def cadastrar_nova_rota():
    ''' Essa função é responsável por cadastrar uma nova rota
    
    Inputs:
    - Nome da rota
    - Bairros
    
    Output:
    - Adiciona uma nova rota na lista de rotas
    
    '''
    exibir_subtitulo('Cadastro de novas Rotas')
    nome_da_rota = input('Digite o nome da rota que deseja cadastrar: ')
    bairro = input('Digite os bairros que sua rota vai passar: ')
    modalidade = int(input('Digite a modalidade do transporte: (1) VAN, (2) V8, (3) W8, (4) ÔNIBUS e (5) CARRO: '))

    rota = {}  # Criando um novo dicionário para cada rota
    
    if modalidade == 1:
        rota['modalidade'] = 'VAN'

    elif modalidade == 2:
        rota['modalidade'] = 'V8'

    elif modalidade == 3:
        rota['modalidade'] = 'W8'

    elif modalidade == 4:
        rota['modalidade'] = 'ÔNIBUS'

    elif modalidade == 5:
        rota['modalidade'] = 'CARRO'

    else:
        print('Item inválido!')

    fornecedor = int(input('Digite o fornecedor do transporte: (1) ZENATUR, (2) TRANSSILVESTRE e (3) TRANSMEGA: '))

    if fornecedor == 1:
        rota['fornecedor'] = 'Zenatur'
        print('Zenatur cadastrado!')

    elif fornecedor == 2:
        rota['fornecedor'] = 'Transsilvestre'
        print('Transsilvestre cadastrado!')

    elif fornecedor == 3:
        rota['fornecedor'] = 'Transmega'
        print('Transmega cadastrado!')

    else:
        print('Item inválido!')

    rota['nome'] = nome_da_rota
    rota['bairro'] = bairro
    rota['ativo'] = False

    rotas.append(rota)
    print(f'A {nome_da_rota} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()
 
def listar_rotas():
    exibir_subtitulo('Listando suas rotas:')

    ''' Essa função é para organizar as listas de rotas'''

    print(f"{'Nome da rota'.ljust(18)} | {'Bairro'.ljust(40)} | {'Modalidade'.ljust(20)} | {'Fornecedor'.ljust(20)} | Status")
    for rota in rotas:
        nome_rota = rota['nome']
        bairro = rota['bairro']
        modalidade = rota['modalidade']
        fornecedor = rota['fornecedor']
        ativo = 'ativado' if rota['ativo'] else 'desativado'
        print(f'- {nome_rota.ljust(16)} | {bairro.ljust(40)} | {modalidade.ljust(20)} | {fornecedor.ljust(20)} | {ativo}')
 
    voltar_ao_menu_principal()

def alternar_estado_rota():

    ''' Essa função é responsável por alterar o status de qualquer rota cadastrada'''

    exibir_subtitulo('Alterando estado das rotas')
    nome_rota = input('Digite o nome da rota que deseja alterar o estado: ')
    rota_encontrada = False

    for rota in rotas:
        if nome_rota == rota['nome']:
            rota_encontrada = True
            rota['ativo'] = not rota['ativo']
            mensagem = f'A {nome_rota} foi ativado com sucesso' if rota['ativo'] else f'a rota {nome_rota} foi desativado com sucesso'
            print(mensagem)

    if not rota_encontrada:
        print('A rota não foi encontrado')

    voltar_ao_menu_principal() 
    

def editar_rota():

    ''' Essa função é responsável por editar qualquer rota e bairros'''

    exibir_subtitulo('Editando as rotas')
    nome_rota = input('Digite o nome da rota que deseja editar: ')
    rota_encontrada = False

    for rota in rotas:
        if nome_rota == rota['nome']:
            rota_encontrada = True
            print(f'A sua rota tem esses campos {rota}\n')
            print('1. Editar Nome Rota')
            print('2. Editar Bairros')
            print('3. Editar Modalidade')
            print('4. Editar Fornecedor \n')
            editar = int(input('Escolha uma opção: '))

            if editar == 1:
                novo_valor = input('\nDigite o novo nome: ')
                rota['nome'] = novo_valor
                print(f'O nome de sua rota foi atualizada para: {novo_valor}')
                print(rota)

            elif editar == 2:
                novo_valor = input('Digite os novos Bairros: ')
                rota['bairro'] = novo_valor
                print(f'Os Bairros de sua rota foram atualizados para: {novo_valor}')
                print(rota)

            elif editar == 3:
                novo_valor = input('Digite a nova modalidade: ')
                rota['modalidade'] = novo_valor
                print(f'A modalidade foi atualizada para: {novo_valor}')
                print(rota)

            elif editar == 4:
                novo_valor = input('Digite o novo fornecedor: ')
                rota['fornecedor'] = novo_valor
                print(f'O fornecedor foi atualizada para: {novo_valor}')
                print(rota)
             
            else:
                print('Campo inválido!')

            if not rota_encontrada:
                print('A rota não foi encontrado')

            voltar_ao_menu_principal()
         
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
 
        if opcao_escolhida == 1:
            cadastrar_nova_rota()
        elif opcao_escolhida == 2:
            listar_rotas()
        elif opcao_escolhida == 3:
            alternar_estado_rota()
        elif opcao_escolhida == 4:
            editar_rota()
        elif opcao_escolhida == 5:
            finalizar_app() 
        else:
            opcao_invalida()
    except:
        opcao_invalida()
 
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
 
if __name__ == '__main__':
    main()