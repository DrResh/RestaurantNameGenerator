import streamlit as st
import LangChainSupport
st.title(" Restaurant Name Generator by Lang Chain ")

cuisine=st.sidebar.selectbox("Pick a cuisine",("Italian","Indian",  "Mexican", "Arabic",
                                        "American","Chinese"))

if cuisine:
    response = LangChainSupport.generate_menu(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    print(menu_items)
    print(response['restaurant_name'].strip())
    st.write("Menu Items")
    for item in menu_items:
        st.write("-", item)
        print(item)
        print("me")
    st.write("end")
    print("end")
