import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Obter o diretório do script atual
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

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

# Definir os nomes das colunas corretamente
COLUMNS_DESIRED = ["time", "channel1", "channel2", "channel3", "channel4"]

for arquivo in arquivos:
    # Ler o arquivo sem cabeçalhos
    df = pd.read_csv(arquivo, sep="\t", header=None)

    # Definir os nomes das colunas (excluindo a coluna time que será adicionada depois)
    df.columns = ["channel1", "channel2", "channel3", "channel4"]

    # Criar a coluna de tempo começando em 0.000
    df.insert(0, "time", np.arange(0, len(df) * 0.001, 0.001))

    # Adicionar a coluna 'position' com o nome do arquivo sem '.txt'
    nome_arquivo = arquivo.split("/")[-1].replace(".txt", "")
    df["position"] = nome_arquivo

    # Adicionar ao conjunto de DataFrames
    dfs.append(df)

# Empilhar todos os arquivos
df_final = pd.concat(dfs, ignore_index=True)

# Criar o caminho relativo para salvar o arquivo
output_path = os.path.join(SCRIPT_DIR, "arquivo_empilhado.csv")

# Salvar o novo arquivo combinado
df_final.to_csv(output_path, index=False)

print(f"Todos os arquivos foram empilhados e salvos como '{output_path}'!")
