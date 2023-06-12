import streamlit as st
import numpy as np
from scipy import stats


def home_page():
    st.title("Simple Statistics and Matrix Calculator")
    st.write(
        "Simple Statistic and Matrix Calculator, Please select the option below:"
    )

    if st.button("Operasi Matriks"):
        st.session_state["current_page"] = "matrix"

    if st.button("Uji T"):
        st.session_state["current_page"] = "t_test"

    if st.button("Uji Z"):
        st.session_state["current_page"] = "z_test"

    if st.button("Distribusi"):
        st.session_state["current_page"] = "distribution"


def matrix_page():
    st.title("Operasi Matriks")
    st.write("Halaman Operasi Matriks")

    st.write("Masukkan matriks A:")
    a_rows = st.number_input(
        "Jumlah baris", min_value=1, value=2, step=1, key="matrix_a_rows"
    )
    a_cols = st.number_input(
        "Jumlah kolom", min_value=1, value=2, step=1, key="matrix_a_cols"
    )

    matrix_a = np.zeros((a_rows, a_cols))

    for i in range(a_rows):
        for j in range(a_cols):
            matrix_a[i][j] = st.number_input(
                f"Elemen A[{i+1}][{j+1}]", key=f"matrix_a_{i}_{j}"
            )

    st.write("Matriks A:")
    st.write(matrix_a)

    st.write("Masukkan matriks B:")
    b_rows = st.number_input(
        "Jumlah baris", min_value=1, value=2, step=1, key="matrix_b_rows"
    )
    b_cols = st.number_input(
        "Jumlah kolom", min_value=1, value=2, step=1, key="matrix_b_cols"
    )

    matrix_b = np.zeros((b_rows, b_cols))

    for i in range(b_rows):
        for j in range(b_cols):
            matrix_b[i][j] = st.number_input(
                f"Elemen B[{i+1}][{j+1}]", key=f"matrix_b_{i}_{j}"
            )

    st.write("Matriks B:")
    st.write(matrix_b)

    if a_cols == b_rows:
        result = np.dot(matrix_a, matrix_b)
        st.write("Hasil perkalian matriks A dan B:")
        st.write(result)
    else:
        st.write("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B.")

    if st.button("Back"):
        st.session_state["current_page"] = "home"


def t_test_page():
    st.title("Uji T")
    st.write("Halaman Uji T")

    st.write("Masukkan data untuk Grup 1:")
    data1 = st.text_area("Data Grup 1 (pisahkan dengan koma)", key="t_test_data1")

    st.write("Masukkan data untuk Grup 2:")
    data2 = st.text_area("Data Grup 2 (pisahkan dengan koma)", key="t_test_data2")

    try:
        data1 = [float(x.strip()) for x in data1.split(",")]
        data2 = [float(x.strip()) for x in data2.split(",")]

        t_stat, p_value = stats.ttest_ind(data1, data2)

        st.write("Hasil Uji T:")
        st.write(f"T-Statistic: {t_stat}")
        st.write(f"P-Value: {p_value}")
    except ValueError:
        st.write(
            "Data yang dimasukkan tidak valid. Pastikan untuk memasukkan angka yang valid dan dipisahkan oleh koma."
        )

    if st.button("Back"):
        st.session_state["current_page"] = "home"


def z_test_page():
    st.title("Uji Z")
    st.write("Halaman Uji Z")

    st.write("Masukkan data:")
    data = st.text_area("Data (pisahkan dengan koma)", key="z_test_data")

    try:
        data = [float(x.strip()) for x in data.split(",")]

        z_stat, p_value = stats.zscore(data), stats.norm.sf(abs(stats.zscore(data))) * 2

        st.write("Hasil Uji Z:")
        st.write(f"Z-Statistic: {z_stat}")
        st.write(f"P-Value: {p_value}")
    except ValueError:
        st.write(
            "Data yang dimasukkan tidak valid. Pastikan untuk memasukkan angka yang valid dan dipisahkan oleh koma."
        )

    if st.button("Back"):
        st.session_state["current_page"] = "home"


def distribution_page():
    st.title("Distribusi")
    st.write("Halaman Distribusi")

    st.write("Pilih jenis distribusi:")
    distribution_type = st.selectbox(
        "Distribusi", ("Normal", "Uniform", "Exponential"), key="distribution_type"
    )

    if distribution_type == "Normal":
        mean = st.number_input("Mean", value=0.0, key="normal_mean")
        std_dev = st.number_input("Standard Deviation", value=1.0, key="normal_std_dev")
        x = st.number_input("Nilai x", value=0.0, key="normal_x")
        probability = stats.norm.cdf(x, mean, std_dev)
        st.write(f"Probabilitas P(X <= {x}) pada distribusi normal: {probability}")

    elif distribution_type == "Uniform":
        a = st.number_input("Batas bawah (a)", value=0.0, key="uniform_a")
        b = st.number_input("Batas atas (b)", value=1.0, key="uniform_b")
        x = st.number_input("Nilai x", value=0.0, key="uniform_x")
        probability = (x - a) / (b - a)
        st.write(f"Probabilitas P(X <= {x}) pada distribusi uniform: {probability}")

    elif distribution_type == "Exponential":
        scale = st.number_input("Skala (Lambda)", value=1.0, key="exponential_scale")
        x = st.number_input("Nilai x", value=0.0, key="exponential_x")
        probability = 1 - np.exp(-scale * x)
        st.write(
            f"Probabilitas P(X <= {x}) pada distribusi eksponensial: {probability}"
        )

    if st.button("Back"):
        st.session_state["current_page"] = "home"


def main():
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "home"

    if st.session_state["current_page"] == "home":
        home_page()
    elif st.session_state["current_page"] == "matrix":
        matrix_page()
    elif st.session_state["current_page"] == "t_test":
        t_test_page()
    elif st.session_state["current_page"] == "z_test":
        z_test_page()
    elif st.session_state["current_page"] == "distribution":
        distribution_page()


if __name__ == "__main__":
    main()
