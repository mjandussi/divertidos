import streamlit as st
import datetime
import time
from num2words import num2words

# Configuração da página
st.set_page_config(page_title="Calculadora do Golpi", page_icon="🧮")

# CSS personalizado
st.markdown("""
    <style>
    .big-font { font-size:55px !important; font-weight: bold; color: #ff4b4b; text-align: center; }
    .blink { animation: blinker 0.5s linear infinite; color: #FFA500; font-size: 30px; text-align: center; font-weight: bold;}
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

st.title("🧮 Calculadora do Golpi")
st.info(f"📅 Data de hoje: {datetime.date.today().strftime('%d/%m/%Y')}")

st.write("---")

hoje = datetime.date.today()
col1, col2 = st.columns(2)

with col1:
    a = st.number_input("Digite o dia:", value=hoje.day)

with col2:
    b = st.number_input("Digite o mês:", value=hoje.month)

st.caption(f"Detecção automática: Dia {a} do mês {b}")

if st.button("CALCULAR RESULTADO"):
    resultado = a + b
    
    with st.spinner('Validando a matemática do golpe...'):
        time.sleep(2)

    # CORREÇÃO DA LÓGICA:
    # Agora verificamos se o dia digitado é 8, o mês é 1 E se hoje é realmente 08/01
    if a == 8 and b == 1 and hoje.day == 8 and hoje.month == 1:
        
        # 🔊 Gargalhada Automática
        #st.audio("https://www.myinstants.com/media/sounds/risada-do-bola.mp3", autoplay=True)
        
        # 🎉 Efeitos Visuais
        st.balloons()
        st.snow()
    
        resultado_extenso = num2words(resultado, lang='en').upper()
        
        st.success("🚨 Golpe de Mestre Detectado!")
        st.markdown('<p class="blink">KKKKKKKKKKKKKKKKK!!!! 🤣</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="big-font">{a} + {b} = {resultado_extenso}</p>', unsafe_allow_html=True)
        
    else:
        # Se for qualquer outra data ou qualquer outro número que não seja 8 e 1
        st.metric(label="Resultado Comum", value=resultado)
        st.warning("Matemática normal detectada. Sem graça!")
        st.write("Dica: O golpe só funciona se você somar o dia 8 com o mês 1 no dia de hoje!")

st.write("---")