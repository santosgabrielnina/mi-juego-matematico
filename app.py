import streamlit as st

st.set_page_config(page_title="Juego Matemático PA3", layout="centered")

# --- ESTILOS ---
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🧮 Quiz Matemático</h1>", unsafe_allow_html=True)

# --- INICIALIZACIÓN ---
if 'indice' not in st.session_state: st.session_state.indice = 0
if 'fallos' not in st.session_state: st.session_state.fallos = 0

preguntas = [
    {"p": "¿Cuál es el valor de x en: x/2 = 5?", "ops": ["2.5", "10", "7", "3"], "r": "10"},
    {"p": "Resuelve: x/3 + 1 = 4", "ops": ["9", "12", "1", "15"], "r": "9"},
    {"p": "Si 2x/5 = 4, ¿cuánto vale x?", "ops": ["8", "10", "20", "4"], "r": "10"}
]

# --- LÓGICA ---
vidas = 10 - st.session_state.fallos

if vidas <= 0:
    st.error("💀 ¡GAME OVER! Te quedaste sin vidas.")
    if st.button("REINTENTAR"):
        st.session_state.fallos = 0; st.session_state.indice = 0; st.rerun()
else:
    st.sidebar.metric("❤️❤️ Vidas", vidas)
    if st.session_state.indice < len(preguntas):
        actual = preguntas[st.session_state.indice]
        st.info(actual["p"])
        sel = st.radio("Elige tu respuesta:", actual["ops"], key=f"p{st.session_state.indice}")
        
        if st.button("Enviar Respuesta"):
            if sel == actual["r"]:
                st.success("¡CORRECTO! ⭐")
                st.session_state.indice += 1
                st.rerun()
            else:
                st.session_state.fallos += 1
                st.error("❌ Incorrecto, pierdes una vida.")
    else:
        st.balloons()
        st.success("🎊 ¡FELICIDADES! COMPLETASTE EL DESAFÍO.")
        if st.button("Jugar de nuevo"):
            st.session_state.fallos = 0; st.session_state.indice = 0; st.rerun()