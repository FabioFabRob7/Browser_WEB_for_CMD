import requests
from bs4 import BeautifulSoup



def https():
    l = input("Inserisci link di un sito web che vuoi visualizzare:\n")
    search(l)

def search(l):
    r = requests.get(l)
    soup = BeautifulSoup(r.content, features="lxml")
    stamp(l,r,soup)

def stamp(l,r,soup):
    print("\nPAGINA WEB:")
    for tag in soup.select("body"):
        print(tag.text)
    load(l,r,soup)

def load(l,r,soup):
    print("\nLINK NELLA PAGINA:")
    links = []
    for link in soup.select("a"):
        links.append(link.get('href'))
    print(*links, sep='\n')
    select(links,l,r,soup)

def select(links,l,r,soup):
    print("")
    links_sel = input("Seleziona un link, RICORDA CHE IL PRIMO è 0\nSe vuoi uscire scrivi exit:\n")
    if links_sel == 'exit':
        exit
    else:
        l = links[int(links_sel)]
        search(l)
    

https()