mes = input()
comm = []
def change (og: str, sub: str, rep: str):
    l = [x for x in og]
    og = l.join()
    return og
def reverse (og: str, sub: str):
    l = [x for x in og]
    og = l.join()
    return og
def space (og: str, index: int):
    l = [x for x in og]
    og = l.join()
    return og
while 1 == 1:
    comm = input().split(":|:")
    if comm[0] == 'ChangeAll':
        change(mes, comm[1], comm[2])
        print(mes)
    if comm[0] == 'Reverse':
        reverse(mes, comm[1])
        print(mes)
    if comm[0] == 'InsertSpace':
        space(mes, comm[1])
        print(mes)
    if comm[0] == 'Reveal':
        print(f'You have a new text message: {mes}')    
    
    
