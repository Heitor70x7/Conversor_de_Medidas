print('Bem-vindo ao conversor de medidas em comprimento')
x=float((input('Por favor digite o valor de sua medida: ')))
print('Exemplos: (KM)=Quilometro, (HM)=Hectometro, (DAM)=Decametro, (M)=Metros, (DM)=Decímetro, (CM)=Centímetro, (MM)=Milimetro')
y=(input('Agora digite o seu múltiplo: '))
z=input('Agora digite o múltiplo em que deseja converter o seu número: ')

if y=='M' and z=='DAM':
    print(x/10,'DAM, Decametros')
elif y=='M' and z=='HM':
    print(x/10/10 ,'HM, Hectometros')
elif y=='M' and z=='KM':
    print(x/10/10/10, 'KM, Kilometros')
elif y=='M' and z=='DM':
    print(x*10,'DM, Decimetros')
elif y=='M' and z=='CM':
    print(x*10*10,'CM, Centimetros')
elif y=='M' and z=='MM':
    print(x*10*10*10, 'MM, Milimetros')











