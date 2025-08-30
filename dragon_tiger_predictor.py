import streamlit as st
import random

# -----------------------------
# Setup
# -----------------------------
suits = ["♠", "♥", "♣", "♦"]
ranks = {1: "A", 11: "J", 12: "Q", 13: "K"}
for i in range(2, 11):
    ranks[i] = str(i)

def card_name(card):
    v, s = card
    return f"{ranks[v]}{s}"

def init_shoe(decks=8):
    shoe = []
    for _ in range(decks):
        for v in range(1, 14):
            for s in suits:
                shoe.append((v, s))
    random.shuffle(shoe)
    return shoe

# -----------------------------
# Streamlit App
# -----------------------------
st.title("🔮 Dragon–Tiger Next Card Predictor")

# Initialize session state
if "shoe" not in st.session_state:
    st.session_state.decks = 8
    st.session_state.shoe = init_shoe(st.session_state.decks)
    st.session_state.position = 0

# Controls
with st.sidebar:
    st.header("⚙️ Settings")
    st.session_state.decks = st.number_input("Decks", 1, 20, st.session_state.decks)
    if st.button("🔄 Reset Shoe & Shuffle"):
        st.session_state.shoe = init_shoe(st.session_state.decks)
        st.session_state.position = 0

# Show history
st.subheader("📜 Cards Drawn So Far")
if st.session_state.position == 0:
    st.write("No cards drawn yet.")
else:
    st.write([card_name(c) for c in st.session_state.shoe[:st.session_state.position]])

# Predict next card
if st.session_state.position < len(st.session_state.shoe):
    next_card = st.session_state.shoe[st.session_state.position]
    st.subheader("🔮 Predicted Next Card")
    st.markdown(f"### 👉 {card_name(next_card)}")

    if st.button("➡️ Confirm Draw Next Card"):
        st.session_state.position += 1
else:
    st.subheader("✅ Shoe finished – reshuffle required!")
