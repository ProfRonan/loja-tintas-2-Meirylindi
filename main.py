"""Arquivo principal que será interpretado pelo interpretador."""
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    pintar_area = float(input('Digite a área: '))
    lata_area = 18 * 6
    galao_area = 3.6 * 6
    total_area = pintar_area + (pintar_area * 0.1)
    if total_area % lata_area < lata_area:
      total_lata = (total_area//lata_area + 1)
    else:
      total_lata = total_area/lata_area
    if total_area % galao_area < galao_area:
      total_galao = (total_area//galao_area + 1)
    else:
      total_galao = total_area/galao_area
    valor_lata = total_lata*80
    valor_galao = total_galao*25
    resto_lata = total_area % lata_area
    if resto_lata < galao_area:
      galao = 1
      lata = total_lata - 1
    elif resto_lata % galao_area < galao_area:
      galao = resto_lata//galao_area + 1
      lata = total_lata - 1
    else:
      galao = 0
    print(f'O valor gasto comprando apenas latas é de R$ {valor_lata:.2f}.')
    print(f'Serão necessárias {int(total_lata)} latas.')
    print(f'O valor gasto comprando apenas galões é de R$ {valor_galao:.2f}.') 
    print(f'Serão necessários {int(total_galao)} galões.')
    print(f'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ {lata * 80 + galao * 25:.2f}.')
    print(f'Serão necessárias {int(lata)} latas e {int(galao)} galões.')

    




if __name__ == '__main__':
    main()
