# classificador.py
# Lógica do sistema. Aqui NÃO existe input() nem print():
# as funções só recebem dados e devolvem resultado (ou avisam erros
# com ValueError, que quem chamou trata com try/except).

import math

CATEGORIA_PADRAO = "Outros / Não Classificado"


def normalizar(texto):
    """Deixa o texto em minúsculas e sem espaços nas pontas."""
    return texto.lower().strip()


# ---------------------------------------------------------------
# Sprint 1: classificação
# ---------------------------------------------------------------

def classificar_descricao(descricao, regras):
    """Recebe uma descrição e devolve a categoria encontrada."""
    texto = normalizar(descricao)

    for palavra, categoria in regras.items():
        if palavra in texto:
            return categoria

    return CATEGORIA_PADRAO


def classificar_lancamento(lancamento, regras):
    """Recebe UM lançamento (descricao e valor) e devolve um lançamento
    novo, com a mesma descrição e valor e a categoria acrescentada."""
    categoria = classificar_descricao(lancamento["descricao"], regras)

    return {
        "descricao": lancamento["descricao"],
        "valor": lancamento["valor"],
        "categoria": categoria,
    }


def classificar_extrato(extrato, regras):
    """Recebe o extrato inteiro e devolve uma LISTA NOVA, já classificada.
    O extrato original não é modificado."""
    extrato_classificado = []

    for lancamento in extrato:
        novo = classificar_lancamento(lancamento, regras)
        extrato_classificado.append(novo)

    return extrato_classificado


# ---------------------------------------------------------------
# Sprint 2: regras e lançamentos editáveis
# ---------------------------------------------------------------

def validar_valor(valor):
    """Garante que o valor é um número finito maior que zero.
    Se não for, avisa com ValueError."""
    if not math.isfinite(valor) or valor <= 0:
        raise ValueError("O valor deve ser um número maior que zero.")


def adicionar_regra(regras, palavra, categoria):
    """Acrescenta (ou atualiza) uma regra no dicionário de regras.

    Devolve True se a regra é nova e False se a palavra-chave já existia
    e a categoria foi atualizada. Avisa com ValueError se algo estiver vazio.
    """
    palavra = normalizar(palavra)
    categoria = categoria.strip()

    if palavra == "":
        raise ValueError("A palavra-chave não pode ficar vazia.")
    if categoria == "":
        raise ValueError("A categoria não pode ficar vazia.")

    ja_existia = palavra in regras
    regras[palavra] = categoria
    return not ja_existia


def editar_lancamento(extrato, indice, nova_descricao=None, novo_valor=None):
    """Altera um lançamento do extrato (o próprio extrato é modificado).

    indice começa em 0. Passe None no campo que não quer mudar.
    Avisa com ValueError se o índice ou os novos dados forem inválidos;
    nesse caso NADA é alterado.
    """
    if indice < 0 or indice >= len(extrato):
        raise ValueError("Esse lançamento não existe.")

    # primeiro valida tudo, depois altera (assim não fica edição pela metade)
    if nova_descricao is not None:
        nova_descricao = nova_descricao.strip()
        if nova_descricao == "":
            raise ValueError("A descrição não pode ficar vazia.")

    if novo_valor is not None:
        validar_valor(novo_valor)

    if nova_descricao is not None:
        extrato[indice]["descricao"] = nova_descricao
    if novo_valor is not None:
        extrato[indice]["valor"] = novo_valor
