# main.py
# Ponto de entrada do sistema. Só junta as peças.
# O menu abaixo é PROVISÓRIO (Sprint 2): serve para acessar as novas funções.
# Na Sprint 3 ele é refinado e ganha o resumo por categoria.

from dados import regras_categorias, extrato_corporativo
from classificador import classificar_extrato
from terminal import (
    imprimir_extrato,
    ler_inteiro,
    tela_adicionar_regra,
    tela_editar_lancamento,
)
from testador import executar_testador


def mostrar_menu():
    print("\n" + "=" * 50)
    print("   CLASSIFICADOR DE DESPESAS CORPORATIVAS")
    print("=" * 50)
    print("[1] Ver extrato classificado")
    print("[2] Adicionar regra (palavra-chave)")
    print("[3] Editar um lançamento")
    print("[4] Testador de classificação")
    print("[0] Sair")
    print("-" * 50)


def main():
    while True:
        mostrar_menu()
        opcao = ler_inteiro("Escolha: ")

        if opcao == 1:
            extrato_classificado = classificar_extrato(extrato_corporativo, regras_categorias)
            imprimir_extrato(extrato_classificado)
        elif opcao == 2:
            tela_adicionar_regra(regras_categorias)
        elif opcao == 3:
            tela_editar_lancamento(extrato_corporativo, regras_categorias)
        elif opcao == 4:
            executar_testador()
        elif opcao == 0:
            print("Encerrando sistema...")
            break
        elif opcao is not None:
            print("  Opção inválida.")


if __name__ == "__main__":
    main()
