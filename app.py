import streamlit as st
import pandas as pd

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Yusuf Eren - Gelişim Paneli", layout="wide", initial_sidebar_state="expanded")

# --- ÖZEL STİL AYARLARI ---
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #dcdde1; }
    .stMarkdown h1 { color: #00f5d4; font-family: 'Segoe UI'; }
    .stMarkdown h2 { color: #00f5d4; border-bottom: 2px solid #00f5d4; padding-bottom: 5px; }
    .stMarkdown h3 { color: #a29bfe; margin-top: 20px; }
    .program-box {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #6c5ce7;
        margin-bottom: 10px;
    }
    .machine-name { color: #a29bfe; font-weight: bold; font-size: 0.9em; }
    .warning-text { color: #ff7675; font-style: italic; font-size: 0.85em; }
    .dictionary-card {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 12px;
        border-left: 4px solid #a29bfe;
        margin-bottom: 15px;
    }
    .muscle-tag {
        background-color: #4834d4;
        color: white;
        padding: 2px 8px;
        border-radius: 5px;
        font-size: 0.8em;
        margin-right: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- MENÜ FONKSİYONLARI ---

def show_spor_programi():
    st.title("🏋️ Spor Programı & Makine Rehberi")
    
    st.markdown("## AŞAMA 1: 0-1. HAFTA (ADAPTASYON)")
    st.info("Haftada 2 Gün - Makineleri öğrenme ve kasları uyandırma.")
    st.markdown("""
    <div class='program-box'>• 10 dk Dikey Bisiklet<br><span class='machine-name'>DİKEY BİSİKLET</span></div>
    <div class='program-box'>• Chest Press Machine: 3x12 (Hafif)<br><span class='machine-name'>GÖĞÜS BASKI MAKİNESİ (BENCH PRES MACHINE)</span></div>
    <div class='program-box'>• Lat Pulldown: 3x12 (Geniş tutuş)<br><span class='machine-name'>İSTASYON MAKİNESİ (Üst Çekiş Barı)</span></div>
    <div class='program-box'>• Leg Extension: 3x15<br><span class='machine-name'>BACAK BÜKME MAKİNELERİ (Yukarı İtiş)</span></div>
    """, unsafe_allow_html=True)

    st.markdown("## AŞAMA 2: 1-4. HAFTA (GÜÇLENME)")
    st.info("Haftada 2 Gün - Temel kas kütlesi ve omuz genişletme başlangıcı.")
    st.markdown("""
    <div class='program-box'>• Lateral Raise (Kablolu): 3x15 (Omuz genişliği için en önemli!) <br><span class='machine-name'>KABLOLU MAKARA MAKİNESİ (CABLE CROSSOVER)</span></div>
    <div class='program-box'>• Leg Press: 3x12<br><span class='machine-name'>BACAK PRESİ VE OMUZ ÇÖKME MAKİNESİ (LEG PRES)</span></div>
    """, unsafe_allow_html=True)

    st.markdown("## AŞAMA 3: 4. HAFTA+ (HACİM)")
    st.warning("Haftada 3 Gün - V-Formu (Omuz-Bel oranı) odaklı.")
    st.markdown("""
    <div class='program-box'>• Shoulder Press: 3x10<br><span class='machine-name'>OMUZ MAKİNESİ (SHOLDER PRES)</span><br><span class='warning-text'>(Skolyoz için dik otur, belini yasla!)</span></div>
    <div class='program-box'>• Rear Delt Fly (Ters Kelebek): 3x12<br><span class='machine-name'>GÖĞÜS VE OMUZ AÇIŞ MAKİNESİ (REAR DELT FLY)</span></div>
    <div class='program-box'>• Lower Back Machine: 3x12<br><span class='machine-name'>KARIN BÜKME MAKİNESİ (LOWER BACK)</span><br><span class='warning-text'>(Skolyoz desteği için düşük ağırlık)</span></div>
    """, unsafe_allow_html=True)

def show_beslenme():
    st.title("🥗 Detaylı Beslenme Planı")
    st.success("Günlük Hedef: ~130g Net Protein (Kilonun 2 katı)")
    
    st.markdown("### 1. DÖNEM: İlk 4 Hafta")
    d1 = {
        "Besin": ["Hayvansal Protein", "Karbonhidrat", "Sağlıklı Yağlar"],
        "Spor Günleri": ["400-450g (Öğün başı 150g)", "Yüksek (1.5 sb Tahıl + Meyve)", "10-12 Zeytin + 1yk Zeytinyağı"],
        "Dinlenme Günleri": ["300-350g", "Düşük (Sadece öğle)", "5 Ceviz + 10 Zeytin"]
    }
    st.table(pd.DataFrame(d1))

    st.markdown("### 2. DÖNEM: 4. Hafta Sonrası")
    d2 = {
        "Besin": ["Hayvansal Protein", "Karbonhidrat", "Mikro Besinler"],
        "Spor Günleri (3 Gün)": ["500-600g (Öğün başı 200g)", "Çok Yüksek (3 ana öğün tahıl)", "Takviye D Vitamini (Yağlı öğünle)"],
        "Dinlenme Günleri": ["400g (Onarım için)", "Düşük (Sadece kahvaltı/öğle)", "D Vitamini + Magnezyum"]
    }
    st.table(pd.DataFrame(d2))

def show_takip():
    st.title("📊 Fiziksel Hedefler ve Değerler")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Güncel D Vitamini", "6.81 ng/mL", delta="-23.19 (Kritik)")
        st.metric("Güncel Kilo", "66.5 kg", "Hedef: 70kg")
    with col2:
        st.write("**Omuz Çevresi Hedefi:** 112 cm ➔ 120 cm")
        st.write("**Bel Çevresi Hedefi:** 85 cm ➔ 80 cm")
    
    st.info("Omuz/Bel Oranı Hedefi: 1.6 (İdeal V Formu)")

def show_sozluk():
    st.title("📖 Makine & Kas Sözlüğü")
    st.markdown("""
    <div class='dictionary-card'><div class='machine-title'>DİKEY BİSİKLET</div><span class='muscle-tag'>Alt Vücut</span> Isınma ve kalp ritmi.</div>
    <div class='dictionary-card'><div class='machine-title'>CABLE CROSSOVER</div><span class='muscle-tag'>Omuz/Göğüs</span> Lateral Raise ile omuz genişletme.</div>
    <div class='dictionary-card'><div class='machine-title'>ABS & LOWER BACK</div><span class='muscle-tag'>Core</span> Skolyoz için bel kası güçlendirme.</div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("🧭 Menü")
choice = st.sidebar.radio("Sekme Seçin:", ["Spor Programı", "Beslenme", "Gelişim Takibi", "Makine Sözlüğü"])

if choice == "Spor Programı": show_spor_programi()
elif choice == "Beslenme": show_beslenme()
elif choice == "Gelişim Takibi": show_takip()
else: show_sozluk()
