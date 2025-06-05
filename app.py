
import streamlit as st

st.set_page_config(page_title="Dhruvi the Explorer: USA Life Tour", page_icon="🧭", layout="centered")

# --- Welcome Section ---
st.title("🎒 Dhruvi the Explorer: Your USA Life Trial 🌎")

st.image("images/usa_welcome.png", caption="Fresh off the flight, ready to explore!", use_container_width=True)

st.markdown("""
### 🥳 Welcome to USA, get ready for adventure!

This isn’t just a regular trip. It’s a big step in your life journey — exploring what it might be like to live in California 🇺🇸

You’ll spend 3 weeks with **Local Baba** — your personal guide and spiritual-cooking-lifestyle-nerd companion.

You'll make fun choices, see what life could look like here - try out all the options 💡

No pressure. Just play, laugh, and imagine ✨
""") 
# --- Trip Overview ---
st.subheader("🗓️ The Journey Ahead")

st.markdown("""
You'll be here from **July 18 – August 2**, and here's what the rough layout looks like:

- **Weekend 1:** ✨ Satsang + Explore San Francisco
- **Weekdays:** 🧘‍♀️ Mountain View day-to-day life with Local Baba
- **Weekend 2:** 🌴 Choose your travel adventure: San Diego, Vegas, or Arizona
- **Weekdays Again:** 🍜 Chill local life (Target, cooking, yoga, etc.)
- **Final Weekend:** 🌲 Pick a final trip: Tahoe, Yosemite, or Big Sur

So... this isn't just a game, it's a sneak peek into a possible *life chapter*. Enjoy imagining it 😊
            
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
                      "Ghirardelli Square Chocolate 🍫",
                      "Cable Car Ride 🚋",
                      "Alcatraz Prison Tour 🏰",
                      "Stanford mai padhai karo 📚",
    ])

if sf_choice == "Golden Gate Selfies 📸":
    st.success("Ye nai kiya toh zindagi mai kya kiya? 😄")
elif sf_choice == "Meet Local Baba's Friends 👯":
    st.success("Mil lo hamare haseen dosto se! My friends are the best and they will love you too!")
elif sf_choice == "Eat Indian Food in Berkeley 🍛":
    st.warning("Berkely is nice. Student town!")
elif sf_choice == "Watch Sunset from Twin Peaks 🌄":
    st.success("You’ll never forget that view! It's a must do.")
elif sf_choice == "Ghirardelli Square Chocolate 🍫":
    st.info("Dairy milk is better")
elif sf_choice == "Cable Car Ride 🚋":
    st.info("Will be my first time too!")
elif sf_choice == "Alcatraz Prison Tour 🏰":
    st.info("Jail dekhna hai kya")
elif sf_choice == "Stanford mai padhai karo 📚":
    st.info("Beautiful campus!")

# --- Weekday Activities ---
st.header("📅 Weekday Life in Mountain View")
st.markdown("Now for a peek into day-to-day living:")

restaurant = st.radio("Pick your first restaurant experience:", 
                      ["In-N-Out 🍔", "Desi Dosa Place 🍛", "Local Baba's Kitchen 👨‍🍳"])
if restaurant == "In-N-Out 🍔":
    st.info("USA ka vada paav")
elif restaurant == "Desi Dosa Place 🍛":
    st.info("Madras ki yaad aa jaegi Mountain View mai")
elif restaurant == "Local Baba's Kitchen 👨‍🍳":
    st.info("Iska toh koi beat hi nai hai")


todo = st.radio("What would you like to do on a weekday evening?", 
    ["Trader Joe's Run 🛒", 
     "Yoga with Baba 🧘", 
     "Walk in Shoreline Park 🚶", 
     "Half moon bay palace 🌊",
     "Call Parents 😅", 
     "Co-working at a cafe ☕", 
     "Try a weird Asian snacks 🍭", 
     "Get confused at CVS for 20 minutes 🧴",
     "Go feed the cows 🐄",
     "Go to the local farmer's market 🥕",
     "Visit Gurudwara that I never go to 🕌",
     "Eat the best vegan sushi ever 🍣",
     "Shopping 🛍️"])

if todo == "Trader Joe's Run 🛒":
    st.info("He who masters Trader Joe’s freezer aisle, masters life. Welcome to USA, where we have freshly frozen samosas.")
elif todo == "Yoga with Baba 🧘":
    st.warning("I don't do yoga, but who knows maybe this will make me start.")
elif todo == "Walk in Shoreline Park 🚶":
    st.success("Sunset toh banta hai.")
elif todo == "Half moon bay palace 🌊":
    st.success("THIS I AM DEFINITELY GOING TO SHOW YOU IT's MY FAVORITE PLACE EVAAAAAAA")
elif todo == "Call Parents 😅":
    st.success("Aww, they miss you already!")
elif todo == "Co-working at a cafe ☕":
    st.warning("Meet my grandparents probably from another life - at Cafe Capuchino.")
elif todo == "Try a weird Asian snacks 🍭":
    st.info("Bay area is weird im telling you.")
elif todo == "Get confused at CVS for 20 minutes 🧴":
    st.info("Okay this is totally CHATGPT option, i will admit. But it happens.")
elif todo == "Go feed the cows 🐄":
    st.info("Kabhi India mai bhi nai kiya hoga")
elif todo == "Go to the local farmer's market 🥕":
    st.info("Gajar khareedne. Idhar koi dunzo nai hai.")
elif todo == "Visit Gurudwara that I never go to 🕌":
    st.info("Suppressed desire of mine that has not been fultilled yet. :P")
elif todo == "Eat the best vegan sushi ever 🍣":
    st.info("It's called Shizen - thank me later. USA ka paisa vasool.")
elif todo == "Shopping 🛍️":
    st.info("Kuch toh khareedo ge na?")

# --- Weekend 2 Travel ---
st.header("🏖️ Weekend 2: Big Travel Time")
trip2 = st.radio("Choose your weekend destination:", ["San Diego", "Las Vegas", "Phoenix"])

if trip2 == "San Diego":
    st.image("https://i.imgur.com/JnYvQJm.jpeg", caption="Beach walks and burritos")
    st.write("Nice choice! Looks like you like the beach huh. In San Diego, you explore neighborhoods, eat tacos, and vibe with the ocean. Book and airbnb on the beach. Explore the fancy restraunts at night. It's one of my family's favorite places to go vacation. And I've heard they have some nice night life too!")
    st.write("Here are some of my favorite places in San Diego")
    st.write("Mission Beach - https://www.sandiego.org/explore/things-to-do/beaches-bays/mission-beach.aspx - there are so many cool air bnb's here and it's right next to the beach. This is where I had gone with Mom and Dad and sent you photos. It's a great vibe.")
    st.write("Coronado - has some huge beaches and some great restraunts - https://www.ilfornaio.com/location/il-fornaio-coronado/ a fav one")
elif trip2 == "Las Vegas":
    st.image("https://i.imgur.com/0UCD9YM.png", caption="Lights, dice, and too many signs")
    st.write("You laugh, dance, lose 5 dollars, and win a weird keychain. Maybe more than 5 dollars, much more.")
    st.write("Or you win, who knows!?")
    st.write("Vegas is Vegas and yeah definitely a must go if you've never been. It's drivable 5 hours from Phoenix too.")
else:
    st.image("https://i.imgur.com/7xxisoE.jpeg", caption="Meet the fam!")
    st.write("You have deep convos, masala chai, and sleep a lot. Well deep convos will be had anyway I'm sure :)")
    st.write("There are so many places to go around here!")
    st.write("All time favorite is Sedona which we had gone with your Dad! https://www.sedona.net/")



# --- Final Weekend Trip ---
st.header("🌲 Final Weekend: One Last Adventure")
trip3 = st.radio("Choose your final weekend destination:", 
                 ["Lake Tahoe", "Yosemite", "Big Sur & Monterey"])

if trip3 == "Lake Tahoe":
    st.image("https://i.imgur.com/C51zFcJ.jpeg", caption="Snowy serenity")
elif trip3 == "Yosemite":
    st.image("https://i.imgur.com/3PQKz5R.jpeg", caption="Majestic waterfalls and granite cliffs")
elif trip3 == "Big Sur & Monterey":
    st.image("https://i.imgur.com/eJpEC4I.jpeg", caption="Coastal curves and ocean breezes")

# --- Summary ---
st.header("💌 Your Custom Itinerary Summary")

st.markdown("### 📓 Your 3-Week USA Life Trial with Local Baba")

st.markdown(f"**Satsangs attended:** {', '.join(satsang_choices) if satsang_choices else 'None 😇'}")
st.markdown(f"**Post-satsang SF fun:** {sf_choice}")
st.markdown(f"**Weekday restaurant:** {restaurant}")
st.markdown(f"**Weekday activity:** {todo}")
st.markdown(f"**2nd Weekend Trip:** {trip2}")
st.markdown(f"**Final Weekend Adventure:** {trip3}")


st.markdown("---")
st.markdown("✨ *Created with 🧡 by Local Baba for Dhruvi the Explorer* ✨")


