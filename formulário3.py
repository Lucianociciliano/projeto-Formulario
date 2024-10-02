import tkinter as tk
from tkinter import messagebox

class Aplicação(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
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

        self.botao_enviar = tk.Button(self)
        self.botao_enviar["text"] = "Enviar"
        self.botao_enviar["command"] = self.enviar_formulario
        self.botao_enviar.pack(side="top")

        self.sair = tk.Button(self, text="SAIR", fg="red",
                              command=self.master.destroy)
        self.sair.pack(side="bottom")

    def enviar_formulario(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()

        if nome and email and telefone:
            messagebox.showinfo("Formulário Enviado", "Obrigado por enviar o formulário!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

root = tk.Tk()
app = Aplicação(master=root)
app.mainloop()
