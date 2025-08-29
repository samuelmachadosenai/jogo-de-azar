import time
import random 

saldo = 100
numero = (1, 2, 3, 4, 5)
repeticoes = 10
aposta_minima = 0.40  

print("Bem-vindo à roleta!")

try:
    while True:
        print(f"\nSaldo atual é: R${saldo}")  

        
        aposta = float(input(f'Quanto você deseja apostar? (mínimo de R${aposta_minima}): '))  

        if aposta < aposta_minima:
            print(f'Aposta mínima é R${aposta_minima}, tente novamente.')
            continue  

        
        if aposta > saldo:
            print(f"Você não tem saldo suficiente para lançar uma aposta. Tente novamente.")
            continue  
        
        print("A roleta está girando...")
        print("A roleta está girando", end="")
        for i in range(5):  
         time.sleep(1)
        print(".", end="", flush=True)
        print()  
        numero_girado = random.choice(numero)
        print(f"O número sorteado foi: {numero_girado}")

        resultado = random.choice([True, False]) 

        if resultado:
            saldo += aposta  
            print(f"Parabéns, você ganhou! Seu novo saldo é: R${saldo}")
        else:
            saldo -= aposta 
            print(f"Você perdeu. Seu novo saldo é: R${saldo}")

        
        if saldo <= 0:
            print("Você ficou sem saldo. Fim do jogo!")
            break  

        time.sleep(2)

except:
    print(f"Ocorreu um erro: {e}")