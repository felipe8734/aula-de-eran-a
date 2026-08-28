class Carro:
    def __init__(self, carro, nome, ano, senha):
        self.carro = carro
        self.nome = nome  
        self.ano = ano
        self.senha = senha

    def ligar_motor(self):
        
        print(f'[SISTEMA]: motor do {self.nome} roncando forte!')



class CarroEsportivo(Carro):
    def __init__(self, marca, nome, ano, senha, modo_pista):
        super().__init__(marca, nome, ano, senha)
        self.modo_pista = modo_pista
    
    def activar_nitro(self):
        print(f"[PERFORMANCE]: Nitro ativado no {self.nome}! Modo {self.modo_pista} ativo.")


class CarroClassico(Carro):
    def __init__(self, marca, nome, ano, senha, placa_preta):
        super().__init__(marca, nome, ano, senha)
        self.placa_preta = placa_preta  

    def exibir_status(self):
        status = "Sim" if self.placa_preta else "Não"
        print(f"[COLEÇÃO]: {self.nome} ({self.ano}) - Placa Preta: {status}.")



garagem = {
    1: CarroEsportivo('McLaren', 'Senna', 2019, 'senna123', 'Race'),
    2: CarroEsportivo('Ferrari', 'Roma', 2021, 'roma2026', 'Sport'),
    3: CarroEsportivo('Lamborghini', 'Huracán STO', 2022, 'lambosto', 'Trofeo'),
    4: CarroClassico('Mitsubishi', '3000GT', 1994, '3000gt', True),
    5: CarroClassico('Nissan', 'Skyline GT-R R34', 1999, 'skylineR34', False),
    6: CarroClassico('Toyota', 'Supra MK4', 1998, 'supraMK4', True)
}

print('=== BEM-VINDO À SUA GARAGEM DOS SONHOS ===')

print('qual carro o senhor vai querer hj:'
'\n1-mclarem sena' \
'\n2-ferrari roma ' 
'\n3-Lamborghini Huracán STO '
'\n4-mitsubishi 3000gt' 
'\n5-Nissan Skyline GT-R R34 ' 
'\n6- Toyota Supra MK4')  

try:
    r = int(input('escolha o seu carro senhor(a): '))
    
    if r in garagem:
        carro_escolhido = garagem[r]
        senha_digitada = input(f'Digite a senha para liberar o {carro_escolhido.nome}: ')
        
        if senha_digitada == carro_escolhido.senha:
            print('\nAcesso permitido!')
            carro_escolhido.ligar_motor() 
            
            if isinstance(carro_escolhido, CarroEsportivo):
                carro_escolhido.activar_nitro()
            elif isinstance(carro_escolhido, CarroClassico):
                carro_escolhido.exibir_status()
                
            print('Boa viagem! ')
        else:
            print('\nSenha incorreta! Alarme disparado.')
    else:
        print('\nOpção inválida! Escolha de 1 a 6.')
except ValueError:
    print('\nPor favor, digite apenas números inteiros.')