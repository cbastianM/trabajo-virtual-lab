import streamlit as st
import sympy as sp


x = sp.symbols("x")
M1 = sp.symbols("M1")
m1 = sp.symbols("m1")
M2 = sp.symbols("M2")
m2 = sp.symbols("m2")

menu = st.sidebar.radio(
    "Menú Principal",
    ["Nivel 1", "Nivel 2", "Nivel 3"]
)

if menu == "Nivel 1":

    

    st.title("Trabajo virtual. Nivel 1")
    st.header("Estructuras indeterminadas")
    st.write("Determinar la reacción en el apoyo B. EI constante")

    st.image("images/E1_ejemplo_2.1.png", caption="Ejemplo 1")

    # Input numérico con valor predeterminado (0) y rango de 0 a 100
    P = st.number_input(
        label="Ingresa el valor de la carga P:",
        min_value=0,
        max_value=100,
        value=50,  # Valor inicial predeterminado
        step=1     # Incremento/decremento en pasos de 1
    )

    d = st.number_input(
        label="Ingresa el valor de la distancia d:",
        min_value=0,
        max_value=100,
        value=6,  # Valor inicial predeterminado
        step=1    # Incremento/decremento en pasos de 1
    )

    st.write("Realice los corte empezando desde A ")

    col1, col2= st.columns(2)
    # Botón 1
    with col1:
        if st.button("M1"):
            st.write("Ecuación para el momento Real 1")
            MR1 = -P * (d-x)
            real1=sp.Eq(M1,MR1)
            st.latex(sp.latex(real1))

    # Botón 2
    with col1:
        if st.button("M2"):  # Botón destacado
            st.write("Ecuación para el momento Real 2")
            MR2 = 0
            real2=sp.Eq(M2,MR2)
            st.latex(sp.latex(real2))
    # Botón 3
    with col1:
        if st.button("m1"):
            st.write("Ecuación para el momento virtual 1")
            mv1 = 2*d-x
            virtual1=sp.Eq(m1,mv1)
            st.latex(sp.latex(virtual1))
    # Botón 4
    with col1:
        if st.button("m2"):
            st.write("Ecuación para el momento virtual 2")
            mv2 = d-x
            virtual2=sp.Eq(m2,mv2)
            st.latex(sp.latex(virtual2))
    # Botón 4
    with col2:
        if st.button("Reacción en B"):
            numerador = P * (2 * d**2 - 9 * d + 12)
            denominador = 5 * d**2 - 18 * d + 24
            resultado = numerador / denominador            
            st.success(f"La reacción en B es: {resultado} KN")

    with col2:
        st.link_button("Solución detallada", "https://www.canva.com/design/DAGtqo3Ii2Y/8ZUSHOSUqvFwtYvNST1-SA/edit?utm_content=DAGtqo3Ii2Y&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
