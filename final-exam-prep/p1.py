mes = input()
comm = []
def change (og: str, sub: str, rep: str):
    og = og.replace(sub, rep)
    return og
def reverse (og: str, sub: str):
    og = og.replace(sub, sub[::-1], 1)
    return og     
def space (og: str, index: int):
    l = [og[:index], ' ', og[index:]]
    og = ''.join(l)
    return og
for i in range(20):
    comm = input().split(":|:")
    if comm[0] == 'ChangeAll':
        mes = change(mes, comm[1], comm[2]) 
        print(mes)
    if comm[0] == 'Reverse':
        if comm[1] in mes:
            mes = reverse(mes, comm[1])
            print(mes)
        else:
            print('error')
    if comm[0] == 'InsertSpace':
        mes = space(mes, int(comm[1]))
        print(mes)
    if comm[0] == 'Reveal':
        print(f'You have a new text message: {mes}')
        break    
    
    
