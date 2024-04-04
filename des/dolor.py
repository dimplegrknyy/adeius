from rich import print

def cprint(text, color):
    print(f'[{color}]{text}[/{color}]')

cprint(f'\n>>> stake VST | {address_wallet} | {error}', 'red')
