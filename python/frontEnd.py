from projeto import*
import flet as ft    

#página do flet
def main(page: ft.Page):
    hotel = GerenciadorDeReservas()
    page.title = "App Hotel" 

    output = ft.Text()
    
    def ver_quartos_disponiveis(e):
        output.value = "\n".join([f"ID: {quarto.id} - Nome: {quarto.nome}" for quarto in hotel.verQuartosDisponiveis()])
        page.update()

    def ver_quartos_reservados(e):
        output.value = "\n".join([f"ID: {quarto.id} - Nome: {quarto.nome}" for quarto in hotel.verQuartosReservados()])
        page.update()

    def fazer_reserva(e):
        # Mostra quartos disponíveis
        quartos_disponiveis = hotel.verQuartosDisponiveis()
        if quartos_disponiveis:
            escolha_quarto = "\n".join([f"ID:{quarto.id} - Nome: {quarto.nome} - R${quarto.valor}" for quarto in quartos_disponiveis])
            output.value = f"Escolha um quarto disponível:\n{escolha_quarto}\n\nDigite o ID do quarto:"
            page.update()

            def reservar_quarto(e):
                id_quarto = int(e.control.value)
                quarto_selecionado = next((quarto for quarto in hotel.lista_de_quartos if quarto.id == id_quarto), None)
                if quarto_selecionado and quarto_selecionado.disponibilidade:
                    clientes_lista = "\n".join([f"{cliente.id} - {cliente.nome}" for cliente in hotel.lista_de_clientes])
                    output.value = f"Escolha um cliente:\n{clientes_lista}\n\nDigite o ID do cliente:"
                    page.update()

                    def finalizar_reserva(e):
                        id_cliente = int(e.control.value)
                        cliente_selecionado = next((cliente for cliente in hotel.lista_de_clientes if cliente.id == id_cliente), None)
                        if cliente_selecionado:
                            data_entrada = "2024-12-01"  # Substitua conforme necessário
                            data_saida = "2024-12-10"  # Substitua conforme necessário
                            reserva = Reserva(id=hotel.id_reservas, data_entrada=data_entrada, quarto=quarto_selecionado, cliente=cliente_selecionado, data_saida=data_saida)
                            hotel.fazerReserva(reserva)
                            hotel.id_reservas += 1
                            output.value = f"Reserva do quarto {quarto_selecionado.nome} feita com sucesso para {cliente_selecionado.nome}"
                            page.update()
                    page.add(ft.TextField(label="ID Cliente", on_submit=finalizar_reserva))
                else:
                    output.value = "Quarto não disponível ou inválido."
                    page.update()
            page.add(ft.TextField(label="ID Quarto", on_submit=reservar_quarto))
        else:
            output.value = "Não há quartos disponíveis."
            page.update()

    def encerrar_reserva(e):
        reservas_atuais = "\n".join([f"{reserva.id} - {reserva.quarto.nome} - {reserva.cliente.nome}" for reserva in hotel.lista_de_reservas])
        output.value = f"Reservas ativas:\n{reservas_atuais}\nDigite o ID da reserva para encerrar:"
        page.update()

        def encerrar_reserva_final(e):
            id_reserva = int(e.control.value)
            reserva_selecionada = next((reserva for reserva in hotel.lista_de_reservas if reserva.id == id_reserva), None)
            if reserva_selecionada:
                hotel.encerrarReserva(id_reserva)
                output.value = f"Reserva de {reserva_selecionada.cliente.nome} no quarto {reserva_selecionada.quarto.nome} encerrada com sucesso."
                page.update()
            else:
                output.value = "Reserva não encontrada."
                page.update()
        page.add(ft.TextField(label="ID Reserva", on_submit=encerrar_reserva_final))


#--------------------------------------------------------------------------------------------------------------------------
#                                        gerenciar quartos e clientes
#--------------------------------------------------------------------------------------------------------------------------
    
    #CLIENTES
    def gerenciar_clientes(e):
        txt_titulo_clientes = ft.Text("Cadastrar Clientes:", size=15, weight="bold")
        page.update()

        def adicionar_clientes(e):
            if not txt_nome_cliente.value:
                txt_nome_cliente.error_text = "Por favor digite o nome do Cliente"
            if not txt_cpf_cliente.value:
                txt_cpf_cliente.error_text = "Por favor insira o valor do quarto"
            if not txt_idade.value:
                txt_idade.error_text = "Por favor insira a idade do cliente"
            if not txt_email.value:
                txt_email.error_text = "Por favor insira o email do cliente"
            if not txt_numero.value:
                txt_numero.error_text = "Por favor insira o numero do cliente"
            else:
                nome_cliente = txt_nome_cliente.value
                valor_cpf = txt_cpf_cliente.value
                email_cliente = txt_email.value
                idade_cliente = txt_idade.value
                numero_cliente = txt_numero.value
                novo_cliente = Cliente(id=len(hotel.lista_de_clientes) + 1, nome=nome_cliente,
                                        cpf=valor_cpf, email=email_cliente, idade=idade_cliente, telefone=numero_cliente)
                hotel.adicionarCliente(novo_cliente)
                txt_resultado.value = f"Cliente {nome_cliente} adicionado com sucesso!"           
        
                page.update()
        
        #AJEITAR AQUI
        def botao_voltar(e):
            page.clean()
            page.add()

        titulo_nome = ft.Text("Nome:", size=12, weight="bold")
        titulo_cpf = ft.Text("CPF:", size=12, weight="bold")
        titulo_idade = ft.Text("Idade:", size=12, weight="bold")
        titulo_email = ft.Text("Email:", size=12, weight="bold")
        titulo_numero = ft.Text("Número:", size=12, weight="bold")
        txt_nome_cliente = ft.TextField(label="Digite o nome do cliente")
        txt_cpf_cliente = ft.TextField(label="Digite o CPF do cliente")
        txt_idade = ft.TextField(label="Digite a idade do cliente")
        txt_email = ft.TextField(label="Digite o email do cliente")
        txt_numero = ft.TextField(label="Digite o numero do cliente")

        txt_resultado = ft.Text(value="")
        btn_enviar = ft.ElevatedButton(
            text="Salvar",color="BLUE", on_click=adicionar_clientes)
        
        btn_voltar = ft.ElevatedButton(text="Voltar", color="RED",on_click=botao_voltar)
        page.update()
        page.clean()
        page.add(txt_titulo_clientes,
                titulo_nome,
                txt_nome_cliente,
                titulo_cpf,
                txt_cpf_cliente,
                titulo_idade,
                txt_idade,
                titulo_email,
                txt_email,
                titulo_numero,
                txt_numero,
                txt_resultado,
                btn_enviar, btn_voltar)
    
    def btns(e):
        def ver_clientes(e):
            clientela = "\n".join([f"ID: {clientes.id}\nNome: {clientes.nome}\nCPF:{clientes.cpf}" for clientes in hotel.verClientes()])
            page.clean()
            page.add(ft.Text(clientela))
            page.update()
        
            def botao_voltar_ver_clientes(e):
                page.clean()
                page.add(btn_cadastrar_cliente, btn_verclientes, btn_voltar_clientes)

            btn_voltar_ver_clientes = ft.ElevatedButton("Voltar", icon=ft.icons.ARROW_BACK, on_click=botao_voltar_ver_clientes)
            page.add(btn_voltar_ver_clientes)
        
        def btn_voltar(e):
            page.clean()
            menu()
        
        btn_cadastrar_cliente = ft.ElevatedButton("Cadastrar", icon=ft.icons.ADD, on_click=gerenciar_clientes)
        btn_verclientes = ft.ElevatedButton("Ver Clientes Cadastrados", icon=ft.icons.SEARCH, on_click=ver_clientes)
        btn_voltar_clientes = ft.ElevatedButton("Voltar", icon=ft.icons.ARROW_BACK, on_click=btn_voltar)
        
        page.update()
        page.clean()
        page.add(btn_cadastrar_cliente, btn_verclientes, btn_voltar_clientes)
#------------------------------------------------------------------------------------------------------------------------    
    #QUARTOS
    # 100% feito
    def gerenciar_quartos(e):
        titulo_quartos = ft.Text("Adicionar Quarto:", size=15, color="BLACK", weight=ft.FontWeight.BOLD)
        page.update()
        page.add(titulo_quartos)

        def adicionar_quarto(e):
            if not txt_nome_quarto.value:
                txt_nome_quarto.error_text = "Por favor digite o nome do quarto"
            if not txt_valor_quarto.value:
                txt_valor_quarto.error_text = "Por favor insira o valor do quarto"
            else:
                nome_quarto = txt_nome_quarto.value
                valor_quarto = txt_valor_quarto.value
                novo_quarto = Quarto(id=len(hotel.lista_de_quartos) + 1, nome=nome_quarto, valor=valor_quarto, disponibilidade=True)
                hotel.adicionarQuarto(novo_quarto)
                txt_resultado.value = f"Quarto {nome_quarto} adicionado com sucesso!"           
        
            page.update()

        def botao_voltar(e):
            page.clean()
            menu()
        
        txt_nome_quarto = ft.TextField(label="Digite o nome do quarto")
        txt_valor_quarto = ft.TextField(label="Digite o valor do quarto")
        txt_resultado = ft.Text(value="")
        btn_enviar = ft.ElevatedButton(
            text="Salvar",color="BLUE", on_click=adicionar_quarto
        )
        btn_voltar = ft.ElevatedButton(text="Voltar", color="RED",on_click=botao_voltar)
        page.update()
        page.clean()
        page.add(titulo_quartos,
                 txt_nome_quarto,
                 txt_valor_quarto,
                 txt_resultado,
                 btn_enviar, btn_voltar)
        
    def menu():
        page.add(
            ft.Column([
                ft.Text("MENU DO HOTEL",size=20, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Ver Quartos disponíveis", on_click=ver_quartos_disponiveis, color="BLACK"),
                ft.ElevatedButton("Ver Quartos reservados", on_click=ver_quartos_reservados, color="BLACK"),
                ft.ElevatedButton("Fazer uma Reserva", on_click=fazer_reserva, color="BLACK"),
                ft.ElevatedButton("Encerrar uma Reserva", on_click=encerrar_reserva, color="BLACK"),
                ft.ElevatedButton("Gerenciar Clientes", on_click=btns, color="BLACK"),
                ft.ElevatedButton("Gerenciar Quartos", on_click=gerenciar_quartos, color="BLACK"),
                ft.ElevatedButton("Sair", on_click=gerenciar_quartos, color="RED"),
                output,
            ])
        )
        page.update()
    
    menu()

ft.app(target=main)