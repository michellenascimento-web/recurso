// Dados da ficha
const dadosFicha = {
    autor: "Nascimento, Michelle Santos",
    textoPrincipal: "Educação Física escolar e Tecnologia Educacional: uma reflexão sobre o uso das ferramentas educacionais google no ensino dos jogos e a formação continuada do professor/Michelle Santos do Nascimento. – Muzambinho/MG",
    descricaoFisica: "xxx f : il. ; XX cm + X Tipo (XX p./il./XX cm/son., color.)",
    modoAcesso: "Modo de acesso: http://www....",
    orientador: "Orientador(a): Prof. Dr. Evandro Antonio Corrêa",
    descritores: "1 Descritor. 2. Descritor. 3 . Descritor. I. Autor II. Título."
};

function preencherFicha() {
    const elementos = {
        'ficha-autor': dadosFicha.autor,
        'ficha-texto': dadosFicha.textoPrincipal,
        'ficha-descricao': dadosFicha.descricaoFisica,
        'ficha-acesso': dadosFicha.modoAcesso,
        'ficha-orientador': dadosFicha.orientador,
        'ficha-dissertacao': dadosFicha.dissertacaoInfo,
        'ficha-descritores': dadosFicha.descritores
    };

    for (const [id, texto] of Object.entries(elementos)) {
        const el = document.getElementById(id);
        if (el) {
            el.innerText = texto;
        }
    }
}

document.addEventListener('DOMContentLoaded', preencherFicha);
