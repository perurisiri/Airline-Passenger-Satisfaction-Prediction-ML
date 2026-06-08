import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.joblib")

st.title("Airline Satisfaction Prediction")

# Categorical
type_of_travel = st.selectbox(
    "Type of Travel",
    ["Business travel", "Personal Travel"]
)

travel_class = st.selectbox(
    "Class",
    ["Business", "Eco", "Eco Plus"]
)

# Numerical
age = st.number_input("Age", min_value=1, max_value=100, value=30)

flight_distance = st.number_input(
    "Flight Distance",
    min_value=0,
    value=1000
)

online_boarding = st.selectbox(
    "Online Boarding",
    [0, 1, 2, 3, 4, 5]
)

wifi = st.selectbox(
    "In-flight WiFi Service",
    [0, 1, 2, 3, 4, 5]
)

entertainment = st.selectbox(
    "In-flight Entertainment",
    [0, 1, 2, 3, 4, 5]
)

seat_comfort = st.selectbox(
    "Seat Comfort",
    [0, 1, 2, 3, 4, 5]
)

leg_room = st.selectbox(
    "Leg Room Service",
    [0, 1, 2, 3, 4, 5]
)

onboard_service = st.selectbox(
    "On-board Service",
    [0, 1, 2, 3, 4, 5]
)

cleanliness = st.selectbox(
    "Cleanliness",
    [0, 1, 2, 3, 4, 5]
)

ease_booking = st.selectbox(
    "Ease of Online Booking",
    [0, 1, 2, 3, 4, 5]
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "type_of_travel": [type_of_travel],
        "class": [travel_class],
        "age": [age],
        "flight_distance": [flight_distance],
        "online_boarding": [online_boarding],
        "in-flight_wifi_service": [wifi],
        "in-flight_entertainment": [entertainment],
        "seat_comfort": [seat_comfort],
        "leg_room_service": [leg_room],
        "on-board_service": [onboard_service],
        "cleanliness": [cleanliness],
        "ease_of_online_booking": [ease_booking]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Passenger is Satisfied")
    else:
        st.error("Passenger is Not Satisfied")