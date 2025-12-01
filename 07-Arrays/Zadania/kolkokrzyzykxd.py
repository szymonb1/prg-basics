b=[' ']*9
p='XO'
while 1:
    print(f'{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}')
    i=int(input(f'{p[0]}: '))-1
    if b[i]!=' ': continue
    b[i]=p[0]
    if any(b[a]==b[b2]==b[c] != ' ' for a,b2,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]):
        print(f'{p[0]} wins!'); break
    if ' ' not in b: print('Draw'); break
    p=p[::-1]
