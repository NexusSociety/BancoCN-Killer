import pyfiglet


def show_banner():

    disclaimer = '''
    [ Este software explora uma vulnerabilidade conhecida como SQL Injection no site "BANCO DA COREIA DO NORTE". ]
    [ O site em questão pertence á empresa Solyd, uma empresa voltada para a area de cibersegurnaça. ]
    [ Existe a permissão previa da empresa para a exploração de vulnerabilidades em aplicativo web! ]
    '''
    # Banner da aplicação
    banner = pyfiglet.Figlet('cosmic')
    print(banner.renderText('CSQLeak'))
    print(banner)
    print(disclaimer)
