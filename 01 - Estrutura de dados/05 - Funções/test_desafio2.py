import io
import sys
from unittest.mock import patch


def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # Processamento das reservas - verificar cada reserva
    confirmadas = []
    recusadas = []
    
    # Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            confirmadas.append(reserva)
        else:
            recusadas.append(reserva)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))


def teste_exemplo_1():
    """
    Entrada: 101 102 103 104 / 102 105 101 103
    Saída esperada:
    Reservas confirmadas: 102 101 103
    Reservas recusadas: 105
    """
    entrada = "101 102 103 104\n102 105 101 103\n"
    saida_esperada = "Reservas confirmadas: 102 101 103\nReservas recusadas: 105\n"
    
    with patch('sys.stdin', io.StringIO(entrada)):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            processar_reservas()
            resultado = mock_stdout.getvalue()
    
    assert resultado == saida_esperada, f"Teste 1 falhou!\nEsperado:\n{saida_esperada}\nObtido:\n{resultado}"
    print("✓ Teste 1 passou")


def teste_exemplo_2():
    """
    Entrada: 201 202 203 204 205 / 205 202 208 201 203
    Saída esperada:
    Reservas confirmadas: 205 202 201 203
    Reservas recusadas: 208
    """
    entrada = "201 202 203 204 205\n205 202 208 201 203\n"
    saida_esperada = "Reservas confirmadas: 205 202 201 203\nReservas recusadas: 208\n"
    
    with patch('sys.stdin', io.StringIO(entrada)):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            processar_reservas()
            resultado = mock_stdout.getvalue()
    
    assert resultado == saida_esperada, f"Teste 2 falhou!\nEsperado:\n{saida_esperada}\nObtido:\n{resultado}"
    print("✓ Teste 2 passou")


def teste_exemplo_3():
    """
    Entrada: 10 20 30 40 50 / 25 30 10 40 50 60
    Saída esperada:
    Reservas confirmadas: 30 10 40 50
    Reservas recusadas: 25 60
    """
    entrada = "10 20 30 40 50\n25 30 10 40 50 60\n"
    saida_esperada = "Reservas confirmadas: 30 10 40 50\nReservas recusadas: 25 60\n"
    
    with patch('sys.stdin', io.StringIO(entrada)):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            processar_reservas()
            resultado = mock_stdout.getvalue()
    
    assert resultado == saida_esperada, f"Teste 3 falhou!\nEsperado:\n{saida_esperada}\nObtido:\n{resultado}"
    print("✓ Teste 3 passou")


if __name__ == "__main__":
    teste_exemplo_1()
    teste_exemplo_2()
    teste_exemplo_3()
    print("\n✓ Todos os testes passaram!")
