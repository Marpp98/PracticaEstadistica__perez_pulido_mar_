import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind, chi2_contingency

def pintar_grafico_barras_uni(df,columnas,cols = 2):
    ''' Función que crea un grid para dibujar un gráfico de barras para cada una de las variables que se pasan.

      df: dataframe a analizar
      columnas: lista de columnas
      cols: número de columnas que quieres que aparezcan en el grid. Por defecto es dos.
      '''
    total = len(columnas)
    filas = (total + cols - 1) // cols

    fig, axes = plt.subplots(filas, cols, figsize=(6*cols, 5*filas))

    if filas * cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
    
    for i,col in enumerate(columnas):
        sns.countplot(data=df, x=col, hue = col, ax = axes[i])
        axes[i].set_title(f'Distribución de {col}')

    for j in range(total, len(axes)):
        axes[j].axis("off")

    plt.tight_layout(pad = 3)
    plt.show()

def boxplot_uni(df,columnas, cols = 3):
    ''' Función que crea un grid para dibujar el diagrama de caja de cada una de las variables que se pasan.
      
      df: dataframe a analizar.
      columnas: lista de columnas.
      cols: número de columnas que quieres que aparezcan en el grid. Por defecto es tres.
      '''

    total = len(columnas)
    filas = (total + cols - 1) // cols

    fig, axes = plt.subplots(filas, cols, figsize=(6*cols, 5*filas))

    if filas * cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i,col in enumerate(columnas):
        sns.boxplot(data=df, y=col, ax = axes[i])
        axes[i].set_title(f'Boxplot de {col}', fontsize = 16)
        axes[i].set_ylabel(col, fontsize = 12)
     
    for j in range(total, len(axes)):
        axes[j].axis("off")

    plt.tight_layout(pad = 3)
    plt.show()



def pintar_distrib_num_uni(df,columnas,cols = 3):
    ''' Función que crea un grid para dibujar el histograma de cada una de las variables que se pasan,
      ajustando los bins a la cantidad máxima de valores unicos de cada variable.
      
      df: dataframe a analizar
      columnas: lista de columnas
      cols: número de columnas que quieres que aparezcan en el grid. Por defecto es tres.
      '''
    
    total = len(columnas)
    filas = (total + cols - 1) // cols

    fig, axes = plt.subplots(filas, cols, figsize=(5*cols, 4*filas))

    if filas * cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i,col in enumerate(columnas):
        n_bins = df[col].nunique()
        sns.histplot(df[col], bins=n_bins, kde=True, ax = axes[i])
        axes[i].set_title(f'Distribución de {col}', fontsize = 16)
        axes[i].set_xlabel(col)
        axes[i].xaxis.set_major_locator(mtick.MaxNLocator(integer=True))


    for j in range(total, len(axes)):
        axes[j].axis("off")

    plt.tight_layout(pad = 3)
    plt.show()



def grafico_barras_categoricas_target(df,columnas,target,cols = 2):
    ''' Función que crea un grid para dibujar un grafico de barras agrupado por los grupos de otra variable.
      
      df: dataframe a analizar.
      columnas: lista de columnas.
      target: variable que divide la columna en base a grupos.
      cols: número de columnas que quieres que aparezcan en el grid. Por defecto es dos.
      '''

    total = len(columnas)
    filas = (total + cols - 1) // cols

    fig, axes = plt.subplots(filas, cols, figsize=(6*cols, 5*filas))

    if filas * cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i,col in enumerate(columnas):
        sns.countplot(data=df, x=target, hue=col, ax = axes[i])
        axes[i].set_title(f'Distribución de {target} según {col}', fontsize = 16)
        

    for j in range(total, len(axes)):
        axes[j].axis("off")

    plt.tight_layout(pad = 3)
    plt.show()




def boxplot_bivariante(df,target,columnas, cols = 3):
    ''' Función que crea un grid para dibujar el diagrama de caja de cada una de las variables que se pasan.
      
      df: dataframe a analizar.
      columnas: lista de columnas.
      target: variable que divide la columna en base a grupos.
      cols: número de columnas que quieres que aparezcan en el grid. Por defecto es tres.
      '''

    total = len(columnas)
    filas = (total + cols - 1) // cols

    fig, axes = plt.subplots(filas, cols, figsize=(6*cols, 5*filas))

    if filas * cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i,col in enumerate(columnas):
        sns.boxplot(data=df, x=target, y=col, hue= target, palette='tab10', ax = axes[i])
        axes[i].set_title(f'{col} según {target}', fontsize = 16)
        axes[i].set_xlabel(target)
        axes[i].set_ylabel(f'{col}')
     
    for j in range(total, len(axes)):
        axes[j].axis("off")

    plt.tight_layout(pad = 3)
    plt.show()

def obtener_p_value (df,target,valor1,valor2,columnas):
    for i in columnas:
        target_1 = df[df[target]==valor1][i]
        target_2 = df[df[target]==valor2][i]
        t, p = ttest_ind(target_1, target_2, nan_policy="omit")

        print(f'P-value de {i} = {p}')



def obtener_p_value (df,target,valor1,valor2,columnas):
    ''' Función que permite obtener el p-value de las variables numericas
    
    df: dataframe a analizar
    target: variable con la que se quiere analizar el resto
    valor1,valor2: valores de la columna target
    columnas: lista de columnas numéricas
    '''

    for i in columnas:
        target_1 = df[df[target]==valor1][i]
        target_2 = df[df[target]==valor2][i]
        t, p = ttest_ind(target_1, target_2, nan_policy="omit")

        print(f'P-value de {i} = {p}')


def calculo_tabla_contingencia_chi2(df,target,columnas):
    ''' Función que permite obtener el p-value de las variables categoricas.
    
    df: dataframe a analizar
    target: variable con la que se quiere analizar el resto
    columnas: lista de columnas categóricas
    '''

    for i in columnas:    
        tabla_contingencia = pd.crosstab(df[target], df[i])
        chi2, p_value, d, e = chi2_contingency(tabla_contingencia)

        print (tabla_contingencia)
        print(f'\nP-value de {i} = {p_value}')
        print (f'--------------------------')


def dibujar_medias_por_grupo(df, target,columnas,max_cols=3):
    '''Función que va creando grids en funcion de si las variables son de tiempo, cantidad o tamaño y representa sus valores medios segín grupos.
    df: dataframe que se quiere representar
    target: variable por la que se quieren agrupar las demás
    columnas: lista de variables que se quieren repreentar
    max_cols: maximo de columnas a representar. Por defecto es 3.
    '''
    grupos = {
        "Tiempo": ['time_spent_alone'],
        "Cantidad": ['social_event_attendance',
                    'going_outside',
                    'post_frequency'],
        "Tamaño": ['friends_circle_size']
    }
    
    for grupo, columnas in grupos.items():
        total = len(columnas)
        cols = min(total, max_cols)
        filas = (total + cols - 1) // cols

        fig, axes = plt.subplots(filas, cols, figsize=(5*cols, 4*filas))

        if filas * cols == 1:
            axes = [axes]
        else:
            axes = axes.flatten()

        for i, col in enumerate(columnas):
            sns.barplot(data=df, x=target, y=col, hue = target, ax=axes[i], dodge=False)
            axes[i].set_title(col)
            axes[i].set_xlabel(target)
            axes[i].set_ylabel("Media")

        for j in range(total, len(axes)):
            axes[j].axis("off")


        plt.tight_layout(pad=2)
        plt.suptitle(f"Variables de {grupo}", fontsize=18, y=1.02)
        plt.show()


def dibujar_pairplot(df,target,columnas):
        '''Función que dibuja un pairplot de las variables numericas respecto a una columna categorica.

        df: dataframe a analizar
        target: variable discriminatoria
        columnas: lista de columnas a dibujar
        '''
        grafico = sns.pairplot(df, hue=target, vars=columnas, palette="tab10")

        for ax in grafico.axes.flatten():
            if ax is not None:
                ax.xaxis.set_major_locator(mtick.MaxNLocator(integer=True, nbins = 3))
                ax.yaxis.set_major_locator(mtick.MaxNLocator(integer=True, nbins = 5))

        grafico.fig.tight_layout(pad=1)
        grafico.fig.subplots_adjust(right=0.95)

        grafico._legend.set_bbox_to_anchor((1.05, 0.5)) # x: derecha del grid, y: centro vertical
        grafico._legend.set_title(target)
        plt.show()