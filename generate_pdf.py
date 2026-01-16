import os
import asyncio
from playwright.async_api import async_playwright

async def run():
    # Caminho absoluto para o arquivo HTML
    html_file_path = os.path.abspath("pdf_version.html")
    file_url = f"file:///{html_file_path.replace(os.path.sep, '/')}"
    
    output_pdf = "manual_do_aluno.pdf"

    print(f"Iniciando conversão de: {file_url}")

    async with async_playwright() as p:
        # Lança o navegador (Chromium)
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Carrega o HTML
        print("Carregando página...")
        await page.goto(file_url, wait_until="networkidle")

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
