import streamlit as st
import datetime
import time
from num2words import num2words

# Configuração da página para ficar com uma cara profissional (ou não)
st.set_page_config(page_title="Calculadora do Golpi", page_icon="🧮")

# CSS personalizado para deixar o texto do resultado gigante
st.markdown("""
    <style>
    .big-font { font-size:50px !important; font-weight: bold; color: #ff4b4b; text-align: center; }
    .english-font { font-size:30px !important; color: #1c83e1; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧮 Calculadora do Golpi")
st.write("---")

# Sidebar com informações inúteis
with st.sidebar:
    st.info(f"📅 Data de hoje: {datetime.date.today().strftime('%d/%m/%Y')}")
    st.write("---")

# Falsos Inputs
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Digite o dia:", value=8)
with col2:
    b = st.number_input("Digite o mês:", value=1)

if st.button("CALCULAR RESULTADO"):
    hoje = datetime.date.today()
    resultado = a + b
    
    # Processamento
    with st.spinner('Calculando...'):
        time.sleep(3)

    # Lógica 
    if hoje.day == 8 and hoje.month == 1 and resultado == 9:
        # EFEITOS ESPECIAIS
        st.balloons()
        st.snow()
    
        resultado_extenso = num2words(resultado, lang='en').upper()
        st.success("🚨 Cálculo Realizado!")
        st.markdown(f'<p class="big-font">{a} + {b} = {resultado_extenso}</p>', unsafe_allow_html=True)
        
    else:
        # Resultado comum e "sem graça"
        st.metric(label="Resultado", value=resultado)
        st.write("Nada de especial por aqui hoje. Tente somar 8 + 1 no dia 08 de Janeiro!")

# Rodapé
st.write("---")
