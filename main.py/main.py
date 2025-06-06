import streamlit as st
import smtplib
from email.message import EmailMessage

st.header("Welcome to our Video Game Store")
st.subheader("We're glad to have you here!")

# Store selected games in session
x = st.session_state.setdefault("words", [])

# User inputs
name = st.text_input("What is your name?")
gmail = st.text_input("What is your Gmail address?")

if name:
    st.write(f"Hello {name}!")

# Game selection
st.write("We have the following games. Which would you like to buy?")
selected_game = st.selectbox("Games in stock:", ["", "minecraft", "free fire", "call of duty", "GTA5"])

if selected_game and selected_game not in x:
    st.write(f"{selected_game} is a great choice!")
    x.append(selected_game)

# User rating
rating = st.slider("What will you rate us?", 1, 5)

st.write(f"Your order list is {x}")

# Send email on button click
if st.button("Send order confirmation to Gmail"):
    if gmail and "@" in gmail:
        try:
            # Compose email
            msg = EmailMessage()
            msg['From'] = "goyalskonark532@gmail.com"
            msg['To'] = gmail
            msg['Subject'] = "Your ordered list from our game shop"
            msg.set_content(f"Hello {name},\n\nThank you for your order!\n\nYou ordered: {', '.join(x)}\nYour rating: {rating}/5\n\nWe appreciate your support!\n\n- Game Store Team")

            # Send email via SMTP
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login("goyalskonark532@gmail.com", "aqfd lgbm patx tybc")  # Use environment variables instead
                server.send_message(msg)

            st.success("Email sent successfully.")
        except Exception as e:
            st.error(f"Failed to send email: {e}")
    else:
        st.warning("Please enter a valid Gmail address.")
