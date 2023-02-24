import streamlit

streamlit.title('My Parents new healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('oatmeal')
streamlit.text('Smoothie')
streamlit.text('Boiled eggs')

streamlit.header('Build your own fruit smoothie')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
