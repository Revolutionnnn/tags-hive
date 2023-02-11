# tags-hive
Este código utiliza la librería beem y pandas para analizar la ganancia en HBD (una moneda digital en la plataforma Hive) asociada con los 10 tags más populares en la plataforma Hive que comienzan con la palabra "hive".

El código define una función llamada comments_payouts que toma una fila de un DataFrame como entrada y devuelve el resultado de dividir el valor total de los pagos (total_payouts) por el número de publicaciones de mayor pago (top_posts).

A continuación, se crea un objeto q que utiliza la clase Query de beem para acceder a los tags más populares en la plataforma Hive. Se utiliza la función Trending_tags para agregar los tags a una lista y crear un DataFrame (df) con estos datos.

Se reemplaza el texto " HBD" en la columna "total_payouts" con valores numéricos para que sea posible realizar cálculos con ellos. Luego, se filtra el DataFrame para mostrar solo aquellos tags que tienen más de 500 comentarios, y se ordena de mayor a menor por número de comentarios.

Por último, se agrega una nueva columna llamada "ganancia" al DataFrame utilizando la función comments_payouts y el método apply de pandas, y se imprime el resultado final.

Este código puede ser útil para aquellos que deseen conocer las ganancias asociadas con los tags más populares en la plataforma Hive y comparar la relación entre el número de comentarios y los pagos en HBD.
