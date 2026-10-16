# terminal.py
# Tudo o que aparece na tela ou é digitado pelo usuário fica aqui.
# Regra de dependência: terminal.py usa classificador.py, nunca o contrário.

from classificador import (
    classificar_extrato,
    classificar_lancamento,
    adicionar_regra,
    editar_lancamento,
    validar_valor,
    normalizar,
)


# ---------------------------------------------------------------
# Exibição
# ---------------------------------------------------------------

def formatar_valor(valor):
    """Transforma 45.9 em 'R$ 45,90'."""
    texto = f"{valor:.2f}".replace(".", ",")
    return f"R$ {texto}"


def imprimir_extrato(extrato_classificado, numerar=False):
    """Mostra o extrato classificado em colunas alinhadas.
    Com numerar=True, cada linha ganha um número (começando em 1)."""
    largura = 72 if numerar else 66
    print("=" * largura)

    cabecalho = f"{'VALOR':>12} | {'DESCRIÇÃO':<28} | CATEGORIA"
    if numerar:
        cabecalho = f"{'Nº':>3} | " + cabecalho
    print(cabecalho)
    print("=" * largura)

    numero = 1
    for item in extrato_classificado:
        valor = formatar_valor(item["valor"])
        linha = f"{valor:>12} | {item['descricao']:<28} | {item['categoria']}"
        if numerar:
            linha = f"{numero:>3} | " + linha
        print(linha)
        numero += 1

    print("=" * largura)


def listar_regras(regras):
    """Mostra as regras atuais (palavra-chave -> categoria)."""
    print("Regras atuais:")
    for palavra, categoria in regras.items():
        print(f"  {palavra} -> {categoria}")


# ---------------------------------------------------------------
# Leitura segura: repete até o usuário digitar algo válido
# ---------------------------------------------------------------

def ler_texto(mensagem, opcional=False):
    """Lê um texto. Se não for opcional, repete enquanto estiver vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto != "" or opcional:
            return texto
        print("  Entrada vazia. Tente novamente.")


def ler_valor(mensagem, opcional=False):
    """Lê um valor em reais (aceita vírgula ou ponto).
    Repete enquanto for inválido. Se opcional e vazio, devolve None."""
    while True:
        texto = input(mensagem).strip()

        if texto == "" and opcional:
            return None

        try:
            valor = float(texto.replace(",", "."))
        except ValueError:
            print("  Valor inválido. Digite apenas números, ex: 45,90")
            continue

        try:
            validar_valor(valor)
        except ValueError as erro:
            print(f"  {erro}")
            continue

        return valor


def ler_inteiro(mensagem):
    """Lê um número inteiro. Se for inválido, avisa e devolve None."""
    texto = input(mensagem).strip()
    try:
        return int(texto)
    except ValueError:
        print("  Digite um número inteiro.")
        return None


# ---------------------------------------------------------------
# Telas (Sprint 2)
# ---------------------------------------------------------------

def tela_adicionar_regra(regras):
    """Pede uma palavra-chave e uma categoria e cria a regra."""
    print("\n--- ADICIONAR REGRA ---")
    listar_regras(regras)

    palavra = ler_texto("Nova palavra-chave: ")
    categoria = ler_texto("Categoria correspondente: ")

    try:
        eh_nova = adicionar_regra(regras, palavra, categoria)
    except ValueError as erro:
        print(f"  Não foi possível adicionar: {erro}")
        return

    verbo = "criada" if eh_nova else "atualizada"
    print(f"  Regra {verbo}: '{normalizar(palavra)}' -> '{categoria}'")


def tela_editar_lancamento(extrato, regras):
    """Mostra o extrato numerado e deixa o usuário editar um lançamento."""
    print("\n--- EDITAR LANÇAMENTO ---")
    imprimir_extrato(classificar_extrato(extrato, regras), numerar=True)

    numero = ler_inteiro("Número do lançamento (0 para cancelar): ")
    if numero is None or numero == 0:
        return

    if numero < 1 or numero > len(extrato):
        print("  Esse lançamento não existe.")
        return

    indice = numero - 1
    atual = extrato[indice]
    print(f"Editando: {atual['descricao']} ({formatar_valor(atual['valor'])})")
    print("(Aperte Enter para manter o campo como está)")

    nova_descricao = ler_texto("Nova descrição: ", opcional=True)
    novo_valor = ler_valor("Novo valor: ", opcional=True)

    if nova_descricao == "":
        nova_descricao = None

    if nova_descricao is None and novo_valor is None:
        print("  Nenhuma alteração feita.")
        return

    try:
        editar_lancamento(extrato, indice, nova_descricao, novo_valor)
    except ValueError as erro:
        print(f"  Não foi possível editar: {erro}")
        return

    atualizado = classificar_lancamento(extrato[indice], regras)
    print("  Lançamento atualizado:")
    print(f"  -> {formatar_valor(atualizado['valor'])} | "
          f"{atualizado['descricao']} | [{atualizado['categoria']}]")
