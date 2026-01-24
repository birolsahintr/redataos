import streamlit as st
import google.generativeai as genai
import os

# Sayfa Başlığı
st.set_page_config(page_title="AI Asistanım")
st.title("🤖 AI Chatbot")

# API Anahtarını Al (Secrets kısmından)
# Önce environment variable kontrol et, yoksa streamlit secrets'a bak
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except:
        st.warning("Lütfen API anahtarınızı girin.")
        st.stop()

# Gemini Ayarları
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Sohbet Geçmişini Sakla
if "messages" not in st.session_state:
    st.session_state.messages = []

# Eski Mesajları Göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan Girdi Al
if prompt := st.chat_input("Bir şeyler yazın..."):
    # Kullanıcı mesajını ekle
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI Cevabını Üret
    try:
        response = model.generate_content(prompt)
        ai_msg = response.text
        
        # AI mesajını ekle
        with st.chat_message("assistant"):
            st.markdown(ai_msg)
        st.session_state.messages.append({"role": "assistant", "content": ai_msg})
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
