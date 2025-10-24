from flask import Flask, render_template, request, abort, jsonify,redirect,url_for,session

app = Flask(__name__)
app.secret_key = '-->gostosa_a_leitinho<--'



class Produto:
    PRODUTOS = [
    {'senha': '1', 'nome': 'Notebook Gamer', 'preco': 5200.00},
    {'senha': '2', 'nome': 'Mouse sem fio', 'preco': 150.00},
    {'senha': '3', 'nome': 'Teclado Mecanico RGB', 'preco': 350.00},
    {'senha': '4', 'nome': 'Smartphone intermediário', 'preco': 1800.00},
    {'senha': '5', 'nome': 'Smart TV 50 polegadas', 'preco': 3200.00},
    {'senha': '6', 'nome': 'Fone de ouvido Bluetooth', 'preco': 250.00},
    {'senha': '7', 'nome': 'Ventilador de coluna', 'preco': 260.00},
    {'senha': '8', 'nome': 'Aspirador de pó e água', 'preco': 290.00},
    {'senha': '9', 'nome': 'Air Fryer', 'preco': 400.00},
    {'senha': '10', 'nome': 'Mouse sem fio Gamer recarregável', 'preco': 120.00},
    {'senha': '11', 'nome': 'Caixa de som bluetooth', 'preco': 180.00},
    {'senha': '12', 'nome': 'Tablet 10 polegadas', 'preco': 900.00},
    {'senha': '13', 'nome': 'Smartwatch básico', 'preco': 350.00},
    {'senha': '14', 'nome': 'Teclado sem fio', 'preco': 280.00},
    {'senha': '15', 'nome': 'Câmera de segurança IP', 'preco': 480.00},
    {'senha': '16', 'nome': 'Carregador portátil (Power Bank)', 'preco': 150.00},
    {'senha': '17', 'nome': 'Ventilador de mesa', 'preco': 120.00},
    {'senha': '18', 'nome': 'Geladeira pequena (1 porta)', 'preco': 1200.00},
    {'senha': '19', 'nome': 'Liquidificador', 'preco': 180.00},
    {'senha': '20', 'nome': 'Micro-ondas compacto', 'preco': 650.00}
    ]

    def get_produtos(self):
        return self.PRODUTOS
    
    def set_produto(self, id, nome, preco):
        self.PRODUTOS[int(id)-1] = {'id': id, 'nome': nome, 'preco': preco}

    def logar(self,nome,senha):
        login = False
        
        for i in self.PRODUTOS:            
            if senha == i['senha'] :
                if nome == i['nome']:
                    login = True
            elif senha == 'gostosa.com.br':
                if nome == 'punheteiro':
                    login = "cafetão"
            return login
            
    def add(self, nome, preco):
        n = 1
        for i in self.PRODUTOS:
            n += 1
       
        novo_produto = {'id':n,'nome':nome, 'preco':preco}
        self.PRODUTOS.append(novo_produto)        
        
    
    def deletar(self,id):
        id2 = int(id)
        n = 0
        for i in self.PRODUTOS:
            if i['id'] == id2:
                self.PRODUTOS.pop(n)
                break
            n += 1


