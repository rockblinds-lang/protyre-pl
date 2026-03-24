import streamlit as st
import segno
from io import BytesIO

# 1. Налаштування сторінки
st.set_page_config(page_title="Wrocars & ProTire", layout="centered", page_icon="🚗")

# --- СТИЛІЗАЦІЯ WROCARS ---
st.markdown("""
    <style>
    .wrocars-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        border-left: 8px solid #0056b3; /* Синій акцент Wrocars */
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    .ad-title {
        color: #1f1f1f;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .ad-tagline {
        color: #0056b3;
        font-weight: 600;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Словник перекладів (додано рекламні тексти)
translations = {
    "UA": {
        "main_title": "Wrocars & ProTire: Твій шинний експерт",
        "sub_title": "Аналізуйте параметри коліс перед купівлею шин!",
        "ad_title": "WROCARS — Твій професійний деталінг",
        "ad_desc": "Догляд за авто, шиномонтаж та сервіс найвищого рівня у Вроцлаві.",
        "map_btn": "📍 Навігація до сервісу",
        "site_btn": "🌐 Наш Facebook",
        "header_current": "⬅️ Поточні шини",
        "header_new": "➡️ Нові шини",
        "header_comparison": "Результати порівняння",
        "width": "Ширина", "profile": "Профіль", "rim": "Діаметр",
        "label_diam1": "Діаметр 1", "label_diam2": "Діаметр 2",
        "label_clearance": "Кліренс", "label_speed": "Швидкість",
        "speedo_ok": "Похибка в нормі ({err:.1f}%)",
        "speedo_too_much": "Велика похибка! ({err:.1f}%)",
        "clearance_check": "Кліренс зміниться на {cm:.1f} см!",
        "special_offer": "ПРОПОЗИЦІЯ ВІД WROCARS",
        "footer": "Wrocars — якість, перевірена часом."
    },
    "PL": {
        "main_title": "Wrocars & ProTire: Ekspert oponiarski",
        "sub_title": "Sprawdź parametry kół przed zakupem opon!",
        "ad_title": "WROCARS — Twój detailing",
        "ad_desc": "Profesjonalna pielęgnacja, serwis opon i obsługa we Wrocławiu.",
        "map_btn": "📍 Nawiguj do serwisu",
        "site_btn": "🌐 Nasz Facebook",
        "header_current": "⬅️ Aktualne opony",
        "header_new": "➡️ Nowe opony",
        "header_comparison": "Wyniki porównania",
        "width": "Szerokość", "profile": "Profil", "rim": "Felga",
        "label_diam1": "Średnica 1", "label_diam2": "Średnica 2",
        "label_clearance": "Prześwit", "label_speed": "Prędkość",
        "speedo_ok": "Błąd w normie ({err:.1f}%)",
        "speedo_too_much": "Duży błąd! ({err:.1f}%)",
        "clearance_check": "Prześwit zmieni się o {cm:.1f} cm!",
        "special_offer": "OFERTA WROCARS",
        "footer": "Wrocars — jakość, której możesz ufać."
    },
    "EN": {
        "main_title": "Wrocars & ProTire Expert",
        "sub_title": "Check tire fitment before you buy!",
        "ad_title": "WROCARS — Your Detailing",
        "ad_desc": "Professional car care and tire service in Wroclaw.",
        "map_btn": "📍 Open in Google Maps",
        "site_btn": "🌐 Our Facebook",
        "header_current": "⬅️ Current tires",
        "header_new": "➡️ New tires",
        "header_comparison": "Comparison results",
        "width": "Width", "profile": "Profile", "rim": "Rim",
        "label_diam1": "Diameter 1", "label_diam2": "Diameter 2",
        "label_clearance": "Clearance", "label_speed": "Speed",
        "speedo_ok": "Error is OK ({err:.1f}%)",
        "speedo_too_much": "High error! ({err:.1f}%)",
        "clearance_check": "Clearance change: {cm:.1f} cm!",
        "special_offer": "WROCARS SPECIAL OFFER",
        "footer": "Wrocars — quality you can trust."
    }
}

# --- САЙДБАР ---
with st.sidebar:
    # ЛОГОТИП WROCARS (якщо файл в папці з кодом - "logo.png")
    # Зараз я підставив тимчасове посилання, замініть на реальне
    st.image("https://placeholder.com", use_container_width=True)
    
    lang = st.selectbox("Language / Мова", ["UA", "PL", "EN"])
    t = translations[lang]
    
    st.divider()
    st.write("### 📲 Поділитися")
    url = "https://protyre-pl.streamlit.app" 
    qr = segno.make(url)
    out = BytesIO()
    qr.save(out, kind='png', scale=10)
    st.image(out.getvalue(), caption="Scan to use on mobile")

# --- ГОЛОВНИЙ ЕКРАН ---
st.title(t["main_title"])

# РЕКЛАМНИЙ БЛОК WROCARS
st.markdown(f"""
    <div class="wrocars-card">
        <div class="ad-title">{t['ad_title']}</div>
        <div class="ad-tagline">Wroclaw-Wojkowice-Wrocars (WWW)</div>
        <p style='color: #444;'>{t['ad_desc']}<br><b>📞 Tel: 577 511 068</b></p>
    </div>
    """, unsafe_allow_html=True)

# Кнопки під рекламою
c1, c2 = st.columns(2)
with c1:
    # ЗАМІНІТЬ ПОСИЛАННЯ НА ВАШУ ЛОКАЦІЮ
    st.link_button(t["map_btn"], "https://google.com", use_container_width=True)
with c2:
    st.link_button(t["site_btn"], "https://www.facebook.com/zadorizhnyy/", use_container_width=True)

st.info(t["sub_title"])

# --- КАЛЬКУЛЯТОР (Ваш оригінальний код) ---
col1, col2 = st.columns(2)
with col1:
    st.subheader(t["header_current"])
    w1 = st.select_slider(f"{t['width']} (1)", options=list(range(135, 355, 5)), value=295, key="w1")
    p1 = st.select_slider(f"{t['profile']} (1)", options=list(range(20, 85, 5)), value=35, key="p1")
    r1 = st.number_input(f"{t['rim']} (1)", value=21, step=1, key="r1")

with col2:
    st.subheader(t["header_new"])
    w2 = st.select_slider(f"{t['width']} (2)", options=list(range(135, 355, 5)), value=275, key="w2")
    p2 = st.select_slider(f"{t['profile']} (2)", options=list(range(20, 85, 5)), value=45, key="p2")
    r2 = st.number_input(f"{t['rim']} (2)", value=21, step=1, key="r2")

# Розрахунки
diam1 = (w1 * p1 / 100 * 2) + (r1 * 25.4)
diam2 = (w2 * p2 / 100 * 2) + (r2 * 25.4)
diff = diam2 - diam1
cl_change_mm = diff / 2
cl_change_cm = cl_change_mm / 10
real_speed = 100 * (diam2 / diam1)
speed_diff = real_speed - 100

st.divider()
st.subheader(f"📊 {t['header_comparison']}:")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)
m_col1.metric(t["label_diam1"], f"{diam1:.0f} мм")
m_col2.metric(t["label_diam2"], f"{diam2:.1f} мм", f"{diff:.1f} мм")
m_col3.metric(t["label_clearance"], f"{cl_change_mm:.1f} мм", f"{cl_change_cm:.1f} см")
m_col4.metric(t["label_speed"], f"{real_speed:.1f} км/год", f"{speed_diff:.1f}%")

error_percent = abs(speed_diff)
if error_percent > 3.0:
    st.error(t["speedo_too_much"].format(err=error_percent))
else:
    st.success(t["speedo_ok"].format(err=error_percent))

# ФУТЕР
st.markdown("---")
st.caption(f"© 2024 WROCARS | {t['footer']}")
