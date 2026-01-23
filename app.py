import streamlit as st
import google.generativeai as genai

# 1. Sayfa Ayarları
st.set_page_config(page_title="Gayrimenkul Asistanı", layout="centered")
st.title("🏗️ Gayrimenkul Yönetim Asistanı")

# 2. API Anahtarı Kontrolü
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfen .streamlit/secrets.toml dosyasına GOOGLE_API_KEY ekleyin.")
    st.stop()

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# 3. Model Ayarları ve SİSTEM TALİMATI (En önemli kısım burası)
system_instruction = """
Sen, bulut tabanlı (Cloud-Native) bir Gayrimenkul Portföy ve Talep Yönetim Platformu'nun ana yönetim modülüsün. 
Cevapların profesyonel, sektöre hakim ve çözüm odaklı olmalı. 
Kullanıcıya gayrimenkul terimleriyle hitap et.
"""

# Modeli talimatla birlikte başlatıyoruz
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction=system_instruction
)

# 4. Sohbet Geçmişini Başlat
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Eski Mesajları Ekrana Yazdır
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # message["parts"] liste olduğu için ilk elemanı alıyoruz
        st.markdown(message["parts"][0])

# 6. Kullanıcıdan Girdi Al
if prompt := st.chat_input("Talep veya sorunuzu girin..."):
    # Kullanıcı mesajını ekrana bas
    st.chat_message("user").markdown(prompt)
    
    # Geçmişe ekle (API formatına uygun: parts bir liste olmalı)
    st.session_state.messages.append({"role": "user", "parts": [prompt]})

    # Cevap üret
    try:
        with st.spinner("Asistan düşünüyor..."):
            # Tüm geçmişi modele gönderiyoruz
            response = model.generate_content(st.session_state.messages)
            text_response = response.text
            
        # Cevabı ekrana bas
        st.chat_message("ai").markdown(text_response)
        
        # Asistan cevabını geçmişe ekle
        st.session_state.messages.append({"role": "model", "parts": [text_response]})
        
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
