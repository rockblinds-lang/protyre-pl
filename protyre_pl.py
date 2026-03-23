import streamlit as st
import segno
from io import BytesIO


# Початок обгортки (без відступу)

    # ТУТ ПІШОВ ВІДСТУП (4 пробіли або Tab) ДЛЯ ВСЬОГО КОДУ:
st.markdown(
    """
    <script async src="https://www.googletagmanager.com"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'G-V589LFJ6DD');
    </script>
    """,
    unsafe_allow_html=True
)

# 1. Наш словник перекладів
translations = {
"UA": {

    "main_title": "ProTyre: Твій персональний шинний експерт",
    "sub_title": "Перед купівлею шин проаналізуйте, чи не будуть колеса зачіпати арки та як зміняться параметри ходової!",
    "pay_attention": "Зверніть увагу!",
    "clearance_check": "Увага! Кліренс зміниться на {cm} см. Це може вплинути на керованість.",
    "header_current": "⬅️ Ваші поточні шини",
    "header_new": "➡️ Нові шини (плановані)",
    "header_comparison": "📊 Порівняння результатів",
    "width": "Ширина",
    "profile": "Профіль",
    "rim": "Діаметр диска (дюйми)",
    "label_diam1": "Діаметр 1",
    "label_diam2": "Діаметр 2",
    "label_clearance": "Кліренс",
    "label_speed": "Швидкість",
    "warning_text": "Увага! Зміна кліренсу:",
    "result_warn": "⚠️ Увага! Зміна кліренсу:",
    "danger_msg": "**Перед купівлею шин проаналізуйте, як зміняться параметри вашої ходової!**",
    "speedo_too_much": "Похибка спідометра: {err:.1f}%. Це забагато!",
    "clearance_check": "Кліренс зміниться на {cm:.1f} см. Перевірте арки!",
    "special_offer": "СПЕЦІАЛЬНА ПРОПОЗИЦІЯ ВІД РОЗРОБНИКА",
    "disclaimer": "⚠️ Цей інструмент надає інформацію для ознайомлення; перед заміною шин проконсультуйтеся з фахівцем.",
    "speedo_ok": "Похибка спідометра в межах норми ({err:.1f}%)"
},
"EN": {
    "main_title": "ProTyre: Your Personal Tire Expert",
    "sub_title": "Before buying tires, analyze whether the wheels will hit the arches and how the suspension parameters will change!",
    "pay_attention": "Pay Attention!",
    "clearance_check": "Warning! Clearance will change by {cm} cm. This may affect handling.",
    "header_current": "⬅️ Your current tires",
    "header_new": "➡️ New tires (planned)",
    "header_comparison": "📊 Comparison Results",
    "width": "Width",
    "profile": "Profile",
    "rim": "Rim diameter (inches)",
    "label_diam1": "Diameter 1",
    "label_diam2": "Diameter 2",
    "label_clearance": "Clearance",
    "label_speed": "Speed",
    "warning_text": "Warning! Clearance change:",
    "result_warn": "⚠️ Warning! Clearance change:",
    "danger_msg": "**Before buying tires, analyze how your suspension parameters will change!**",
    "speedo_too_much": "Speedometer error: {err:.1f}%. This is too much!",
    "clearance_check": "Clearance will change by {cm:.1f} cm. Check the arches!",
    "special_offer": "SPECIAL OFFER FROM THE DEVELOPER",
    "disclaimer": "⚠️ This tool is for informational purposes only; consult a specialist before changing tires.",
    "speedo_ok": "Speedometer error is within normal range ({err:.1f}%)"
},
"PL": {
    "main_title": "ProTyre: Twój osobisty ekspert oponiarski",
    "sub_title": "Przed zakupem opon przeanalizuj, czy koła nie będą ocierać o nadkola i jak zmienią się parametry zawieszenia!",
    "pay_attention": "Uważać na!",
    "clearance_check": "Uwaga! Prześwit zmieni się o {cm} cm. Może to wpłynąć na prowadzenie.",
    "header_current": "⬅️ Twoje aktualne opony",
    "header_new": "➡️ Nowe opony (planowane)",
    "header_comparison": "📊 Porównanie wyników",
    "width": "Szerokość",
    "profile": "Profil",
    "rim": "Średnica felgi (cale)",
    "label_diam1": "Średnica 1",
    "label_diam2": "Średnica 2",
    "label_clearance": "Prześwit",
    "label_speed": "Prędkość",
    "warning_text": "Uwaga! Zmiana prześwitu:",
    "result_warn": "⚠️ Uwaga! Zmiana prześwitu:",
    "danger_msg": "**Przed zakupem opon przeanalizuj, jak zmienią się parametry Twojego zawieszenia!**",
    "speedo_too_much": "Błąd prędkościomierza: {err:.1f}%. To za dużo!",
    "clearance_check": "Prześwit zmieni się o {cm:.1f} cm. Sprawdź nadkola!",
    "special_offer": "SPECJALNA OFERTA OD DEWELOPERA",
    "disclaimer": "⚠️ To narzędzie służy wyłącznie do celów informacyjnych; przed wymianą opon skonsultuj się ze specjalistą.",
    "speedo_ok": "Błąd prędkościomierza mieści się w normie ({err:.1f}%)"
},
}

# Вибір мови в боковій панелі
lang = st.sidebar.selectbox("Language / Мова", ["UA", "EN", "PL"])
t = translations[lang]

# 3. Створюємо коротку змінну 't', яка буде містити слова обраної мови
t = translations[lang]

import streamlit as st

# 1. Налаштування сторінки
st.set_page_config(page_title="ProTyre", layout="centered")

st.title(t["main_title"])
st.info(t["sub_title"])
# --- ВВІД ДАНИХ У ДВІ КОЛОНКИ ---
# --- ВАШ ОНОВЛЕНИЙ ВВІД ДАНИХ ---
col1, col2 = st.columns(2)

with col1:
    st.subheader(t["header_current"]) # Використовуємо словник
    w1 = st.select_slider(f"{t['width']} (1)", options=list(range(135, 355, 5)), value=295, key="w1")
    p1 = st.select_slider(f"{t['profile']} (1)", options=list(range(20, 85, 5)), value=35, key="p1")
    r1 = st.number_input(f"{t['rim']} (1)", value=21, step=1, key="r1")
with col2:
    st.subheader(t["header_new"]) # Використовуємо словник
    w2 = st.select_slider(f"{t['width']} (2)", options=list(range(135, 355, 5)), value=275, key="w2")
    p2 = st.select_slider(f"{t['profile']} (2)", options=list(range(20, 85, 5)), value=45, key="p2")
    r2 = st.number_input(f"{t['rim']} (2)", value=21, step=1, key="r2")
    
    # --- МАТЕМАТИКА (повна версія) ---
    # --- МАТЕМАТИКА ---
    diam1 = (w1 * p1 / 100 * 2) + (r1 * 25.4)
    diam2 = (w2 * p2 / 100 * 2) + (r2 * 25.4)
    diff = diam2 - diam1
    cl_change_mm = diff / 2
    cl_change_cm = cl_change_mm / 10
    
    # Розрахунок швидкості
    ratio = diam2 / diam1
    real_speed = 100 * ratio
    speed_diff = real_speed - 100
    
    st.divider()
    
    # --- ВИВІД РЕЗУЛЬТАТІВ ---
    st.write("---")
    st.subheader(f"📊 {t.get('header_comparison', 'Порівняння результатів')}:")
    # Створюємо 4 колонки
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    
    st.subheader(f"📊 {t['pay_attention']}")
    
    m_col1.metric(t["label_diam1"], f"{diam1:.0f} мм")
    m_col2.metric(t["label_diam2"], f"{diam2:.1f} мм", f"{diff:.1f} мм")
    m_col3.metric(t["label_clearance"], f"{cl_change_mm:.1f} мм", f"{cl_change_cm:.1f} см")
    m_col4.metric(t["label_speed"], f"{real_speed:.1f} км/год", f"{speed_diff:.1f}%")
    
    # --- ПОПЕРЕДЖЕННЯ ---
    error_percent = abs(speed_diff)
if error_percent > 3.0:
    # Використовуємо ключ "speedo_too_much" зі словника
    st.error(t["speedo_too_much"].format(err=error_percent))
else:
    # Використовуємо новий ключ "speedo_ok"
    st.success(t["speedo_ok"].format(err=error_percent))
    
    
if abs(cl_change_mm) > 15:
    st.warning(t["clearance_check"].format(cm=cl_change_cm))
    
    # --- РЕКЛАМНИЙ БЛОК (Тепер він помітний!) ---
    st.success("🎁 СПЕЦІАЛЬНА ПРОПОЗИЦІЯ ВІД РОЗРОБНИКА")
    st.markdown("""
    **Якісні жалюзі та ролети від "РОМІГО"**  
    ☀️ Захистіть свою оселю від яскравості сонця!  
    📍 м. Львів, вул. Зелена 115з (вхід з вул.Півколо),__ТК"Південний" навпроти поліклініки "Веселка"  
    📞 **Телефонуйте: 067 244 45 03  **
    **про новинки та АКЦІЇ тут: https://www.facebook.com/romigozaluzi/**
    """)
if st.button("🌐 Перейти на наш сайт"):
    st.write("www.zaluzi.com.ua")
    
    st.caption("Розроблено спеціально для відповідальних автовласників.")
    
    
    # Твій Рекламний Блок
with st.expander("🎁 Отримати бонус від розробника"):
    st.success("незабаром інформація про наступні акції, не пропустіть")
    st.write("☀️ Слідкуйте за знижками в застосунку!")
    st.markdown("📞 **Додайте, будь ласка, коментар чи вподобайку у нашу ФБ сторінку **")
if st.button("🌐 www.zaluzi.com.ua"):
        st.write("Перенаправлення...")
    import segno
    from io import BytesIO
    
    # Створюємо бічну панель для QR-коду
with st.sidebar:
    st.write("### Поділитися додатком")
    
    # Створюємо QR-код, який веде на адресу вашого сайту
    url = " https://calc-app-bpnejes72n7bpfuukqudzb.streamlit.app/" # Перевірте, чи це ваша адреса
    qr = segno.make(url)
    
    # Зберігаємо QR-код у пам'ять, щоб Streamlit міг його показати
    out = BytesIO()
    qr.save(out, kind='png', scale=10)
    st.image(out.getvalue(), caption="Скануй та рахуй у смартфоні")
