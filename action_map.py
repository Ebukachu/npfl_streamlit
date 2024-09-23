import streamlit as st
import pandas as pd
from mplsoccer import VerticalPitch

# Streamlit app title and subheader
st.title("Club Action Map")
st.subheader("Filter to any player to see all their actions!")

# Load the data
df = pd.read_csv('club_actions.csv')
df = df[['player', 'action', 'x', 'y']]



# Function to filter the DataFrame
def filter_data(df: pd.DataFrame, player: str, action: str):
    if player:
        df = df[df['player'] == player]
    if action:
        df = df[df['action'] == action]
    return df

# Function to plot actions on the pitch
def plot_actions(df, ax, pitch):
    general_color = 'blue'  # General color for all actions
    for x in df.itertuples(index=False):
        pitch.scatter(
            x=float(x.x) * 1.2,  # Scale x coordinate
            y=float(x.y) * 0.8,  # Scale y coordinate
            ax=ax,
            s=300,  # Marker size
            color=general_color,
            edgecolors='black',
            alpha=0.7
        )

# Get unique players and actions for filtering
unique_players = df['player'].sort_values().unique()
unique_actions = df['action'].sort_values().unique()

# Filter the df based on user input
player = st.selectbox("Select a player", unique_players, index=None)
action = st.selectbox("Select an action", unique_actions, index=None)
filtered_df = filter_data(df, player, action)

# Set up the pitch visualization
pitch = VerticalPitch(pitch_type='statsbomb', line_zorder=2, pitch_color='#f0f0f0', line_color='black', half=False)
fig, ax = pitch.draw(figsize=(10, 10))

# Plot the filtered actions
plot_actions(filtered_df, ax, pitch)

# Display the pitch with actions
st.pyplot(fig)
