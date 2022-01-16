from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()
test = st.container()

training_data = pd.read_csv("dataset/train.csv")
testing_data = pd.read_csv("dataset/test.csv")
healthy = Image.open('dataset/train_2.jpg')
multiple_diseases = Image.open('dataset/train_1.jpg')
rust = Image.open('dataset/train_3.jpg')
scrab = Image.open('dataset/train_7.jpg')

with header:
    st.title('Đề tài xác định bệnh thực vật')
    st.write('Trong đề tài này, nhóm em tập trung vào việc tìm kiếm dữ liệu, huấn luyện mô hình và kiểm thử')

with dataset:
    st.header('Dataset')
    st.write('Dataset sử dụng trong đề tài được lấy ở  Plant Pathology 2020 – FGVC7')
    st.write('Bộ dữ liệu gồm:')
    st.write('+ 1 bộ ảnh gồm n tấm ảnh')
    st.write('+ 1 file train.csv')
    st.write('+ 1 file test.csv')
    st.subheader("train.csv")
    st.write(training_data.head())
    st.subheader("test.csv")
    st.write(testing_data.head())
    st.subheader("Một vài hình ảnh trong dataset")
    st.image(healthy, caption="Healthy leaves")
    st.image(multiple_diseases, caption="Leaves with multiple diseases")
    st.image(rust, caption="Leaves with rust")
    st.image(scrab, caption="Leaves with scab")


with features:
    st.header('The features I created')
    st.write('I found dataset on...')

with model_training:
    st.header('Time to train model')
    st.write('I found dataset on...')

with test:
    st.header('Thử nhận biết một số lá')
    uploaded_file = st.file_uploader("Chọn một lá bất kỳ")
    if uploaded_file is not None:
        test_image = "dataset/images/" + uploaded_file.name
        st.image(test_image, caption="test")
    
    result = st.button('Dự đoán')

    if result:
        st.write('Hello')
