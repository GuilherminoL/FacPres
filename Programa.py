import pyautogui
import time
pyautogui.alert('abra o Slack no canal da sua turma \n Após clicar em ok não mecha no computador')
pyautogui.hotkey('Ctrl','Alt','t')
time.sleep(3)
pyautogui.write('slack') 
pyautogui.press('Enter')
time.sleep(2)
pyautogui.click(573, 943) # X: 573  y:943 essa é a posição do comentarios do ultimo post     !!no meu pc!!
time.sleep(3)
pyautogui.hotkey('Ctrl','a')
time.sleep(1)
pyautogui.hotkey('Ctrl','c')
# até  aqui apenas abrimos o Slack demos um Ctrl A e um Ctrl C
pyautogui.hotkey('Ctrl','Alt','t')
time.sleep(3)
pyautogui.write('cd Desktop') 
pyautogui.press('Enter')
pyautogui.write('touch Checkin.txt')
pyautogui.press('Enter')
time.sleep(1)
pyautogui.write('xdg-open Checkin.txt')
pyautogui.press('Enter')
time.sleep(3)
pyautogui.hotkey('Ctrl','a')
pyautogui.hotkey('Backspace')
pyautogui.hotkey('Ctrl','v')
pyautogui.hotkey('Ctrl','s')
pyautogui.hotkey('Ctrl','q')
# Agora criamos (caso ja não exista) e colocamos o conteudo que copiamos em um txt
# Hora de tratar oq temos :)
arquivo = open('/home/guilher/Desktop/Checkin.txt','r+').readlines(-0)
ultimaOcorrencia = arquivo[::-1].index('Devs check-inAPP  14h\n') +47
arquivo = arquivo[ultimaOcorrencia:-1]
contagem = 0
saida = [[]]
cont = 0
for item in arquivo:
    if item == 'Responder…\n':
        break

    if item == '(editado)\n':
        continue

    if (item == '\n' or item == '1\n'):
        continue

    contagem += 1

    if contagem % 4 == 0:
        saida.append([])
        cont += 1

    if item[0] == ':':
        continue

    saida[cont].append(item)