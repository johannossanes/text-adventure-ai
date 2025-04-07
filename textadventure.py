import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext

genai.configure(api_key="API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")  

contexto = """
Você é um narrador mestre de uma aventura interativa em texto. 
Crie descrições ricas e imersivas. Adapte a história conforme as ações do jogador.
Sempre descreva o que está acontecendo e o que o jogador vê, ouve e sente. 
Nunca tome decisões pelo jogador. Dê sempre opções abertas para ele explorar o mundo.

Comece a aventura com o jogador acordando em um lugar misterioso.
"""

historia = contexto 

def chatbot(prompt):
    global historia
    historia += f'Jogador: {prompt} \nNarrador: '
    response = model.generate_content(historia)
    historia+= response.text
    return response.text

#INTERFACE GRÁFICA

def enviar_mensagem():
    entrada = campo_entrada.get()
    if entrada.strip().lower() == 'sair':
        janela.destroy()
        return

    campo_texto.insert(tk.END, f'\nVocê: {entrada}','jogador')
    campo_entrada.delete(0, tk.END)

    resposta = chatbot(entrada)
    campo_texto.insert(tk.END, f'\nNarrador: {resposta}', 'narrador')
    campo_texto.see(tk.END)


#JANELA PRINCIPAL 

janela = tk.Tk()
janela.title('Text Adventure com IA')
janela.geometry = ('600x500')
janela.configure(bg="#1e1e1e")

#CAMPO DE TEXTO (NARRATIVA)

campo_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, bg='#121212', fg='#f0f0f0', font=('Consolas', 12))
campo_texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
campo_texto.tag_config('jogador', foreground='#7ec0ee')
campo_texto.tag_config('narrador', foreground='#98fb98')

#CAMPO DE ENTRADA 

campo_entrada = tk.Entry(janela, font=('Consolas', 12))
campo_entrada.pack(padx=10, pady=(0, 10), fill=tk.X)
campo_entrada.bind("<Return>", lambda event: enviar_mensagem())

#BOTAO ENVIAR

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(pady=(0,10))

# MENSAGEM INICIAL
introducao = chatbot("Comece a aventura")
campo_texto.insert(tk.END, f"{introducao}\n", "narrador")

# INICIAR A JANELA
janela.mainloop()


