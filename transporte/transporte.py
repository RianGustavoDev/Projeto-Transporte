import os
 
rotas = [{'nome':'Rota 1', 'bairro':'Alvorada, Bairro da Paz, Redenção', 'ativo':False},
         {'nome':'Rota 2', 'bairro':'Compensa, Nova Esperança, Planalto', 'ativo':True},
         {'nome':'Rota 3', 'bairro':'Coroado, Mauazinho, Novo Aleixo', 'ativo':False }]


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
    bairro = input(f'Digite os bairros que sua rota vai passar: ')
    dados_da_rota = {'nome':nome_da_rota,'bairro':bairro, 'ativo':False}
    rotas.append(dados_da_rota)
    print(f'A rota {nome_da_rota} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()
 
def listar_rotas():
    exibir_subtitulo('Listando suas rotas:')

    ''' Essa função é para organizar as listas de rotas'''

    print(f"{'Nome da rota'.ljust(18)} | {'Bairro'.ljust(40)} | Status")
    for rota in rotas:
        nome_rota = rota['nome']
        bairro = rota['bairro']
        ativo = 'ativado' if rota['ativo'] else 'desativado'
        print(f'- {nome_rota.ljust(16)} | {bairro.ljust(40)} | {ativo}')
 
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
            mensagem = f'A rota  {nome_rota} foi ativado com sucesso' if rota['ativo'] else f'a rota  {nome_rota} foi desativado com sucesso'
            print(mensagem)

    if not rota_encontrada:
        print('A rota não foi encontrado')

    voltar_ao_menu_principal()

def editar_rota():

    ''' Essa função é responsável por editar qualquer rota'''

    exibir_subtitulo('Editando as rotas')
    nome_rota = input('Digite o nome da rota que deseja editar: ')
    rota_encontrada = False

    for rota in rotas:
        if nome_rota == rota['nome']:
            rota_encontrada = True
            print(f'A sua rota tem esses campos {rota}\n')
            editar = input('Digite o campo que deseja editar: ')

            if editar == 'nome':
                novo_valor = input('Digite o novo nome: ')
                rota['nome'] = novo_valor
                print(f'O nome de sua rota foi atualizada para: {novo_valor}')
                print(rota)

            elif editar == 'bairro':
                novo_valor = input('Digite os novos Bairros: ')
                rota['bairro'] = novo_valor
                print(f'Os Bairros de sua rota foram atualizados para: {novo_valor}')
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