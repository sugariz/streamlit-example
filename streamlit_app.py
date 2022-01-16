import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Đề tài xác định bệnh thực vật')
    st.text('Trong đề tài này, nhóm em tập trung vào việc tìm kiếm dữ liệu, huấn luyện mô hình và kiểm thử')

with dataset:
    st.header('Dataset')
    st.text('Dataset sử dụng trong đề tài được lấy ở  Plant Pathology 2020 – FGVC7')

with features:
    st.header('The features I created')
    st.text('I found dataset on...')

with model_training:
    st.header('Time to train model')
    st.text('I found dataset on...')
