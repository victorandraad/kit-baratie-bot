import pyautogui
import keyboard
from functions import *

window = Window('Grand Line Adventures')

print("Posicione o seu mouse no pixel de coletar os alimentos e pressione aspas simples -> (').")

keyboard.wait("'")

x, y = pyautogui.position()

print(f'x = {x}, y = {y}')

while True:
    qntkits = int(input('quantidade de kits desejada: '))
    if qntkits < 8 and qntkits > 0:
        break
    print("A quantidade de kits deve estar entre 0 e 7")

print(f'Para fazer {qntkits} você precisa de {qntkits * 3700} beries.')

print("Se posicione olhando para a geladeira ao lado da lista de receitas para o kit baratie.")
print("E pressione aspas simples -> (') quando estiver pronto.")

keyboard.wait("'")

sleep(2)

armario = {
    'potato' : 4,
    'onion' : 23,
    'oil' : 10,
    'garlic' : 14,
    'rice' : 16,
    'farinha': 22,
    'shoyo' : 3,
    'salt' : 35,
    'tomato_sauce' : 14
}


geladeira = {
    'tomato': 10,
    'ovos' : 1,
    'bacon' : 3,
    'folha' : 12,
    'water' : 54,
    'cheese' : 3,
    'fish' : 10,
    'beef' : 20,
    'lemon' : 3
}

subcomponentes = {
    'macarrao' : 4,
    'arroz' : 8,
    'bife_frito' : 6,
    'prime_beef' : 7,
}

massas = 2 * qntkits
tigelas = 12 * qntkits

for item in armario:
    armario[item] *= qntkits

for item in geladeira:
    geladeira[item] *= qntkits

for item in subcomponentes:
    subcomponentes[item] *= qntkits

cortaveis = [
    geladeira['tomato'],
    geladeira['fish'],
    geladeira['lemon'],
    armario['onion'],
    armario['garlic'],
]

n_cortaveis = max(cortaveis)

def set_foreground_window():
    return window.set_foreground_window(window.hwnd)

def fazer_item(qnt, pegar=True):
    res_qnt = qnt     
    while res_qnt > 0:
        if res_qnt > 100:
            qnt = 100

        else:
            qnt = res_qnt
        
        set_foreground_window()
        keyboard.press_and_release('ctrl+enter')
        for c in range(qnt - 1):
            sleep(0.2)
            window.key(RIGHT)

        set_foreground_window()
        sleep(0.2)
        keyboard.press_and_release('enter')

        if pegar:
            pegar_item()

        res_qnt -= qnt

def pegar_item():
    pyautogui.moveTo(x, y)
    sleep(0.2)
    pyautogui.click(x, y)

def down(times):
    for c in range(times):
        sleep(0.2)
        window.key(DOWN)

def up(times):
    for c in range(times):
        sleep(0.2)
        window.key(UP)

def left(times):
    for c in range(times):
        sleep(0.2)
        window.key(LEFT)

def right(times):
    for c in range(times):
        sleep(0.2)
        window.key(RIGHT)


def open_door():
    set_foreground_window()
    sleep(0.2)

    keyboard.press_and_release('x')
    sleep(1)

    keyboard.press_and_release('x')
    sleep(1)

def close_door():
    sleep(0.2)
    keyboard.send('esc')
    sleep(1)

def spam_x(n):
    for c in range(n):
        set_foreground_window()
        sleep(0.4)
        keyboard.press_and_release('x')
    sleep(3)

# pegar os cortaveis geladeira
def pegar_os_cortaveis_geladeira():
    left(2)

    open_door()

    down(1)

    fazer_item(cortaveis[0])

    down(8)

    fazer_item(cortaveis[1])

    down(2)

    fazer_item(cortaveis[2])

    up(10)

    close_door()

#pegar os cortaveis armario
def pegar_os_cortaveis_armario():
    up(1)

    left(1)

    open_door()

    down(2)

    fazer_item(cortaveis[3])

    down(2)

    fazer_item(cortaveis[4])

    up(3)

    close_door()

# cortar os cortaveis
def cortar_os_cortaveis():
    right(1)
    up(1)
    right(1)
    
    sleep(1)
    spam_x(n_cortaveis)

# pegar farinha
def pegar_farinha():
    down(1)

    left(1)

    open_door()

    down(6)

    fazer_item(armario['farinha'])

    up(5)

    close_door()

# pegar agua
def pegar_agua():
    down(1)
    left(1)

    open_door()

    down(7)

    fazer_item(geladeira['water'])

    up(6)

    close_door()

# transformar em massa
def transformar_em_massa():
    down(2)
    right(1)
    sleep(1)

    spam_x(armario['farinha'])

# cortar o suficiente para macarrao
def cortar_massa():
    up(4)

    right(1)
    sleep(1)

    spam_x(subcomponentes['macarrao'] * 5)

# colocar o macarrao para fazer
def fazer_macarrao():
    up(1)

    left(1)

    sleep(1)

    open_door()

    down(1)

    fazer_item(subcomponentes['macarrao'])

    close_door()

# pegar o resto do armario
def pegar_resto_armario():
    down(2)

    left(1)

    sleep(1)

    open_door()

    down(1)

    fazer_item(armario['potato'])

    down(2)

    fazer_item(armario['oil'])

    down(2)

    fazer_item(armario['rice'])

    down(2)

    fazer_item(armario['shoyo'])

    down(1)

    fazer_item(armario['salt'])

    down(1)

    fazer_item(armario['tomato_sauce'])

    up(8)

    close_door()

# pegar o resto do geladeira
def pegar_resto_geladeira():
    down(2)

    left(1)

    sleep(1)

    open_door()

    down(3)

    fazer_item(geladeira['ovos'])

    down(1)

    fazer_item(geladeira['bacon'])

    down(1)

    fazer_item(geladeira['folha'])

    down(3)

    fazer_item(geladeira['cheese'])

    down(2)

    fazer_item(geladeira['beef'])

    up(9)

    close_door()

# pegar tigelas
def pegar_tigelas():
    down(1)

    left(1)

    sleep(1)

    open_door()

    down(1)

    fazer_item(tigelas)

    close_door()

# colocar o resto os subcomponentes para fazer
def fazer_bife_frito():
    down(2)

    left(1)

    sleep(1)

    open_door()

    down(1)

    fazer_item(subcomponentes['bife_frito'], False)

    close_door()

    

def fazer_bife_prime():
    up(1)

    left(1)

    sleep(1)

    open_door()

    down(1)

    fazer_item(subcomponentes['prime_beef'], False)

    close_door()


def fazer_arroz():
    up(6)

    left(1)

    sleep(1)

    open_door()

    down(2)

    fazer_item(subcomponentes['arroz'], False)

    close_door()


# coletar os subcomponentes
def coletar_subcomponenetes():
    #cozinhar
    open_door()

    down(1)

    pegar_item()

    down(1)

    pegar_item()

    up(1)

    close_door()

    down(7)

    left(1)

    # fritar
    open_door()

    down(1)

    pegar_item()

    close_door()

    up(1)

    left(1)

    open_door()

    down(1)

    pegar_item()

    close_door()

    down(1)
    
    left(1)


# fazer o resto
def fazer_componenetes():
    open_door()
    down(2)

    for c in range(5):
        fazer_item(1 * qntkits, False)
        down(1)

    up(5)

    close_door()

    up(1)
    left(1)


    open_door()
    
    down(2)

    fazer_item(2 * qntkits, False)

    down(2)

    fazer_item(1 * qntkits, False)

    up(3)

    close_door()

    up(6)

    left(1)

    open_door()

    down(3)

    fazer_item(1 * qntkits, False)

    down(1)

    fazer_item(2 * qntkits, False)

    down(3)

    fazer_item(1 * qntkits, False)

    close_door()

    right(1)

    sleep(1)

    open_door()

    down(1)

    for c in range(4):
        fazer_item(1 * qntkits, False)
        down(1)

    up(3)

    close_door()


# montar o kit
def montar_kit():
    down(7)

    left(1)

    sleep(1)

    open_door()

    down(2)

    for c in range(5):
        pegar_item()
        down(1)

    up(5)

    close_door()

    up(1)

    left(1)

    open_door()
    
    down(2)

    pegar_item()

    down(2)

    pegar_item()

    up(3)

    close_door()

    up(6)
    
    left(1)

    open_door()

    down(3)

    pegar_item()

    down(1)

    pegar_item()

    down(3)

    pegar_item()

    close_door()

    right(1)
    sleep(1)

    open_door()

    down(1)

    for c in range(4):
        pegar_item()
        down(1)

    down(2)

    fazer_item(qntkits, False)

    up(6)

    close_door()



pegar_os_cortaveis_geladeira()
pegar_os_cortaveis_armario()
cortar_os_cortaveis()
pegar_farinha()
pegar_agua()
transformar_em_massa()
cortar_massa()
fazer_macarrao()
pegar_resto_armario()
pegar_resto_geladeira()
pegar_tigelas()
fazer_bife_frito()
fazer_bife_prime()
fazer_arroz()

for c in range(240 * qntkits):
    print(f'Proxima ação em {(240 * qntkits) - c} segundos...')
    sleep(1)

print("Pressione aspas simples (') para continuar o bot.")
keyboard.wait("'")

coletar_subcomponenetes()
fazer_componenetes()

for c in range(540 * qntkits):
    print(f'Proxima ação em {(540 * qntkits) - c} segundos...')
    sleep(1)

print("Pressione aspas simples (') para continuar o bot.")
keyboard.wait("'")

montar_kit()