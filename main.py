"""Arquivo principal que será interpretado pelo interpretador."""
import math

METROS_POR_LITRO = 6
LITROS_POR_LATA = 18
LITROS_POR_GALAO = 3.6
VALOR_LATA = 80
VALOR_GALAO = 25
FOLGA = 0.1

def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""

    # Entrada dos dados.
    area = float(input('Digite a área: '))
    
    # Manipulação
    area_total = area * FOLGA + area
    quantidade_litros = area_total / METROS_POR_LITRO
    
    total_latas = math.ceil(quantidade_litros / LITROS_POR_LATA)
    preco_total_latas = total_latas * VALOR_LATA
     
    total_galoes = math.ceil(quantidade_litros / LITROS_POR_GALAO)
    preco_total_galoes = total_galoes * VALOR_GALAO

    resto_lata = quantidade_litros % LITROS_POR_LATA
    total_galao = math.ceil(resto_lata / LITROS_POR_GALAO)
    total_lata = math.floor(quantidade_litros / LITROS_POR_LATA)


    menor_desperdicio = (total_lata * VALOR_LATA) + (total_galao * VALOR_GALAO)

    # Exibição.
    print(f'O valor gasto comprando apenas latas é de R$ {preco_total_latas:.2f}.')
    print(f'Serão necessárias {total_latas} latas.')
    print(f'O valor gasto comprando apenas galões é de R$ {preco_total_galoes:.2f}.')
    print(f'Serão necessários {total_galoes} galões.')
    print(f'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ {menor_desperdicio:.2f}.')
    print(f'Serão necessárias {total_lata} latas e {total_galao} galões.')


if __name__ == '__main__':
    main()
