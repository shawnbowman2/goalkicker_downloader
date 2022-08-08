import requests
from bs4 import BeautifulSoup
from pathlib import Path
from colorama import Fore, Back, Style

def get_links(resp: requests.Response) -> list[str]:
    """Return a list of links for the request.Response object provided.

    This function uses BeautifulSoup to parse the text of the request.Response object and filters out the 'buymecoffee' link assuming that to be the only non-interesting link.

    Args:
        resp (requests.Response) : request object to parse.
    
    Returns:
        A list of the links in the request.Response object provided.
    """
    soup = BeautifulSoup(resp.text, features="html.parser")
    links = soup.find_all('a')
    links = [link for link in links if link['href'] != 'https://www.buymeacoffee.com/GoalKickerBooks']
    return [(link['href']) for link in links]

if __name__ == "__main__":
    baseurl = 'https://goalkicker.com/'
    main_page = requests.get(baseurl)
    links = get_links(main_page)
    links = [f'{baseurl}{link}' for link in links]
    download_links = []
    for link in links:
        #print(link)
        book_page = requests.get(link)
        new_links = get_links(book_page)
        filename = new_links[0]
        filepath = Path(Path.cwd(), 'books', filename)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        download_link = f'{link}{filename}'
        print(Fore.BLUE + f'Downloading {filename}...')
        resp = requests.get(download_link)
        with filepath.open('wb') as f:
            f.write(resp.content)
        print(Fore.GREEN + f'Download to {filepath}')
