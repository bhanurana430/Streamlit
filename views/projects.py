import streamlit as st

st.title('These are some of my projects')

st.divider()

# List of projects
projects = [
    {
        "name": "DRL for Stock Trading",
        "image": "static/project img/DRL.jpg",  # Replace with actual image URL
        "short_desc": "Using Deep Reinforcement Learning models like DQN and PPO to trade stocks",
        "page": "DRL",
        "col" : 1
    },
    {
        "name": "Backtesting - VectorBt",
        "image": "static/project img/DRL.jpg",
        "short_desc": "Using VectorBt library to analyze and backtest trading strategies",
        "page": "VectorBT",
        "col" : 2
    },
    {
        "name": "LSMT Forecasting on financial data",
        "image": "static/project img/DRL.jpg",
        "short_desc": "Using Long Short Term Memory networks to forecast stock prices - Regression and Classification", 
        "page": "LSTM-forecasting",
        "col" : 1
    },
    {
        "name": "Titanic Survival Prediction",
        "image": "static/project img/DRL.jpg",
        "short_desc": "Full FLedged ML project to predict survival on Titanic dataset - With deployed website",
        "page": "titanic",
        "col" : 2
    },
    {
        "name": "Table Tennis Analyzer",
        "image": "static/project img/DRL.jpg",
        "short_desc": "Leveraging OpenCV to analyze table tennis matches and provide insights - Includes an automated scoreboard",
        "page": "table-tennis",
        "col" : 1
    },
    {
        "name": "Time Series Analysis",
        "image": "static/project img/DRL.jpg",
        "short_desc": "Less of a project, more of a learning journey - Includes various time series forecasting techniques and models",
        "page": "time-series",
        "col" : 2
    }
]

# Display projects as cards
col1, col2 = st.columns(2)  # Create columns dynamically

for i, project in enumerate(projects):
    if project["col"] == 1:
        cols = col1
        with cols:
            st.image(project["image"], width=300)
            st.write(f"**{project['name']}**")
            st.write(project["short_desc"])
            if st.button(f"Learn More", key=project["page"]):
                st.session_state["selected_project"] = project["page"]
                st.rerun()
            st.divider()
    else:
        cols = col2
        with cols:
            st.image(project["image"], width=300)
            st.write(f"**{project['name']}**")
            st.write(project["short_desc"])
            if st.button(f"Learn More", key=project["page"]):
                st.session_state["selected_project"] = project["page"]
                st.rerun()
            st.divider()

# Redirect to the selected project page
if "selected_project" in st.session_state:
    st.switch_page(st.session_state["selected_project"])
