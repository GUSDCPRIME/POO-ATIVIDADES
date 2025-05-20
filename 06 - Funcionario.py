# Criando a classe mãe funcionario
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        
# Criando as funções da classe
    def get_nome(self): # obter nome
        print(f"Nome do funcionário identificado: {self._nome}")
        
    def set_nome(self, novo_nome): # mudar nome
        self._nome = novo_nome
        print(f"Novo nome do funcionário identificado: {self._nome}")

    def get_cpf(self): # obter cpf
        print(f"CPF do funcionário identificado: {self._cpf}")
        
    def set_cpf(self, novo_cpf): #mudar cpf
        self._cpf = novo_cpf
        print(f"Novo CPF do funcionário identificado: {self._cpf}")

    def get_salario(self): # obter salário
        print(f"Salário do funcionário identificado: {self._salario}")
        
    def set_salario(self, novo_salario): # mudar salário
        self._salario = novo_salario
        print(f"Novo salário do funcionário identificado: {self._salario}")
        
    def exibir_dados(self): # exibir dados do funcionário
        print("DADOS DO FUNCIONÁRIO IDENTIFICADO")
        print(f"Nome: {self._nome}")
        print(f"CPF: {self._cpf}")
        print(f"Salário: {self._salario}")
    
#Criando as classes filhas
class Operador(Funcionario): # criando a classe filha de operador
    def __init__(self, nome, cpf, salario, turno):
        super().__init__(nome, cpf, salario)
        self._turno = turno
    # recriando as mesmas funções da classe mãe  
    def get_nome(self):
        print(f"Nome do operador identificado: {self._nome}")
    
    def set_nome(self, novo_nome):
        self._nome = novo_nome
        print(f"Novo nome do operador identificado: {self._nome}")

    def get_cpf(self):
        print(f"CPF do operador {self._nome}: {self._cpf}")
        
    def set_cpf(self, novo_cpf):
        self._cpf = novo_cpf
        print(f"Novo CPF do operador {self._nome}: {self._cpf}")

    def get_salario(self):
        print(f"Salário do operador : {self._salario}")
        
    def set_salario(self, novo_salario):
        self._salario = novo_salario
        print(f"Novo salário do operador {self._nome}: {self._salario}")
        
    # criando funções para o atributo adicional      
    def get_turno(self): # obter o turno
        print(f"Turno do operador {self._nome}: {self._turno}")
      
    def set_turno(self): # mudar o turno
        print(f"Novo turno operador {self._nome}:")
        print(f"1. Manhã")
        print("2. Tarde")
        print("3. Noite")
        novo_turno = int(input("Escolha o novo turno: "))
        
        if novo_turno == 1:
            self._turno = "Manhã"
        elif novo_turno == 2:
            self._turno = "Tarde"
        elif novo_turno == 3:
            self._turno = "Noite"
            
        
    def exibir_dados(self): # exibindo dados com o atributo adicional
        print("DADOS DO FUNCIONÁRIO IDENTIFICADO")
        print(f"Nome: {self._nome}")
        print(f"CPF: {self._cpf}")
        print(f"Salário: {self._salario}")
        print(f"Turno: {self._turno}")
        
class Gerente(Funcionario): # criando a classe filha do gerente
    def __init__(self, nome, cpf, salario, bonus):
        super().__init__(nome, cpf, salario)
        self._bonus = bonus
    
    # recriando as funções da classe mãe
    def get_nome(self):
        print(f"Nome do gerente identificado: {self._nome}")
    
    def set_nome(self, novo_nome):
        self._nome = novo_nome
        print(f"Novo nome do gerente identificado: {self._nome}")

    def get_cpf(self):
        print(f"CPF do gerente {self._nome}: {self._cpf}")
        
    def set_cpf(self, novo_cpf):
        self._cpf = novo_cpf
        print(f"Novo CPF do gerente {self._nome}: {self._cpf}")

    def get_salario(self):
        print(f"Salário do gerente {self._nome}: {self._salario}")
        
    def set_salario(self, novo_salario):
        self._salario = novo_salario
        print(f"Novo salário do gerente {self._nome}: {self._salario}")
      
    # criando funções para o atributo adicional
    def get_bonus(self): # obter o bonus salarial
        print(f"Turno do gerente {self._nome}: {self._bonus}")
        
    def set_bonus(self, novo_bonus): # mudar o bonus salarial
        self._bonus = novo_bonus
            
    def exibir_dados(self): #exibindo dados com o atributo adicional
        print("DADOS DO GERENTE IDENTIFICADO")
        print(f"Nome: {self._nome}")
        print(f"CPF: {self._cpf}")
        print(f"Salário: {self._salario}")
        print(f"Bonus: {self._bonus}")
        print(f"Salário final = {self._bonus + self._salario}")
        
# Criando os funcionários

operador1 = Operador("Carlos", 16262639326, 1500, "Manhã")
gerente1 = Gerente("Gustavo", 36565629536, 1000, 300)

# tentando as funções dos funcionários
operador1.get_nome()
operador1.get_salario()
operador1.set_salario(1300)
operador1.get_cpf()
operador1.set_turno()
operador1.get_turno()
operador1.exibir_dados()
print('\n')
gerente1.get_nome()
gerente1.get_salario()
gerente1.set_salario(800)
gerente1.get_cpf()
gerente1.set_bonus(600)
gerente1.get_bonus()
gerente1.exibir_dados()