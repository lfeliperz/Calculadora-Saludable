#CALCULADORA SALUDABLE - CONDICIONAL

#Hombre
genero=input("Digite M si es Hombre O digite F si es Mujer: ")
if  genero=="M":
    AlturaH=int(input("Su género es másculino digite su estatura en cm: "))
    PesoH=float(input("Digite su peso actual en Kg: "))
    EdadH=int(input("Digite su edad en años: "))
    ibwH=(56.2+1.41*(AlturaH/2.54-60))
    print("Digite solo 1 opción")
    deporte=float(input("Digite su MET: caminar=2, tenis=5, bicicleta=14, correr=6, nadar=9.8: "))
    tiempo=float(input("Digite en cuanto tiempo realiza el deporte seleccionado en minutos: "))
    calorias=(tiempo*deporte*PesoH/200)
    imcH=(PesoH/(AlturaH*AlturaH))
    GrasaH=(1.20*imcH+0.23*EdadH-16.2)
    indicemeta=((13.397*PesoH)+(4.799*EdadH)-(5.677*AlturaH)+88.362)
    print("Tu peso ideal deberia de ser de: ", ibwH,"y actualmente tu peso es de: ",PesoH)
    print("Actualmente estas quemando: ", calorias, "calorías")
    print("Actualmente posees: ", GrasaH, "de grasa corporal")
    print("Tu índice metabólico basal es de: ",indicemeta)
    exit("Gracias por tu tiempo")

#Mujer
else: 
 if genero=="F":
   AlturaM=int(input("Su género es femenino digite su estatura en cm: "))
   PesoM=float(input("Digite su peso actual en Kg: "))
   edadM=int(input("Digite su edad en años: "))
   ibwM=(53.1+1.36*(AlturaM/2.54-60))
   print("Digite solo 1 opción")
   deporte=float(input("Digite su MET: caminar=2, tenis=5, bicicleta=14, correr=6, nadar=9.8: "))
   tiempo=float(input("Digite en cuanto tiempo realiza el deporte seleccionado en minutos: "))
   caloriasM=(tiempo*deporte*PesoM/200)
   imcM=(PesoM/(AlturaM*AlturaM))
   GrasaM=(1.20*imcM+0.23*edadM-5.4)
   indicemetaM=((9.24*PesoM)+(3.098*edadM)-(4.330*AlturaM)+447.593)
   print("Tu peso ideal deberia de ser de: ", ibwM,"y actualmente tu peso es de: ",PesoM)
   print("Actualmente estas quemando: ", caloriasM, "calorías")
   print("Actualmente posees:", GrasaM, "de grasa corporal")
   print("Tu índice metabólico basal es de: ",indicemetaM)
   exit("Gracias por tu tiempo")


#CALCULADORA SALUDABLE - SIN CONDICIONAL

print(" CALCULADORA SALUDABLE")
print("===========================================================================")
print(" PESO IDEAL")
print("===========================================================================")
print("")


def peso_ideal_h(altura_h):
  
  h=56.2+1.41*(altura_h/2.54-60)
  
  return h


def peso_ideal_m(altura_m):
  
  m=53.1+1.36*(altura_m/2.54-60)
  
  return m


altura_h=float(input("Altura hombre: "))
altura_m=float(input("Altura mujer: "))

result_h=round(peso_ideal_h(altura_h),2)
result_m=round(peso_ideal_m(altura_m),2)

print("Peso ideal hombre: ", result_h)
print("Peso ideal mujer: ", result_m)


print(" CALCULADORA SALUDABLE")
print("===========================================================================")
print(" PESO IDEAL")
print("===========================================================================")
print("")


def peso_ideal_h(altura_h):
  
  h=56.2+1.41*(altura_h/2.54-60)
  
  return h


def peso_ideal_m(altura_m):
  
  m=53.1+1.36*(altura_m/2.54-60)
  
  return m


altura_h=float(input("Altura hombre: "))
altura_m=float(input("Altura mujer: "))

result_h=round(peso_ideal_h(altura_h),2)
result_m=round(peso_ideal_m(altura_m),2)

print("Peso ideal hombre: ", result_h)
print("Peso ideal mujer: ", result_m)


print("")
print("===========================================================================")
print(" CALORIAS QUEMADAS")
print("===========================================================================")
print("")


def calorias_quemadas(t_ac, met, peso):

  cal=(t_ac * met * peso)/200

  return cal


met=float(input("Digite su MET: caminar=2, tenis=5, bicicleta=14, correr=6, nadar=9.8: "))
t_ac=float(input("Digite su tiempo en actividad en minutos: "))
peso=float(input("Digite su peso en kilogramos: "))

resultado=calorias_quemadas(t_ac, met, peso)
print("Sus calorias quemadas son: ", resultado)


print("")
print("===========================================================================")
print(" ÍNDICE METABÓLICO BASAL")
print("===========================================================================")
print("")


def indice_metabilico_basal_h(pesoh, edadh, altura_h):
  indicemetah=((13.397*pesoh)+(4.799*edadh)-(5.677*altura_h)+88.362)
  return indicemetah

def indice_metabilico_basal_m(pesom, edadm, altura_m):
  indicemetaM=((9.24*pesom)+(3.098*edadm)-(4.330*altura_m)+447.593)
  return indicemetaM
  
  
pesoh=float(input("Digite el peso del hombre: "))
pesom=float(input("Digite el peso de la mujer: "))

edadh=float(input("Digite la edad del hombre: "))
edadm=float(input("Digite la edad de la mujer: "))

resultadoimbh=indice_metabilico_basal_h(pesoh, edadh, altura_h)
resultadoimbm=indicemetaM=indice_metabilico_basal_m(pesom, edadm, altura_m)


print("Tu índice metabólico basal del hombre es de: ",round(resultadoimbh),2)
print("Tu índice metabólico basal de la mujer es de: ",round(resultadoimbm),2)


print("")
print("===========================================================================")
print(" IMC")
print("===========================================================================")
print("")


def imch(pesoh, altura_h):
  imc=(pesoh/(altura_h*altura_h))
  return imc

def imcm(pesom, altura_m):
  imc=(pesom/(altura_m*altura_m))
  return imc


resultadoimc=imch(pesoh, altura_h)
resultadoimcm=imc=imcm(pesom, altura_m)


print("El IMC del hombre es: ", round((resultadoimc*10000),2))
print("El IMC de la mujer es: ",round((resultadoimcm*10000),2))
      

print("")
print("===========================================================================")
print(" GRASA CORPORAL")
print("===========================================================================")
print("")


def grasa_corporal_h(resultadoimc, edadh):
   GrasaH=(1.20*resultadoimc+0.23*edadh-16.2)
   return GrasaH

def grasa_corporal_m(resultadoimcm, edadm):
  GrasaM=(1.20*resultadoimcm+0.23*edadm-5.4)
  return GrasaM

resultadograsah=grasa_corporal_h(resultadoimc, edadh)
resultadograsam=grasa_corporal_m(resultadoimcm, edadm)

print("Actualmente el hombre posee:", round(-resultadograsah,2), "de grasa corporal")
print("Actualmente la mujer posee:", round(resultadograsam,2), "de grasa corporal")

print("")
print("===========================================================================")
print(" GRACIAS POR USAR LA CALCULADORA SALUDABLE ")
print("===========================================================================")