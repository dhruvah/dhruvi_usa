
import streamlit as st

st.set_page_config(page_title="Dhruvi the Explorer: USA Life Tour", page_icon="🧭", layout="centered")

# --- Welcome Section ---
st.title("🎒 Dhruvi the Explorer: Your USA Life Trial 🌎")

st.image("https://i.imgur.com/BQaiUuF.jpeg", caption="Fresh off the flight, ready to explore!", use_column_width=True)

st.markdown("""
### 🥳 Welcome to USA, get ready for adventure!

This isn’t just a regular trip. It’s a big step in your life journey — exploring what it might be like to live in California 🇺🇸

You’ll spend 3 weeks with **Local Baba** — your personal guide and spiritual-cooking-lifestyle-nerd companion.

You'll make fun choices, see what life could look like here, and get a custom summary at the end 💡

No pressure. Just play, laugh, and imagine ✨
""") 

# --- Satsang Selection ---
st.header("🛕 Satsang Options")
st.markdown("Spiritual vibes included. Snacks optional.")

satsang1 = st.radio("Will you attend the July 19 (Saturday morning) satsang?", ["Yes 🙏", "No thanks 😴"])
satsang2 = st.radio("How about the August 1 (Friday evening) satsang?", ["Yes 💫", "Nope 🙃"])

satsang_choices = []
if satsang1 == "Yes 🙏":
    satsang_choices.append("July 19 - Saturday Morning")
    st.success("You feel energized and spiritually lifted!")
else:
    st.info("No worries — you took your time easing in!")

if satsang2 == "Yes 💫":
    satsang_choices.append("August 1 - Friday Evening")
    st.success("A divine way to wrap up your visit!")
else:
    st.info("You decided to rest before heading home.")

# --- SF Chill Weekend ---
st.header("🌉 Weekend 1: Chill in San Francisco")

sf_choice = st.radio("What would you most love to do after satsang?", 
                     ["Golden Gate Selfies 📸", 
                      "Meet Local Baba's Friends 👯", 
                      "Eat Indian Food in Berkeley 🍛", 
                      "Watch Sunset from Twin Peaks 🌄",
                      "Check out the local beaches",
                      "Get the best coffee in the world"])

# --- Weekday Activities ---
st.header("📅 Weekday Life in Mountain View")
st.markdown("Now for a peek into day-to-day living:")

restaurant = st.radio("Pick your first restaurant experience:", 
                      ["In-N-Out 🍔", "Tamarine 🥢", "Desi Dosa Place 🍛", "Local Baba's Kitchen 👨‍🍳"])

todo = st.radio("What would you like to do on a weekday afternoon?", 
                ["Trader Joe's Run 🛒", "Yoga with Baba 🧘", "Walk in Shoreline Park 🚶", "Call Parents 😅"])



# --- Weekend 2 Travel ---
st.header("🏖️ Weekend 2: Big Travel Time")
trip2 = st.radio("Choose your weekend destination:", ["San Diego", "Las Vegas", "Arizona (Visit Parents)"])

if trip2 == "San Diego":
    st.image("https://i.imgur.com/N05kkfV.jpeg", caption="Beach walks and burritos")
    st.write("You explore neighborhoods, eat tacos, and vibe with the ocean. Book and airbnb on the beach. Explore the fancy restraunts at night.")
elif trip2 == "Las Vegas":
    st.image("https://i.imgur.com/VaPZs8l.jpeg", caption="Lights, dice, and too many signs")
    st.write("You laugh, dance, lose $5, and win a weird keychain. Maybe more than $5.")
else:
    st.image("https://i.imgur.com/tjKXoxf.jpeg", caption="Meet the fam!")
    st.write("You have deep convos, masala chai, and sleep a lot. Well deep convos will be had anyway I'm sure :)")

# --- Weekend 3 Chill ---
st.header("🧺 Weekdays: Local Life Feels")
chill3 = st.radio("How do you want to spend a low-key weekend?",
                  ["Cook a meal together 🥘", "Go to Target 🛍️", "Movie Night 🎬", "Clean the apartment 🧽"])

# --- Final Weekend Trip ---
st.header("🌲 Final Weekend: One Last Adventure")
trip3 = st.radio("Choose your final weekend destination:", 
                 ["Lake Tahoe", "Yosemite", "Big Sur & Monterey"])

if trip3 == "Lake Tahoe":
    st.image("https://i.imgur.com/0e6NquO.jpeg", caption="Snowy serenity")
elif trip3 == "Yosemite":
    st.image("https://i.imgur.com/KX2mSLM.jpeg", caption="Majestic waterfalls and granite cliffs")
elif trip3 == "Big Sur & Monterey":
    st.image("https://i.imgur.com/FjO2cNW.jpeg", caption="Coastal curves and ocean breezes")

# --- Summary ---
st.header("💌 Your Custom Itinerary Summary")

st.markdown("Here’s what you chose for your 3-week USA sampler with Local Baba:")

st.markdown(f"**Satsangs attended:** {', '.join(satsang_choices) if satsang_choices else 'None 😇'}")
st.markdown(f"**Post-satsang SF fun:** {sf_choice}")
st.markdown(f"**Weekday restaurant:** {restaurant}")
st.markdown(f"**Weekday activity:** {todo}")
st.markdown(f"**2nd Weekend Trip:** {trip2}")
st.markdown(f"**3rd Weekend Local Fun:** {chill3}")
st.markdown(f"**Final Weekend Adventure:** {trip3}")

st.markdown("---")
st.markdown("Created with 🧡 by Local Baba for Dhruvi the Explorer")
