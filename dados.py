# dados.py
# Guarda os dados do sistema: as regras de classificação e o extrato simulado.

# Regras: palavra-chave (sempre em minúsculas) -> categoria
regras_categorias = {
    "uber": "Transporte",
    "posto": "Combustível",
    "restaurante": "Alimentação",
    "hotel": "Hospedagem",
}

# Extrato simulado do cartão corporativo (lista de dicionários).
# Repare que aqui ainda NÃO existe categoria: quem descobre é o classificador.
extrato_corporativo = [
    {"descricao": "UBER DO BRASIL", "valor": 45.90},
    {"descricao": "AUTO POSTO IPIRANGA", "valor": 150.00},
    {"descricao": "RESTAURANTE SABOR CARIOCA", "valor": 82.50},
    {"descricao": "HOTEL COPACABANA", "valor": 420.00},
    {"descricao": "LOJA DESCONHECIDA", "valor": 89.90},
]
