print ('BIENVENID@ AL MEJOR JUEGO DEL UNIVERSO')

PREGUNTA = str(input('Colon descubrio America?'))


if PREGUNTA == 'si':
    print('Correcta!')
    PREGUNTA_DOS = str(input('La Independencia de Mexico fue en 1810?'))
    if PREGUNTA_DOS == "si":
        print("Correcta!")
        PREGUNTA_TRES = str(input('The Doors fue una banda de U.S.A.?'))
        if PREGUNTA_TRES == "si":
            print("Ganaste!")
        else:
            print('Perdiste,vuelve a intentarlo!')
    else:
        print('Perdiste,vuelve a intentarlo!')
else:
    print ('Perdiste,vuelve a intentarlo!')

print ()
print ()
print ()
print ('***Desing by @xcabezaderadiox***')
