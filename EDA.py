# =============================================
# BAIXAR DADOS
# =============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import kagglehub

# Configurações visuais
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")

# Criar pastas
Path("images").mkdir(exist_ok=True)
Path("data").mkdir(exist_ok=True)

# Download dataset
print("Baixando dataset...")
path = kagglehub.dataset_download("bishals098/nasa-turbofan-engine-degradation-simulation")
DATA_DIR = Path(path)

# Encontrar arquivos
train_path = next(DATA_DIR.rglob("train_FD001.txt"))
test_path = next(DATA_DIR.rglob("test_FD001.txt"))
rul_path = next(DATA_DIR.rglob("RUL_FD001.txt"))

print("Caminho dataset:", DATA_DIR)
print("Train encontrado:", train_path.exists())
print("Test encontrado:", test_path.exists())
print("RUL encontrado:", rul_path.exists())