import tkinter as tk
import main as main

def calcular():
    dominio = caixa_valor1.get()
    dominio += '='
    contraDominio = caixa_valor2.get()
    resultado = dominio + contraDominio

    T = main.Transformacao(resultado)

    lista_resultado = T.get_dados()

    print_resultado(lista_resultado)

def print_resultado(lista_resultado):
    if(lista_resultado == None):
        rotulo_matriz.config(text=f"Matriz Inválida",bg="#E5F7FF")
    else:
        rotulo_matriz.config(
            text=f"Matriz:\n {lista_resultado[0]}", bg="#E5F7FF")
        rotulo_dimImg.config(
            text=f"Dimensão da Imagem: {lista_resultado[1]}", bg="#E5F7FF")
        rotulo_dimKernel.config(
            text=f"Dimensão do Kernel: {lista_resultado[2]}", bg="#E5F7FF")
        if(lista_resultado[3]):
            rotulo_bijetora.config(
                text=f"É bijetora", bg="#E5F7FF")
        else:
            rotulo_bijetora.config(
                text=f"Não é bijetora", bg="#E5F7FF")
        if(lista_resultado[4]):
            rotulo_operador.config(text=f"É Operadora",bg="#E5F7FF")
            rotulo_autovalores.config(text=f"Autovalores: {lista_resultado[5]}",bg="#E5F7FF")
        else:
            rotulo_operador.config(text=f"Não é Operadora",bg="#E5F7FF")
            rotulo_autovalores.config(text=f"")


def encerrar():
    janela_principal.destroy()

janela_principal = tk.Tk()
janela_principal.title("Formulário de Cálculo")
janela_principal.geometry("500x500")
janela_principal.configure(bg="#F0F0F0")
janela_principal.option_add("*Font", "Arial 12")

rotulo_valor1 = tk.Label(janela_principal, text="Domínio:")
rotulo_valor1.grid(row=0, column=0, padx=10, pady=20)
caixa_valor1 = tk.Entry(janela_principal)
caixa_valor1.grid(row=1, column=0, padx=10, pady=0)

rotulo_valor2 = tk.Label(janela_principal, text="ContraDomínio:")
rotulo_valor2.grid(row=2, column=0, padx=10, pady=0)
caixa_valor2 = tk.Entry(janela_principal)
caixa_valor2.grid(row=3, column=0, padx=10, pady=0)

botao_calcular = tk.Button(
    janela_principal, text="Calcular", command=calcular, width=10)
botao_calcular.grid(row=2, column=1, padx=10, pady=15)

botao_encerrar = tk.Button(
    janela_principal, text="Encerrar", command=encerrar, width=10)
botao_encerrar.grid(row=3, column=1, padx=10, pady=15)

rotulo_matriz = tk.Label(janela_principal, text="", bg="#F0F0F0")
rotulo_matriz.grid(row=4, column=0, padx=0, pady=15)

rotulo_dimImg = tk.Label(janela_principal, text="", bg="#F0F0F0")
rotulo_dimImg.grid(row=4, column=1, padx=0, pady=15)

rotulo_dimKernel = tk.Label(janela_principal, text="", bg="#F0F0F0")
rotulo_dimKernel.grid(row=5, column=1, padx=0, pady=15)

rotulo_bijetora = tk.Label(janela_principal, text="", bg="#F0F0F0")
rotulo_bijetora.grid(row=5, column=0, padx=0, pady=15)

rotulo_operador = tk.Label(janela_principal, text="", bg="#F0F0F0")
rotulo_operador.grid(row=6, column=0, padx=0, pady=15)

rotulo_autovalores = tk.Label(janela_principal, text="", bg="#F0F0F0")
rotulo_autovalores.grid(row=6, column=1, padx=0, pady=15)

janela_principal.grid_columnconfigure(0, weight=1)
janela_principal.grid_columnconfigure(1, weight=1)

janela_principal.mainloop()