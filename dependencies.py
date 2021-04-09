from pynput.keyboard import Key, Controller
import pyperclip
from time import sleep


def menu(menu_msg):
    print('-' * 20)
    print(f'{menu_msg: ^20}')
    print('-' * 20)


def mensagem():
    while True:
        try:
            msg = str(input('Digite a mensagem: '))
        except:
            print('Por alguma razao sua mensagem e invalida')
        else:
            if len(msg) > 0:
                print('Mensagem copiada com sucesso!')
                break
    pyperclip.copy(f'{msg}')


def quantidade():
    while True:
        try:
            qnt = int(input('Qual a quantidade de mensagem: '))
        except:
            print('Digite um numero valido!')
        else:
            if qnt > 0:
                print('Quantidade captada com sucesso!')
                return qnt
            else:
                print('Digite um numero maior que 0!')


def timer(qunt):
    from time import sleep
    cont = qunt + 1
    while True:
        cont -= 1
        print(f'{cont}')
        sleep(1)
        if cont == 1:
            print(f'{"Comecando o ataque!": ^30}')
            break


def spammer(quantidade):
    keyboard = Controller()
    pico = 0
    while pico != quantidade:
        pico += 1
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release(Key.ctrl)
        keyboard.release('v')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(0.06)
        if pico % 10 == 0:
            print(f'{pico}')
    print(f'Atacado com sucesso!\nTotal {pico} mensagens.')


def continuar():
    while True:
        menu('Deseja continuar ( S / N )')
        resposta = str(input('')).lower().strip()
        while resposta not in 'sn':
            print('Digite uma opcao valida ( S / N )')
            resposta = str(input('')).lower().strip()
        return resposta
