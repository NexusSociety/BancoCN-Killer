import inquirer


class OptionsHandler:
    def __init__(self) -> None:
        pass

    def get_user_option(self):

        try:
            questions = [
                inquirer.List('options',
                              message='Selecione uma opção',
                              choices=['Bancos de Dados',
                                       'Tabelas', 'Colunas', 'Usuarios']
                              ),
            ]

            answers = inquirer.prompt(questions)

            selected_option = answers['options']

            if selected_option == 'Bancos de Dados':
                return 0, answers['options']

            elif selected_option == 'Tabelas':
                return 1, answers['options']

            elif selected_option == 'Colunas':
                return 2, answers['options']

            elif selected_option == 'Usuarios':
                return 3, answers['options']

            else:
                raise ValueError('Opção inválida.')

        except KeyboardInterrupt:
            print('[+] App Aborted!')
            exit(1)
        except TypeError:
            print('[+] App Aborted!')
            exit(1)
