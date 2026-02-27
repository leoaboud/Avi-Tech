# 1. IMPORTS
import pandas as pd
from pathlib import Path
import kagglehub

# 2. LOAD DATA
path = kagglehub.dataset_download("bishals098/nasa-turbofan-engine-degradation-simulation")
DATA_DIR = Path(path)

train_path = next(DATA_DIR.rglob("train_FD001.txt"))
test_path = next(DATA_DIR.rglob("test_FD001.txt"))
rul_path = next(DATA_DIR.rglob("RUL_FD001.txt"))

columns = ['unit','cycle'] + [f'sensor{i}' for i in range(1,22)]

df = pd.read_csv(train_path, sep=r'\s+', header=None, names=columns)

max_cycles = df.groupby('unit')['cycle'].max()

df['RUL'] = df.apply(
    lambda row: max_cycles[row['unit']] - row['cycle'],
    axis=1
)

print("Caminho dataset:", DATA_DIR)
print("Dados carregados")
print("Train encontrado:", train_path.exists())
print("Test encontrado:", test_path.exists())
print("RUL encontrado:", rul_path.exists())
print("Shape:", df.shape)
print("Colunas:", df.columns.tolist())
print(df.head())
print("RUL criado")