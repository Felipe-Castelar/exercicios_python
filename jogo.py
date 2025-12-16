import random
class Personagem:
    def __init__(self, nome, nivel,vida):
        self.__nome= nome
        self.__nivel = nivel
        self.__vida = vida
           
    def get_nome(self):
        return self.__nome
    
    def get_nivel(self):
        return self.__nivel
    
    def get_vida(self):
        return self.__vida
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
    
    def receber_dano(self,dano):
        self.__vida -= dano
        if self.__vida <0:
            self.vida = 0
        
    
class Heroi(Personagem):
    def __init__(self, nome, nivel, classe, vida, habilidade):
        super().__init__(nome, nivel, vida)
        
        self.__habilidade = habilidade
        self.__classe = classe
    def get_habilidade(self):
        return self.__habilidade
    
    def get_classe(self):
        return self.__classe
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\nClasse: {self.get_classe()}\n"
    
    def Ataque_especial(self,alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8 )
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
        
    
class Inimigo(Personagem):
    def __init__(self, nome, nivel, vida, tipo):
        super().__init__(nome, nivel, vida)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\ntipo: {self.get_tipo()}\n"

class Jogo:
    '''classe orquestradora do jogo'''

    def __init__(self):
        self.heroi = Heroi(nome="clorisvaldo", vida=100, nivel=10, habilidade="cuzada",classe="trabalhador")
        self.inimigo= Inimigo(nome="macaco", vida=100, nivel=8, tipo="preto")
    
    def iniciar_batalha(self):
        '''fazer a gestão da batalha em turnos'''
        print("Iniciando a batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhe do herói:")
            print(self.heroi.exibir_detalhes())
            print("\nDetalhe do macaco:")
            print(self.inimigo.exibir_detalhes())
            
            input("Pressione Enter para atacar...")
            escolha=input("Escolha (1 - Ataque Normal, 2 - Ataque Especial):")
            
            if escolha =='1':
                self.heroi.atacar(self.inimigo)
            
            elif escolha == "2":
                self.heroi.Ataque_especial(self.inimigo)
                
            else:
                print("Escolha invalida. escolha novamente.")

            if self.inimigo.get_vida() > 0:
                #inimigo ataca heroi
                self.inimigo.atacar(self.heroi)
        
        if self.heroi.get_vida() > 0:
            print("Parabens, você venceu a batalha")
            
        else:
            print("Você foi derrotado")

#Criar instancia do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()