import random
import string
import colorama
import time
from colorama import Fore, Style

colorama.init(autoreset=True)

banner = f'''
{Fore.RED}
                          _                 _                   
                         / |_              / |_                 
 _ .--.   _ .--.   .--. `| |-'.---.  .---.`| |-' .--.   _ .--.  
[ '/'`\ \[ `/'`\]/ .'`\ \| | / /__\\/ /'`\]| | / .'`\ \[ `/'`\] 
 | \__/ | | |    | \__. || |,| \__.,| \__. | |,| \__. | | |     
 | ;.__/ [___]    '.__.' \__/ '.__.''.___.'\__/ '.__.' [___]    
[__|                                                            
{Fore.RED}GitHub: https://github.com/Hilerna{Fore.RED}
{Style.RESET_ALL}
'''

print(banner)

security = input(f"{Fore.GREEN}Choisissez un niveau de sécurité (fort/moyen/basic): ").lower()

def strong_password():
    length = random.randint(12, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def medium_password():
    length = random.randint(8, 10)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def basic_password():
    length = random.randint(6, 8)
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if security == "fort":
    password = strong_password()
elif security == "moyen":
    password = medium_password()
elif security == "basic":
    password = basic_password()
else:
    print(f"{Fore.GREEN}Niveau de sécurité non valide. Choisissez parmi 'fort', 'moyen' ou 'basic'.")
    exit()

print(f"{Fore.GREEN}Votre mot de passe {security} est : {password}")

with open('mdp.txt', 'w') as file:
    file.write(f"Mot de passe {security}: {password}\n")

time.sleep(3)
print(f"{Fore.WHITE}Fermeture...")