"""
Script: Remover referências aos SDKs inexistentes
Remove as linhas que carregam _sdk/element_sdk.js e _sdk/data_sdk.js
"""

import os
import re
from pathlib import Path

BASE_PATH = Path(r"c:\Users\gerson_6061\Desktop\Michelle\recurso")

print("=" * 70)
print("🧹 REMOVENDO REFERÊNCIAS AOS SDKs INEXISTENTES")
print("=" * 70)

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
        lines = f.readlines()
    
    original_lines = lines.copy()
    
    # Filtrar linhas que contenham referências aos SDKs
    new_lines = []
    for line in lines:
        # Pular linhas que contenham _sdk
        if '_sdk' not in line:
            new_lines.append(line)
    
    if new_lines != original_lines:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        count += 1
        removed = len(original_lines) - len(new_lines)
        print(f"   ✅ {str(html_file.relative_to(BASE_PATH)):40s} ({removed} linhas removidas)")

print(f"\n" + "=" * 70)
print(f"✨ CONCLUÍDO!")
print(f"=" * 70)
print(f"\nTotal de arquivos atualizados: {count}")
print(f"Referências a _sdk removidas de todos os HTMLs")
