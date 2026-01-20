"""
Teste: Botões de Navegação "Anterior"
Valida se todos os botões "Anterior" apontam para a página correta
"""

import os
import re
from pathlib import Path

BASE_PATH = Path(r"c:\Users\gerson_6061\Desktop\Michelle\recurso")
PAGES_PATH = BASE_PATH / "pages"

# Cores para output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def test_back_buttons():
    """Testa todos os botões 'Anterior'"""
    
    print("=" * 70)
    print("🔙 TESTE: Botões de Navegação 'Anterior'")
    print("=" * 70)
    
    # Mapa: arquivo -> link esperado do botão "Anterior"
    expected_back_links = {
        "02_folha_rosto.html": "../index.html",
        "03_ficha.html": "02_folha_rosto.html",
        "04_sumario.html": "03_ficha.html",
        "05_introducao.html": "04_sumario.html",
        "06_menu_aulas.html": "05_introducao.html",
        "07_final.html": "06_menu_aulas.html",
        "08_referencias.html": "07_final.html",
        "09_vazio.html": "08_referencias.html",
        "10_contracapa.html": "09_vazio.html",
    }
    
    errors = []
    passed = 0
    
    for filename, expected_link in expected_back_links.items():
        file_path = PAGES_PATH / filename
        
        if not file_path.exists():
            errors.append(f"❌ {filename}: Arquivo não encontrado")
            continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Procurar pelo link "Anterior"
        # Padrão: <a href="XXX" ... >Anterior ou ← Anterior
        pattern_anterior = re.search(
            r'<a\s+href="([^"]+)"[^>]*>\s*(?:←\s*)?Anterior',
            content,
            re.IGNORECASE
        )
        
        if not pattern_anterior:
            errors.append(f"❌ {filename}: Botão 'Anterior' não encontrado")
            continue
        
        actual_link = pattern_anterior.group(1)
        
        if actual_link == expected_link:
            print(f"  {Colors.GREEN}✓{Colors.RESET} {filename:25s} → {expected_link}")
            passed += 1
        else:
            errors.append(
                f"❌ {filename}: Link incorreto\n"
                f"     Esperado: {expected_link}\n"
                f"     Atual:    {actual_link}"
            )
            print(f"  {Colors.RED}✗{Colors.RESET} {filename:25s} → {actual_link} (esperado: {expected_link})")
    
    # Resumo
    print("\n" + "=" * 70)
    print("📊 RESUMO")
    print("=" * 70)
    
    total = len(expected_back_links)
    print(f"\nTotal de páginas testadas: {total}")
    print(f"Testes passados: {Colors.GREEN}{passed}{Colors.RESET}")
    print(f"Testes falhados: {Colors.RED}{len(errors)}{Colors.RESET}")
    
    if errors:
        print(f"\n{Colors.RED}ERROS ENCONTRADOS:{Colors.RESET}\n")
        for error in errors:
            print(f"  {error}")
        print()
        return 1
    else:
        print(f"\n{Colors.GREEN}✨ TODOS OS BOTÕES 'ANTERIOR' ESTÃO CORRETOS!{Colors.RESET}\n")
        return 0

if __name__ == "__main__":
    exit_code = test_back_buttons()
    exit(exit_code)
