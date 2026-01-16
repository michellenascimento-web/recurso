# Documento de Estratégia: Geração Automatizada de PDF Interativo

## 1. Objetivo do Projeto
Automatizar a conversão do conteúdo web (curso HTML Interativo) para um arquivo **PDF Único**, garantindo:
- **Alta Fidelidade Visual**: O PDF deve ser idêntico à versão web (cores, fontes, layout).
- **Interatividade**: Links internos (navegação entre menus e aulas) devem funcionar perfeitamente.
- **Automação**: Processo executável via script Python, sem necessidade de "imprimir" manualmente pelo navegador.

## 2. Análise de Ferramentas (Bibliotecas Python)

Para converter HTML moderno (com Tailwind/CSS Grid/Flexbox) para PDF com qualidade, avaliamos as melhores opções:

### Opção A: Playwright (Recomendada 🏆)
Utiliza um motor de navegador real (Chromium) controlado pelo Python.
- **Prós**:
    - Renderização **perfeita** (exatamente o que se vê no Chrome).
    - Suporte total a CSS moderno (Tailwind, Grid, Flex).
    - Gera links internos funcionais.
    - Permite injetar CSS ou JS antes de imprimir.
- **Contras**:
    - Requer instalação do browser (comando `playwright install`).

### Opção B: WeasyPrint
Biblioteca Python pura focada em renderização de PDF baseada em padrões web.
- **Prós**:
    - Leve, não precisa de browser instalado.
    - Excelente suporte para paginação e padrões específicos de impressão.
- **Contras**:
    - Pode "quebrar" com CSS muito moderno ou hacks de browser (comum em Tailwind se não configurado).
    - Renderização de fontes pode variar do navegador.

### Opção C: pdfkit / wkhtmltopdf
- **Veredito**: **Não recomendado**. Baseado em tecnologia antiga (QtWebkit), falha frequentemente com layouts modernos (Flexbox/Grid).

## 3. Plano de Execução (Roadmap)

### Fase 1: Preparação do Ambiente
- [ ] Escolher a biblioteca (Recomendação: **Playwright** pela fidelidade visual).
- [ ] Instalar dependências.

### Fase 2: Script de Geração (`generate_pdf.py`)
- [ ] Ler o arquivo [pdf_version.html](file:///c:/Users/michelle_4478/Desktop/RECURSO/pdf_version.html) (já tratado na etapa anterior).
- [ ] Configurar layout de página (A4, margens, escala).
- [ ] Executar a conversão.
- [ ] Validar se os links de âncora (`#aula-1`, etc) estão clicáveis no PDF final.

### Fase 3: Refinamento
- [ ] Ajustar quebras de página onde necessário (CSS `break-inside: avoid`).
- [ ] Otimizar tamanho do arquivo final.
- [ ] Adicionar Metadados ao PDF (Título, Autor).

## 4. Próximos Passos Imediatos
1. Instalar Playwright no ambiente Python.
2. Criar script inicial de teste.
