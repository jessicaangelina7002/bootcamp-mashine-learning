
import streamlit as st
import pandas as pd
import joblib

# Memuat model yang tadi sempat kita serialisasi
model = joblib.load("model_kredit.pkl")

st.title("Aplikasi Persetujuan Kredit Based on AI Model")
st.write("Aplikasi ini memprediksi apakah pengajuan kredit disetujui atau tidak.")

with st.form("Form Credit")
    #2. membuat form input untuk user kita
    gaji = st.number_input("Gaji Bulanan (Juta Rupiah)", min_value=1, max_value=30, value=5)
    umur = st.number_input("Umur", min_value=17, max_value=100, value=25)
    cicilan = st.number_input("cicilan di bank lain (juta rupiah): ", min_value = 0, value = 1)

    submit_button = st.form_submit_button("prediksi status kredit")

if submit_button:
    data_baru = pd.DataFrame({
        'Gaji':[gaji],
        'Umur':[umur],
        'Cicilan':[cicilan]
    })

hasil= model.predict(data.baru)[0]

st.markdown("----")
if hasil == 1:
    st.success("selamat pengajuan kredit anda kemungkinan di terima")
else:
    st.error("yahh maaf pengajuan kredit anda di tolak")
