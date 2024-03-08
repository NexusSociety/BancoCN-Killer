import pyfiglet


def show_banner():
    # Banner da aplicação
    banner = ''' '''
    
    disclaimer = '''
    [ Este software explora uma vulnerabilidade conhecida como SQL Injection no site "BANCO DA COREIA DO NORTE". ]
    [ O site em questão pertence á empresa Solyd, uma empresa voltada para a area de cibersegurnaça. ]
    [ Existe a permissão previa da empresa para a exploração de vulnerabilidades no aplicativo web! ]
    '''

    # banner = pyfiglet.Figlet('cosmic')
    # print(banner.renderText('Thief oF'))
    # print(banner.renderText('Korean'))
    print(banner)
    print(disclaimer)
