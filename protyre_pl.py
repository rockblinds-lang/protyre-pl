import streamlit as st
import segno
from io import BytesIO

# 1. Налаштування сторінки
st.set_page_config(page_title="QR ProTire PL", layout="centered", page_icon="🛞")

# Вставка Google Analytics (GA4)
st.markdown(
    """
    <script async src="https://googletagmanager.com"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-V589LFJ6DD');
    </script>
    """,
    unsafe_allow_html=True
)

# 2. Словник перекладів
translations = {
    "UA": {
        "main_title": "QR ProTire PL: Твій персональний шинний експерт",
        "sub_title": "Перед купівлею шин проаналізуйте, чи не будуть колеса зачіпати арки та як зміняться параметри ходової!",
        "pay_attention": "Зверніть увагу!",
        "header_current": "⬅️ Ваші поточні шини",
        "header_new": "➡️ Нові шини (плановані)",
        "header_comparison": "Результати порівняння",
        "width": "Ширина",
        "profile": "Профіль",
        "rim": "Діаметр диска (дюйми)",
        "label_diam1": "Діаметр 1",
        "label_diam2": "Діаметр 2",
        "label_clearance": "Кліренс",
        "label_speed": "Швидкість",
        "speedo_too_much": "Похибка спідометра: {err:.1f}%. Це забагато!",
        "speedo_ok": "Похибка спідометра в межах норми ({err:.1f}%)",
        "clearance_check": "Кліренс зміниться на {cm:.1f} см. Перевірте арки!",
        "special_offer": "СПЕЦІАЛЬНА ПРОПОЗИЦІЯ ВІД РОЗРОБНИКА",
        "footer": "Розроблено спеціально для відповідальних автовласників."
    },
    "PL": {
        "main_title": "QR ProTire PL: Twój osobisty ekspert oponiarski",
        "sub_title": "Przed zakupem opon przeanalizuj, czy koła nie będą ocierać o nadkola!",
        "pay_attention": "Uwaga!",
        "header_current": "⬅️ Twoje aktualne opony",
        "header_new": "➡️ Nowe opony (planowane)",
        "header_comparison": "Wyniki porównania",
        "width": "Szerokość",
        "profile": "Profil",
        "rim": "Średnica felgi (cale)",
        "label_diam1": "Średnica 1",
        "label_diam2": "Średnica 2",
        "label_clearance": "Prześwit",
        "label_speed": "Prędkość",
        "speedo_too_much": "Błąd prędkościomierza: {err:.1f}%. To za dużo!",
        "speedo_ok": "Błąd prędkościomierza w normie ({err:.1f}%)",
        "clearance_check": "Prześwit zmieni się o {cm:.1f} cm. Sprawdź nadkola!",
        "special_offer": "SPECJALNA OFERTA OD DEWELOPERA",
        "footer": "Zaprojektowane dla odpowiedzialnych kierowców."
    },
    "EN": {
        "main_title": "QR ProTire PL: Your Personal Tire Expert",
        "sub_title": "Analyze your tire fitment and suspension changes before you buy!",
        "pay_attention": "Attention!",
        "header_current": "⬅️ Current tires",
        "header_new": "➡️ New tires",
        "header_comparison": "Comparison Results",
        "width": "Width",
        "profile": "Profile",
        "rim": "Rim (inches)",
        "label_diam1": "Diameter 1",
        "label_diam2": "Diameter 2",
        "label_clearance": "Clearance",
        "label_speed": "Speed",
        "speedo_too_much": "Speedometer error: {err:.1f}%. Too high!",
        "speedo_ok": "Speedometer error is OK ({err:.1f}%)",
        "clearance_check": "Clearance change: {cm:.1f} cm. Check arches!",
        "special_offer": "SPECIAL OFFER FROM DEVELOPER",
        "footer": "Developed for responsible car owners."
    }
}

# Вибір мови
lang = st.sidebar.selectbox("Language / Мова", ["UA", "PL", "EN"])
t = translations[lang]

st.title(t["main_title"])
st.info(t["sub_title"])

# --- ВВІД ДАНИХ ---
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

# --- РОЗРАХУНКИ ---
diam1 = (w1 * p1 / 100 * 2) + (r1 * 25.4)
diam2 = (w2 * p2 / 100 * 2) + (r2 * 25.4)
diff = diam2 - diam1
cl_change_mm = diff / 2
cl_change_cm = cl_change_mm / 10
real_speed = 100 * (diam2 / diam1)
speed_diff = real_speed - 100

st.divider()

# --- РЕЗУЛЬТАТИ ---
st.subheader(f"📊 {t['header_comparison']}:")
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

m_col1.metric(t["label_diam1"], f"{diam1:.0f} мм")
m_col2.metric(t["label_diam2"], f"{diam2:.1f} мм", f"{diff:.1f} мм")
m_col3.metric(t["label_clearance"], f"{cl_change_mm:.1f} мм", f"{cl_change_cm:.1f} см")
m_col4.metric(t["label_speed"], f"{real_speed:.1f} км/год", f"{speed_diff:.1f}%")

# Попередження
error_percent = abs(speed_diff)
if error_percent > 3.0:
    st.error(t["speedo_too_much"].format(err=error_percent))
else:
    st.success(t["speedo_ok"].format(err=error_percent))

if abs(cl_change_mm) > 15:
    st.warning(t["clearance_check"].format(cm=cl_change_cm))

# --- РЕКЛАМНИЙ БЛОК РОМІГО ---
st.divider()
st.success(f"🎁 {t['special_offer']}")

st.markdown("""
### **"WROCARS"**  
☀️ **WROCARS - Twoj detaling**  
📍 Wroclaw-Wojkowice-Wrocars (WWW),  
**  <Bartek & Friend>  
📞 **Tel: 577 511 068**  

🆕 **Про новинки та АКЦІЇ тут:** [://https://www.facebook.com/zadorizhnyy/)
""")

if st.button("🌐 Перейти на наш сайт"):
    st.markdown("[Відкрити ://zaluzi.com.ua](https://://zaluzi.com.ua)")

# Бонус
with st.expander("🎁 Отримати бонус від розробника"):
    st.info("Незабаром інформація про наступні акції, не пропустіть!")
    st.write("☀️ Слідкуйте за знижками в застосунку!")
    st.markdown("💬 **Додайте, будь ласка, коментар чи вподобайку на нашу ФБ сторінку**")

st.caption(t["footer"])

# --- QR-КОД У САЙДБАРІ ---
with st.sidebar:
    st.write("### Поділитися додатком")
    # ЗАМІНІТЬ ПІСЛЯ ДЕПЛОЮ НА НОВУ АДРЕСУ
    url = "https://protyre-pl.streamlit.app" 
    qr = segno.make(url)
    out = BytesIO()
    qr.save(out, kind='png', scale=10)
    st.image(out.getvalue(), caption="Скануй та рахуй у смартфоні")
