from bs4 import BeautifulSoup

class HtmlHandler:
    def __init__(self) -> None:
        pass
    
    def html_handler(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        div_header_text = soup.find('div', class_='header-text')
        db_informations = div_header_text.find_next('p')

        return db_informations.text if db_informations else 'Nenhuma informação encontrada!'
