import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def selecionar_arquivo():
    """Abre uma janela para selecionar um arquivo"""
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    arquivo = filedialog.askopenfilename(title="Selecione um arquivo", filetypes=[("Text Files", "*.txt")])
    return arquivo

# Lista para armazenar os arquivos selecionados
arquivos = []

# Loop para permitir a seleção de múltiplos arquivos
while True:
    arquivo = selecionar_arquivo()
    if not arquivo:
        print("Nenhum arquivo foi selecionado.")
        break
    
    arquivos.append(arquivo)

    # Perguntar ao usuário se deseja adicionar mais arquivos
    continuar = messagebox.askyesno("Adicionar mais arquivos?", "Deseja adicionar outro arquivo?")
    if not continuar:
        break

# Verificar se ao menos um arquivo foi selecionado
if not arquivos:
    print("Nenhum arquivo foi processado.")
    exit()

# Lista para armazenar os DataFrames convertidos
dfs = []

for arquivo in arquivos:
    # Ler o arquivo sem cabeçalhos
    df = pd.read_csv(arquivo, sep="\t", header=None)

    # Definir os nomes das colunas
    colunas_desejadas = ["chanel1", "chanel2", "chanel3", "chanel4"]
    df.columns = colunas_desejadas

    # Criar a coluna de tempo começando em 0.000
    df.insert(0, "time", np.arange(0, len(df) * 0.001, 0.001))

    # Adicionar a coluna 'position' com o nome do arquivo sem '.txt'
    nome_arquivo = arquivo.split("/")[-1].replace(".txt", "")
    df["position"] = nome_arquivo

    # Adicionar ao conjunto de DataFrames
    dfs.append(df)

# Empilhar todos os arquivos
df_final = pd.concat(dfs, ignore_index=True)

# Salvar o novo arquivo combinado
df_final.to_csv("arquivo_empilhado.csv", index=False)

print("Todos os arquivos foram empilhados e salvos como 'arquivo_empilhado.csv'!")
