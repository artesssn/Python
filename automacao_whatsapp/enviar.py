import pandas as pd
import pywhatkit as kit
import time
import pyautogui

# --- COORDENADAS PARA TELA 2 (À ESQUERDA) so se tiver o whats na segunda tela---
X_CAMPO_ZAP = -800  
Y_CAMPO_ZAP = 600   
# --------------------------------------------

print("Lendo planilha e iniciando disparos...")
mensagem = "Mensagem de teste."

df = pd.read_excel("numeros.xlsx")

for numero in df["numero"]:
    numero = str(numero)
    if not numero.startswith("55"):
        numero = "55" + numero

    print(f"Abrindo conversa para {numero}...")

    # 1. Abre o WhatsApp (Isso cria uma aba nova)
    kit.sendwhatmsg_instantly(
        phone_no=f"+{numero}",
        message=mensagem,
        wait_time=15, 
        tab_close=False
    )

    # 2. Espera a página carregar totalmente
    time.sleep(5) 

    # 3. Dá o foco na tela 2 e envia
    pyautogui.click(X_CAMPO_ZAP, Y_CAMPO_ZAP)
    time.sleep(2)
    pyautogui.press("enter")
    
    print(f"✅ Mensagem enviada para {numero}")

    # --- Funçao importante para fechar a aba ---
    # Esperamos o envio e FECHAMOS a aba imediatamente.
    # Assim, quando o próximo número rodar, o navegador estará limpo
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w') 
    
    print("Aguardando fechamento total para o próximo...")
    time.sleep(5) 

print("Processo finalizado!")