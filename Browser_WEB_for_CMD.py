import requests
from bs4 import BeautifulSoup



def https():
    l = input("Enter a link to a website you want to view:\n")
    search(l)

def search(l):
    r = requests.get(l)
    soup = BeautifulSoup(r.content, features="lxml")
    stamp(l,r,soup)

def stamp(l,r,soup):
    print("\nWEB PAGE:")
    for tag in soup.select("body"):
        print(tag.text)
    load(l,r,soup)

def load(l,r,soup):
    print("\nLINKS OF THE PAGE:")
    i = 1
    links = dict()
    for link in soup.select("a"):
        links[i] = link.get("href")
        i = i + 1
    for i, value in links.items():
        print(i, ":",value)

    select(links,l,r,soup,i)

def select(links,l,r,soup,i):
    print("")
    i = input("Select a link or\nif you want to exit type exit:\n")
    if i == 'exit':
        exit
    else:
        l = links[int(i)]
        search(l)
    

https()