"""Script para verificar se todos os IDs de destino dos links existem no HTML"""
import re

with open('pdf_version.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar todos os links href="#..." 
link_pattern = r'href="#([^"]+)"'
links = set(re.findall(link_pattern, content))

# Encontrar todos os IDs no documento
id_pattern = r'id="([^"]+)"'
ids = set(re.findall(id_pattern, content))

print("=== ANÁLISE DE LINKS DO PDF ===\n")
print(f"Total de links únicos encontrados: {len(links)}")
print(f"Total de IDs únicos no documento: {len(ids)}\n")

# Verificar links quebrados (que apontam para IDs inexistentes)
broken_links = links - ids

if broken_links:
    print(f"⚠️  LINKS QUEBRADOS ({len(broken_links)}):")
    for link in sorted(broken_links):
        print(f"  - #{link}")
    print()
else:
    print("✅ Todos os links apontam para IDs válidos!\n")

# Mostrar alguns exemplos de links funcionais
working_links = links & ids
if working_links:
    print(f"✅ Links Funcionais (primeiros 10):")
    for link in sorted(list(working_links))[:10]:
        print(f"  - #{link}")
