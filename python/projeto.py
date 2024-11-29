class Cliente:
    def __init__(self, id, nome, cpf, idade, email, telefone):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.telefone = telefone

class Quarto:
    def __init__(self, id, nome, valor, disponibilidade):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.disponibilidade = disponibilidade

class Reserva:
    def __init__(self, id, data_entrada, quarto, cliente, data_saida):
        self.id = id
        self.data_entrada = data_entrada
        self.quarto = quarto
        self.cliente = cliente
        self.data_saida = data_saida

class GerenciadorDeReservas:
    def __init__(self):
        self.lista_de_reservas = []
        self.historico_de_reservas = []
        self.lista_de_quartos = []
        self.lista_de_clientes = []
        self.id_reservas = 1

    def adicionarQuarto(self, quarto):
        self.lista_de_quartos.append(quarto)

    def verQuartos(self):
        return self.lista_de_quartos

    def editarQuarto(self, id, novo_quarto):
        for quarto in self.lista_de_quartos:
            if quarto.id == id:
                quarto.nome = novo_quarto.nome
                quarto.valor = novo_quarto.valor
                quarto.disponibilidade = novo_quarto.disponibilidade

    def excluirQuarto(self, id):
        self.lista_de_quartos = [quarto for quarto in self.lista_de_quartos if quarto.id != id]

    def verQuartosDisponiveis(self):
        return [quarto for quarto in self.lista_de_quartos if quarto.disponibilidade]

    def verQuartosReservados(self):
        return [quarto for quarto in self.lista_de_quartos if not quarto.disponibilidade]

    def fazerReserva(self, reserva):
        self.lista_de_reservas.append(reserva)
        reserva.quarto.disponibilidade = False

    def encerrarReserva(self, id):
        for reserva in self.lista_de_reservas:
            if reserva.id == id:
                self.lista_de_reservas.remove(reserva)
                reserva.quarto.disponibilidade = True
                self.historico_de_reservas.append(reserva)

    def adicionarCliente(self, cliente):
        self.lista_de_clientes.append(cliente)

    def verClientes(self):
        return self.lista_de_clientes


