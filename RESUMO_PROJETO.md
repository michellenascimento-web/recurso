# Resumo do Projeto: Trilha Formativa em Tecnologias Educacionais

## 🎯 Objetivo Principal
Recurso Educacional Digital (RED) voltado para educadores, focado no uso pedagógico de tecnologias (Google for Education). O projeto funciona como uma aplicação web estática (SPA simulada) com navegação entre páginas e aulas interativas.

---

## ✅ Estrutura do Projeto (v2.0)

O projeto foi reestruturado para melhor organização e integridade:

### 1. Diretórios Principais
- **`index.html`**: Página de entrada (Capa).
- **`pages/`**: Páginas de conteúdo sequencial (02 a 10).
- **`aulas/`**: 11 Aulas práticas (aula01 a aula11).
- **`assets/`**: Imagens e ícones (migrado de `public/`).
- **`src/`**: Estilos (`styles.css`) e scripts (`script.js`).
- **`tools/`**: Scripts de automação e testes em Python.

### 2. Melhorias Recentes
- **Renumeração de Páginas**: Removida página vazia 02; sequência ajustada de 02 a 10.
- **Correção de Navegação**: Todos os links "Anterior/Próxima" validados.
- **Migração de Assets**: Pasta `public` renomeada para `assets` para compatibilidade com servidores.
- **Limpeza de Código**: Removidas referências a SDKs inexistentes (`_sdk/`) que causavam erros 404.
- **Favicon**: Adicionado favicon personalizado em todas as páginas.

---

## �️ Ferramentas e Scripts

Ferramentas Python criadas para garantir a qualidade do projeto:

### Testes de Regressão (`tools/`)
1. **`test_navigation_back.py`**: Valida todos os botões "Anterior".
2. **`test_navigation_next.py`**: Valida todos os botões "Próxima".
3. **`verify_assets.py`**: Valida a existência de todos os arquivos referenciados (CSS, JS, Imagens).
4. **`run_all_tests.py`**: Executa a suite completa de testes.

### Comandos de Teste
Para verificar a integridade do projeto, execute:
```bash
python tools/run_all_tests.py
```

---

## � Funcionalidades Web
- **Progresso**: Sistema de desbloqueio de aulas via `localStorage` (Vanilla JS).
- **Navegação**: Links relativos para navegação offline/estática.
- **Responsividade**: TailwindCSS para adaptação mobile/desktop.

---

## � Status Atual
- **Versão**: 2.0 (Estável)
- **Cobertura de Testes**: 100% (Integridade estrutural e navegação)
- **Erros de Console**: 0 (Zero 404s)

---

## 📂 Arquivos Importantes
- `task.md`: Lista de tarefas e histórico de alterações.
- `walkthrough.md`: Detalhes técnicos da implementação.
