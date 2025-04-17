import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit.")

st.header("🚀 Welcome to Your Growth Journey.")
st.write("Embrace challanges,learn from mistakes,and Unlock your full potential.This AI Powered app helps you build a growth mindset with reflections,challanges and achievements!.⭐")

# quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("“Success is not final, failure is not fatal: its the courage to continue that counts.” Winston Churchill")

st.header("🔧 What's Your Challange Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# condition

if user_input:
    st.success(f"💪you re facing {user_input}.keep pushing forward towards you'r goal!.🚀")
else:
    st.warning("Please enter a challenge to get started.")


# relection section
st.header("📝 Reflect on Your Growth")
reflection = st.text_area("Share your thoughts on a recent experience that helped you grow:")

if reflection:
    st.success(f"✨Great Insight! your reflection: {reflection}.")
else:
    st.info("Reflecting on past experiances Help you grow!.Share you'r difficulties.")

# achievements section

st.header("🏆 Celeberate Your Wins!")
achievement = st.text_input("Share a recent achievement, no matter how small:")

if achievement:
    st.success(f"🎉 Awesome! You achieved: {achievement}. Keep up the great work!")
else:
    st.info("Every step counts! Share your achievements to inspire yourself and others.")

# footer section

st.write("- - -")
st.write("🌱 Remember, growth is a journey, not a destination. Embrace the process and keep pushing forward!")
st.write("⛔ Created by Hammad Afzal.")
