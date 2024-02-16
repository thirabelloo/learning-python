# Imagine que você está desenvolvendo um aplicativo chamado Fokus, inspirado na técnica Pomodoro de gerenciamento de tempo. 
# O objetivo do Fokus é ajudar as pessoas a se concentrarem em suas tarefas usando períodos de trabalho focados intercalados com breves intervalos. 
# Uma característica importante do seu aplicativo é permitir que o usuário escolha o tempo de foco e o tempo de pausa.

# Você precisa escrever uma função que pergunte ao usuário quanto tempo deseja configurar para o período de foco e, em seguida, use condicionais para verificar se 
# o tempo inserido está dentro de um intervalo aceitável (por exemplo, entre 25 e 45 minutos).

# Qual das seguintes implementações da função configurar_tempo_foco está correta e segue as melhores práticas aprendidas no curso?


def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if 25 <= tempo <= 45:
        print("Tempo configurado para", tempo, "minutos.")
    else:
        print("Valor inválido. Configure um tempo entre 25 e 45 minutos.")

configurar_tempo_foco()

def configurar_tempo_foco_2():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if tempo < 25:
        print("Valor muito baixo. Configure um tempo maior ou igual a 25 minutos.")
    elif tempo > 45:
        print("Valor muito alto. Configure um tempo menor ou igual a 45 minutos.")
    else:
        print("Tempo configurado para", tempo, "minutos.")