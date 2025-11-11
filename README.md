# Parcial
## Alejandra Suarez Sepulveda

---

## Cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa.
Se debe crear un segundo microservicio de historial en el cual almacenaremos la informacion en una base de datos puede ser mysqlite3 y se modificaria el microservicio presente de factorial para que se comunique con el otro servicio con la instruccion clave de request.post, asi en el microservicio original, después de calcular el factorial, hacemos una llamada HTTP POST al servicio de historial.

Si comparamos los 2 diseños cambiaria la arquitectura, ya que de 1servicio pasariamos a 2 servicios que se comunican. En el primero no hay comunicación y en el segundo	se comunican por HTTP (requests POST). Ademas el acoplamiento	en la primera seria directo	y en la segunda bajo, esto le permite ser independiente y escalable por servicio.
