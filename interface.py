import tkinter as tk
import main as main

# Exec Calcs
def calcular():
    func = "".join([input1.get(), '=', input2.get()])

    T = main.Transform(func)
    results = T.getData()
    printResults(results)

    windowMain.geometry("520x480")

# Show Results
def printResults(results):
    if(results == None):
        labelMatrix.config(text=f"Matriz Inválida",bg=bgDefault)

    else:
        labelMatrix.config(
            text=f"Matriz:\n {results[0]}", bg=bgDefault)
        labelImgDim.config(
            text=f"Dimensão da Imagem: {results[1]}", bg=bgDefault)
        labelKernelDim.config(
            text=f"Dimensão do Kernel: {results[2]}", bg=bgDefault)
        
        if(results[3]):
            labelBijector.config(
                text=f"Bijetora: Sim", bg=bgDefault)
        else:
            labelBijector.config(
                text=f"Bijetora: Não", bg=bgDefault)
            
        if(results[4]):
            labelOperator.config(text=f"Operadora: Sim", bg=bgDefault)
            labelEigenvalue.config(text=f"Autovalores:\n {results[5]}",bg=bgDefault)
        else:
            labelOperator.config(text=f"Operadora: Não", bg=bgDefault)
            labelEigenvalue.config(text=f"")

# End
def encerrar():
    windowMain.destroy()

# Colors
bgMarked = "#F0F0F0"
bgDefault = "#E5F7FF"

# Window
windowMain = tk.Tk()
windowMain.title("Calculadora de Matriz")
windowMain.geometry("520x230")
windowMain.configure(bg=bgMarked)
windowMain.option_add("*Font", "Arial 12")

# Labels
label1 = tk.Label(windowMain, text="Domínio:")
label1.grid(row=0, column=0, pady=10)
label2 = tk.Label(windowMain, text="ContraDomínio:")
label2.grid(row=1, column=0)

# Inputs
input1 = tk.Entry(windowMain)
input1.grid(row=0, column=1, padx=20, sticky=tk.E+tk.W)

input2 = tk.Entry(windowMain)
input2.grid(row=1, column=1, padx=20, sticky=tk.E+tk.W)

# Buttons
buttonEnd = tk.Button(
    windowMain, text="Encerrar", command=encerrar, width=10)
buttonEnd.grid(row=2, column=0, padx=40, pady=100)

buttonCalc = tk.Button(
    windowMain, text="Calcular", command=calcular, width=10)
buttonCalc.grid(row=2, column=1, padx=40, sticky=tk.E)

# Results
labelOperator = tk.Label(windowMain, text='', bg="#F0F0F0")
labelOperator.grid(row=3, column=0)

labelImgDim = tk.Label(windowMain, bg=bgMarked)
labelImgDim.grid(row=3, column=1)

labelKernelDim = tk.Label(windowMain, bg=bgMarked)
labelKernelDim.grid(row=4, column=1, pady=15)

labelBijector = tk.Label(windowMain, bg=bgMarked)
labelBijector.grid(row=4, column=0, pady=15)

labelMatrix = tk.Label(windowMain, bg=bgMarked)
labelMatrix.grid(row=5, column=0)

labelEigenvalue = tk.Label(windowMain, bg=bgMarked)
labelEigenvalue.grid(row=5, column=1)

# Grid Config
windowMain.grid_columnconfigure(0, weight=1)
windowMain.grid_columnconfigure(1, weight=1)

# While True
windowMain.mainloop()