import pandas as pd

#cargar el archivo Excel
df = pd.read_excel('data3.xlsx')

#imprime las primeras 5 y ultimas 5 filas
#print(df)

# Coloca el maximo numero de filas
#pd.options.display.max_rows = 200

#imprimir todo la tabla
#print(df.iloc[:20, :30])

#imprimir y localizar la fila uno
print(df.loc[1])

#imprimir la fila uno, y dos
#print(df.loc[[0, 1]])

#calcular el patrimonio por declaracion ano empleado
