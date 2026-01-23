import streamlit as st
import google.generativeai as genai

# ---------------------------------------------------------
# 1. SAYFA YAPILANDIRMASI (Site Başlığı ve İkonu)
# ---------------------------------------------------------
st.set_page_config(
    page_title="ReData - Kurumsal Hafıza",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. TASARIM VE CSS (Sizin HTML'deki Renkler)
# ---------------------------------------------------------
# Burası sitenizin "Sohbet Botu" gibi değil, profesyonel bir
# "Web Uygulaması" gibi görünmesini sağlar.
st.markdown("""
    <style>
        /* ReMax/ReData Renkleri */
        :root {
            --primary-blue: #0054A6;
            --primary-red: #E11B22;
        }
        
        /* Ana Başlık Stili */
        .main-header {
            color: var(--primary-blue);
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 0rem;
        }
        
        /* Alt Başlık */
        .sub-header {
            color: #64748b;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }

        /* Buton Stili */
        .stButton > button {
            background-color: var(--primary-red);
            color: white;
            border-radius: 8px;
            font-weight: bold;
            border: none;
            width: 100%;
            padding: 0.5rem 1rem;
        }
        .stButton > button:hover {
            background-color: #b91c1c;
            color: white;
        }
        
        /* Sidebar (Sol Menü) Rengi */
        [data-testid="stSidebar"] {
            background-color: #f8fafc;
            border-right: 1px solid #e2e8f0;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. API BAĞLANTISI (AI Studio Beyni)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("⚠️ API Anahtarı bulunamadı. Lütfen Streamlit ayarlarından secrets.toml dosyasını düzenleyin.")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Model Ayarları (AI Studio'daki ayarlarınız)
generation_config = {
    "temperature": 0.4, # Daha tutarlı, az yaratıcı (Kurumsal için uygun)
    "top_p": 0.95,
    "max_output_tokens": 8192,
}

# SİSTEM TALİMATI (Buraya AI Studio'daki talimatınızı yapıştırın)
system_instruction = """
Sen ReData isimli Kurumsal Gayrimenkul Hafıza Sistemisin.
Görevin: Kullanıcının girdiği gayrimenkul verilerini, tapu bilgilerini veya
notları analiz ederek profesyonel, maddeler halinde ve kurumsal bir dille raporlamaktır.
Asla sohbet etme, sadece analiz sonucunu ver.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction
)

# ---------------------------------------------------------
# 4. ARAYÜZ (UI) - GAYRİMENKUL ANALİZ FORMATI
# ---------------------------------------------------------

# Sol Menü
with st.sidebar:
    st.title("📂 ReData Menü")
    st.info("Kurumsal Hafıza Sistemi v1.0")
    st.markdown("---")
    secim = st.radio("İşlem Seçiniz:", ["Hızlı Analiz", "Tapu Sorgu", "Pazar Raporu"])
    st.markdown("---")
    st.caption("© 2024 ReData Technology")

# Ana Ekran
st.markdown('<h1 class="main-header">ReData Analiz Sistemi</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Akıllı veri yönetimi ve tapu analizi modülü.</p>', unsafe_allow_html=True)

# İki Kolonlu Yapı
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Veri Girişi")
    user_input = st.text_area(
        "Analiz edilecek metni, tapu bilgisini veya müşteri notunu buraya yapıştırın:",
        height=200,
        placeholder="Örn: İzmir Bergama 123 ada 4 parsel nolu tarla vasıflı taşınmaz..."
    )
    
    analyze_btn = st.button("🚀 SİSTEME İŞLE VE ANALİZ ET")

with col2:
    st.markdown("### ℹ️ Bilgi Paneli")
    st.info("""
    Bu modül **Gemini 1.5 Flash** altyapısını kullanır.
    
    * Hukuki metin analizi
    * Tapu veri ayrıştırma
    * Yatırım potansiyeli özeti
    """)

# ---------------------------------------------------------
# 5. SONUÇ ÜRETME (Output)
# ---------------------------------------------------------
if analyze_btn and user_input:
    with st.spinner("ReData yapay zekası verileri işliyor..."):
        try:
            # Modele tek seferlik istek atıyoruz (Chat değil, Prompt)
            response = model.generate_content(user_input)
            
            st.markdown("---")
            st.success("✅ Analiz Tamamlandı")
            
            # Sonucu şık bir kart içinde göster
            st.markdown(f"""
            <div style="background-color: #f1f5f9; padding: 20px; border-radius: 10px; border-left: 5px solid #0054A6;">
                {response.text}
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")

elif analyze_btn and not user_input:
    st.warning("Lütfen analiz edilecek bir veri giriniz.")
