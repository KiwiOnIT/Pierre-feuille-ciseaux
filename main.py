import random
from simple_term_menu import TerminalMenu
from colorama import *
import os

class Main:
    def __init__(self, computer_wins, user_wins):
            self.computer_wins = computer_wins
            self.user_wins = user_wins

    def choice(self):
        options = ['Pierre', 'Papier', 'Ciseaux', 'Quitter']
        terminal_menu = TerminalMenu(options)
        user_input = terminal_menu.show()
        print('Tu as choisis ' + Fore.CYAN + str(options[user_input]) + Fore.RESET + '.')
        self.Computer_pick(options[user_input])
        
    def Computer_pick(self, user_input):
        options = ['pierre', 'papier', 'ciseaux']
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print("L'ordi a choisi " + Fore.CYAN + computer_pick + Fore.RESET + '.')
        self.result(user_input, computer_pick)

    def result(self, user_input, computer_pick):
        if user_input.casefold() == 'quitter':
            os.system('clear')
            print('Ta gagné', self.user_wins, 'de fois.')
            print("L'ordi a gagné", self.computer_wins, 'de fois.')
            quit()
        if user_input.casefold() == computer_pick.casefold():
            print(Fore.LIGHTGREEN_EX + 'Egalité')
            print(Fore.RESET + '______________________________________')

        elif user_input.casefold() == 'pierre' and computer_pick.casefold() == 'ciseaux':
            print(Fore.GREEN + 'Tu as gagné !')
            print(Fore.RESET + '______________________________________')
            self.user_wins += 1

        elif user_input.casefold() == 'papier' and computer_pick.casefold() == 'pierre':
            print(Fore.GREEN + 'Tu as gagné !')
            print(Fore.RESET + '______________________________________')
            self.user_wins += 1

        elif user_input.casefold() == 'ciseaux' and computer_pick .casefold()== 'papier':
            print(Fore.GREEN + 'Tu as gagné !')
            print(Fore.RESET + '______________________________________')
            self.user_wins += 1
        else:
            print(Fore.RED + 'Tu as perdu...')
            print(Fore.RESET + '______________________________________')
            self.computer_wins += 1

launch = Main(0, 0)

while True:
    launch.choice()
