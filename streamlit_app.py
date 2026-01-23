import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="ReData",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. GÜÇLENDİRİLMİŞ CSS (Streamlit Cloud'a Özel)
st.markdown("""
    <style>
        /* 1. Ana kapsayıcı boşluklarını yok et */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            margin: 0px !important;
            max-width: 100% !important;
        }

        /* 2. Streamlit Cloud'un üstteki renkli şeridini (Decoration) gizle */
        [data-testid="stDecoration"] {
            display: none !important;
            height: 0px !important;
        }

        /* 3. Üst Menü (Hamburger ve Deploy butonları) */
        header { 
            visibility: hidden !important; 
            height: 0px !important;
        }
        #MainMenu { visibility: hidden !important; }
        [data-testid="stToolbar"] { display: none !important; }
        
        /* 4. Alt Bilgi (Footer) */
        footer { visibility: hidden !important; display: none !important; }
        
        /* 5. "Manage App" butonunu gizlemeye çalış (Bazen Streamlit bunu engeller) */
        .stDeployButton { display: none !important; }
        div[class*="stDeployButton"] { display: none !important; }
        
        /* 6. Uygulamanın arka planını temizle */
        .stApp {
            background-color: white !important; /* veya HTML'deki renginiz */
            margin-top: 0px !important;
        }

        /* 7. iframe ayarları */
        iframe {
            display: block !important;
            border: none !important;
            width: 100% !important;
            /* Yüksekliği biraz daha artırarak çift scroll'u engelle */
            height: 100vh !important; 
        }
    </style>
""", unsafe_allow_html=True)

# 3. HTML Yükleme
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Yükseklik değerini artırdık (1200 -> 1300)
    components.html(html_code, height=1300, scrolling=True)

except FileNotFoundError:
    st.error("index.html bulunamadı.")
