import streamlit as st

# Title and Introduction
st.title("EcoBot: Your Sustainable Living Assistant")
st.header("🌱 Let's help you live more sustainably!")

# User Input Section
st.header("Tell us about your daily habits:")
electricity = st.slider("Monthly electricity usage (in units):", 0, 1000, 200)
transportation = st.selectbox("Main mode of transportation:", ["Car", "Bike", "Public Transport", "Walk"])
waste = st.selectbox("How do you dispose of food waste?", ["Compost", "Throw away", "Feed animals"])

# Suggestion Section
if st.button("Get Tips"):
    st.subheader("🌟 Personalized Eco-Friendly Tips:")
    if electricity > 500:
        st.write("🔌 Reduce electricity usage by turning off appliances when not in use.")
    if transportation == "Car":
        st.write("🚗 Switch to carpooling or public transport to reduce emissions.")
    if waste == "Throw away":
        st.write("🌱 Start composting food scraps to reduce waste.")
    else:
        st.write("🎉 Great job! Keep up the good work!")

# Visualization Section
import matplotlib.pyplot as plt

st.header("Your Progress")
data = [50, 30, 20]  # Example data (can be dynamic)
labels = ["Electricity", "Transport", "Waste"]

fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct='%1.1f%%')
st.pyplot(fig)

# Carbon Footprint Calculator
def calculate_footprint(electricity, transportation):
    transport_emissions = {"Car": 2.3, "Bike": 0.5, "Public Transport": 0.8, "Walk": 0}
    footprint = (electricity * 0.7) + (transport_emissions[transportation] * 30)
    return footprint

footprint = calculate_footprint(electricity, transportation)
st.write(f"🌍 Your estimated carbon footprint is {footprint:.2f} kg CO₂ per month.")

# Chatbot Section
import openai

st.header("Ask EcoBot!")
question = st.text_input("Type your question:")
if st.button("Ask"):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Provide an eco-friendly solution for: {question}",
        max_tokens=100
    )
    st.write(response["choices"][0]["text"])
