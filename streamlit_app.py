import streamlit as st
import modelbit
import pandas as pd

def recommend(movie_name):
    response_json = modelbit.get_inference(
        region="ap-south-1",
        workspace="mustafaansari",
        deployment="recommend",
        data=movie_name
    )
    data_list = response_json['data']
    df = pd.DataFrame(data_list)
    df.index = df.index + 1
    return df

# Set up the Streamlit app
st.set_page_config(
    page_title="Movie Recommender",
    page_icon=":clapper:",
    layout="wide"
)

# Sidebar
st.sidebar.image("assets/stre.png", use_column_width=True)
st.sidebar.title("Developed:")
st.sidebar.markdown(
    """
     
    **Email:** mustafaansari@mail.com  
    **LinkedIn:** [LinkedIn/mustafaansaari/](https://www.linkedin.com/in/mustafaansaari/)  
    **GitHub:** [github/mustafaansaari/](https://github.com/mustafaansarii)  
    """
)

# Add title and input for movie name
st.title("Hollywood Movie Recommendation System")
movie_name = st.text_input("Enter a Hollywood movie name", "Avatar")

# Display recommendations
if st.button("Get Recommendations"):
    recommendations = recommend(movie_name)
    st.table(recommendations)

# Add styling
st.markdown(
    """
    <style>
    .table {
        width: 90%;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
