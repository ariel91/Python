score = input ("Ingrese nota")
ingreso = float (score)
if ingreso >= 0.9:
    print ("A")
else:
    if ingreso >= 0.8:
        print ("B")
    else:
        if ingreso >= 0.7:
            print ("C")
        else:
            if ingreso >= 0.6:
                print ("D")
            else:
                if ingreso < 0.6:
                    print ("F")
