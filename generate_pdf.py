import os
import asyncio
from datetime import datetime
from playwright.async_api import async_playwright

async def run():
    # Caminho absoluto para o arquivo HTML
    html_file_path = os.path.abspath("pdf_version.html")
    file_url = f"file:///{html_file_path.replace(os.path.sep, '/')}"
    
    # Criar pasta pdf/ se não existir
    pdf_dir = os.path.abspath("pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Gerar nome do arquivo com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"manual_do_aluno_{timestamp}.pdf"
    output_pdf = os.path.join(pdf_dir, output_filename)
    
    print(f"Iniciando conversão de: {file_url}")
    print(f"PDF será salvo em: {output_pdf}")

    async with async_playwright() as p:
        # Lança o navegador (Chromium)
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Carrega o HTML
        print("Carregando página...")
        await page.goto(file_url, wait_until="networkidle")

        # IMPORTANTE: Remover todas as classes "hidden" para garantir que os links internos funcionem
        # O Playwright precisa que os elementos de destino estejam "visíveis" no DOM
        print("Removendo classes 'hidden' para ativar links...")
        await page.evaluate("""
            () => {
                // Remove a classe 'hidden' de TODOS os elementos
                document.querySelectorAll('.hidden').forEach(el => {
                    el.classList.remove('hidden');
                });
                
                // Garante que tudo está visível
                document.querySelectorAll('[class*="hidden"]').forEach(el => {
                    el.style.display = 'block';
                    el.style.visibility = 'visible';
                    el.style.opacity = '1';
                });
                
                console.log('✅ Classes hidden removidas com sucesso');
            }
        """)

        # Injeta um CSS extra para garantir que o formato A4 seja respeitado
        # e para ocultar scrollbars que possam aparecer
        await page.add_style_tag(content="""
            @page {
                size: A4;
                margin: 0;
            }
            body {
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
            /* Garantir que backgrounds sejam impressos */
            * {
                box-sizing: border-box;
            }
        """)

        # Configurações de impressão
        print(f"Gerando PDF: {output_pdf}...")
        await page.pdf(
            path=output_pdf,
            format="A4",
            print_background=True, # Importante para ver cores e imagens de fundo
            margin={
                "top": "0px",
                "right": "0px",
                "bottom": "0px",
                "left": "0px"
            },
            # Escala pode ser ajustada se o conteúdo estiver muito grande/pequeno
            scale=1.0 
        )

        await browser.close()
        print("PDF gerado com sucesso!")

if __name__ == "__main__":
    asyncio.run(run())
