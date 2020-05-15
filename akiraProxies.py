from bs4 import BeautifulSoup
import requests
import os
from io import StringIO


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()

def term():

    print("\
        __   .__             __________                     .__               \n\
_____  |  | _|__|___________ \______   \_______  _______  __|__| ____   ______\n\
\__  \ |  |/ /  \_  __ \__  \ |     ___/\_  __ \/  _ \  \/  /  |/ __ \ /  ___/\n\
 / __ \|    <|  ||  | \// __ \|    |     |  | \(  <_> >    <|  \  ___/ \___ \ \n\
(____  /__|_ \__||__|  (____  /____|     |__|   \____/__/\_ \__|\___  >____  >\n\
     \/     \/              \/                             \/       \/     \/ ")

    print("\
    \n\
    \n\
    [0]Claim proxies\n\
    [1]Clear\n\
    [2]Exit")

term()


def proxies():
    type = input("\n    Type of the proxies [http, https, socks4, socks5]> ")
    anon = input('\n    Anon of the proxies [transparent, anonymous, elite]> ')
    choicecountry = input("\n    Do you want a specific country? [Y/N]> ")
    if choicecountry == "Y":
        country = input("\n    Country ISO code> ")
        url="https://www.proxy-list.download/api/v1/get?type=" + type + "&anon=" + anon + "&country=" + country
    elif choicecountry == "N":
        url="https://www.proxy-list.download/api/v1/get?type=" + type + "&anon=" + anon
    else:
        print("\n    Error.")
        return
    path = input("\n    Path to the output> ")
    name_file = input("\n    Name of the file> ")
    os.chdir(path)
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    page=soup.find('p')
    data=page.text
    file = open(name_file + ".txt", 'x')
    file.write(data)
    file.close()
    print("\n    The file is ready.")


terminal=True

while terminal:
    choice=input("\n    akiraProxies> ")
    if choice == "0":
        proxies()
    elif choice == "1":
        clear()
        term()
    elif choice =="2":
        terminal=False
        print("\n\n    Goodbye :)")