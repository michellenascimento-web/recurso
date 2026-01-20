"""
Script Unificado: Executa todos os testes de navegação
"""

import subprocess
import sys
from pathlib import Path

def run_test(test_file):
    """Executa um arquivo de teste e retorna o código de saída"""
    print(f"\nExecutando: {test_file.name}")
    print("-" * 70)
    
    result = subprocess.run(
        [sys.executable, str(test_file)],
        capture_output=False,
        text=True
    )
    
    return result.returncode

def main():
    tools_dir = Path(__file__).parent
    
    tests = [
        tools_dir / "test_navigation_back.py",
        tools_dir / "test_navigation_next.py",
        tools_dir / "verify_assets.py",
    ]
    
    print("=" * 70)
    print("🧪 EXECUTANDO TODOS OS TESTES DE NAVEGAÇÃO")
    print("=" * 70)
    
    failed_tests = []
    
    for test_file in tests:
        if not test_file.exists():
            print(f"\n⚠️  AVISO: {test_file.name} não encontrado")
            continue
        
        exit_code = run_test(test_file)
        
        if exit_code != 0:
            failed_tests.append(test_file.name)
    
    # Resumo final
    print("\n" + "=" * 70)
    print("📊 RESUMO GERAL")
    print("=" * 70)
    
    total_tests = len(tests)
    passed_tests = total_tests - len(failed_tests)
    
    print(f"\nTotal de suites de teste: {total_tests}")
    print(f"Suites passadas: {passed_tests}")
    print(f"Suites falhadas: {len(failed_tests)}")
    
    if failed_tests:
        print(f"\n❌ Testes que falharam:")
        for test in failed_tests:
            print(f"  - {test}")
        print()
        return 1
    else:
        print(f"\n✨ TODOS OS TESTES PASSARAM!\n")
        return 0

if __name__ == "__main__":
    exit(main())
