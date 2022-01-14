import streamlit as st 
import pickle


#st.image('images/Fitting_2.0.png')

with open('pickledmodels/logreg_transform.pkl', 'rb') as f:
    transform = pickle.load(f)

with open('pickledmodels/logreg_model.pkl', 'rb') as f:
    model = pickle.load(f)

def metric_converter(metric, weight, height):
    if metric == 'lbs/inches':
        weight = weight /  2.2046
        height = height * 2.54
    return weight, height


def predict_size(weight, age, height):
    inputs = transform.transform([[weight, age, height]])
    pred = model.predict(inputs)[0]
    return pred

size_chart = {1: 'Extra Extra Small (XXS)', 2:'Small (S)', 3:'Medium (M)', 4:'Large (L)', 5:'Extra Large (XL)', 6:'Extra Extra Large (XXL)', 7:'Extra Extra Extra Large (XXXL)'}

st.title('Clothing Size Predictor')

st.header('Find your estimated clothing size with a few simple inputs!')

selected_metric = st.selectbox('Choose A Metric!', ('kg/cm', 'lbs/inches'))

weight = st.number_input("Enter your weight!", min_value=0, max_value=300, value=0, step=1)

age = st.number_input("Enter your age!", min_value=0, max_value=100, value=0, step=1)

height = st.number_input("Enter your height!", min_value=0, max_value=200, value=0, step=1)


result = st.button('Click Here')

if weight <= 0:
    st.write('Your inputs are incomplete, please enter your correct estimated weight.')
if age <= 0:
    st.write('Your inputs are incomplete, please enter your correct age.')
if height <= 0:
    st.write('Your inputs are incomplete, please enter your correct estimated height.')

else:
    convert_weight, convert_height = metric_converter(selected_metric, weight, height)
    pred = predict_size(convert_weight,age,convert_height)
    st.write('Your predicted size is: ', size_chart[pred])
