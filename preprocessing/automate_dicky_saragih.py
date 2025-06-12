# automate_dicky_saragih.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# === 1. Atur Path Dataset ===
input_path = "namadataset_raw/WineQT.csv"
output_path = "preprocessing/namadataset_preprocessing/WineQT_processed.csv"

# Validasi apakah file input tersedia
if not os.path.exists(input_path):
    raise FileNotFoundError(f"File input tidak ditemukan: {input_path}")

# === 2. Muat Dataset dan Lakukan Preprocessing ===
df = pd.read_csv(input_path)
print(f"Dataset dimuat: {df.shape[0]} baris, {df.shape[1]} kolom")

# Hapus duplikat dan nilai kosong
df = df.drop_duplicates().dropna()

# Pisahkan fitur dan target
X = df.drop("quality", axis=1)
y = df["quality"]

# Standarisasi fitur numerik
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Gabungkan kembali fitur dan target ke dalam DataFrame
df_processed = pd.DataFrame(X_scaled, columns=X.columns)
df_processed["quality"] = y.values

# === 3. Simpan Dataset Hasil Preprocessing ===
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df_processed.to_csv(output_path, index=False)

print(f"Dataset hasil preprocessing disimpan di: {output_path}")
