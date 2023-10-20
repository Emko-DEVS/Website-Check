import sys
import requests
import time
from colorama import Fore
from pystyle import Colors, Colorate, Add
import os

banner = Fore.RED + f"""
           .    .
          |\   |
       _..;|;__;|;
     ,'   ';` \';`-.
     7;-..     :   )
.--._)|   `;==,|,=='
{Fore.RED} `\`@; \_ `<`G," G).
   `\/-;,(  )  .>. )
       < ,-;'-.__.;'
        `\_ `-,__,'
           `-..,;,>
              `;;;;
               `  ` """ + Fore.RESET

text = f"{Fore.YELLOW}Website Check by Lopusnik <3{Fore.RED}"

def check_website_status(url):
    os.system("cls || clear")
    print(Add.Add(banner, text, 4))
    while True:
        start_time = time.time()

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Website {Fore.GREEN}{url} {Fore.RESET}is {Fore.GREEN}online.{Fore.RESET} - {Fore.YELLOW}{((time.time() - start_time) * 1000):.2f} ms{Fore.RESET}")
            else:
                print(f"The website {Fore.RED}{url} {Fore.RESET}is {Fore.RED}not responding. {Fore.RESET}Status code: {Fore.MAGENTA}{response.status_code}.{Fore.RESET} - {Fore.YELLOW}{((time.time() - start_time) * 1000):.2f} ms {Fore.RESET}")
        except requests.exceptions.RequestException as e:
            print(f"There was an error while trying to access {url}: {str(e)}. Time taken: {((time.time() - start_time) * 1000):.2f} ms")
        
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 webcheck.py <url>")
    else:
        website_url = sys.argv[1]
        print(f"Checking status of {website_url} every second...")
        check_website_status(website_url)
