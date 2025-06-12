import streamlit as st

st.title("🧮 Calculadora Simple")
st.write("¡Pon a prueba lo que has aprendido!")

while True:
    num1 = st.number_input("Introduce el primer número", value=0.0)
    num2 = st.number_input("Introduce el segundo número", value=0.0)
    
    operacion = st.selectbox(
        "Selecciona una operación:",
        ("Sumar", "Restar", "Multiplicar", "Dividir")
    )
    
    if st.button("Calcular"):
        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            if num2 != 0:
                resultado = num1 / num2
            else:
                st.error("No se puede dividir por cero")
                resultado = None
        
        if resultado is not None:
            st.success(f"Resultado: {resultado}")
    
    break
