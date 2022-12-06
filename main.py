import streamlit as st
import pandas as pd
import scipy.stats as stats
import plotly.express as px
# import plotly.figure_factory as ff

st.write(''' 
# Aplikasi Uji-t Berpasangan
Ini adalah aplikasi menguji efektifitas suatu percobaan menggunakan Streamlit
''')

uploaded_file  = st.file_uploader('Upload File')

if uploaded_file is not None:
    st.success('Upload File {} Berhasil !'.format(uploaded_file))
    df = pd.read_csv(uploaded_file)

    st.write('Please choose one of them : {}'.format(df.columns.tolist()))
    pre_test_col = st.text_input('Pretest column')
    post_test_col = st.text_input('Postest column')

    hitung = st.button('Analisa Uji t-test')

    if hitung:
        pre_test = df[pre_test_col]
        post_test = df[post_test_col]

        sampling_difference = post_test-pre_test
        norm_test = stats.shapiro(sampling_difference)
        
        if norm_test[1]>0.05:
            st.write('#### Normality Test')
            dist_plot = px.histogram(df[pre_test_col]-df[post_test_col], marginal='box')
            st.plotly_chart(dist_plot)
            st.success('The difference of two related sample data is normally distributed')

            st.write('#### Paired t-test result')
            line_chart = px.line(df[[pre_test_col, post_test_col]], markers=True)
            st.plotly_chart(line_chart)
            ttest = stats.ttest_rel(pre_test, post_test, alternative='less')
            if norm_test[1]<0.05:
                st.success('The experiment is effective than pretest')
            else:
                st.warning('The experiment is not significantly effective than pretest')

        else:
            st.write("The difference of two related sample data doesn't follow normal distribution")

else:
    st.warning('You need to upload a csv or excel file.')


# alas = st.number_input('Masukan Alas', 0)
# tinggi = st.number_input('Masukan Tinggi', 0)
# hitung = st.button('Hitung Luas')

# if hitung:
#     luas = 0.5*alas*tinggi
#     st.write('Luas segitiganya adalah', luas)
#     st.success(f'Luas segitiganya adalah P{luas}')