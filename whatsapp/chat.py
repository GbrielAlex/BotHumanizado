"""
preciso automatisar minhas mensagens para meus clientes gostaria de saber valores, e gostaria que entrasse em contato comigo para explicar meljor, quero poder mandar
mensagens de conbrança em determinado dia com o clientes com vencimento diferente
"""

import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
# deescrever os passos manuais e dps trasnformar isso em codigo


webbrowser.open('web.whatsapp.com/')
sleep(20)
# ler planilhas e extrarir informações dela

workbook = openpyxl.load_workbook("clientes.xlsx")
pagina_cliente = workbook["Sheet1"]

for linha in pagina_cliente.iter_rows(min_row=2):
    # nome , telefone e vencimento
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    # criar liks personalisados do whatsapp e enviar mensagens para cada cliente com base nos dados da planilhas
    # htttps://web.whatsapp.com/send?phone=55555555&text=

    mensagem = f"Olá {nome} seu boleto vence no dia {vencimento.strftime('%d/%m/%y')}"
    link_mensagem_whatsapp = f"web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
    webbrowser.open(link_mensagem_whatsapp)
    sleep(10)
    seta = pyautogui.locateCenterOnScreen('seta.png', confidence=0.8, region=(0, 0, 1920, 1080))
    sleep(5)
    pyautogui.click(seta[0],seta[1])
    sleep(5)
    pyautogui.hotkey('ctrl','w')
    sleep(5)




