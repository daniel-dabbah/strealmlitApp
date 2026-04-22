import streamlit as st

st.title("בודק מצב רוח 😄")

# בחירת מצב רוח
mood = st.selectbox(
    "איך אתה מרגיש היום?",
    ["שמח 😄", "עייף 😴", "לחוץ 😰"]
)

# בחירת אנרגיה
energy = st.slider("כמה אנרגיה יש לך?", 0, 10)

# כפתור
if st.button("תן לי המלצה"):
    
    if mood == "שמח 😄":
        if energy > 5:
            st.write("לך לבלות עם חברים 🎉")
        else:
            st.write("תשמע מוזיקה טובה 🎧")
    
    elif mood == "עייף 😴":
        st.write("לך לישון קצת 😴")
    
    elif mood == "לחוץ 😰":
        st.write("קח נשימה עמוקה 🧘‍♂️")
