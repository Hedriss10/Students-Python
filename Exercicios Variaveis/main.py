

import os
import shutil

caminho_original = "C:\Users\Henrique"
caminho_novo = "C:\Users\Henrique\videos"

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'pasta{caminho_novo} já existe.')

for root, dirs, file in os.walk(caminho_original):
    for file in file:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        shutil.move(old_file_path, new_file_path)
        print(f'Arquivo {file} movido com sucesso!')

