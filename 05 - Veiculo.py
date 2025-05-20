# Criando a classe mãe "Veiculo"
class Veiculo:
    def __init__(self, modelo, ano, velocidade): # Criando os atributos
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
     
    # Criando as funções   
    def acelerar(self): # Criando a função de acelerar
        if self.velocidade == 0:
            self.velocidade += 10 
            print(f"O veículo começou a andar {self.velocidade} km/h!")
        elif self.velocidade > 0 and self.velocidade < 100:
            self.velocidade += 10
            print(f"O veículo acelerou e agora está andando {self.velocidade} km/h!")
        else:
            print("O veículo está no limite máximo de 100 km/h, não é possível acelerar mais!")
            
    def frear(self): # Criando a função de frear
        if self.velocidade == 0:
            print(f"O veículo está parado e não tem como frear mais!")
        elif self.velocidade > 10:
            self.velocidade -= 10
            print(f"O veículo freou e agora está andando {self.velocidade} km/h!")
        else:
            self.velocidade -= 10
            print("O veículo freou e agora está parado!")
  
# Criando as classes filhas           
class Carro(Veiculo): # Criando uma classe carro
    def __init__(self, modelo, ano, velocidade, portas, mala):
        super().__init__(modelo, ano, velocidade)
        self.portas = portas
        self.mala = mala
    
    def acelerar(self):
        if self.velocidade == 0:
            self.velocidade += 10 
            print(f"O carro {self.modelo} começou a andar {self.velocidade} km/h!")
        elif self.velocidade > 0 and self.velocidade < 100:
            self.velocidade += 10
            print(f"O carro {self.modelo} acelerou e agora está andando {self.velocidade} km/h!")
        else:
            print(f"O carro {self.modelo} está no limite máximo de 100 km/h, não é possível acelerar mais!")
            
    def frear(self):
        if self.velocidade == 0:
            print(f"O carro {self.modelo} está parado e não tem como frear mais!")
        elif self.velocidade > 10:
            self.velocidade -= 10
            print(f"O carro {self.modelo} freou e agora está andando {self.velocidade} km/h!")
        else:
            self.velocidade -= 10
            print(f"O carro {self.modelo} freou e agora está parado!")
            
    def abrir_mala(self):
        if self.velocidade == 0:
            if self.mala == False:
                print(f"A mala do carro {self.modelo} já está aberta!")
            else:
                self.mala = False
                print(f"A mala do carro {self.modelo} foi aberta!")
        else:
            print(f"Não é possível mexer na mala do carro {self.modelo} em movimento!")
            
    def fechar_mala(self):
        if self.velocidade == 0:
            if self.mala == True:
                print(f"A mala do carro {self.modelo} já está fechada!")
            else:
                self.mala = True
                print(f"A mala do carro {self.modelo} foi fechada!")
        else:
            print(f"Não é possível mexer na mala do carro {self.modelo} em movimento!")
            
    def status(self):
        print("STATUS DO VEÍCULO: \n")
        print(f"Veículo: Carro")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Portas: {self.portas}")
        print(f"Mala fechada: {self.mala}")

            
class Moto(Veiculo): # Criando uma classe moto
    def acelerar(self):
        if self.velocidade == 0:
            self.velocidade += 10 
            print(f"A moto {self.modelo} começou a andar {self.velocidade} km/h!")
        elif self.velocidade > 0 and self.velocidade < 100:
            self.velocidade += 10
            print(f"A moto {self.modelo} acelerou e agora está andando {self.velocidade} km/h!")
        else:
            print(f"A moto {self.modelo} está no limite máximo de 100 km/h, não é possível acelerar mais!")
            
    def frear(self):
        if self.velocidade == 0:
            print(f"A moto {self.modelo} está parado e não tem como frear mais!")
        elif self.velocidade > 10:
            self.velocidade -= 10
            print(f"A moto {self.modelo} freou e agora está andando {self.velocidade} km/h!")
        else:
            self.velocidade -= 10
            print(f"A moto {self.modelo} freou e agora está parado!")
            
    def empinar(self):
        print(f"A moto {self.modelo} foi empinada!")
        
    def status(self):
        print("STATUS DO VEÍCULO: \n")
        print(f"Veículo: Moto")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


#Criando os veículos           
moto1 = Moto("motoquin", 2008, 0)
carro1 = Carro("Optimus Prime", 2000, 0, 4, True)

# Chamando as funções dos veículos
print("----MEXENDO COM A MOTO----")
moto1.acelerar()
moto1.acelerar()
moto1.frear()
moto1.frear()
moto1.frear()
moto1.empinar()
moto1.status()
print("\n----MEXENDO COM O CARRO----")
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.abrir_mala()
carro1.fechar_mala()
carro1.status()