// Dados da ficha catalográfica oficial
// Fonte: Sistema de Geração de Ficha Catalográfica - IFSULDEMINAS
// Elaborada por: Clarissa Benassi - CRB 2423/6

const dadosFicha = {
    cabecalho: "Sistema de Geração de Ficha Catalográfica do Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas Gerais",
    subCabecalho: "Dados Internacionais de Catalogação na Publicação (CIP)",
    codigo: "N196t",
    autor: "Nascimento, Michelle Santos do",
    textoPrincipal: "Trilha formativa em tecnologias educacionais : curso para educadores : uso pedagógico da tecnologia na educação / Nascimento, Michelle Santos do, 2026.",
    descricaoFisica: "27 f.",
    orientador: "Orientador(a): Dr.(a) Evandro Antonio Corrêa",
    dissertacaoInfo: "Dissertação (Mestrado Profissional em Educação Física - PROEF) - Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas Gerais - Campus Muzambinho, 2026.",
    descritores: "1. Educação Física 2. Professores - Formação 3. Tecnologia Educacional I. Título.",
    cdd: "CDD: 372.86",
    elaboradaPor: "Elaborada por: Clarissa Benassi - CRB 2423/6",
    bibliotecario: "Bibliotecário(a) IFSULDEMINAS - Campus Muzambinho"
};

function preencherFicha() {
    const elementos = {
        'ficha-cabecalho':    dadosFicha.cabecalho,
        'ficha-subcabecalho': dadosFicha.subCabecalho,
        'ficha-codigo':       dadosFicha.codigo,
        'ficha-autor':        dadosFicha.autor,
        'ficha-texto':        dadosFicha.textoPrincipal,
        'ficha-descricao':    dadosFicha.descricaoFisica,
        'ficha-orientador':   dadosFicha.orientador,
        'ficha-dissertacao':  dadosFicha.dissertacaoInfo,
        'ficha-descritores':  dadosFicha.descritores,
        'ficha-cdd':          dadosFicha.cdd,
        'ficha-elaborada':    dadosFicha.elaboradaPor,
        'ficha-bibliotecario':dadosFicha.bibliotecario
    };

    for (const [id, texto] of Object.entries(elementos)) {
        const el = document.getElementById(id);
        if (el) {
            el.innerText = texto;
        }
    }
}

document.addEventListener('DOMContentLoaded', preencherFicha);
