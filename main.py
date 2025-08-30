import time
import random 

saldo = 100
numero = (1, 2, 3, 4, 5,6,7,8,9,10,11,11,13,14,15)
repeticoes = 10
aposta_minima = 0.40  

print("Bem-vindo ao roda-roda impar par!!! ")
print("se cair par você ganha, DINHEIRO FACIL!!! 50/50 de chance de ganho.")

try:
    chance_mais_impar = 1
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

        if numero_girado %2 == 0:
            saldo += aposta
            print(f"parabens, caiu um numero par ({numero_girado}).voce ganhou! seu novo saldo é: R${saldo}")
        else:
          saldo -= aposta
          print(f"caiu um numero ({numero_girado}). seu novo saldo é:R${saldo} ")

        
        if saldo <= 0:
            print("Você ficou sem saldo. Fim do jogo!")
            break  

        time.sleep(2)

except:
     print(f"Ocorreu um erro")