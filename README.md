OVERVIEW

The Club Action Map is a Streamlit application designed to visualize player actions during football matches. Users can filter actions by player and action type, providing an interactive way to analyze player performance on the pitch.

FEATURES

- Interactive Filters: Select a player and specific action to visualize.
- Visual Representation: Actions are plotted on a pitch diagram, giving a clear view of where on the pitch each action occurred.

REQUIREMENTS

To run this application, you need to have Python installed along with the following packages:

- Streamlit
- Pandas
- mplsoccer

INSTALLATION
1. Install Required Packages:
   Open the terminal in your project directory and run:
   ```bash
   pip install streamlit pandas mplsoccer
   ```

2. Run the Application:
   Execute the following command in the terminal:
   ```bash
   streamlit run club_action_map.py (insert your python file name here)
   ```

HOW TO USE
1. Launch the application using the command above.
2. In the web interface, select a player from the dropdown menu.
3. Select an action to visualize specific actions performed by the player.
4. The pitch will display the selected player's actions in a blue marker.

DATA

The application uses a CSV file (`club_actions.csv`) containing the following columns:

- `player`: Name of the player
- `action`: Type of action performed
- `x`: X-coordinate on the pitch
- `y`: Y-coordinate on the pitch

Ensure the CSV file is formatted correctly and located in the same directory as the script.

DEVELOPMENT

This application was developed using Visual Studio Code.
