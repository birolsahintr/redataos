import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları (Geniş ekran modu)
st.set_page_config(layout="wide", page_title="ReData - Kurumsal Hafıza")

# 2. Streamlit'in kendi menülerini gizle (Sadece sizin tasarımınız görünsün)
st.markdown("""
    <style>
        /* Kenar boşluklarını sıfırla */
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
            height: 100vh;
        }
    </style>
""", unsafe_allow_html=True)

# 3. index.html dosyasını bul, oku ve çalıştır
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
        
    # Sitenizi ekrana basıyoruz (Yüksekliği 1000px veya daha fazla yapabilirsiniz)
    components.html(html_code, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("HATA: index.html dosyası bulunamadı! Lütfen GitHub'da app.py ile index.html'in yan yana olduğundan emin olun.")
