#Librerias necesarias para el i2c y la eeprom
from smbus import SMBus
import time
import time
import subprocess 
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
 
 
# Creacion de la i2x
i2c = busio.I2C(SCL, SDA)
 
# Creacion de la oled y su pixeles
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
 
# limpieza del display.
disp.fill(0)
disp.show()
 
# Imagen en balnco para la imagen del oled
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
 
# Se utiliza para poder limpiar la oled y no sobreescribir
draw.rectangle((0, 0, width, height), outline=0, fill=0)
padding = -2
top = padding
bottom = height - padding
x = 0
font = ImageFont.load_default()


#Variables necesarias para el manejo de la eeprom y de todo el programa
bus = SMBus(1)
address = 0x50
regmsbyte = 0
reglsbyte = 0
sumaPar = 0
restaNon = 0
multiplicaPrimo = 1
sumaCuadrados = 0


#Codigo para definir si un número es par
def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

#Codigo para definir si un número es primo
def primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

#Codigo para definir si un número es multiplo de 3
def multiplo_3(num):
    if num % 3 == 0:
        return True
    else:
        return False


#Creación de la lista que se utilizara para que el usuario introduzca los datos a la memoria
lNum = list()
count = 1
for i in range(20):
    #Ingreso de datos a una lista
    print('Ingresa tu dato numero',i+1,': ')
    num = int(input(''))
    lNum.append(num)

#Escribir en memoria la lista
lNum.insert(0, reglsbyte)
bus.write_i2c_block_data(address, regmsbyte, lNum)
time.sleep(2)


#Localidades pares
#Metodo que lee todas las localidades de la memoria y extrae las que son pares para poder sumarlas
print('Pares')
addressT = address
bus.write_byte_data(addressT, regmsbyte, reglsbyte)
numString = ''
time.sleep(1)
for i in range(1,22):
    if i <21:
        #Leer localidades y extraerlas de memoria
        if (par(i)):
            numT = bus.read_byte(addressT)
            sumaPar = sumaPar + numT
            print('Numero', numT)
            numString = numString + str(numT)
        else:
            bus.read_byte(addressT)
    else:
        #Impresion en consola y en oled del resultado 
        print('Suma Par: ', sumaPar)
        lNum.insert(21,sumaPar)
        bus.write_i2c_block_data(address, regmsbyte, lNum)
        time.sleep(2)
        #Impresion de datos en oled
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), "Suma Par: " + str(sumaPar), font=font, fill=255) 
        draw.text((x, top + 10), "Numeros usados: ", font=font, fill = 255)
        draw.text((x, top + 20), "" + numString, font = font, fill = 255) 
        # Display image.
        disp.image(image)
        disp.show()
        time.sleep(5)
print(sumaPar)

#Localidades nones
#Metodo que lee todas las localidades de la memoria y extrae las que son nones para poder restarlas
print('Nones')
addressT = address
bus.write_byte_data(addressT, regmsbyte, reglsbyte)
numString = ''
# Clear display.
disp.fill(0)
disp.show()
time.sleep(1)
for i in range(1,22):
    if i <21:
        if (not par(i)):
            #Leer localidades de la memoria y ver cuales son impares de los datos y su resta correspondiente
            numT = bus.read_byte(addressT)
            restaNon = restaNon - num
            print('Numero', numT)
            numString = numString + str(numT)
        else:
            bus.read_byte(addressT)
    else:
        #Impresion en consola y en oled del resultado 
        print('Resta Nones: ', restaNon)
        lNum.insert(22,restaNon)
        bus.write_i2c_block_data(address, regmsbyte, lNum)
        time.sleep(2)
        #Impresion de datos en la oled
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), "Resta Nones: " , font=font, fill=255) 
        draw.text((x, top + 8), "" + str(restaNon), font = font, fill = 255) 
        draw.text((x, top + 16), "Numeros usados: ", font=font, fill = 255)
        draw.text((x, top + 24), "" + numString, font = font, fill = 255) 
        # Display image.
        disp.image(image)
        disp.show()
        time.sleep(5)    
print(restaNon)

    
#Localidades primas
print('Primos')
addressT = address
bus.write_byte_data(addressT, regmsbyte, reglsbyte)
numString = ''
# Clear display.
disp.fill(0)
disp.show()
time.sleep(1)
for i in range(1,22):
    if i <21:
        if (primo(i)):
            #Leer localidades de memoria y decir cual es primo, para poder sacar la multiplicacion de todas
            numT = bus.read_byte(addressT)
            multiplicaPrimo = multiplicaPrimo * numT
            print('Numero', numT)
            numString = numString + str(numT)
        else:
            bus.read_byte(addressT)
    else:
        #Impresion en consola y en oled del resultado 
        print('Multiplo: ',multiplicaPrimo)
        lNum.insert(23,multiplicaPrimo)
        bus.write_i2c_block_data(address, regmsbyte, lNum)
        time.sleep(2)
        #La impresion de datos en la oled
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), "Multiplo: " + str(multiplicaPrimo), font=font, fill=255)
        draw.text((x, top + 10), "Numeros usados: ", font=font, fill = 255)
        draw.text((x, top + 20), "" + numString, font = font, fill = 255)   
        # Display image.
        disp.image(image)
        disp.show()
        time.sleep(5)
print(multiplicaPrimo)

#Localidades multiplo 3
print('Multiplos de 3')
addressT = address
bus.write_byte_data(addressT, regmsbyte, reglsbyte)
numString = ''
# Clear display.
disp.fill(0)
disp.show()
time.sleep(1)
for i in range(1,22):
    if i <21:
        if (multiplo_3(i)):
            #Lee las localidades de memoria, para ver cual es multiplo de 3 y saber la sumatoria de su cuadrado
            numT = bus.read_byte(addressT)
            sumaCuadrados = sumaCuadrados + (numT*numT)
            print('Numero', numT) 
            numString = numString + str(numT)               
        else:
            bus.read_byte(addressT)
    else:
        #Impresion en consola y en oled del resultado 
        print('Suma Cuadrados: ',sumaCuadrados)
        lNum.insert(24,sumaCuadrados)
        bus.write_i2c_block_data(address, regmsbyte, lNum)
        time.sleep(2)
        #Impresion de datos en la pantalla oled
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), "Suma Cudrados: " + str(sumaCuadrados), font=font, fill=255)  
        draw.text((x, top + 10), "Numeros usados: ", font=font, fill = 255)
        draw.text((x, top + 20), "" + numString, font = font, fill = 255)   
        # Display image.
        disp.image(image)
        disp.show()
        time.sleep(5)
print(sumaCuadrados)


#Impresion de como estan acomodados los datos
addressT = address
bus.write_byte_data(addressT, regmsbyte, reglsbyte)
for i in range(1,25): 
    numT = bus.read_byte(addressT)
    print('Localidad', i, 'Numero', numT)

#Añade nuevos numeros a la localidad 21-24    
addressT = address
bus.write_byte_data(addressT, regmsbyte, reglsbyte)
numString = ''
# Clear display.
disp.fill(0)
disp.show()
time.sleep(1)
for i in range(1,26):
    if i <22:
        bus.read_byte(addressT)
    elif i < 25:
        #Se ingresan los numeros en las localidades correspondientes y se suman con la localidad 21 
        print('Localidad', i, end=' ')
        numT = int(input('Ingresa el numero nuevo: '))   
        lNum[i-1] = numT
        numString = numString + str(numT)
        sumaPar = sumaPar + numT
    else:
        #Impresion en consola y en oled del resultado 
        bus.write_i2c_block_data(address, regmsbyte, lNum)
        time.sleep(2)
        #Impresion de pantalla oled de los resultaos
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top + 0), "Añadiste numeros: " , font=font, fill=255) 
        draw.text((x, top + 8), "" + numString, font = font, fill = 255) 
        draw.text((x, top + 16), "Suma Nuevos", font = font, fill = 255)
        draw.text((x, top + 24), "" + str(sumaPar), font = font, fill = 255)
        time.sleep(5)
print(sumaPar)

#Arreglo final de las localidades y datos        
addressT = address
bus.write_byte_data(addressT, regmsbyte, reglsbyte)
for i in range(1,25): 
    numT = bus.read_byte(addressT)
    print('Localidad', i, 'Numero', numT)
    
# Display image.
disp.image(image)
disp.show()
time.sleep(2)
