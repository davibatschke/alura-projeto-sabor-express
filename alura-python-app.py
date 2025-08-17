# Exemplo de Aplicação criada durante as Aulas do Curso de Python da ALURA
import os
lista_restaurante = [{'nome': 'DaviLanches', 'categoria': 'Lancheria', 'ativo': True},
                     {'nome': 'ParáLanches', 'categoria': 'Pizzaria', 'ativo': False},
                     {'nome': 'De Comprido', 'categoria': 'Italiana', 'ativo': False}
                     ]

def exibir_nome_programa():
    '''
    - Essa função tem como objetivo mostrar na tela do usuário um texto personalizado com o nome do programa.
    - Este texto personalizado foi pego através do site: FSymbols
    '''

    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
''')

def exibir_subtitulos(texto):
    '''
    - Esta função tem como objetivo exibir os subtitulos de cada uma das opções do App.
    Ex: def categoria_exemplo():
        exibir_subtitulos('Texto de exemplo')
    '''

    os.system('cls')
    contorno_do_titulo = '-' * (len(texto))
    print(contorno_do_titulo)
    print(texto)
    print(contorno_do_titulo)
    print()

def exibir_opcoes():
    '''
    - Esta função tem como objetivo exibir as opções que o App oferece ao usuário.
    '''

    print('1. Cadastrar Restaurante.')
    print('2. Listar Restaurante.')
    print('3. Alternar Estado do Restaurante.')
    print('4. Sair.\n')

def finalizar_app():
    '''
    - Esta função tem o objetivo de encerrar o sistema.
    '''

    exibir_subtitulos('Encerrando o Sistema...')

def retornar_ao_menu():
    '''
    - Esta função oferece ao usuário a opção de voltar para o menu principal
    - Ele aparece ao final de todos os menus (exceto do principal)
    '''
    
    input('\nPressione qualquer tecla para Continuar. ')
    main()

def opcao_invalida():
    '''
    - Esta função tem o objetivo de informar ao usuário que a opção escolhida no menu não existe.
    '''

    print('A opção que você escolheu é Inválida!')
    input('Pressione qualquer tecla para continuar. ')
    main()

def cadastro_de_restaurante():
    '''
    - Esta função tem como objetivo cadastrar um novo restaurante.

    Input:
    - Nome do Restaurante
    - Categoria do Restaurante
    Output:
    - Coloca os dados obtidos na lista de restaurantes
    '''

    exibir_subtitulos('Faça o Cadastro do Seu Restaurante.')
    nome_restaurante = input('Digite o Nome do Seu Restaurante: ')
    categoria_restaurante = input('Digite qual a Categoria do Seu Restaurante: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    lista_restaurante.append(dados_restaurante)
    print(f'Parabéns! O Restaurante {nome_restaurante} foi Cadastrado!\n')
    retornar_ao_menu()

def lista_restaurante_cadastrado():
    '''
    - Esta função tem como objetivo listar todos os restaurantes cadastrados.

    Output:
    - Mostra pro usuário a lista de restaurantes, com suas respectivas categorias e se estão ou não ativados.
    '''

    exibir_subtitulos('Listando todos os Restaurantes...')

    print(f'{'Nome:'.ljust(17)} | {'Categoria:'.ljust(15)} | Estado:')
    for restaurante in lista_restaurante:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        restaurante_ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(15)} | {categoria_restaurante.ljust(15)} | {restaurante_ativo}')
    retornar_ao_menu()

def alternar_estado_restaurante():
    '''
    - Esta função tem como objetivo alterar o estado de um restaurante cadastrado.

    Input:
    - Requisita o nome de algum restaurante cadastrado.
    Output:
    - Retorna ao usuário se o restaurante foi ativado ou desativado.
    - Também retorna caso o restaurante procurado não seja encontrado.
    '''

    exibir_subtitulos('Vamos alternar o Estado do Seu Restaurante.')
    nome_restaurante = input('Digite o nome do Restaurante e alterar seu Estado: ')
    restaurante_encontrado = False

    for restaurante in lista_restaurante:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O Restaurante {nome_restaurante} foi Ativado com Sucesso!' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} foi Desativado com Sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O Restaurante não foi Encontrado.')
    
    retornar_ao_menu()

def escolhendo_opcoes():
    '''
    - Esta função mostra ao usuário quais opções nosso sistema oferece.
    - Como o de cadastro, listagem, etc.
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção acima: '))
        if opcao_escolhida == 1:
            cadastro_de_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurante_cadastrado()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''
    - Esta função é responsável por formar o menu principal.
    - Mostrando o titulo do programa, as opções, etc.
    '''

    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolhendo_opcoes()

if __name__ == '__main__':
    main()