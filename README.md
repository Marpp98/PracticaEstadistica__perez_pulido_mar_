# Proyecto de Estadística para Data Science
## 📈 Análisis estadístico de la depresión en la problación estadounidense desde 2007 hasta 2023

Este proyecto se centra en el análisis estadístico de las variables recogidas en diferentes datsets de Nhanes desde 2007 hasta 2023 para poder determinar el grado de depresión de una persona estadounidense.

### 📂 Estructura del Repositorio
```
/
├── data/                       # Datos originales y transformados
│   ├── 2007 - 2008             # Cada año contiene los archivos correspondientes a los siguientes
│   ├── 2009 - 2010             datasets: 
│   ├── 2011 - 2012             - Demográficos
│   ├── 2013 - 2014             - Salud Menal - depresión
│   ├── 2015 - 2016             - Activiad física
│   ├── 2017 - 2020             - Problemas de sueño
│   ├── 2021 - 2023
│   └── PracticaEstadistica_perez_pulido_mar_.ipynb
│
│
├── notebooks/                  # Notebooks de trabajo
│   ├── limpieza_datos.ipynb
│   └── PracticaEstadistica_perez_pulido_mar_.ipynb
│
├── src/                        # Funciones aplicadas en el proyecto
│   ├── __init__.py
│   ├── visualizaciones.py      # Funciones para análisis y gráficos
│   └── transformaciones.py     # Funciones de limpieza y transformación de datos
|
├── .gitignore                  # Archivo que indica que elementos debe ignorar Git
│
└── README.md                   # Documentación principal del repositorio      

```

### 🧩 Metodología
Se ha trabajado sobre los datos obtenidos de la web de [NHANES](https://wwwn.cdc.gov/nchs/nhanes/), en la cual se han seleccionado los periodos desde 2007 hasta 2023.
Para ello se han seleccionado los datasets correspondiendes a encuestas sobre:
- Demografía
- Actividad física
- Problemas de sueño
- Salud mental - depresión

El proyecto ha seguido los siguientes pasos para su desarrollo:
1. **Recopilación, limpieza y normalización**
2. **Análisis descriptivo**
3. **Inferencia y modelado(regresión lineal y logística)**
4. **Regresión Lineal "From Scratch" con datos simulados**
5. **Series temporales con datos simulados** 

### 📊 Conclusiones

### 🛠️ Tecnologías Utilizadas
- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit - learn
- Jupyter Notebook
