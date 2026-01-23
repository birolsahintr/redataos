import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarı (Geniş Ekran)
st.set_page_config(layout="wide", page_title="ReData System")

# 2. Streamlit Çerçevelerini Gizle (Tam Ekran Görünüm İçin)
st.markdown("""
<style>
    .block-container {padding: 0 !important; margin: 0 !important;}
    header, footer, #MainMenu {visibility: hidden;}
    [data-testid="stToolbar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# 3. HTML Dosyasını Oku ve Web Sitesi Olarak Çalıştır
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # components.html KULLANILMALI (st.write DEĞİL!)
    # height=1000 ekran boyuna göre ayarlanabilir
    components.html(html_code, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("index.html bulunamadı!")
