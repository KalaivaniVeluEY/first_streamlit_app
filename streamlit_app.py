import streamlit
streamlit.title('Hello World!!!')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado toast')
streamlit.header('Let me make my own smoothie')

#Lets import a csv file and view it
import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

#Lets add a pick list to pick the fruits needed for the smootie
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lemon'])

streamlit.dataframe(my_fruit_list)
