import streamlit as st
import streamlit.components.v1 as components

# 1. SAYFA AYARLARI
# 'layout="wide"' sitenin sağa sola yayılmasını sağlar.
# 'initial_sidebar_state="collapsed"' Streamlit'in sol menüsünü kapatır.
st.set_page_config(
    page_title="ReData - Kurumsal Hafıza",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS HACK (Tasarım Bozukluğunu Gideren Kısım)
# Bu kod Streamlit'in üst, alt ve yan boşluklarını tamamen siler.
st.markdown("""
    <style>
        /* Ana içerik kapsayıcısının boşluklarını sıfırla */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            margin: 0px !important;
            max-width: 100% !important;
        }
        
        /* Streamlit'in üst menüsünü (Hamburger menü) gizle */
        #MainMenu { visibility: hidden; }
        header { visibility: hidden; }
        
        /* Alt bilgiyi (Footer) gizle */
        footer { visibility: hidden; }
        
        /* "Deploy" butonunu gizle */
        .stDeployButton { display: none; }
        
        /* iframe'in etrafındaki border'ı kaldır */
        iframe {
            border: none !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. HTML DOSYASINI OKU VE YÜKLE
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # height=1200: Sitenin dikey boyutu. 
    # Eğer sayfanızda scroll (kaydırma) çıkıyorsa bu sayıyı artırın (örn: 1500).
    components.html(html_code, height=1200, scrolling=True)

except FileNotFoundError:
    # Dosya bulunamazsa hata yerine bilgi verelim
    st.error("⚠️ 'index.html' dosyası bulunamadı. Lütfen GitHub'a app.py ile aynı yere yüklediğinizden emin olun.")
