%%writefile spor_app.py
import streamlit as st
import pandas as pd

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Kişisel Gelişim Paneli", layout="wide")

# Ortak Stil (Koyu Tema)
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #dcdde1; }
    .stMarkdown h1 { color: #00f5d4; }
    .stMarkdown h2 { color: #00f5d4; border-bottom: 2px solid #00f5d4; }
    .program-box { background-color: #1e1e1e; padding: 15px; border-radius: 10px; border-left: 5px solid #6c5ce7; margin-bottom: 10px; }
    .machine-name { color: #a29bfe; font-weight: bold; }
    .dictionary-card { background-color: #1e1e1e; padding: 15px; border-radius: 12px; border-left: 4px solid #a29bfe; margin-bottom: 15px; }
    .muscle-tag { background-color: #4834d4; color: white; padding: 2px 8px; border-radius: 5px; font-size: 0.8em; margin-right: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- MENÜ FONKSİYONLARI ---

def show_spor_programi():
    st.title("🏋️ Spor Programı & Rehber")
    st.markdown("## AŞAMA 1: 0-1. HAFTA")
    st.markdown("<div class='program-box'>• 10 dk Dikey Bisiklet<br><span class='machine-name'>DİKEY BİSİKLET</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='program-box'>• Chest Press: 3x12<br><span class='machine-name'>GÖĞÜS BASKI MAKİNESİ</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='program-box'>• Lat Pulldown: 3x12<br><span class='machine-name'>İSTASYON MAKİNESİ (Üst Çekiş)</span></div>", unsafe_allow_html=True)
    
    st.markdown("## AŞAMA 2: 1-4. HAFTA")
    st.markdown("<div class='program-box'>• Lateral Raise: 3x15<br><span class='machine-name'>KABLOLU MAKARA (CABLE CROSSOVER)</span></div>", unsafe_allow_html=True)
    
    st.markdown("## AŞAMA 3: 4. HAFTA+")
    st.markdown("<div class='program-box'>• Rear Delt Fly: 3x12<br><span class='machine-name'>REAR DELT FLY MAKİNESİ</span></div>", unsafe_allow_html=True)

def show_beslenme():
    st.title("🥗 Beslenme Düzeni")
    st.info("Kilonun 2 katı protein (130g net) almayı hedefle!")
    tab1, tab2 = st.tabs(["1. Dönem (İlk 4 Hafta)", "2. Dönem (Hacim)"])
    with tab1:
        st.table(pd.DataFrame({"Öğün": ["Protein", "Karb"], "Spor": ["450g", "Yüksek"], "Dinlenme": ["350g", "Düşük"]}))
    with tab2:
        st.table(pd.DataFrame({"Öğün": ["Protein", "Karb"], "Spor": ["600g", "Çok Yüksek"], "Dinlenme": ["400g", "Düşük"]}))

def show_strateji():
    st.title("⚡ Spor Öncesi & Sonrası")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Öncesi (Enerji)")
        st.write("🍌 Muz + Fındık (D Vitamini emilimi için yağ şart!)")
    with col2:
        st.subheader("Sonrası (Onarım)")
        st.write("🍳 200g Köfte/Tavuk + Pirinç Pilavı")

def show_takip():
    st.title("📊 Gelişim Hedefleri")
    st.metric("Güncel Kilo", "66.5 kg", "Target: 70kg")
    st.metric("D Vitamini", "6.81 ng/mL", "Hedef: 30-50", delta_color="inverse")
    st.write("Omuz Hedefi: 112cm -> 120cm")

def show_sozluk():
    st.title("📖 Makine Sözlüğü")
    st.markdown("""
    <div class='dictionary-card'>
        <div class='machine-title'>SHOULDER PRESS</div>
        <span class='muscle-tag'>Omuz</span><div class='desc-text'>Skolyoz için dik oturarak yapılmalı.</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>ABS & LOWER BACK</div>
        <span class='muscle-tag'>Core</span><div class='desc-text'>Bel kaslarını güçlendirerek omurgayı destekler.</div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVİGASYON ---
st.sidebar.title("🧭 Menü")
choice = st.sidebar.radio("Gitmek istediğin yer:", ["Spor Programı", "Beslenme", "Öncesi/Sonrası", "Gelişim Takibi", "Makine Sözlüğü"])

if choice == "Spor Programı": show_spor_programi()
elif choice == "Beslenme": show_beslenme()
elif choice == "Öncesi/Sonrası": show_strateji()
elif choice == "Gelişim Takibi": show_takip()
else: show_sozluk()
