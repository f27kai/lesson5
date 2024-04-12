# from colorama import init
# init()
# from colorama import Fore, Back, Style
# print(Fore.GREEN + 'green text')
# print(Back.YELLOW + 'yellow back')
# print(Style.BRIGHT + 'bright' + Style.RESET_ALL)
# print('default')


class Hello:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello World {self.name}"

hel = Hello("Asan")
print(hel)