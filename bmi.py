import streamlit as st
import matplotlib.pyplot as plt

# Create a title for the app
st.title("Pengukur Berat Badan")

# Create a sidebar with sliders for weight, height, and age input
st.sidebar.header("Input Data")
weight = st.sidebar.slider("Masukkan berat badan (dalam kg):", min_value=0.0, max_value=200.0, value=70.0, step=0.1)
height = st.sidebar.slider("Masukkan tinggi badan (dalam m):", min_value=0.5, max_value=2.5, value=1.75, step=0.01)
age = st.sidebar.slider("Masukkan usia:", min_value=10, max_value=100, value=30, step=1)
gender = st.sidebar.selectbox("Pilih jenis kelamin:", ["Laki-laki", "Perempuan"])

# Create a button to calculate the BMI
if st.sidebar.button("Hitung BMI"):
    # Calculate the BMI
    if gender == "Laki-laki":
        bmi = weight / (height ** 2) * 0.95
    else:
        bmi = weight / (height ** 2) * 1.05
    # Display the BMI
    st.write(f"BMI Anda adalah: {bmi:.2f}")
    # Determine the weight category
    if bmi < 18.5:
        st.write("Anda kurang berat badan.")
    elif bmi < 25:
        st.write("Anda memiliki berat badan normal.")
    elif bmi < 30:
        st.write("Anda kelebihan berat badan.")
    else:
        st.write("Anda obesitas.")

    # Provide health recommendations based on age, gender, and BMI
    if age < 30 and bmi < 25:
        st.write("Anda memiliki kesehatan yang baik! Tetap menjaga pola hidup seimbang.")
    elif age < 30 and bmi >= 25:
        st.write("Anda perlu menjaga pola hidup seimbang dan berolahraga lebih banyak.")
    elif age >= 30 and bmi < 25:
        st.write("Anda perlu menjaga pola hidup seimbang dan memantau kesehatan Anda lebih ketat.")
    else:
        st.write("Anda perlu menjaga pola hidup seimbang, berolahraga lebih banyak, dan memantau kesehatan Anda lebih ketat.")

    # Provide exercise recommendations
    if bmi < 18.5:
        st.write("Rekomendasi olahraga: Berjalan kaki 30 menit sehari, 3 kali seminggu.")
    elif bmi < 25:
        st.write("Rekomendasi olahraga: Berjalan kaki 30 menit sehari, 5 kali seminggu.")
    elif bmi < 30:
        st.write("Rekomendasi olahraga: Berjalan kaki 45 menit sehari, 5 kali seminggu.")
    else:
        st.write("Rekomendasi olahraga: Berjalan kaki 60 menit sehari, 7 kali seminggu.")

    # Provide diet recommendations
    if bmi < 18.5:
        st.write("Rekomendasi pola makan: Makan 3 kali sehari, dengan porsi yang lebih besar.")
    elif bmi < 25:
        st.write("Rekomendasi pola makan: Makan 3 kali sehari, dengan porsi yang seimbang.")
    elif bmi < 30:
        st.write("Rekomendasi pola makan: Makan 3 kali sehari, dengan porsi yang lebih kecil.")
    else:
        st.write("Rekomendasi pola makan: Makan 2 kali sehari, dengan porsi yang sangat kecil.")

    # Create a BMI chart
    fig, ax = plt.subplots()
    ax.plot([18.5, 25, 30], [0, 0, 0], 'k-')
    ax.plot([bmi], [0], 'ro')
    ax.set_xlabel('BMI')
    ax.set_ylabel('')
    ax.set_title('BMI Chart')
    st.pyplot(fig)

# Footer
st.sidebar.info('Pembaruan secara berkala')
st.sidebar.text('Created by HUZAIR BAWAZIR (HAJER)')
