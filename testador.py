# testador.py
# Testador interativo: você digita uma descrição e um valor,
# e o sistema mostra como o lançamento seria classificado.
# Se não houver regra, ele oferece criar uma na hora.
# Para rodar:  python testador.py

from dados import regras_categorias
from classificador import classificar_lancamento, CATEGORIA_PADRAO
from terminal import formatar_valor, ler_texto, ler_valor, tela_adicionar_regra


def executar_testador():
    print("=== TESTADOR DE CLASSIFICAÇÃO ===")
    print("Digite 'sair' na descrição para encerrar.\n")

    while True:
        descricao = ler_texto("Descrição: ")
        if descricao.lower() == "sair":
            print("Encerrando testador...")
            break

        valor = ler_valor("Valor (ex: 45,90): ")

        lancamento = {"descricao": descricao, "valor": valor}
        resultado = classificar_lancamento(lancamento, regras_categorias)

        print(f"  -> {formatar_valor(resultado['valor'])} | "
              f"{resultado['descricao']} | [{resultado['categoria']}]")

        if resultado["categoria"] == CATEGORIA_PADRAO:
            resposta = ler_texto("  Sem regra para isso. Criar uma agora? (s/n): ",
                                 opcional=True).lower()
            if resposta == "s":
                tela_adicionar_regra(regras_categorias)

        print()


# Só roda o testador quando este arquivo é executado diretamente.
if __name__ == "__main__":
    executar_testador()
