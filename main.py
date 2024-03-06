# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample DataFrame
# data = {
#     "Date": ["2015-06-20", "2015-06-21", "2015-06-22", "2015-06-23", "2015-06-24"],
#     "Store_1_actual_Sales": [1.021029, 0.158782, 0.621737, 0.564550, 0.570365],
#     "Store_1_forecast_sale": [1.029717, -0.025151, 0.962598, 0.985394, 0.975543],
#     "Store_2_actual_Sales": [0.8, 0.7, 0.9, 0.6, 0.5],
#     "Store_2_forecast_sale": [0.85, 0.75, 0.95, 0.65, 0.55],
# }
# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df = df.set_index("Date")

# # Streamlit app
# st.title("Store Sales Visualization")

# # Dropdown for store selection
# selected_store = st.selectbox(
#     "Select Store:", options=[col for col in df.columns if "actual_Sales" in col]
# )

# # Plot actual and forecast sales for the selected store
# fig, ax = plt.subplots(figsize=(10, 6))
# store_name = selected_store.split("_")[1]
# ax.plot(df.index, df[selected_store], label=f"{store_name} Actual Sales", marker="o")
# forecast_column = selected_store.replace("actual_Sales", "forecast_sale")
# ax.plot(df.index, df[forecast_column], label=f"{store_name} Forecast Sales", marker="o")

# ax.set_xlabel("Date")
# ax.set_ylabel("Sales")
# ax.set_title(f"Sales Comparison for {store_name}")
# ax.legend()

# # Display the plot using st.pyplot()
# st.pyplot(fig)

# # Display DataFrame
# st.write(df)

import streamlit as st
import pandas as pd
import numpy as np
import os

st.markdown("## Store Sales Visualization")

st.divider()

# css = """
# <style>
#     .container {
#         display: flex;
#         flex-wrap: wrap;
#         justify-content: center;
#         align-items: center;
#         height: 500px; /* Adjust the height as needed */
#     }
#     .big-box {
#         width: 400px; /* Adjust the width of the big box */
#         height: 400px; /* Adjust the height of the big box */
#         border: 1px solid black;
#         margin: 10px;
#         position: relative;
#     }
#     .box {
#         width: 100px; /* Adjust the width of each box */
#         height: 100px; /* Adjust the height of each box */
#         border: 1px solid black;
#         position: absolute;
#     }
#     .box1 { top: 0; left: 0; }
#     .box2 { top: 0; right: 0; }
#     .box3 { bottom: 0; left: 0; }
#     .box4 { bottom: 0; right: 0; }
# </style>
# """

# st.markdown(css, unsafe_allow_html=True)
# # Create the skeleton layout
# st.write('<div class="container">', unsafe_allow_html=True)
# # st.write('<div class="big-box"> <div class="box">Box 1</div> <div class="box">Box 2</div> <div class="box">Box 3</div> <div class="box">Box 4</div> </div>', unsafe_allow_html=True)
# st.write('<div class="big-box"> <div class="box">Box 1</div> </div>', unsafe_allow_html=True)
# st.write('</div>', unsafe_allow_html=True)

import streamlit as st

# css = """
#     <style>
#     .parent {
#     position:relative;
#     border:3px solid blue;
#     height:300px;
#     width:500px;
#     padding:0;
# }
# .box{
#     position:absolute;
#     border:2px solid;
#     margin:0;
#     padding:5px;
#     border:3px solid red;
# }
# .box1 {
#     border-color:green;
#     top:0;
#     left:0;   
#     border:3px solid green; 
# }
# p:nth-child(2) {
#     border-color:red;
#     top:0;
#     right:0;
# }
# p:nth-child(3) {
#     border-color:yellow;
#     bottom:0;
#     left:0;
# }
# p:nth-child(4) {
#     border-color:pink;
#     bottom:0;
#     right:0;
# }
#     </style>
# """


# st.title("Stores Sale Visualization")
# current_dir = os.getcwd()

# st.markdown(css, unsafe_allow_html=True)

# st.write('<div class="parent">', unsafe_allow_html=True)
# st.write('<div class="box"> BOX 1</div>', unsafe_allow_html=True)
# # st.write('<div class="parent box3">Box 3</div>', unsafe_allow_html=True)
# # st.write('<div class="parent box4">Box 4</div>', unsafe_allow_html=True)
# st.write('</div>', unsafe_allow_html=True)



css = """
<style>
.container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(5, 100px);
  border: 2px solid red;
}

.corner {
  border: 1px solid black;
  position: relative;
  border: 2px solid green;
}

.corner:nth-of-type(1) {
  grid-column: 1;
  grid-row: 1;
  border: 2px solid ;
}

.corner:nth-of-type(2) {
  grid-column: 5;
  grid-row: 1;
}

.corner:nth-of-type(2) .inset {
  right: 0; 
}

.corner:nth-of-type(3) {
  grid-column: 1;
  grid-row: 5;
}

.corner:nth-of-type(3) .inset { 
  bottom: 0;
}

.corner:nth-of-type(4) {
  grid-column: 5;
  grid-row: 5;
}

.corner:nth-of-type(4) .inset {
  bottom: 0;
  right: 0;
}

.corner .inset {
  background: pink;
  width: 75%;
  height: 75%;
  position: absolute;
}

.mid {
  grid-column: 3;
  grid-row: 3;
  background: darkred;
  padding: 12.5%;
}

.mid .inset {
  width: 100%;
  height: 100%;
  background: red;
}
</style>
"""

# st.markdown(css, unsafe_allow_html=True)

# st.write('<div class="container">', unsafe_allow_html=True)
# st.write('<span class="corner"><div class="inset"></div></span>', unsafe_allow_html=True)
# st.write('<span class="corner"><div class="inset"></div></span>', unsafe_allow_html=True)
# st.write('<div class="mid"><div class="inset"></div></div>', unsafe_allow_html=True)
# st.write('<span class="corner"><div class="inset"></div></span>', unsafe_allow_html=True)
# st.write('<span class="corner"><div class="inset"></div></span>', unsafe_allow_html=True)
# # st.write('<div class="parent box3">Box 3</div>', unsafe_allow_html=True)
# # st.write('<div class="parent box4">Box 4</div>', unsafe_allow_html=True)
# st.write('</div>', unsafe_allow_html=True)


# if st.button("Store 1"):
#     file_path = "pages/store_1.py"
#     st.switch_page(file_path)
# elif st.button("Store 2"):
#     file_path = "pages/store_2.py"
#     st.switch_page(file_path)
# elif st.button("Store 3"):
#     file_path = "pages/store_3.py"
#     st.switch_page(file_path)
# elif st.button("Store 4"):
#     file_path = "pages/store_4.py"
#     st.switch_page(file_path)

# `st.markdown(css, unsafe_allow_html=True)` is a Streamlit function that allows you to include custom
# CSS styling within your Streamlit app. In this case, it is injecting the CSS code defined in the
# `css` variable into the HTML of the Streamlit app. The `unsafe_allow_html=True` parameter is used to
# indicate that the HTML content being injected is safe and can be rendered without any security
# concerns. This enables you to apply custom styling to elements in your Streamlit app, such as
# changing the appearance of buttons, containers, or other components.
# st.markdown(css, unsafe_allow_html=True)
# Add buttons for stores at corners


import streamlit as st
import streamlit as st



# Add buttons for stores at corners
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Store 1", key="store1"):
            file_path = "pages/store_1.py"
            st.write("Store 1 selected")
            st.switch_page(file_path)

    with col2:
        if st.button("Store 2", key="store2"):
            file_path = "pages/store_2.py"
            st.write("Store 2 selected")
            st.switch_page(file_path)

    # Add empty space between Store 1 and Store 3
    st.text("")

    col3, col4 = st.columns(2)

    with col3:
        if st.button("Store 3", key="store3"):
            file_path = "pages/store_3.py"
            st.write("Store 3 selected")
            st.switch_page(file_path)

    with col4:
        if st.button("Store 4", key="store4"):
            file_path = "pages/store_4.py"
            st.write("Store 4 selected")
            st.switch_page(file_path)

# Close the container div
st.markdown("</div>", unsafe_allow_html=True)
