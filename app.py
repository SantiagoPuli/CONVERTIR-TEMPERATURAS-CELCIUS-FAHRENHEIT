import streamlit as st

def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """
    Convierte una temperatura de grados Fahrenheit a Celsius.
    """
    return (fahrenheit - 32) * 5/9

# Configuración de la página
st.set_page_config(
    page_title="Conversor de Temperaturas",
    page_icon="🌡️",
    layout="centered"
)

# Título y descripción
st.title("🌡️ Conversor de Temperaturas")
st.markdown("---")
st.write("Esta aplicación te permite convertir temperaturas entre Celsius y Fahrenheit de forma instantánea.")

# --- Controles de la Aplicación ---
# Selector de tipo de conversión
conversion_type = st.radio(
    "**Selecciona el tipo de conversión:**",
    ("Celsius a Fahrenheit", "Fahrenheit a Celsius"),
    key="conversion_selector"
)

st.markdown("---")

# Contenedor para la entrada y el resultado
input_col, result_col = st.columns(2)

with input_col:
    if conversion_type == "Celsius a Fahrenheit":
        st.subheader("De Celsius a Fahrenheit")
        # Campo de entrada para Celsius
        celsius_val = st.number_input(
            "Ingresa la temperatura en Celsius:",
            value=None,
            placeholder="Ej: 25.0",
            format="%.2f",
            key="celsius_input"
        )
        temp_input = celsius_val
        unit_from = "°C"
        unit_to = "°F"
    else:
        st.subheader("De Fahrenheit a Celsius")
        # Campo de entrada para Fahrenheit
        fahrenheit_val = st.number_input(
            "Ingresa la temperatura en Fahrenheit:",
            value=None,
            placeholder="Ej: 77.0",
            format="%.2f",
            key="fahrenheit_input"
        )
        temp_input = fahrenheit_val
        unit_from = "°F"
        unit_to = "°C"

with result_col:
    st.subheader("Resultado")
    if temp_input is not None:
        try:
            # Realiza la conversión según el tipo seleccionado
            if conversion_type == "Celsius a Fahrenheit":
                converted_temp = celsius_a_fahrenheit(temp_input)
            else:
                converted_temp = fahrenheit_a_celsius(temp_input)

            # Muestra el resultado
            st.success(f"**{temp_input:.2f}{unit_from}** es igual a **{converted_temp:.2f}{unit_to}**")
        except TypeError:
            st.warning("Por favor, ingresa un número válido para la conversión.")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
    else:
        st.info(f"Ingresa un valor en {unit_from} para ver el resultado en {unit_to}.")

st.markdown("---")

# --- Estilos Personalizados ---
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 2rem;
        max-width: 700px;
        margin: auto;
    }
    h1 {
        color: #0E1117;
        text-align: center;
        margin-bottom: 0.5em;
    }
    h2, h3 {
        color: #262730;
    }
    .stRadio > label {
        font-size: 1.1em;
        font-weight: bold;
        color: #262730;
    }
    .stNumberInput > label {
        font-size: 1em;
        font-weight: normal;
        color: #4B4B4B;
    }
    div[data-testid="stSuccess"] {
        background-color: #e6ffed;
        color: #1a5e2d;
        border-left: 5px solid #4CAF50;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        display: flex;
        align-items: center;
        min-height: 5em;
    }
    div[data-testid="stInfo"] {
        background-color: #e6f7ff;
        color: #09618d;
        border-left: 5px solid #2196F3;
        padding: 10px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        min-height: 5em;
    }
    div[data-testid="stWarning"] {
        background-color: #fff3e0;
        color: #9c5700;
        border-left: 5px solid #FF9800;
        padding: 10px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        min-height: 5em;
    }
</style>
""", unsafe_allow_html=True)

st.info("¡Gracias por usar el Conversor de Temperaturas!")
