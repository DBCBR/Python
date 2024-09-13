import tkinter as tk
from tkinter import simpledialog, messagebox

class Tabuada:
    def __init__(self, número):
        self.número = número

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        if self.i <= 10:
            resultado = self.número * self.i
            operação = f"{self.i} * {self.número} = {resultado}"
            self.i += 1
            return operação
        else:
            raise StopIteration

def calcular_tabuada():
    número = simpledialog.askinteger("Tabuada", "Digite um número inteiro para saber a Tabuada:")
    if número is not None:
        tabuada = Tabuada(número)
        resultado = "\n".join([item for item in tabuada])
        messagebox.showinfo("Resultado", resultado)

def main():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    while True:
        calcular_tabuada()
        resposta = messagebox.askquestion("Continuar", "Você quer calcular outra tabuada?")
        if resposta != 'yes':
            messagebox.showinfo("Fim", "Programa finalizado.")
            break

if __name__ == "__main__":
    main()
    