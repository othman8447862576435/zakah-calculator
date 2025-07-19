import streamlit as st

st.set_page_config(page_title="حاسبة الزكاة", page_icon="🕌", layout="centered")

st.title("🕌 حاسبة الزكاة")
st.markdown("احسب زكاة المال أو الذهب بسهولة وبدون تعقيد ✨")

option = st.radio("اختر نوع الزكاة", ["💰 زكاة المال", "🏆 زكاة الذهب"])

if option == "💰 زكاة المال":
    amount = st.number_input("أدخل المبلغ الذي تملكه (بالدينار)", min_value=0.0, step=0.5)
    if st.button("احسب الزكاة"):
        zakah = amount * 0.025
        st.success(f"الزكاة المستحقة: {zakah:.2f} دينار")
        
elif option == "🏆 زكاة الذهب":
    weight = st.number_input("أدخل وزن الذهب (بالجرام)", min_value=0.0, step=0.1)
    price_per_gram = st.number_input("أدخل سعر الجرام الحالي", min_value=0.0, step=0.1)
    if st.button("احسب الزكاة"):
        total_value = weight * price_per_gram
        zakah = total_value * 0.025
        st.success(f"الزكاة المستحقة: {zakah:.2f} دينار (إجمالي قيمة الذهب: {total_value:.2f})")

st.markdown("---")
st.caption("تم التطوير بواسطة عثمان 😎")
