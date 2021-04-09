from dependencies import *

while True:
    # print the menu
    menu('Facao travazap 3000')

    # gets the message
    mensagem()

    # gets hwo many times the message should be sent
    qnt = quantidade()

    # timer
    timer(5)
    # spams the message how many times you selected
    spammer(qnt)

    # asks if you want to spam again
    resposta = continuar()
    if resposta == 'n':
        input('Aperte enter para fechar!')
        break
    elif resposta == 's':
        continue
