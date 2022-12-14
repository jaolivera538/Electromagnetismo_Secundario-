import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import webbrowser as wb
import openpyxl as op
import io

tab1, tab2, tab3 = st.tabs(['Tabla Teórica', 'Actividad 1', 'Actividad 2'])
with tab1:
    
    """
        # Campo Eléctrico generado por una carga puntual           
        El *campo eléctrico* $ E $ creado por la carga puntual $ q $ en un punto cualquiera P se define como:
        $ E = \cfrac{k*q}{r^2} $
        
        donde $ q $ es la *carga creadora del campo* (carga fuente), $ k $ es la *constante*, $ r $ es la *distancia* desde la carga fuente al punto P.
        *El campo eléctrico* depende únicamente de la carga fuente (carga creadora del campo) y en el Sistema Internacional se mide en N/C o V/m.
        
        * $ E $ : Campo eléctrico 
        * $ q $ : Carga (en $ \C (coulombios) $)
        * $ r $ : Distancia desde la carga eléctrica al punto (en $ \m (metros) $)
        * $ k $ : Constante eléctrostática del medio (su valor es $ \ 9*10^{9} N*m^2*C^{-2} $)
        
    """
    st.write('## Tabla Ejemplo')
    """
        En ésta tabla se muestra la relación entre la *intensidad del Campo Eléctrico*, la *intensidad de la carga eléctrica* y la *distancia*, respectivamente. Notesé que cuando una de las varibles cambia, la otra se mantiene constante; y vice versa.
    """
    q1 = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    r = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    q1_fija = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    r_fija = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    datos_tabla = {'Carga (nC)': q1, 'Distancia (cm)': r, 'Carga fija (nC)': q1_fija, 'Distancia fija (cm)': r_fija}
    df = pd.DataFrame(data=datos_tabla)

    ruta_archivo = "C:\\Users\\MANUEL\\Desktop\\Python\\tabla1.xlsx"
    df.to_excel(ruta_archivo) 
    
    df['Campo Eléctrico q fija'] = ((df['Carga fija (nC)'] * 10 **(-9) * 9 * 10 **9)/(((df['Distancia (cm)']) *10 **(-2)) **2)) 
    print(df)

    df['Campo Eléctrico r fija'] = ((df['Carga (nC)'] * 10 **(-9) * 9 * 10 **9)/(((df['Distancia fija (cm)']) *10 **(-2)) **2)) 
    print(df)

    st.table(df)
    st.write('### Variación del *Campo Eléctrico* vs. *Distancia*')
    st.line_chart(data=df, x='Distancia (cm)', y='Campo Eléctrico q fija')
    st.write('### Variación del *Campo Eléctrico* vs. *Carga*')
    st.line_chart(data=df, x='Carga (nC)', y='Campo Eléctrico r fija')
    
    
    
    
with tab2:
    """
    # Actividad 1
    ## Tomando como punto de partida el *ejemplo* del dibujo:
    1. Intentá reproducirlo con el simulador PhET
    """
    url = 'https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_es.html'

    if st.button('Usar PhET de Campo Eléctrico'):
        wb.open_new_tab(url)

    """
    2. Seleccioná una carga positiva de 1nC.
    3. Seleccioná una segunda carga negativa de 1nC.
    4. Seleccioná el ítem Campo Eléctrico.
    5. Medí la distancia entre ambas cargas con la cinta métrica.
    6. Medí la intensidad del Campo con el Voltímetro.
    7. Utilizando la Grilla Cuadriculada, medí el módulo de los vectores.
    8. Calculá el Campo Eléctrico usando la Ecuación a continuación. 
    """
    st.image('./image/ejemplo2.png')

    """
    $ E = \cfrac{k*q}{r^2} $
    * $ E $ : Campo eléctrico 
    * $ q $ : Carga (en $ \C (coulombios) $)
    * $ r $ : Distancia desde la carga eléctrica al punto (en $ \m (metros) $)
    * $ k $ : Constante eléctrostática del medio (su valor es $ \ 9*10^{9} N*m^2*C^{-2} $)
    """
    
with tab3:
    """
    # Actividad 2
    ## ¡Hacelo vos mismo!:
    ### Ahora que aprendiste como varían el valor de la carga y la distancia con respecto al campo eléctrico, te invitamos a que lo pruebes.
    1. Ingresá al valor de carga con con el botón *CARGA*.
    2. Observá como varía el campo Eléctrico en el gráfico punteado ROJO.
    3. Ingresá al valor de distancia con con el botón *DISTANCIA*.
    4. Observá como varía el campo Eléctrico en el gráfico punteado AZUL.
    """
           
    col1, col2 = st.columns(2)

    with col1:

        carga = st.number_input('CARGA (nC)', 0, 10, 5, 1)
        st.write(f'El valor ingresado es {carga}')

    with col2: 
        distancia = st.number_input('DISTANCIA (m)', 0, 20, 10, 1)
        st.write(f'El valor ingresado es {distancia}')
       
    carga_1 = linspace(0.0, 20.0, 100)
    distancia_1 = linspace(0.0, 20.0, 100)
    
    campo_eléctrico   = carga * 10** (-9) * 9 * 10 **(9) / ((distancia_1) ** (2))
    f = plt.figure()
    plt.plot(carga_1 , campo_eléctrico , lw=2, ls='--', c='r')
    f
  
    campo_eléctrico2   = carga_1 * 10** (-9) * 9 * 10 **(9) / ((distancia) ** (2))
    g = plt.figure()
    plt.plot(distancia_1 , campo_eléctrico2 , lw=2, ls='-.', c='b')
    g

    """ 
    5. Descargá la *TABLA DE EXCEL* desde el botón a continuación.
    """
    Q = np.array([3e-4, 5e-5, 3e-6])  # Carga puntual (Coulomb)
    r_1 = np.array([0.1, 0.02, 0.001])  # Distancias de separación entre cargas (metros)
    k = 9e9  # Constante de la Ley de Coulomb
    E = [f'=B{fila}*9e9/C{fila}^2' for fila in range(2, 2 + len(Q))]  
    
    datos_tabla = {'Carga 1 [C]': Q, 'Separación [m]': r_1, 'Campo Eléctrico [N/C]': E}
    tabla = pd.DataFrame(data=datos_tabla)

    contenido_archivo = io.BytesIO()  # Variable en memoria RAM para almacenar el contenido del Excel
    tabla.to_excel(contenido_archivo)  # Vuelco la tabla a la variable anterior

    # Botón de descarga para lo almacenado en la variable 'contenido_archivo':
    st.download_button('⬇ Descargar tabla', data=contenido_archivo, file_name='Electrostática.xlsx')

    """
    6. Usando el Simulador de PHeT, tomá valores y guardalos en las celdas de la tabla de excel.
    7. Usando la tabla de excel realizá los cálculos y los gráficos. En el caso en que no sepas hacer un gráfico con excel, acá te dejo un tutorial. 
    """   
    url = 'https://www.youtube.com/watch?v=FCj2YworGFg'
    if st.button('Crear gráficos de línea en Excel'):
        wb.open_new_tab(url)
