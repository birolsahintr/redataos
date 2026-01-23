import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları (Geniş Mod)
st.set_page_config(
    page_title="ReData - Kurumsal Hafıza",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit Arayüzünü Tamamen Gizleme (CSS Hack)
# Bu kod üstteki boşluğu, menüyü ve footer'ı yok eder.
st.markdown("""
    <style>
        /* Ana kapsayıcıdaki boşlukları kaldır */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        /* Streamlit elementlerini gizle */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stToolbar"] {display: none;}
        
        /* İframe'i tam ekran yap */
        iframe {
            display: block;
            border: none;
            width: 100%;
            height: 100vh; /* Ekran yüksekliği kadar */
        }
    </style>
""", unsafe_allow_html=True)

# 3. HTML Dosyasını Oku ve Bas
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
        
    # Yüksekliği ekran boyuna (viewport height) eşitliyoruz
    components.html(html_code, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("HATA: index.html dosyası app.py ile aynı klasörde bulunamadı.")
