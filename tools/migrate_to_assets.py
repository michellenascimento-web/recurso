"""
Script: Migração de public/ para assets/
Renomeia a pasta e atualiza todas as referências nos arquivos HTML
"""

import os
import shutil
from pathlib import Path

BASE_PATH = Path(r"c:\Users\gerson_6061\Desktop\Michelle\recurso")
PUBLIC_DIR = BASE_PATH / "public"
ASSETS_DIR = BASE_PATH / "assets"

print("=" * 70)
print("📦 MIGRAÇÃO: public/ → assets/")
print("=" * 70)

# 1. Renomear pasta
print("\n1. Renomeando pasta...")
if PUBLIC_DIR.exists():
    shutil.move(str(PUBLIC_DIR), str(ASSETS_DIR))
    print(f"   ✅ {PUBLIC_DIR} → {ASSETS_DIR}")
else:
    print(f"   ⚠️  Pasta {PUBLIC_DIR} não encontrada")

# 2. Atualizar referências em todos os arquivos HTML
print("\n2. Atualizando referências nos arquivos HTML...")

html_files = []

# Index.html
html_files.append(BASE_PATH / "index.html")

# Todas as páginas
pages_dir = BASE_PATH / "pages"
html_files.extend(pages_dir.glob("*.html"))

# Todas as aulas
aulas_dir = BASE_PATH / "aulas"
for aula_folder in aulas_dir.glob("aula*"):
    aula_index = aula_folder / "index.html"
    if aula_index.exists():
        html_files.append(aula_index)

count = 0
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituir todas as referências
    original_content = content
    
    # Padrões a substituir
    content = content.replace('href="public/', 'href="assets/')
    content = content.replace('href="../public/', 'href="../assets/')
    content = content.replace('href="../../public/', 'href="../../assets/')
    content = content.replace('src="public/', 'src="assets/')
    content = content.replace('src="../public/', 'src="../assets/')
    content = content.replace('src="../../public/', 'src="../../assets/')
    
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"   ✅ {html_file.relative_to(BASE_PATH)}")

print(f"\n   Total de arquivos atualizados: {count}")

# 3. Verificar se os arquivos existem na nova pasta
print("\n3. Verificando arquivos em assets/...")
expected_files = ["favicon.svg", "muzambinho-hor.png"]

for file in expected_files:
    file_path = ASSETS_DIR / file
    if file_path.exists():
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file} não encontrado")

print("\n" + "=" * 70)
print("✨ MIGRAÇÃO CONCLUÍDA!")
print("=" * 70)
print(f"\nPasta renomeada: public/ → assets/")
print(f"Arquivos HTML atualizados: {count}")
