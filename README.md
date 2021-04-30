# Raspberry + 24LC256 (I2C)

Guía paso a paso para el envío de 20 datos, usando Raspberry y una memoria 24LC256.

Desarrollar un programa en Raspberry que permita realizar la siguiente tarea:

1. Escribir 20 diferentes datos en las 10 primeras localidades de memoria de una 24LC256. Los datos serán ingresado por el usuario a través de la terminal. Los datos los vamos a etiquetar del 1 al 20 y se realizarán las siguientes operaciones.

     a. Las localidades pares se suman y se almacena el resultado en la localidad 21

     b. Las localidades nones se restan y se almacena el resultado en la localidad 22

     c. Las localidades que son número primo se multiplican y se almacenan en la localidad 23

     d. Las localidades que son múltiplo de 3 se eleva cada valor al cuadrado y se suman y se almacena en la localidad 24

2. Al finalizar las operaciones, se muestran los datos usados en cada operación y el resultado de la misma en una pantalla OLED

3. Después de mostrar los resultados en la pantalla OLED se permite al usuario escribir en las localidades 21 a 24 con los valores que decida.

4. Se toma el resultado de la suma de las localidades pares y se suman los valores recién agregados a las localidades 21 a 24. Se imprime el resultado en la pantalla OLED

5. Finaliza el programa

Puedes visitar el [wiki](https://github.com/AaroniSalinas/RaspberryI2C/wiki) para más información.

**Equipo Dinamita**
- Nashely Chan
- Rodrigo Olivares
- Aaroni Salinas
