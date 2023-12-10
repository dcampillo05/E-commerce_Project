import re

def valida_CPF(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf != 11):
        return False
    
    newCPF = cpf[:2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(newCPF[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
                total = 0
                newCPF += str(d)

    sequencia = newCPF == str(newCPF(0)) * len(cpf)

    if cpf == newCPF and not sequencia:
        return True
    else:
        return False 