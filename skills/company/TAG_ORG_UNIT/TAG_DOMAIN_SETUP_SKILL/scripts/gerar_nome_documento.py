#!/usr/bin/env python3
"""
gerar_nome_documento.py — Calcula o nome de arquivo padronizado [COMPANY_PRODUCT]
seguindo o padrao:

    DATA_SETOR_NOMEDODOCUMENTO_CLIENTE_V{versao}R{revisao}

Esse padrao existe para que qualquer documento gerado pela equipe seja
identificavel, rastreavel e recuperavel sem depender de metadados externos
(alinhado aos principios de identificacao e controle de documentos da
ISO 9001:2015 clausula 7.5 e de gestao de registros da ISO 15489).

Uso via linha de comando:

    python3 gerar_nome_documento.py \
        --setor [ORG_UNIT] \
        --documento "Termo de Homologacao" \
        --cliente "[CLIENT_NAME_1]" \
        --versao 1 \
        --revisao 1

    # data e opcional -- se omitida, usa a data de hoje (formato AAAAMMDD)
    # extensao e opcional -- se informada, e anexada ao final (ex: .docx)

Tambem pode ser importado e usado como funcao:

    from gerar_nome_documento import gerar_nome_documento
    nome = gerar_nome_documento(
        setor="[ORG_UNIT]",
        documento="Termo de Homologacao",
        cliente="[CLIENT_NAME_1]",
        versao=1,
        revisao=1,
        data="[DATE]",
    )
"""

import argparse
import re
import sys
import unicodedata

# Tabela oficial de siglas de setor da [COMPANY_PRODUCT].
# Se o usuario pedir um setor que nao esta aqui, NAO invente uma sigla --
# pergunte a sigla correta e, se for de uso recorrente, sugira adicionar
# aqui.
SETORES = {
    "[ORG_UNIT]": "Projetos",
    "CML": "Comercial",
    "ADM": "Administrativo",
    "TEC": "Tecnologia",
    "GOV": "Governanca",
    "MKT": "Marketing",
}


def _normalizar(texto: str) -> str:
    """
    Deixa o texto seguro para nome de arquivo, seguindo o padrao [COMPANY_PRODUCT]:
    - remove acentos/cedilha (NFKD + remove marcas combinantes)
    - deixa em maiusculas
    - remove tudo que nao for letra ou numero (espacos, hifens, pontuacao)
    """
    sem_acento = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join(c for c in sem_acento if not unicodedata.combining(c))
    maiusculo = sem_acento.upper()
    somente_alfanumerico = re.sub(r"[^A-Z0-9]", "", maiusculo)
    return somente_alfanumerico


def gerar_nome_documento(
    setor: str,
    documento: str,
    cliente: str,
    versao,
    revisao,
    data: str = None,
    extensao: str = None,
) -> str:
    """
    Monta o nome de arquivo padronizado. Levanta ValueError se o setor
    nao estiver na tabela SETORES.
    """
    setor_norm = setor.strip().upper()
    if setor_norm not in SETORES:
        conhecidos = ", ".join(sorted(SETORES))
        raise ValueError(
            f"Setor '{setor}' nao esta na tabela de siglas conhecidas "
            f"({conhecidos}). Confirme a sigla correta com o usuario "
            "antes de gerar o nome -- nao invente uma sigla nova."
        )

    if data is None:
        raise ValueError(
            "Parametro 'data' e obrigatorio nesta funcao (use AAAAMMDD). "
            "Quando chamado via linha de comando, a data de hoje e "
            "preenchida automaticamente se --data for omitido."
        )

    documento_norm = _normalizar(documento)
    cliente_norm = _normalizar(cliente)
    versao_revisao = f"V{int(versao)}R{int(revisao)}"

    partes = [data, setor_norm, documento_norm, cliente_norm, versao_revisao]
    nome = "_".join(partes)

    if extensao:
        ext = extensao if extensao.startswith(".") else f".{extensao}"
        nome += ext

    return nome


def _data_hoje_aaaammdd() -> str:
    # Import local para nao forcar dependencia de datetime em quem so
    # importa a funcao gerar_nome_documento com uma data ja definida.
    from datetime import date

    return date.today().strftime("%Y%m%d")


def main():
    parser = argparse.ArgumentParser(
        description="Gera o nome de arquivo padronizado [COMPANY_PRODUCT] "
        "(DATA_SETOR_DOCUMENTO_CLIENTE_V#R#)."
    )
    parser.add_argument(
        "--setor",
        required=True,
        help=f"Sigla do setor. Conhecidas: {', '.join(sorted(SETORES))}",
    )
    parser.add_argument("--documento", required=True, help="Nome do documento, ex: 'Termo de Homologacao'")
    parser.add_argument("--cliente", required=True, help="Nome do cliente, ex: '[CLIENT_NAME_1]'")
    parser.add_argument("--versao", required=True, type=int, help="Numero da versao, ex: 1")
    parser.add_argument("--revisao", required=True, type=int, help="Numero da revisao, ex: 1")
    parser.add_argument(
        "--data",
        default=None,
        help="Data no formato AAAAMMDD. Se omitido, usa a data de hoje.",
    )
    parser.add_argument(
        "--extensao",
        default=None,
        help="Extensao do arquivo a anexar, ex: docx, xlsx, pdf, html (opcional).",
    )

    args = parser.parse_args()
    data = args.data or _data_hoje_aaaammdd()

    try:
        nome = gerar_nome_documento(
            setor=args.setor,
            documento=args.documento,
            cliente=args.cliente,
            versao=args.versao,
            revisao=args.revisao,
            data=data,
            extensao=args.extensao,
        )
    except ValueError as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        sys.exit(1)

    print(nome)


if __name__ == "__main__":
    main()
