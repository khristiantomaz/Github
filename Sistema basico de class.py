class Pessoa:
    def __init__(self, Nome , Rua):
        self.set_Nome(Nome)
        self.set_Rua(Rua)

# definindo o nome
    def set_Nome(self, Nome):
        self.Nome = Nome

# definindo a  rua
    def set_Rua(self, Rua):
        self.Rua= Rua

# fazendo a função de puxar 
    def get_Rua(self):
        return self.Rua
    
    def get_Nome(self):
        return self.Nome
    
# adicinando o usuario na class
pessoa1= Pessoa ('Khristian tomaz', 'maresias 123')

# imprimindo os dados de usuario
print(f'Nome:{pessoa1.get_Nome()}, Endereço:{pessoa1.get_Rua()}')
