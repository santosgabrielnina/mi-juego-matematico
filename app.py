import streamlit as st
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Math Master Elite", page_icon="🏆", layout="wide")

# 2. ESTILOS CSS PERSONALIZADOS
st.markdown("""
<style>
    /* Fondo con degradado naranja y textura de matemáticas */
    .stApp {
        background: 
            linear-gradient(135deg, rgba(255, 154, 68, 0.8) 0%, rgba(252, 255, 43, 0.8) 100%),
            url('https://www.transparenttextures.com/patterns/math.png');
        background-attachment: fixed;
        background-size: cover;
    }
    /* Caja de la pregunta azul oscuro */
    .caja-pregunta {
        background-color: #002244 !important;
        color: white !important;
        padding: 30px !important;
        border-radius: 20px !important;
        font-size: 35px !important;
        font-weight: bold !important;
        text-align: center !important;
        border: 4px solid white;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }
    /* Respuestas en cuadrícula */
    div.stRadio > div { 
        display: grid; 
        grid-template-columns: 1fr 1fr; 
        gap: 20px !important; 
    }
    /* Botones de respuesta blancos */
    div.stRadio > div > label {
        background-color: white !important;
        color: #333 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        border: 2px solid #ddd !important;
        box-shadow: 0px 5px 10px rgba(0,0,0,0.1) !important;
    }
    /* Botón Verificar Amarillo */
    .stButton>button {
        width: 100%;
        background-color: #ffcc00 !important;
        color: black !important;
        font-size: 1.8rem !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        border: 3px solid #333 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. ENLACE DE IMAGEN DEL PROFESOR (ESTABLE)
# Usamos un enlace de Google para asegurar que no se caiga
URL_PROFESOR = "https://fonts.gstatic.com/s/i/productlogos/googleg_standard/v9/64.png" # Icono temporal de prueba
# Reemplazo por el profesor 3D visualmente similar al que te gustó:
URL_PROFESOR_FINAL = "https://i.postimg.cc/85M6X8mG/profe.png"

# 4. FUNCIONES DE AUDIO
def musica_fondo():
    url = "https://www.mfiles.co.uk/mp3-downloads/beethoven-symphony5-1.mp3"
    st.components.v1.html(f'<audio src="{url}" autoplay loop id="bgm"></audio><script>document.getElementById("bgm").volume=0.3;</script>', height=0)

# 5. ESTADOS DEL JUEGO
if 'preguntas' not in st.session_state:
    st.session_state.preguntas = [
        {"p": "¿(18 - 12) ÷ 3?", "ops": ["2", "6", "14", "4"], "r": "2"},
        {"p": "¿x / 2 = 5, cuánto es x?", "ops": ["2.5", "10", "7", "5"], "r": "10"},
        {"p": "¿Raíz cuadrada de 144?", "ops": ["10", "11", "12", "14"], "r": "12"}
    ]
if 'indice' not in st.session_state: st.session_state.indice = 0
if 'vidas' not in st.session_state: st.session_state.vidas = 5
if 'jugando' not in st.session_state: st.session_state.jugando = False

# 6. LÓGICA DE PANTALLAS
if not st.session_state.jugando:
    # PANTALLA DE INICIO
    st.markdown("<br><h1 style='text-align:center; color:white; text-shadow: 3px 3px 6px #000; font-size:60px;'>MATH MASTER ELITE</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.image(URL_PROFESOR_FINAL, use_container_width=True)
        if st.button("🚀 EMPEZAR DESAFÍO"):
            st.session_state.jugando = True
            st.rerun()

elif st.session_state.vidas > 0 and st.session_state.indice < len(st.session_state.preguntas):
    # PANTALLA DE JUEGO
    musica_fondo()
    actual = st.session_state.preguntas[st.session_state.indice]
    st.sidebar.metric("❤️ VIDAS", st.session_state.vidas)
    
    col_juego, col_profe = st.columns([1.8, 1])
    
    with col_juego:
        st.markdown(f'<div class="caja-pregunta">{actual["p"]}</div>', unsafe_allow_html=True)
        sel = st.radio("Respuestas:", actual["ops"], key=f"r{st.session_state.indice}", label_visibility="collapsed")
        if st.button("VERIFICAR 🎯"):
            if sel == actual["r"]:
                st.balloons()
                st.session_state.indice += 1
            else:
                st.session_state.vidas -= 1
            st.rerun()

    with col_profe:
        # El profesor aparece aquí gigante al lado de la pregunta
        st.image(URL_PROFESOR_FINAL, width=450)

else:
    # FINAL DEL JUEGO
    st.markdown("<h1 style='text-align:center; color:white;'>¡FIN DEL JUEGO!</h1>", unsafe_allow_html=True)
    if st.button("REINTENTAR"):
        st.session_state.indice = 0; st.session_state.vidas = 5; st.session_state.jugando = False; st.rerun()
