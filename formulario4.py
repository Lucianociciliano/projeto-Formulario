import tkinter as tk
from tkinter import messagebox
import sqlite3

class Aplicação(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Campos do formulário
        self.nome_label = tk.Label(self)
        self.nome_label["text"] = "Nome:"
        self.nome_label.pack(side="top")

        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack(side="top")

        self.email_label = tk.Label(self)
        self.email_label["text"] = "Email:"
        self.email_label.pack(side="top")

        self.email_entry = tk.Entry(self)
        self.email_entry.pack(side="top")

        self.telefone_label = tk.Label(self)
        self.telefone_label["text"] = "Telefone:"
        self.telefone_label.pack(side="top")

        self.telefone_entry = tk.Entry(self)
        self.telefone_entry.pack(side="top")

        self.endereco_label = tk.Label(self)
        self.endereco_label["text"] = "Endereço:"
        self.endereco_label.pack(side="top")

        self.endereco_entry = tk.Entry(self)
        self.endereco_entry.pack(side="top")

        self.cidade_label = tk.Label(self)
        self.cidade_label["text"] = "Cidade:"
        self.cidade_label.pack(side="top")

        self.cidade_entry = tk.Entry(self)
        self.cidade_entry.pack(side="top")

        self.estado_label = tk.Label(self)
        self.estado_label["text"] = "Estado:"
        self.estado_label.pack(side="top")

        self.estado_entry = tk.Entry(self)
        self.estado_entry.pack(side="top")

        self.cep_label = tk.Label(self)
        self.cep_label["text"] = "CEP:"
        self.cep_label.pack(side="top")

        self.cep_entry = tk.Entry(self)
        self.cep_entry.pack(side="top")

        # Botão de envio
        self.botao_enviar = tk.Button(self)
        self.botao_enviar["text"] = "Enviar"
        self.botao_enviar["command"] = self.enviar_formulario
        self.botao_enviar.pack(side="top")

        # Botão de sair
        self.sair = tk.Button(self, text="SAIR", fg="red",
                              command=self.master.destroy)
        self.sair.pack(side="bottom")

    def enviar_formulario(self):
        # Obter os dados do formulário
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        endereco = self.endereco_entry.get()
        cidade = self.cidade_entry.get()
        estado = self.estado_entry.get()
        cep = self.cep_entry.get()

        # Validar os dados
        if nome and email and telefone and endereco and cidade and estado and cep:
            # Conectar ao banco de dados
            conn = sqlite3.connect("formulario.db")
            cursor = conn.cursor()

            # Inserir os dados no banco de dados
            cursor.execute("INSERT INTO formulario (nome, email, telefone, endereco, cidade, estado, cep) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (nome, email, telefone, endereco, cidade, estado, cep))

            # Fechar a conexão com o banco de dados
            conn.commit()
            conn.close()

            # Exibir uma mensagem de sucesso
            messagebox.showinfo("Formulário Enviado", "Obrigado por enviar o formulário!")
        else:
            # Exibir uma mensagem de erro
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

root = tk.Tk()
app = Aplicação(master=root)
app.mainloop()
