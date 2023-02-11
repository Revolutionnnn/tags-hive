#Libreria HIVE
from beem.discussions import Query, Trending_tags
#Libreria Pandas para crear frame
import pandas as pd


def comments_payouts(row):
  """
  Calculo de ganancia en total pagado por TAG, y cantidad
  de comentarios para obtener un valor, mas acertado
  """
  resultado = float(row['total_payouts']) / float(row['top_posts'])
  return resultado


# Acceso a los TAGS
q = Query(limit=10, start_tag="hive")
# Con esta list agrego a una lista los TAGS para poder crear el FRAME
value = [i for i in Trending_tags(q)]
# Creo el frame para ordenarlas
df = pd.DataFrame(value)
# Reemplace HBD(Ya que es un texto) para poder utilizar los valores numericos
df['total_payouts'] = df['total_payouts'].str.replace(' HBD', '')
# Hice que me mostrara solo TAGS que tuvieran mas comentarios para tener TAGS
# con una buena participacion
df = df[df['comments'] > 500]
# Hice que me mostrara de mayor a menos los comentarios
df = df.sort_values(by='comments', ascending=False)
# Cree una nueva fila en la cual calcule el POST/PAGOS HBD = TAG GANANDOR
df['ganancia'] = df.apply(comments_payouts, axis=1)
# Imprimo todos los valores!! YEEE vamos a ver el resultado
print(df)
