import pandas as pd
import numpy as np


def clasificador_variables(df,target):
    '''Función que clasifica las variables en numéricas, categóricas y la columna objetivo.

    df: dataframe del que queremos clasificar las columnas
    target: columna objetivo
    '''
    numericas = []
    categoricas = []
    for i in df.columns:
        if i == target:
            target = i    
        elif (df[i].dtype in ['int64', 'float64']) and (i!= target ):
            numericas.append(i)  
        elif (i not in numericas) and (i != target):
            categoricas.append(i)
            
    return target,numericas, categoricas


def contar_valores_categoricos(df,columnas):
    '''Función que realiza un conteo de los valores únicos de las variables categóricas incluyendo los nulos.

    df: dataframe del que queremos contar los valores únicos de las columnas
    columnas: lista de columnas
    '''
    for i in columnas:
        print(f'Columna {i}:')
        print(df[i].value_counts(dropna = False))
        print('\n')

def normalizar_columnas(df):
    '''Función que cambia los titulos de las columnas a minuscula, elimina los posibles espacios delante 
    o detras de ellos y lo pasa a snake_case.
    
    df: dataframe al que queremos modificar los títulos de las columnas.
    '''

    df.columns = df.columns.str.lower().str.strip()
    df.columns = df.columns.str.replace(' ','_')
    return df.columns

def normalizar_valores_categoricos (df,columnas):
    '''Función para normalizar los valores de las columnas categóricas. 
    Elimina los posibles espacios que existan antes y después de cada valor y lo pasa todo a minúscula.

    df: dataframe del que queremos normalizar los valores
    columnas: lista de columnas
    '''
    for i in columnas:
        df[i] = df[i].str.lower().str.strip()
    return df


def cambiar_tipos(df,categoricas,numericas):
    '''Función que cambia los tipos de las columnas que representan categorías por category 
    e int64 para las variables numericas discretas.

    df: dataframe del que queremos modificar los tipos
    categoricas: columnas categóricas que queremos cambiar el tipo
    numericas: columnas numéricas que queremos cambiar el tipo
    '''
    df[categoricas]= df[categoricas].astype('category')

    for i in numericas:
        df[i] = pd.to_numeric(df[i], errors = 'coerce').astype('Int64')

    return df.info()


def contar_nulos(df,columnas):
    ''' Función que obtiene los nulos de las columnas indicas.

    df: dataframe que queremos analizar.
    columnas: lista de columnas a analizar
    '''
    for i in columnas:
        nulos = df[i].isna().sum()
        print(f'Valores nulos de {i} = {nulos}')


def comparativa_media_mediana_moda(df,columnas,target):
    '''Función que permite obtener la media, la media y la moda agrupada por la columna de preferencia.
    df: dataframe del que queremos obtener los valoes estadísticos agrupados.
    columnas: lista de columnas.
    target: columna mediante la cual se hará la agrupación
    '''

    for i in columnas:
        print(f'Media de {i} según {target}:')
        print(df.groupby(target)[i].mean().round())
        print('\n')

        print(f'Mediana de {i} según {target}:')
        print(df.groupby(target)[i].agg(lambda x: x.median()))
        print('\n')
        
        print(f'Moda de {i} según {target}:')
        print(df.groupby(target)[i].agg(lambda x: x.mode()))
        print('\n---------------------------------------------------------\n')

def imputar_mediana_grupos(df,columnas,target):
    for i in columnas:
        df[i] = df.groupby(target)[i].transform(lambda x:x.fillna(x.median()))
    return df

def categorizar_estudios(titulo, masters,grados):
    
    if titulo in masters:
        return 'Master'
    elif titulo in grados:
        return 'Grados'
    elif titulo == 'Class 12':
        return 'Bachillerato'
    elif titulo == 'PhD':
        return 'Doctorado'
    else:
        return 'Otros'
    

def deteccion_outliers(df,columnas):
    ''' Función que calcula max., mín., Q1, Q3, IQR y los límites superiores e inferiores para detectar la existencia de outliers.
    df = dataframe sobre el que se va obtener los datos 
    columnas = listado de columnas sobre el cual se itera para detectar valores atípicos
    '''

    for i in columnas:
        maximo = np.nanmax(df[i])
        minimo = np.nanmin(df[i])
        Q1 = np.nanpercentile(df[i],25)
        Q3 = np.nanpercentile(df[i],75)
        IQR = Q3 - Q1
        low_outlier = Q1 - (1.5*IQR)
        high_outlier = Q3 + (1.5*IQR)

        if (low_outlier < minimo) and (high_outlier > maximo) :
            print(f'{i} no presenta outliers')

        elif (low_outlier < minimo) and (high_outlier < maximo):
            print(f'Outlier superior de {i} por encima de {high_outlier}')

        elif (low_outlier > minimo) and (high_outlier > maximo):
            print(f'Outlier inferior de {i} por debajo de {low_outlier}')
            
        else:
            print(f'Outlier inferior de {i} por debajo de {low_outlier}')
            print(f'Outlier superior de {i} por encima de {high_outlier}')
        
        print('-------------------------------------------')


print('Funciones ejecutadas correctamente')