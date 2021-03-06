from status import Status #Importação da Super classe
from time import sleep


class Personagem(Status): # Classe com a Super classe
    def __init__(self, nome, dinheiro=5, alimento=10, estamina=5): # Inicialização da classe com os atributos próprios dela e os que serão utilizados da Super
        super().__init__(dinheiro, alimento, estamina) #inicialização da Super classe dentro da classe Personagem
        self.__nome = nome
      
    def __str__(self):  
        return f'''
                        Você está com:
                         {self.dinheiro} de dinheiro
                         {self.estamina} de estamina
                         {self.alimento} de alimento

                '''

    @property #Properties e Setters dos atributos privados
    def nome(self):
        return self.__nome

    def dormir(self):
        self.estamina += 10

    def dinheiroAD(self, valor):
        self.dinheiro += valor

    def dinheiroRE(self, valor):
        self.dinheiro -= valor

    def estaminaAD(self, valor):
        self.estamina += valor

    def estaminaRE(self, valor):
        self.estamina -= valor

    def alimentoAD(self, valor):
        self.alimento += valor

    def alimentoRE(self, valor):
        self.alimento -= valor

    def diaAdd(self, valor):
        self.dia += valor

    def aleatorios(self): #Método para eventos aleatórios ao jogador escolher trabalho presencial
        from random import randint, choice #importação das bibliotecas a serem utilizadas no méto. Para fins didáticos colocamos dentro do método
        aleatorio = randint(1, 10) #Variável para receber um número de 1 a 10 onde serão escolhidos os eventos
        if aleatorio > 7:
            eventos = ['acidente de carro', 'dor de barriga',
                       'happy hour', 'dor de cabeça', 'quebrou a perna'] #lista de eventos
            perde_dia = choice(eventos) #função choice para escolher o evento de forma aleatória
            if perde_dia == 'acidente de carro':
                self.dinheiro -= 10 #método importado da super classe para debitar dinheiro
                self.estamina += 10 # Método importado da super classe para adicionar energia, uma vez que o jogador não irá trabalahr
                self.diaAdd(2) # método importada da super classe para adicionar dias
                print(f'''Você sofreu um acidente de carro voltando do trabalho. Ficará impossibilitado de trabalhar por 2 dias.
                    Você não tinha seguro e perdeu 10 unidades de dinheiro''')
            elif perde_dia == 'dor de barriga':
                self.dinheiro -= 5
                self.estamina += 10
                self.diaAdd(1)
                print(f'''Você comeu algo estragado. Ficará impossibilitado de trabalhar por 1 dias.
                    Você perdeu 5 unidade de dinheiro''')
            elif perde_dia == 'happy hour':
                opcao = input(
                    'Você recebeu um convite para um happy hour. Deseja ir? [S/N]').upper().strip()[0]
                if opcao == 'S':
                    self.dinheiro -= 5
                    self.estamina -= 2
                    print(f'''Você exagerou... Chegou tarde em casa e não vai conseguir dormir o número suficiente de horas para recuperar suas energias.''')
                    sleep(3)
                else:
                    print(f'Obrigado... fica para uma próxima vez...')
            elif perde_dia == 'dor de cabeça':
                self.dinheiro -= 1
                self.estamina += 10
                self.diaAdd(1)
                print(f'''Você acordou com uma baita dor de cabeça e não vai conseguir trabalhar por 1 dia.
                    Você perdeu 1 unidade de dinheiro''')
            elif perde_dia == 'quebrou a perna':
                self.dinheiro -= 2
                self.estamina += 10
                self.diaAdd(7)
                print(f'''Você quebrou a perna e não vai conseguir trabalhar por 7 dias.
                    Você perdeu 2 unidades de dinheiro com gastos de medicação''')
