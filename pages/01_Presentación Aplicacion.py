# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd 

tab1, tab2, tab3 =st.tabs(['Campo Eléctrico', 'Inducción magnética', 'Dificultades Específicas del Aprendizaje'])
with tab1:
    st.header("Campo Eléctrico: Un modelo a seguir")
    st.markdown("### Campo Eléctrico: Un modelo a seguir") 
    st.markdown ("## Introducción")
    st.write("Este proyecto intenta explicar y poner en evidencia los entretelones del tema Campo Eléctrico. El mismo fue seleccionado tomando como referencia los Diseños Curriculares para EETP de 4to año del Ciclo Superior de la Provincia de Santa Fe.")

    """
    **El curso seleccionado corresponde a una Escuela Técnica con modalidad en Industria de Procesos de 
    la Ciudad de Recreo, sita 20 km al norte de la Ciudad de Santa Fe; en cuanto a su población, 
    la misma proviene de diversos sectores socioeconómicos y de distintos lugares de la zona.**

    *Tomamos este curso, pues en él participa como docente, un colaborador y amigo, el cual gentilmente 
    se ha prestado para que su curso sea estudiado. De los diseños mencionados, tomamos el Eje
    relacionado con el campo electromagnético a fin de poder desarrollar el tema específico de 
    **Campo Eléctrico**.
    """
    video_magnetismo_campo = open('./video/magnetismo_campo.mp4', 'rb')
    video_bytes = video_magnetismo_campo.read()
    st.video(video_bytes)

    """
    *Surgen, entonces, los modelos que podemos utilizar a fin de contribuir a la abstracción por parte 
    de nuestros alumnos de los distintos fenómenos que analizamos para su estudio y comprensión. Como 
    plantea *Justi (2011) a fin de simplificar identidades complejas, ayudar a la comunicación de 
    ideas o ser un mediador entre la realidad que se toma como modelo y las teorías relacionadas 
    con ella, es que diseñamos el presente mapa conceptual definiendo los conceptos básicos que 
    intervienen dentro de los contenidos de Campo eléctrico, teniendo en cuenta la importancia del 
    lenguaje científico apropiado.*
    """

with tab2:
    st.title("Inducción magnética")
    st.markdown('La inducción magnética es el proceso mediante el cual campos magnéticos generan campos eléctricos. Al generarse un campo eléctrico en un material conductor, los portadores de carga se verán sometidos a una fuerza y se inducirá una corriente eléctrica en el conductor.')
    st.markdown('Cualquier dispositivo (batería, pila…) que mantiene la **diferencia de potencial** entre dos puntos en un circuito se llama'
        'fuente de alimentación.')
    
    
    video_file = open('./video/induccion-magnética.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

with tab3:
    
    """
    Resulta necesario hacer algunas adecuaciones en caso de contar con alumnos con Dificultades Específicas del Aprendizaje (DEA). Para realizar estas tareas se propone lo siguiente:
    * El uso de simuladores como herramienta alternativa a los textos
    * En caso de diseñar una actividad, dar ejemplos similares a la misma
    * Realizar trabajos cortos y significativos a partir de la información o aprendizaje adquirido con los simuladores
    * Explicación de la actividad mediante un mensaje de audio.
    """

    from PIL import Image 
    img = Image.open("./image/dificultades-específicas-del-aprendizaje.jpg") 
    st.image(img, width=700,)


    botondesarrllo =st.button('Contenidos a desarrollar')

    if botondesarrllo is True:
        st.write('Para un correcto desempeño tanto del alumno como del docente en el tema seleccionado, se elaboró el siguiente mapa.El mismo se utilizará como hoja de ruta. Del mismo modo se seleccionó como concepto estructurante a las INTERACCIONES, puesto que éstas nos permiten enlazar diferentes conceptos en una secuencia didáctica.')
