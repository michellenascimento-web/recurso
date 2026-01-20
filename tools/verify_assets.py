"""
Script: Verificação de Assets (Coverage de Integridade)
Verifica se TODOS os recursos referenciados (CSS, JS, Imagens, Icons) existem fisicamente.
"""

import os
import re
from pathlib import Path

BASE_PATH = Path(r"c:\Users\gerson_6061\Desktop\Michelle\recurso")

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def verify_assets():
    print("=" * 70)
    print("🕵️‍♂️  VERIFICAÇÃO DE INTEGRIDADE DE ASSETS")
    print("=" * 70)

    # Encontrar todos os arquivos HTML
    html_files = list(BASE_PATH.glob("**/*.html"))
    
    total_refs = 0
    broken_refs = 0
    
    # Padrões para buscar referências
    patterns = [
        (r'<link[^>]+href="([^"]+)"', "CSS/Icon"),
        (r'<script[^>]+src="([^"]+)"', "Script"),
        (r'<img[^>]+src="([^"]+)"', "Imagem"),
        (r'<source[^>]+src="([^"]+)"', "Media"),
    ]

    for html_file in html_files:
        rel_path = html_file.relative_to(BASE_PATH)
        # print(f"\nVerificando: {rel_path}")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        file_has_error = False
        
        for pattern, type_name in patterns:
            refs = re.finditer(pattern, content)
            
            for match in refs:
                ref_path = match.group(1)
                
                # Ignorar links externos (http/https)
                if ref_path.startswith(('http://', 'https://', '//')):
                    continue
                
                # Ignorar links de âncora (#)
                if ref_path.startswith('#'):
                    continue
                    
                total_refs += 1
                
                # Resolver caminho absoluto
                # Se começar com /, é relativo à raiz (mas cuidado com file system)
                # Se não, é relativo ao arquivo HTML
                
                if ref_path.startswith('/'):
                    # Assumindo raiz do projeto
                    target_path = BASE_PATH / ref_path.lstrip('/')
                else:
                    target_path = (html_file.parent / ref_path).resolve()
                
                # Verificar existência
                if not target_path.exists():
                    broken_refs += 1
                    file_has_error = True
                    print(f"  {Colors.RED}❌ {type_name} quebrado em {rel_path}:{Colors.RESET}")
                    print(f"     Ref: {ref_path}")
                    # print(f"     Alvo: {target_path}")
    
    print("\n" + "=" * 70)
    print("📊 RELATÓRIO DE COBERTURA")
    print("=" * 70)
    
    print(f"Arquivos analisados: {len(html_files)}")
    print(f"Total de referências internas: {total_refs}")
    
    if broken_refs == 0:
        print(f"\n{Colors.GREEN}✨ 100% DAS REFERÊNCIAS VÁLIDAS! (0 erros){Colors.RESET}")
        return 0
    else:
        print(f"\n{Colors.RED}❌ {broken_refs} REFERÊNCIAS QUEBRADAS ENCONTRADAS{Colors.RESET}")
        return 1

if __name__ == "__main__":
    exit(verify_assets())
