import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components  # HTML göstermek için gerekli modül

# 1. Sayfa Ayarları
st.set_page_config(page_title="Gayrimenkul Asistanı", layout="centered")

# --- MANTIK: GİRİŞ EKRANI MI, SOHBET EKRANI MI? ---
if "page" not in st.session_state:
    st.session_state.page = "landing"

# --- DURUM 1: LANDING PAGE (index.html Gösterimi) ---
if st.session_state.page == "landing":
    # index.html dosyasını okuyup ekrana basıyoruz
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html_code = f.read()
            
        # HTML'i ekrana bas (height değerini HTML'inizin uzunluğuna göre ayarlayın)
        components.html(html_code, height=600, scrolling=True)
        
        # Sohbet uygulamasına geçiş butonu
        # (Butonu ortalamak için kolon kullanıyoruz)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🤖 Asistanı Başlat", use_container_width=True):
                st.session_state.page = "chat"
                st.rerun() # Sayfayı yenileyip chat moduna geçirir
                
    except FileNotFoundError:
        st.error("index.html dosyası bulunamadı! Lütfen app.py ile aynı klasörde olduğundan emin olun.")

# --- DURUM 2: SOHBET UYGULAMASI (Sizin Kodunuz) ---
elif st.session_state.page == "chat":
    
    st.title("🏗️ Gayrimenkul Yönetim Asistanı")
    
    # Geri Dön Butonu (İsterseniz ekleyebilirsiniz)
    if st.button("⬅️ Ana Sayfaya Dön"):
        st.session_state.page = "landing"
        st.rerun()

    # --- API ve CHAT KODLARINIZ BURADAN DEVAM EDİYOR ---
    if "GOOGLE_API_KEY" not in st.secrets:
        st.error("Lütfen secrets.toml dosyasını kontrol edin.")
        st.stop()

    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)

    system_instruction = "Sen, bulut tabanlı bir Gayrimenkul Portföy yönetim modülüsün."
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_instruction)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["parts"][0])

    if prompt := st.chat_input("Sorunuzu girin..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "parts": [prompt]})

        try:
            with st.spinner("Düşünüyor..."):
                response = model.generate_content(st.session_state.messages)
                text_response = response.text
            
            st.chat_message("ai").markdown(text_response)
            st.session_state.messages.append({"role": "model", "parts": [text_response]})
        except Exception as e:
            st.error(f"Hata: {e}")
