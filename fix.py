import os
import requests
from colorama import Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
	   ____  ____  __  _           _                   
	  / __ \/ __ \/ /_(_)___ ___  (_)_______  _____    
	 / / / / /_/ / __/ / __ `__ \/ / ___/ _ \/ ___/    
	/ /_/ / ____/ /_/ / / / / / / (__  )  __/ /        
	\____/_/    \__/_/_/ /_/ /_/_/____/\___/_/    

[+] Optimize wordlists like a B0SS | SICARIO 2023 | 1337 [+] 
'''

print(Fore.CYAN + banner + Style.RESET_ALL)

while True:
    print("\n" + Fore.RED + "[Options]" + Style.RESET_ALL)
    print(Fore.RED + "1. Strip 'http://' and 'https://' from URLs")
    print("2. Add 'http://' to domains")
    print("3. Add 'https://' to domains")
    print("0. Exit" + Style.RESET_ALL)

    xrrr = input('\n' + Fore.GREEN + 'Enter your choice: ' + Style.RESET_ALL)

    if xrrr == '1':
        input_filename = input("\n\t\t\t [+] Enter the file name: ").strip("'\"")

        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()

        with open("rslt.txt", 'w') as output_file:
            for line in lines:
                modified_line = line.replace('http://', '').replace('https://', '')
                output_file.write(modified_line)
                print(Fore.RED + '[+]' + Style.RESET_ALL + ' ' + Fore.GREEN + modified_line.strip() + Style.RESET_ALL)

        print("The modified URLs have been saved in 'rslt.txt'.")

    elif xrrr == '2':
        input_filename = input("\t\t\t Enter the input file name: ").strip("'\"")

        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()

        with open("rslt2.txt", 'w') as output_file:
            for line in lines:
                domain = line.strip()
                modified_domain = 'http://' + domain
                output_file.write(modified_domain + '\n')
                print(Fore.RED + '[+]' + Style.RESET_ALL + ' ' + modified_domain)

        print("The modified domains have been saved in 'rslt2.txt'.")

    elif xrrr == '3':
        input_filename = input("\t\t\t Enter the input file name: ").strip("'\"")

        with open(input_filename, 'r') as input_file:
            lines = input_file.readlines()

        with open("rslt3.txt", 'w') as output_file:
            for line in lines:
                domain = line.strip()
                modified_domain = 'https://' + domain
                output_file.write(modified_domain + '\n')
                print(Fore.RED + '[+]' + Style.RESET_ALL + ' ' + modified_domain)

        print("The modified domains have been saved in 'rslt3.txt'.")

    elif xrrr == '0':
        print("Exiting the program...")
        break

    else:
        print("Invalid option! Please try again.")

print("Program execution completed.")

