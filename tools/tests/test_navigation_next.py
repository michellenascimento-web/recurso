"""
Teste: Botões de Navegação "Próxima"
Valida se todos os botões "Próxima" apontam para a página correta
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
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def test_next_buttons():
    """Testa todos os botões 'Próxima'"""
    
    print("=" * 70)
    print("➡️  TESTE: Botões de Navegação 'Próxima'")
    print("=" * 70)
    
    # Mapa: arquivo -> link esperado do botão "Próxima"
    expected_next_links = {
        "02_folha_rosto.html": "03_ficha.html",
        "03_ficha.html": "04_sumario.html",
        "04_sumario.html": "05_introducao.html",
        "05_introducao.html": "06_menu_aulas.html",
        "06_menu_aulas.html": "../aulas/aula01/index.html",  # Botão especial "Iniciar Aulas"
        "07_final.html": "08_referencias.html",
        "08_referencias.html": "09_vazio.html",
        "09_vazio.html": "10_contracapa.html",
        "10_contracapa.html": "../index.html",
    }
    
    errors = []
    passed = 0
    
    for filename, expected_link in expected_next_links.items():
        file_path = PAGES_PATH / filename
        
        if not file_path.exists():
            errors.append(f"❌ {filename}: Arquivo não encontrado")
            continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Procurar pelo link "Próxima" (ou variantes)
        # Padrão: href="XXX" seguido de texto contendo "Próxima" ou variantes
        # Busca mais flexível para capturar diferentes formatos
        
        # Primeiro, encontrar todos os links <a href="...">
        links = re.findall(r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>', content, re.DOTALL)
        
        actual_link = None
        for link_href, link_text in links:
            # Verificar se o texto contém "Próxima", "Próximo", "Iniciar", ou símbolos de navegação
            if any(keyword in link_text for keyword in ["Próxima", "Próximo", "→", "Iniciar Aulas", "Voltar ao Início"]):
                # Ignorar o botão "Anterior" ← 
                if "Anterior" not in link_text and "←" not in link_text:
                    actual_link = link_href
                    break
        
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
    
    total = len(expected_next_links)
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
        print(f"\n{Colors.GREEN}✨ TODOS OS BOTÕES 'PRÓXIMA' ESTÃO CORRETOS!{Colors.RESET}\n")
        return 0

if __name__ == "__main__":
    exit_code = test_next_buttons()
    exit(exit_code)
