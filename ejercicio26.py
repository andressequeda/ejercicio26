nota1  =  float ( input ( "Ingrese la nota 1:" ))
nota2  =  float ( input ( "Ingrese la nota 2:" ))
nota3  =  float ( input ( "Ingrese la nota 3:" ))
nota4  =  float ( input ( "Ingrese la nota 4:" ))
nota5  =  float ( input ( "Ingrese la nota 5:" ))
nota_final  = ( nota1  *  0.15 ) + ( nota2  *  0.20 ) + ( nota3  *  0.15 ) + ( nota4  *  0.30 ) + ( nota5  *  0.20 )
si  nota_final  <  2.0 :
    print ( "No se puede habilitar." )
si  nota_final  <  3.0 :
    imprimir ( "Reprobó." )
si  nota_final  > =  3.0 :
    imprimir ( "Aprobó." )
si  nota_final  >  4.5 :
    print ( "Felicitaciones." )
