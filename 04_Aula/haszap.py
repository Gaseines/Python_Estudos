#ft.FilePicker envia arquivos

#importar o flet
import flet as ft

#Criar uma função para rodar o seu sistema
def main(pagina):
    # TITULO
    titulo = ft.Text("Chat do Gab")

    def enviar_mensagem_tunel(mensagem):

        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_menssagem(e):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_menssagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_menssagem)

    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(e):
        popup.open = False

        pagina.remove(titulo)
        pagina.remove(botao)


        pagina.add(linha_enviar)
        pagina.add(chat)

        
        
        
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        
        pagina.update()
    
    ##Criar Popup
    titulo_popup = ft.Text("Bem vindo ao chat do Gab")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat" , on_click=entrar_chat)
    

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])
    
    # Botão inicial
    def abrir_popup(e):
        print("Clicou no botão")
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    pagina.add(titulo)
    pagina.add(botao)

#Executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)
