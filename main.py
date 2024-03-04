import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    "Date": ["2015-06-20", "2015-06-21", "2015-06-22", "2015-06-23", "2015-06-24"],
    "Store_1_actual_Sales": [1.021029, 0.158782, 0.621737, 0.564550, 0.570365],
    "Store_1_forecast_sale": [1.029717, -0.025151, 0.962598, 0.985394, 0.975543],
    "Store_2_actual_Sales": [0.8, 0.7, 0.9, 0.6, 0.5],
    "Store_2_forecast_sale": [0.85, 0.75, 0.95, 0.65, 0.55],
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

# Streamlit app
st.title("Store Sales Visualization")

# Dropdown for store selection
selected_store = st.selectbox(
    "Select Store:", options=[col for col in df.columns if "actual_Sales" in col]
)

# Plot actual and forecast sales for the selected store
fig, ax = plt.subplots(figsize=(10, 6))
store_name = selected_store.split("_")[1]
ax.plot(df.index, df[selected_store], label=f"{store_name} Actual Sales", marker="o")
forecast_column = selected_store.replace("actual_Sales", "forecast_sale")
ax.plot(df.index, df[forecast_column], label=f"{store_name} Forecast Sales", marker="o")

ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.set_title(f"Sales Comparison for {store_name}")
ax.legend()

# Display the plot using st.pyplot()
st.pyplot(fig)

# Display DataFrame
st.write(df)
