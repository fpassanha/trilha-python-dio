# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# Ordena por prioridade: urgente > idosos > demais
# Critério: urgente (0) > idosos 60+ (1) > normal (2)
# Desempate: maior idade primeiro (menor valor negativo = maior prioridade)
def prioridade(paciente):
    nome, idade, status = paciente
    if status == "urgente":
        return (0, -idade)  # Urgente com idade decrescente
    elif idade >= 60:
        return (1, -idade)  # Idosos com idade decrescente
    else:
        return (2, -idade)  # Demais com idade decrescente

pacientes.sort(key=prioridade)

# Exibe a ordem de atendimento com título e vírgulas
nomes = [paciente[0] for paciente in pacientes]
print("Ordem de Atendimento: " + ", ".join(nomes))