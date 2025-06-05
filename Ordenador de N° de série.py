import tkinter as tk
from tkinter import messagebox

def ordenar_numeros():
    prefixo = entry_prefixo.get()
    numeros = text_numeros.get("1.0", tk.END).strip().split("\n")

    
    if len(prefixo) != 9 or not prefixo.isdigit():
        messagebox.showerror("Erro", "Prefixo deve ter exatamente 9 dígitos numéricos.")
        return

    
    numeros = [n.strip() for n in numeros if n.strip() != ""]

    
    numeros.sort()

    
    resultado = "\n".join(prefixo + n for n in numeros)
    text_resultado.delete("1.0", tk.END)
    text_resultado.insert(tk.END, resultado)


janela = tk.Tk()
janela.title("Ordenar Números com Prefixo")


tk.Label(janela, text="Digite o prefixo (9 dígitos):").pack()
entry_prefixo = tk.Entry(janela)
entry_prefixo.pack()


tk.Label(janela, text="Digite números de 4 dígitos (um por linha):").pack()
text_numeros = tk.Text(janela, height=10, width=30)
text_numeros.pack()


btn_ordenar = tk.Button(janela, text="Ordenar e Mostrar", command=ordenar_numeros)
btn_ordenar.pack(pady=10)


tk.Label(janela, text="Resultado:").pack()
text_resultado = tk.Text(janela, height=10, width=30)
text_resultado.pack()


janela.mainloop()
