# spostare tutti gli zeri a destra
# gli interi positivi devono rimanere nello stesso ordine
# posso scorrere la lista una sola volta
# non posso usare altre liste di appoggio
# stampa la lista risultante

def shrink(ls):
    pos_index = 0
    count_iterations = 0
    while count_iterations < len(ls)-1:
        if ls[pos_index] == 0:
            # sposta lo zero all'ultimo posto della lista
            # e ripeti il controllo sulla posizione
            # (perchè le posizioni sono "shiftate")
            ls.append(ls.pop(pos_index))
            pos_index -= 1
        # passa alla prossima posizione (prossimo intero nella lista)
        pos_index += 1
        count_iterations += 1
    print(" ".join([str(n) for n in ls]))

def try_int(num):
    try:
        return int(num)
    except:
        print('Enter a valid digit!')
        exit()

input_data = input('[*] Enter input data:')
input_data = input_data.replace(' ','')
input_data = [try_int(n) for n in input_data]
shrink(input_data)
