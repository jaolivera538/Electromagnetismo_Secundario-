# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd
from matplotlib.patches import Circle
from streamlit_option_menu import option_menu


@st.cache(allow_output_mutation=True)
def campo_magnetico_e(q, r0, x, y) -> tuple:
    """Retorna el vector de campo eléctrico E=(Ex,Ey) de una carga q en r0"""
    den = np.hypot(x - r0[0], y - r0[1]) ** 3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den


@st.cache(allow_output_mutation=True)
def campo_magnetico_vector(n: int, axis_x: int, axis_y: int) -> dict:
    """Cálculo del campo electromagnetico según la cantidad de dipolos.

    Args:
        n (int): Número de cargas para definir el dipolo

    Returns:
        dict: x,y,charges,Ex,Ey
    """
    # # puntos de los ejes x e y.
    nx, ny = 128, 128
    x = np.linspace(-axis_x, axis_x, nx)
    y = np.linspace(-axis_y, axis_y, ny)
    X, Y = np.meshgrid(x, y)
    # # Crear un multipolo con nq cargas
    # count = número de q. En ese caso es 1 dipolo
    count = n
    nq = 2 ** int(count)
    charges = [
        (i % 2 * 2 - 1, (np.cos(2 * np.pi * i / nq), np.sin(2 * np.pi * i / nq)))
        for i in range(nq)
    ]
    # # Vector de campo eléctrico como componentes separados (Ex,Ey)
    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    for charge in charges:
        ex, ey = campo_magnetico_e(*charge, x=X, y=Y)
        Ex += ex
        Ey += ey
    return {"x": x, "y": y, "charges": charges, "Ex": Ex, "Ey": Ey}

#Menú


def main():
    st.write('# Campo magnético')
    """Generación de la webapp con streamlit"""
    # Definir título
    #st.title("**Campo magnético**")
    st.header("¿Qué es un campo magnético explicar?")
    st.markdown("Un campo magnético es un campo de fuerza creado como consecuencia del movimiento de cargas eléctricas (flujo de la electricidad)." 
    "La fuerza (intensidad o corriente) de un campo magnético se mide en Gauss (G) o Tesla (T). El flujo decrece con la distancia a la fuente que provoca el campo."
    " El fenómeno del magnetismo era conocido ya por los antiguos griegos desde hace más de 2000 años. Se observaba que ciertos minerales (imanes) podían atraer o"
     " repeler pequeños objetos de hierro."
    )
    # Entrada de datos en el sidebar.
    st.sidebar.header("**Entradas:**")
    # min: 1, max: 5, default: 1
    n = int(st.sidebar.slider("Selecionar el valor : ", 1, 10, 1))

    #st.write(f'El numero seleccionado de cambio de polo es:  {n}')
    # SelectBox en sidebar
    min_max_scale = int(
        st.sidebar.selectbox(f'Valor en el gráfico: min,max', list(range(11, 21)))
    )
    
    # Graficar usando matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # Se realiza el cálculod el vector de campo magnético.
    res = campo_magnetico_vector(n, min_max_scale, min_max_scale)
    
    # Muestra la cantidad de polos que se definen en la entrada de datos.
    st.header(f" Gráfico - {2*n} Polos")
    
    # Dibujar las líneas de flujo con mapa de colores y estilos apropiados.
    try:
        color = 2 * np.log(np.hypot(res["Ex"], res["Ey"]))
    except RuntimeWarning:
        color = 2

    ax.streamplot(
        res["x"],
        res["y"],
        res["Ex"],
        res["Ey"],
        color=color,
        linewidth=1,
        cmap=plt.cm.magma,
        density=2,
        arrowstyle="->",
        arrowsize=1.5,
    )

    # Agregar circulos para las cargas.
    charge_colors = {True: "#aa0000", False: "#0000aa"}
    #charge_colors = {True: "#063970", False: "#1F2CB3"}

    for q, pos in res["charges"]:
        ax.add_artist(Circle(pos, 0.05, color=charge_colors[q > 0]))
    
    # Graficar
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_xlim(-min_max_scale, min_max_scale)
    ax.set_ylim(-min_max_scale, min_max_scale)
    ax.set_aspect("equal")
    # plt.show()
    st.pyplot(fig)


if __name__ == "__main__":
    main()

