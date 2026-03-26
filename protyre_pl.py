import streamlit as st
import segno
from io import BytesIO

# 1. Налаштування сторінки
st.set_page_config(page_title="WROCARS & ProTire", layout="centered", page_icon="🏎️")

# --- СТИЛІЗАЦІЯ WROCARS (Золото на темному фоні для акцентів) ---
st.markdown("""
    <style>
    .wrocars-card {
        background-color: #1a1a1a;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #d4af37; /* Золотистий колір як на лого */
        border-left: 10px solid #d4af37;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin: 20px 0;
        color: white;
    }
    .ad-title {
        color: #d4af37;
        font-size: 24px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }
    .ad-tagline {
        color: #ffffff;
        font-size: 14px;
        opacity: 0.8;
        margin-bottom: 15px;
    }
    /* Стилізація кнопок під бренд */
    div.stButton > button:first-child {
        background-color: #d4af37;
        color: black;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Словник перекладів
translations = {
    "PL": {
        "main_title": "WRO CARS: Twój ekspert oponiarski",
        "ad_title": "WRO CARS DETAILING",
        "ad_desc": "Profesjonalna pielęgnacja aut we Wrocławiu. Serwis opon, ceramika, detailing.",
        "map_btn": "📍 Nawiguj (Google Maps)",
        "call_btn": "📞 Zadzwoń: 577 511 068",
        "width": "Szerokość",
        "profile": "Profil",
        "rim": "Felga",
        "header_current": "⬅️ Aktualne opony",
        "header_new": "➡️ Nowe opony",
        "header_comparison": "Wyniki porównania",
        "diameter_current": "Ø Aktualny",
        "diameter_new": "Ø Nowy",
        "clearance": "Prześwit",
        "speed_header": "Wskaźniki prędkości (przy 100 km/h)",
        "speed_real": "Prędkość rzeczywista",
        "speed_diff": "Odchylenie",
        "unit_mm": "mm",
        "unit_kmh": "km/h",
        "footer": "WRO CARS Detailing — pasja do perfekcji."
    },
    "UA": {
        "main_title": "WRO CARS: Твій експерт з шин",
        "ad_title": "WRO CARS DETAILING",
        "ad_desc": "Професійний догляд за авто у Вроцлаві. Сервіс шин, кераміка, детейлінг.",
        "map_btn": "📍 Навігація (Google Maps)",
        "call_btn": "📞 Дзвоніть: 577 511 068",
        "width": "Ширина",
        "profile": "Профіль",
        "rim": "Диск",
        "header_current": "⬅️ Актуальні шини",
        "header_new": "➡️ Нові шини",
        "header_comparison": "Результати порівняння",
        "diameter_current": "Ø Поточний",
        "diameter_new": "Ø Новий",
        "clearance": "Кліренс",
        "speed_header": "Показники швидкості (при 100 км/год)",
        "speed_real": "Реальна швидкість",
        "speed_diff": "Відхилення",
        "unit_mm": "мм",
        "unit_kmh": "км/год",
        "footer": "WRO CARS Detailing — пасія до перфекції."
    }
}

# --- САЙДБАР ---
import os

with st.sidebar:
    # Точна назва вашого файлу з пробілом та розширенням .jpeg
    file_name = "logo Wrocars.jpeg"
    
    if os.path.exists(file_name):
        st.image(file_name, use_container_width=True)
    else:
        # Якщо файл все одно не бачить, виведемо список файлів для перевірки
        st.error(f"Файл '{file_name}' не знайдено")
        st.write("Доступні файли:", os.listdir("."))
    
    lang = st.selectbox("Language / Мова", ["UA", "PL"])
    t = translations[lang]
    
    st.divider()
    st.write("### 📲 Поділитися")
    url = "https://streamlit.app" 
    qr = segno.make(url)
    out = BytesIO()
    qr.save(out, kind='png', scale=10)
    st.image(out.getvalue(), caption="Scan & Calculate")

# --- ГОЛОВНИЙ ЕКРАН ---
st.title(t["main_title"])

# ЕКСКЛЮЗИВНИЙ РЕКЛАМНИЙ БЛОК WRO CARS
st.markdown(f"""
    <div class="wrocars-card">
        <div class="ad-title">{t['ad_title']}</div>
        <div class="ad-tagline">Wojkowice, Gmina Żórawina</div>
        <p>{t['ad_desc']}</p>
    </div>
    """, unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    # ТУТ МИ ВСТАВИЛИ ВАШІ КООРДИНАТИ (50.98578, 17.06936) ПРЯМО В ПОСИЛАННЯ:
    map_url = "https://www.google.com/maps/place/Wroc%C5%82awska+12A,+55-020+Wojkowice,+%D0%9F%D0%BE%D0%BB%D1%8C%D1%89%D0%B0/@50.9857661,17.0670902,710m/data=!3m2!1e3!4b1!4m6!3m5!1s0x470fdb230ca0ff11:0x39cf2f5d037e549c!8m2!3d50.9857628!4d17.0696651!16s%2Fg%2F11c2dkrbc4?authuser=0&entry=ttu&g_ep=EgoyMDI2MDMyMy4xIKXMDSoASAFQAw%3D%3D"
    
    # Тепер ця кнопка відкриє маршрут саме до вас
    st.link_button(t["map_btn"], map_url, use_container_width=True)
with c2:
    # Кнопка швидкого виклику
    st.link_button(t["call_btn"], "tel:577511068", use_container_width=True)

st.divider()

# --- КАЛЬКУЛЯТОР (Ваша логіка) ---
col1, col2 = st.columns(2)
with col1:
    st.subheader(t["header_current"])
    w1 = st.select_slider(f"{t['width']} (1)", options=list(range(135, 355, 5)), value=295, key="w1")
    p1 = st.select_slider(f"{t['profile']} (1)", options=list(range(20, 85, 5)), value=35, key="p1")
    r1 = st.number_input(f"{t['rim']} (1)", value=21, step=1)

with col2:
    st.subheader(t["header_new"])
    w2 = st.select_slider(f"{t['width']} (2)", options=list(range(135, 355, 5)), value=275, key="w2_new")
    p2 = st.select_slider(f"{t['profile']} (2)", options=list(range(20, 85, 5)), value=45, key="p2_new")
    # Тут має бути 4 пробіли від краю:
    r2 = st.number_input(f"{t['rim']} (2)", value=21, step=1, key="r2")

# Розрахунки
diam1 = (w1 * p1 / 100 * 2) + (r1 * 25.4)
diam2 = (w2 * p2 / 100 * 2) + (r2 * 25.4)
diff = diam2 - diam1
cl_change_mm = diff / 2

# Розрахунок швидкості
speed_real = (diam2 / diam1) * 100 if diam1 != 0 else 0
speed_diff = speed_real - 100

st.subheader(f"📊 {t['header_comparison']}:")
m_col1, m_col2, m_col3 = st.columns(3)

# В середині with — знову 4 пробіли:
# --- ВИВІД ОСНОВНИХ РЕЗУЛЬТАТІВ ---
with m_col1:
    st.metric(t["diameter_current"], f"{diam1:.1f} {t.get('unit_mm', 'мм')}")

with m_col2:
    st.metric(t["diameter_new"], f"{diam2:.1f} {t.get('unit_mm', 'мм')}", f"{diff:+.1f} {t.get('unit_mm', 'мм')}")

with m_col3:
    st.metric(t["clearance"], f"{cl_change_mm:+.1f} {t.get('unit_mm', 'мм')}")

# --- РОЗРАХУНОК ШВИДКОСТІ ---
speed_real = (diam2 / diam1) * 100 if diam1 != 0 else 0
speed_diff = speed_real - 100

# --- ВИВІД ПОКАЗНИКІВ ШВИДКОСТІ ---
st.markdown(f"### 🏎️ {t['speed_header']}") 
s_col1, s_col2 = st.columns(2)

with s_col1:
    st.metric(t["speed_real"], f"{speed_real:.1f} {t.get('unit_kmh', 'км/год')}")

with s_col2:
    st.metric(t["speed_diff"], f"{speed_diff:+.1f} {t.get('unit_kmh', 'км/год')}")

# --- ФУТЕР ---
st.markdown("---")
st.caption(f"© 2024 | {t['footer']}")






