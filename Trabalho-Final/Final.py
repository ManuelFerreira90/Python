# entrada tamanho das sequências
x = int(input())
error = False
if x>1000:
  error=True
# entrada sequência bits 1
s1 = input().strip()
s1 = list(s1)
# entrada sequência bits 2
s2 = input().strip()
s2 = list(s2)
# entrada do tipo de operação lógica
operador = input().split(' ')
# contador
c = 0

# resultado
vf = [0 for i in range(x)]
# verificar tamanho das sequências e se são binárias
for i in range(len(s1)):
    c += 1
    if s1[i] != '0' and s1[i] != '1':
        error = True
if c != x:
    error = True
c = 0
for j in range(len(s2)):
    c += 1
    if s2[j] != '0' and s2[j] != '1':
        error = True
if c != x:
    error = True
c = 0
if error==False:
    for i in range(x):
        s1[i] = int(s1[i])
        s2[i] = int(s2[i])
# verificar se operação esta dentro das permitidas
for i in operador:
  if i != 'S1' and i != 'S2':
    if i == "OR" or i == 'AND' or i == 'XOR' or i == 'NAND' or i == 'NOR' or i == 'MOR':
        c+=1
    else:
        error = True
# sequência de tamanho correto e operação dentro das permitidas
if error==False:
    # determinar o tipo de operação e realizar cada operação
    # OR
    if operador[1] == 'OR':
        # S1 OR S2 | S2 OR S1
        if (operador[0] == 'S1' and operador[2] == 'S2') or (operador[0] == 'S2' and operador[2] == 'S1'):
            for i in range(x):
                if s1[i] == 1 or s2[i] == 1:
                    vf[i] = 1
                else:
                    vf[i] = 0
        # S1 OR S1 | S2 OR S2
        elif (operador[0] == 'S1' and operador[2] == 'S1') or (operador[0] == 'S2' and operador[2] == 'S2'):
            if operador[0] == 'S1':
                for i in range(x):
                    if s1[i] == 1:
                        vf[i] = 1
                    else:
                        vf[i] = 0
            elif operador[0] == 'S2':
                for i in range(x):
                    if s2[i] == 1:
                        vf[i] = 1
                    else:
                        vf[i] = 0
        
    # AND
    elif operador[1] == 'AND':
        # S1 AND S2 | S2 AND S1
        if (operador[0] == 'S1' and operador[2] == 'S2') or (operador[0] == 'S2' and operador[2] == 'S1'):
            for i in range(x):
                if s1[i] == 1 and s2[i] == 1:
                    vf[i] = 1
                else:
                    vf[i] = 0
        # S1 AND S1 | S2 AND S2
        elif (operador[0] == 'S1' and operador[2] == 'S1') or (operador[0] == 'S2' and operador[2] == 'S2'):
            if operador[0] == 'S1':
                for i in range(x):
                    if s1[i] == 1:
                        vf[i] = 1
                    else:
                        vf[i] = 0
            elif operador[0] == 'S2':
                for i in range(x):
                    if s2[i] == 1:
                        vf[i] = 1
                    else:
                        vf[i] = 0
       
    # XOR
    elif operador[1] == 'XOR':
        # S1 XOR S2 | S2 XOR S1
        if (operador[0] == 'S1' and operador[2] == 'S2') or (operador[0] == 'S2' and operador[2] == 'S1'):
            for i in range(x):
                if s1[i] != s2[i]:
                    vf[i] = 1
                else:
                    vf[i] = 0
        # S1 XOR S1 | S2 XOR S2
        elif (operador[0] == 'S1' and operador[2] == 'S1') or (operador[0] == 'S2' and operador[2] == 'S2'):
            if operador[0] == 'S1':
                for i in range(x):
                    vf[i] = 0
            elif operador[0] == 'S2':
                for i in range(x):
                  vf[i] = 0
       
    # NAND
    elif operador[1] == 'NAND':
        # S1 NAND S2 | S2 NAND S1
        if (operador[0] == 'S1' and operador[2] == 'S2') or (operador[0] == 'S2' and operador[2] == 'S1'):
            for i in range(x):
                if s1[i] == 1 and s2[i] == 1:
                    vf[i] = 0
                else:
                    vf[i] = 1
        # S1 NAND S1 | S2 NAND S2
        elif (operador[0] == 'S1' and operador[2] == 'S1') or (operador[0] == 'S2' and operador[2] == 'S2'):
            if operador[0] == 'S1':
                for i in range(x):
                    if s1[i] == 1:
                        vf[i] = 0
                    else:
                        vf[i] = 1
            elif operador[0] == 'S2':
                for i in range(x):
                    if s2[i] == 1:
                        vf[i] = 0
                    else:
                        vf[i] = 1

    # NOR
    elif operador[1] == 'NOR':
        # S1 NOR S2 | S2 NOR S1
        if (operador[0] == 'S1' and operador[2] == 'S2') or (operador[0] == 'S2' and operador[2] == 'S1'):
            for i in range(x):
                if s1[i] == 0 and s2[i] == 0:
                    vf[i] = 1
                else:
                    vf[i] = 0
        # S1 NOR S1 | S2 NOR S2
        elif (operador[0] == 'S1' and operador[2] == 'S1') or (operador[0] == 'S2' and operador[2] == 'S2'):
            if operador[0] == 'S1':
                for i in range(x):
                    if s1[i] == 0:
                        vf[i] = 1
                    else:
                        vf[i] = 0
            elif operador[0] == 'S2':
                for i in range(x):
                    if s2[i] == 0:
                        vf[i] = 1
                    else:
                        vf[i] = 0
        
    # MOR
    elif operador[1] == 'MOR':
        # S1 MOR S2 | # S2 MOR S1
        if (operador[0] == 'S1' and operador[2] == 'S2') or (operador[0] == 'S2' and operador[2] == 'S1'):
            for i in range(x):
                if s1[i] == 1 and s2[i] == 0:
                    vf[i] = 0
                else:
                    vf[i] = 1
        # S1 MOR S1 | S2 MOR S2
        elif (operador[0] == 'S1' and operador[2] == 'S1') or (operador[0] == 'S2' and operador[2] == 'S2'):
            if operador[0] == 'S1':
                vf[i] = 1
            elif operador[0] == 'S2':
                for i in range(x):
                    vf[i] = 1

        # caso haja duas operações
    if c == 2:
            # VF OR S1
            if operador[3] == 'OR' and operador[4] == 'S1':
                    for i in range(x):
                        if vf[i] == 1 or s1[i] == 1:
                            vf[i] = 1
                        else:
                            vf[i] = 0
            # VF OR S2
            elif operador[3] == 'OR' and operador[4] == 'S2':
                    for i in range(x):
                        if vf[i] == 1 or s2[i] == 1:
                            vf[i] = 1
                        else:
                            vf[i] = 0
            # VF AND S1
            elif operador[3] == 'AND' and operador[4] == 'S1':
                    for i in range(x):
                        if vf[i] == 1 and s1[i] == 1:
                            vf[i] = 1
                        else:
                            vf[i] = 0
            # VF AND S2
            elif operador[3] == 'AND' and operador[4] == 'S2':
                    for i in range(x):
                        if vf[i] == 1 and s2[i] == 1:
                            vf[i] = 1
                        else:
                            vf[i] = 0
            # VF XOR S1
            elif operador[3] == 'XOR' and operador[4] == 'S1':
                    for i in range(x):
                        if vf[i] != s1[i]:
                            vf[i] = 1
                        else:
                            vf[i] = 0

            # VF XOR S2
            elif operador[3] == 'XOR' and operador[4] == 'S2':
                    for i in range(x):
                        if vf[i] != s2[i]:
                            vf[i] = 1
                        else:
                            vf[i] = 0
            # VF NAND S1
            elif operador[3] == 'NAND' and operador[4] == 'S1':
                    for i in range(x):
                        if vf[i] == 1 and s1[i] == 1:
                            vf[i] = 0
                        else:
                            vf[i] = 1
            # VF NAND S2
            elif operador[3] == 'NAND' and operador[4] == 'S2':
                    for i in range(x):
                        if vf[i] == 1 and s2[i] == 1:
                            vf[i] = 0
                        else:
                            vf[i] = 1
            # VF NOR S1
            elif operador[3] == 'NOR' and operador[4] == 'S1':
                    for i in range(x):
                        if vf[i] == 0 and s1[i] == 0:
                            vf[i] = 1
                        else:
                            vf[i] = 0
            # VF NOR S2
            elif operador[3] == 'NOR' and operador[4] == 'S2':
                    for i in range(x):
                        if vf[i] == 0 and s2[i] == 0:
                            vf[i] = 1
                        else:
                            vf[i] = 0
            # VF MOR S1
            elif operador[3] == 'MOR' and operador[4] == 'S1':
                    for i in range(x):
                        if vf[i] == 1 and s1[i] == 0:
                            vf[i] = 0
                        else:
                            vf[i] = 1
            # VF MOR S2
            elif operador[3] == 'MOR' and operador[4] == 'S2':
                    for i in range(x):
                        if vf[i] == 1 and s2[i] == 0:
                            vf[i] = 0
                        else:
                            vf[i] = 1
# saída
if error == False:
    for i in range(x):
        print(vf[i], end='')
else:
    print("ERRO")