import streamlit as st
from monty_hall import simulate_game
import time

st.title("Mantly Hall Problem")

num_games = st.number_input("Enter number of games to simulate", 
                min_value=1,
                max_value=10000
                )

col1, col2 = st.columns(2)
col1.subheader("Win % wihtout switching")
col2.subheader("Win % with Swithching")


chart1 = col1.line_chart(x=None, y=None)
chart2 = col2.line_chart(x=None, y=None)


wins_no_swithc = 0
wins_switch= 0
for i in range(num_games):
    num_wins_with_switching, num_wins_without_switching = simulate_game(1)
    wins_no_swithc +=num_wins_without_switching
    wins_switch += num_wins_with_switching
    chart1.add_rows([wins_no_swithc / (i + 1)])
    chart2.add_rows([wins_switch / (i +1)])
    time.sleep(0.01)