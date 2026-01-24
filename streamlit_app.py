import streamlit as st
import google.generativeai as genai
import os

# ---------------------------------------------------------
# REDATA - GAYRİMENKUL UZMANI PERSONASI
# ---------------------------------------------------------
RE_DATA_TALIMATI = """
Sen 'ReData' isimli yapay zeka asistanısın. 
Senin görevin: Gayrimenkul ofisleri için akıllı veri yönetimi sağlamak, tapu analizi yapmak ve kurumsal hafıza desteği vermektir.
Mottorun: "Bilgiyi güce dönüştürün."

Davranış Kuralların:
1. Her zaman profesyonel, kurumsal ve analitik bir dille konuş.
2. Gayrimenkul ve tapu terimlerine (Ada, Pafta, Parsel, İntifa, İpotek, Şerh, Kat Mülkiyeti vb.) tam hakimiyetin var. Bu terimleri kullanıcıya basitçe açıkla.
3. Kullanıcı sana bir tapu metni veya karmaşık bir emlak durumu verirse, bunu maddeler halinde özetle ve riskleri belirt.
4. Emlak danışmanlarına yardımcı olmaya odaklan. Onlara veri odaklı stratejiler öner.
5. Cevaplarının uygun yerlerinde "ReData sistemleri analizi tamamladı" gibi kurumsal ifadeler kullanabilirsin.
6. Asla yasal veya finansal "kesin yatırım tavsiyesi" verme, sadece veriyi analiz et ve yol göster.
"""

# Sayfa Ayarları
SAYFA_BASLIGI = "ReData | Kurumsal Emlak Hafızası"
SAYFA_IKONU = "🏢"

# ---------------------------------------------------------

st.set_page_config(page_title=SAYFA_BASLIGI, page_icon=SAYFA_IKONU, layout="wide")

# Başlık ve Logo Alanı
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown(f"# {SAYFA_IKONU}")
with col2:
    st.title("ReData")
    st.caption("Gayrimenkul ofisleri için akıllı veri yönetimi ve tapu analizi.")

st.divider() # Çizgi çek

# API Anahtarı Kontrolü
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except:
        st.error("⚠️ Sistem Başlatılamadı: API Anahtarı eksik. Lütfen yapılandırmayı kontrol edin.")
        st.stop()

# Gemini Modelini ReData Kimliği ile Başlat
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.4, # Daha tutarlı ve ciddi cevaplar için düşük tuttum
    "top_p": 0.95,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    generation_config=generation_config,
    system_instruction=RE_DATA_TALIMATI
)

# Sohbet Geçmişi
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Açılış mesajı
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "ReData sistemlerine hoş geldiniz. Tapu analizi, veri yönetimi veya mevzuat hakkında size nasıl yardımcı olabilirim?"
    })

# Mesajları Ekrana Yaz
for message in st.session_state.messages:
    # İkonları role göre ayarla
    avatar = "🏢" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Kullanıcı Girişi
if prompt := st.chat_input("Tapu detaylarını veya sorunuzu buraya girin..."):
    # Kullanıcı mesajını ekle
    st.chat_message("user", avatar="👤").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # ReData Cevaplıyor...
    try:
        chat_history = []
        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                chat_history.append({"role": "model", "parts": [msg["content"]]})
            else:
                chat_history.append({"role": "user", "parts": [msg["content"]]})

        # Son mesaj hariç geçmişi yükle
        chat = model.start_chat(history=chat_history[:-1])
        
        with st.spinner('ReData veritabanı taranıyor ve analiz yapılıyor...'):
            response = chat.send_message(prompt)
            ai_response = response.text
        
        # Cevabı göster
        with st.chat_message("assistant", avatar="🏢"):
            st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
    except Exception as e:
        st.error(f"Sistem Hatası: {e}")
