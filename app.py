import streamlit as st
import pandas as pd
import streamlit as st

def spor_programi_menusu():
    # Sayfa Başlığı ve Stil Ayarları
    st.markdown("""
        <style>
        .main { background-color: #121212; }
        .stMarkdown h1 { color: #00f5d4; font-family: 'Segoe UI'; }
        .stMarkdown h2 { color: #00f5d4; border-bottom: 2px solid #00f5d4; padding-bottom: 5px; }
        .stMarkdown h3 { color: #a29bfe; margin-top: 20px; }
        .program-box {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #6c5ce7;
            margin-bottom: 10px;
            color: #dcdde1;
        }
        .machine-name { color: #a29bfe; font-weight: bold; font-size: 0.9em; }
        .warning-text { color: #ff7675; font-style: italic; font-size: 0.85em; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🏋️ Kişisel Spor Programım")
    
    # --- AŞAMA 1 ---
    st.markdown("## AŞAMA 1: 0-1. HAFTA (ADAPTASYON)")
    st.info("Amacı: Makinelerin çalışma prensibini öğrenmek ve kasları uyandırmak. (Haftada 2 Gün)")
    
    st.markdown("""
    <div class='program-box'>
        • 10 dk Dikey Bisiklet<br>
        <span class='machine-name'>DİKEY BİSİKLET</span>
    </div>
    <div class='program-box'>
        • Chest Press Machine: 3x12 (Hafif ağırlık)<br>
        <span class='machine-name'>GÖĞÜS BASKI MAKİNESİ (BENCH PRES MACHINE)</span>
    </div>
    <div class='program-box'>
        • Lat Pulldown: 3x12 (Geniş tutuş)<br>
        <span class='machine-name'>İSTASYON MAKİNESİ (STATION MACHINE) Üst Çekiş Barı</span>
    </div>
    <div class='program-box'>
        • Leg Extension: 3x15<br>
        <span class='machine-name'>BACAK BÜKME MAKİNELERİ (Yukarı İtiş)</span>
    </div>
    <div class='program-box'>
        • Shoulder Press Machine: 2x12 (Çok hafif, formu öğrenmek için)<br>
        <span class='machine-name'>OMUZ MAKİNESİ (SHOLDER PRES)</span>
    </div>
    <div class='program-box'>
        • Abs Machine: 2x15<br>
        <span class='machine-name'>KARIN BÜKME MAKİNESİ (ABS)</span>
    </div>
    """, unsafe_allow_html=True)

    # --- AŞAMA 2 ---
    st.markdown("## AŞAMA 2: 1-4. HAFTA (GÜÇLENME)")
    st.info("Amacı: Temel kas kütlesini artırmak ve omuzları genişletmeye başlamak. (Haftada 2 Gün)")
    
    st.markdown("""
    <div class='program-box'>
        • Isınma: 5 dk Uzay Bisikleti<br>
        <span class='machine-name'>UZAY BİSİKLET (ELİPTİK BİSİKLET)</span>
    </div>
    <div class='program-box'>
        • Chest Press Machine: 3x10 (Zorlayan ağırlık)<br>
        <span class='machine-name'>GÖĞÜS BASKI MAKİNESİ (BENCH PRES MACHINE)</span>
    </div>
    <div class='program-box'>
        • Lat Pulldown: 4x10<br>
        <span class='machine-name'>İSTASYON MAKİNESİ (STATION MACHINE) Üst Çekiş Barı</span>
    </div>
    <div class='program-box'>
        • Lateral Raise (Kablolu Makara): 3x15 (Omuz genişliği için en önemli hareket)<br>
        <span class='machine-name'>KABLOLU MAKARA MAKİNESİ (CABLE CROSSOVER)</span><br>
        <span class='warning-text'>(Tutamağı en alt seviyeye getirip yandan yukarı doğru açarak yapmalısın)</span>
    </div>
    <div class='program-box'>
        • Leg Press: 3x12<br>
        <span class='machine-name'>BACAK PRESİ VE OMUZ ÇÖKME MAKİNESİ (LEG PRES)</span>
    </div>
    <div class='program-box'>
        • Leg Curl: 3x12<br>
        <span class='machine-name'>BACAK BÜKME MAKİNELERİ (Geriye/Aşağı Büküş)</span>
    </div>
    <div class='program-box'>
        • Abs Machine: 3x20<br>
        <span class='machine-name'>KARIN BÜKME MAKİNESİ (ABS)</span>
    </div>
    """, unsafe_allow_html=True)

    # --- AŞAMA 3 ---
    st.markdown("## AŞAMA 3: 4. HAFTA SONRASI (HACİM)")
    st.warning("Amacı: Omuz-Bel oranını (V formunu) belirginleştirmek. (Haftada 3 Gün)")
    
    st.markdown("""
    <div class='program-box'>
        • Geniş Tutuş Lat Pulldown: 4x8-10 (Sırt genişliği için)<br>
        <span class='machine-name'>İSTASYON MAKİNESİ (STATION MACHINE) Üst Çekiş Barı</span>
    </div>
    <div class='program-box'>
        • Shoulder Press Machine: 3x10<br>
        <span class='machine-name'>OMUZ MAKİNESİ (SHOLDER PRES)</span><br>
        <span class='warning-text'>(Dik oturarak, belini makineye tam yaslayarak - Skolyoz Dostu Form)</span>
    </div>
    <div class='program-box'>
        • Crossover / Chest Press: 3x10-12<br>
        <span class='machine-name'>KABLOLU MAKARA MAKİNESİ (CABLE CROSSOVER) / GÖĞÜS BASKI MAKİNESİ</span>
    </div>
    <div class='program-box'>
        • Lateral Raise (Kablolu veya Makine): 4x12-15<br>
        <span class='machine-name'>KABLOLU MAKARA MAKİNESİ (CABLE CROSSOVER)</span>
    </div>
    <div class='program-box'>
        • Hack Squat veya Leg Press: 3x10<br>
        <span class='machine-name'>BACAK PRESİ VE OMUZ ÇÖKME MAKİNESİ (HACK SQUAT)</span>
    </div>
    <div class='program-box'>
        • Rear Delt Fly (Ters Kelebek): 3x12<br>
        <span class='machine-name'>GÖĞÜS VE OMUZ AÇIŞ MAKİNESİ (REAR DELT FLY)</span><br>
        <span class='warning-text'>(Kolları ters yöne, arkaya doğru açarak)</span>
    </div>
    <div class='program-box'>
        • Lower Back Machine: 3x12<br>
        <span class='machine-name'>KARIN BÜKME MAKİNESİ (LOWER BACK)</span><br>
        <span class='warning-text'>(Skolyoz desteği için düşük ağırlıkla)</span>
    </div>
    """, unsafe_allow_html=True)

# Menüyü çağırmak için:
spor_programi_menusu()
import streamlit as st
import pandas as pd

def beslenme_menusu():
    # Stil Tanımlamaları
    st.markdown("""
        <style>
        .stMarkdown h2 { color: #00f5d4; border-bottom: 2px solid #00f5d4; padding-bottom: 5px; }
        .info-card {
            background-color: #2d3436;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #00b894;
            margin: 10px 0px;
        }
        .highlight { color: #fab1a0; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🥗 Kişisel Beslenme Planım")

    # Genel Özet Kartı
    st.markdown(f"""
    <div class='info-card'>
        <strong>Özet Hesaplama:</strong> Günlük kilonun 2 katı kadar (<span class='highlight'>130g net protein</span>) almalısın. 
        Bu da günlük yaklaşık 450-600g pişmiş köfte veya et miktarına denk gelir.
    </div>
    """, unsafe_allow_html=True)

    # --- 1. DÖNEM ---
    st.markdown("## 1. DÖNEM: İlk 4 Hafta (Haftada 2 Gün)")
    st.caption("Amaç: Adaptasyon ve yağ kontrolü.")

    donem1_data = {
        "Besin Türü": ["Hayvansal Protein", "Karbonhidrat", "Sağlıklı Yağlar", "Lif / Sebze"],
        "Spor Günleri": ["400-450g (Öğün başı 130-150g)", "Yüksek (1-1.5 sb tahıl + Meyve)", "10-12 Zeytin + 1 yk Zeytinyağı", "Sınırsız yeşil sebze"],
        "Dinlenme Günleri": ["300-350g", "Düşük/Orta (Sadece öğle)", "5 Ceviz + 10 Zeytin", "Sınırsız yeşil sebze"]
    }
    st.table(pd.DataFrame(donem1_data))

    # --- 2. DÖNEM ---
    st.markdown("## 2. DÖNEM: 4. Hafta Sonrası (Haftada 3 Gün)")
    st.caption("Amaç: Kas kütlesi kazanımı (Hypertrophy).")

    donem2_data = {
        "Besin Türü": ["Hayvansal Protein", "Karbonhidrat", "Sağlıklı Yağlar", "Mikro Besinler"],
        "Spor Günleri (3 Gün)": ["500-600g (Öğün başı 180-200g)", "Çok Yüksek (3 öğün tahıl + Hızlı Karb)", "Yarım Avokado veya 1 avuç Kuruyemiş", "Takviye D Vitamini (Yağlı öğünle)"],
        "Dinlenme Günleri (4 Gün)": ["400g (Onarım için yüksek)", "Düşük (Sadece kahvaltı/öğle)", "5-6 Ceviz + 10 Zeytin", "D Vitamini + Magnezyum"]
    }
    st.table(pd.DataFrame(donem2_data))

    # Özel Notlar ve Tercihler
    with st.expander("⚠️ Önemli Beslenme Notlarım"):
        st.markdown(f"""
        * **Protein Tercihi:** Programında tavuk, kıyma veya kuşbaşı yerine tercih ettiğin **köfte** formunu kullanabilirsin.
        * **D Vitamini:** Seviyen düşük olduğu için (6.81 ng/mL), takviyeni mutlaka sağlıklı yağ içeren bir öğünle tüketmelisin.
        * **Karbonhidrat:** Spor yapılmayan akşamlar karbonhidrat tüketmemeye özen göster.
        """)

# Menüyü çalıştır
beslenme_menusu()
import streamlit as st

def spor_oncesi_sonrasi_menusu():
    # Stil Tanımlamaları
    st.markdown("""
        <style>
        .stMarkdown h2 { color: #00f5d4; border-bottom: 2px solid #00f5d4; padding-bottom: 5px; }
        .pre-sport-card {
            background-color: #2d3436;
            padding: 12px;
            border-radius: 8px;
            border-left: 5px solid #fdcb6e;
            margin-bottom: 10px;
        }
        .post-sport-card {
            background-color: #2d3436;
            padding: 12px;
            border-radius: 8px;
            border-left: 5px solid #0984e3;
            margin-bottom: 10px;
        }
        .card-title { color: #ffeaa7; font-weight: bold; margin-bottom: 5px; }
        .card-title-post { color: #74b9ff; font-weight: bold; margin-bottom: 5px; }
        .note-box {
            background-color: #1e1e1e;
            padding: 15px;
            border: 1px dashed #00f5d4;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("⚡ Antrenman Beslenme Stratejisi")

    # --- SPOR ÖNCESİ ---
    st.markdown("## 🕒 Spor Öncesi (60-90 Dakika Önce)")
    st.caption("Hedef: Yüksek enerji ve kas yıkımını önleme.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='pre-sport-card'>
            <div class='card-title'>🍌 Hızlı Enerji</div>
            1 muz + 1 avuç çiğ fındık/badem. (D Vitamini emilimi için yağlar kritik!)
        </div>
        <div class='pre-sport-card'>
            <div class='card-title'>🥣 Fitness Karışımı</div>
            Yoğurt + 3-4 yk yulaf ezmesi + Tarçın.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='pre-sport-card'>
            <div class='card-title'>🥪 Hafif Atıştırmalık</div>
            2 dilim tam buğday ekmeği + 1 tk fıstık ezmesi.
        </div>
        <div class='pre-sport-card'>
            <div class='card-title'>🍎 Pratik Seçenek</div>
            Yarım paket pirinç patlağı + 1 yeşil elma.
        </div>
        """, unsafe_allow_html=True)

    # --- SPOR SONRASI ---
    st.markdown("## 🔄 Spor Sonrası (30-120 Dakika İçinde)")
    st.caption("Hedef: Kas onarımı ve glikojen depolarını doldurma.")

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("""
        <div class='post-sport-card'>
            <div class='card-title-post'>🍳 Kıymalı Kombinasyon</div>
            100g kıyma + 2 yumurta + 1 dilim tam buğday ekmeği + Yeşillik.
        </div>
        <div class='post-sport-card'>
            <div class='card-title-post'>💨 Airfryer Pratik</div>
            200g Tavuk Göğsü (Airfryer'da) + 1 orta boy haşlanmış patates.
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class='post-sport-card'>
            <div class='card-title-post'>🍝 Proteinli Makarna</div>
            150g tavuk parçalı tam buğday makarnası + Domates sosu.
        </div>
        <div class='post-sport-card'>
            <div class='card-title-post'>🥪 Soğuk Sandviç</div>
            150g haşlanmış tavuk + Marul + Domates + Tam buğday ekmeği.
        </div>
        """, unsafe_allow_html=True)

    # --- STRATEJİK NOTLAR ---
    st.markdown("### 📝 Stratejik Notlar")
    st.markdown(f"""
    <div class='note-box'>
        💧 <b>Hidrasyon:</b> Skolyoz kaynaklı disk sağlığın ve kas hücrelerinin verimi için günlük <b>2.5 - 3 litre</b> su tüketimini ihmal etme.<br><br>
        ☀️ <b>D Vitamini:</b> Spor sonrası ana öğününde takviyeni almayı unutma; kas onarım hızını doğrudan etkileyecektir.
    </div>
    """, unsafe_allow_html=True)

# Menüyü çalıştır
spor_oncesi_sonrasi_menusu()
import streamlit as st
import pandas as pd

def fiziksel_takip_menusu():
    # Stil Tanımlamaları
    st.markdown("""
        <style>
        .stMarkdown h2 { color: #00f5d4; border-bottom: 2px solid #00f5d4; padding-bottom: 5px; }
        .target-card {
            background-color: #1e272e;
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #00f5d4;
            text-align: center;
            margin-bottom: 20px;
        }
        .metric-label { color: #dcdde1; font-size: 0.9em; }
        .metric-value { color: #00f5d4; font-size: 1.8em; font-weight: bold; }
        .v-shape { color: #a29bfe; font-weight: bold; font-size: 1.2em; }
        .vitamin-alert { color: #ff7675; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

    st.title("📊 Fiziksel Gelişim ve Hedef Paneli")

    # Üst Özet Kartları
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='target-card'><span class='metric-label'>Güncel Kilo</span><br><span class='metric-value'>66.5 kg</span></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='target-card'><span class='metric-label'>Hedef Kilo</span><br><span class='metric-value'>70 kg+</span></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='target-card'><span class='metric-label'>Hedef Oran</span><br><span class='v-shape'>\"V\" Formu</span></div>", unsafe_allow_html=True)

    # --- KARŞILAŞTIRMA TABLOSU ---
    st.markdown("## 📈 4 Aylık Değişim Projeksiyonu")
    
    data = {
        "Ölçüm / Değer": [
            "Kilo", 
            "Yağ Oranı", 
            "Omuz Çevresi", 
            "Bel Çevresi", 
            "Omuz-Bel Oranı", 
            "D Vitamini"
        ],
        "Bugünkü Durum (Tahmini)": [
            "66.5 kg", 
            "%20 - %23", 
            "108 - 112 cm", 
            "84 - 86 cm", 
            "Dar Omuz Algısı", 
            "6.81 ng/mL"
        ],
        "4 Ay Sonraki Hedef": [
            "69 - 71 kg", 
            "%16 - %18", 
            "116 - 120 cm", 
            "79 - 81 cm", 
            "V Formuna Yakın", 
            "30 - 50 ng/mL"
        ],
        "Değişimin Etkisi": [
            "Kas kütlesi kazanımı", 
            "Bel bölgesi incelirken kaslar belirginleşir", 
            "Lateral Raise ile omuz başları açılır", 
            "Karın kaslarının güçlenmesiyle bel daralır", 
            "İdeal oran olan 1.6'ya yaklaşma", 
            "Kas onarımı ve enerji tavan yapar"
        ]
    }
    
    df = pd.DataFrame(data)
    st.table(df)

    # --- ÖZEL NOTLAR ---
    st.markdown("### 💡 Gelişim Notları")
    st.info("""
    * **Omuz Odaklılık:** Dar omuz algısını kırmak için Lateral Raise hareketlerini en iyi formda yapmaya odaklanmalısın.
    * **Vitamin D Uyarısı:** Mevcut seviyen (6.81) oldukça düşük; hedeflenen 30-50 bandına çıkmak protein sentezini doğrudan hızlandıracaktır.
    * **Bel Ölçüsü:** Yağ yakımı ve karın egzersizleriyle belini 80 cm altına çekmek, omuzlarının olduğundan daha geniş görünmesini sağlayacaktır.
    """)

# Menüyü çalıştır
fiziksel_takip_menusu()
import streamlit as st

def makine_sozlugu_menusu():
    # Stil Tanımlamaları
    st.markdown("""
        <style>
        .stMarkdown h2 { color: #00f5d4; border-bottom: 2px solid #00f5d4; padding-bottom: 5px; }
        .dictionary-card {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 12px;
            border-left: 4px solid #a29bfe;
            margin-bottom: 15px;
        }
        .machine-title { color: #00f5d4; font-weight: bold; font-size: 1.1em; }
        .muscle-tag {
            background-color: #4834d4;
            color: white;
            padding: 2px 8px;
            border-radius: 5px;
            font-size: 0.8em;
            margin-right: 5px;
        }
        .desc-text { color: #dcdde1; font-size: 0.9em; margin-top: 5px; }
        </style>
    """, unsafe_allow_html=True)

    st.title("📖 Makine & Kas Grubu Sözlüğü")
    st.info("Bu bölüm, salondaki makinelerin hangi kaslarını hedeflediğini ve ne işe yaradığını anlamana yardımcı olur.")

    # --- KATEGORİ: KARDİYO ---
    st.markdown("## 🏃 Kardiyo ve Isınma")
    
    st.markdown("""
    <div class='dictionary-card'>
        <div class='machine-title'>DİKEY BİSİKLET</div>
        <span class='muscle-tag'>Alt Vücut</span><span class='muscle-tag'>Kardiyovasküler</span>
        <div class='desc-text'>Ön bacak (Quadriceps) ve kalça kaslarını düşük dirençle ısıtır, kalp ritmini artırır.</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>UZAY BİSİKLET (ELİPTİK BİSİKLET)</div>
        <span class='muscle-tag'>Tüm Vücut</span><span class='muscle-tag'>Eklem Dostu</span>
        <div class='desc-text'>Dizlere yük bindirmeden hem alt hem de üst vücudu koordine şekilde çalıştırır.</div>
    </div>
    """, unsafe_allow_html=True)

    # --- KATEGORİ: ÜST VÜCUT ---
    st.markdown("## 📐 Üst Vücut (Omuz, Göğüs, Sırt)")
    
    st.markdown("""
    <div class='dictionary-card'>
        <div class='machine-title'>OMUZ MAKİNESİ (SHOULDER PRESS)</div>
        <span class='muscle-tag'>Omuz (Deltoid)</span><span class='muscle-tag'>Triceps</span>
        <div class='desc-text'>Omuzun tamamını güçlendirir. Dik oturmak skolyoz güvenliği için şarttır.</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>KABLOLU MAKARA (CABLE CROSSOVER)</div>
        <span class='muscle-tag'>Yan Omuz</span><span class='muscle-tag'>Göğüs</span>
        <div class='desc-text'><b>Lateral Raise</b> yaparak omuzlarını yana doğru genişletmek için en önemli makinedir.</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>GÖĞÜS VE OMUZ AÇIŞ (REAR DELT FLY)</div>
        <span class='muscle-tag'>Arka Omuz</span><span class='muscle-tag'>Üst Sırt</span>
        <div class='desc-text'>Arka omuzları doldurarak duruşunu düzeltir ve omuz başlarını belirginleştirir.</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>GÖĞÜS BASKI (BENCH PRESS MACHINE)</div>
        <span class='muscle-tag'>Büyük Göğüs Kasları</span><span class='muscle-tag'>Ön Omuz</span>
        <div class='desc-text'>Göğüs hacmini artırır, serbest ağırlığa göre daha güvenli bir form sunar.</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>İSTASYON MAKİNESİ (LAT PULLDOWN)</div>
        <span class='muscle-tag'>Kanat (Lats)</span><span class='muscle-tag'>Biceps</span>
        <div class='desc-text'>Sırtı genişleterek belin daha ince, omuzların daha geniş görünmesini sağlar (V Formu).</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>SMITH MACHINE</div>
        <span class='muscle-tag'>Çok Amaçlı</span>
        <div class='desc-text'>Raylı sistemi sayesinde Squat veya Press hareketlerinde dengeyi sağlar.</div>
    </div>
    """, unsafe_allow_html=True)

    # --- KATEGORİ: ALT VÜCUT ---
    st.markdown("## 🦵 Alt Vücut (Bacak)")
    
    st.markdown("""
    <div class='dictionary-card'>
        <div class='machine-title'>BACAK BÜKME (EXTENSION & CURL)</div>
        <span class='muscle-tag'>Ön Bacak</span><span class='muscle-tag'>Arka Bacak</span>
        <div class='desc-text'>Diz eklemini stabilize eder; bacak kaslarının detaylarını belirginleştirir.</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>BACAK PRESİ VE HACK SQUAT</div>
        <span class='muscle-tag'>Kalça</span><span class='muscle-tag'>Tüm Bacak</span>
        <div class='desc-text'>Yüksek ağırlıklarla bacak kütlesi kazanmak için en temel güç makineleridir.</div>
    </div>
    <div class='dictionary-card'>
        <div class='machine-title'>ABDUCTOR VE ADDUCTOR</div>
        <span class='muscle-tag'>İç Bacak</span><span class='muscle-tag'>Dış Kalça</span>
        <div class='desc-text'>Bacakların sıkılaşmasını ve kalça stabilitesini (duruş desteği) sağlar.</div>
    </div>
    """, unsafe_allow_html=True)

    # --- KATEGORİ: CORE ---
    st.markdown("## 🛡️ Karın ve Bel (Core)")
    
    st.markdown("""
    <div class='dictionary-card'>
        <div class='machine-title'>ABS VE LOWER BACK MACHINE</div>
        <span class='muscle-tag'>Karın</span><span class='muscle-tag'>Bel (Erector Spinae)</span>
        <div class='desc-text'><b>Skolyoz için Kritik:</b> Bel kaslarını güçlendirerek omurgaya binen yükü azaltır.</div>
    </div>
    """, unsafe_allow_html=True)

# Menüyü çalıştır
makine_sozlugu_menusu()
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
