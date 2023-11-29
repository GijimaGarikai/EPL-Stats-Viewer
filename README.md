~Made this in 2022 and probably not coming back to finish but it was fun to work on and I forgot to make it public so here we go :3~
# English Premier League (EPL) Statistics Viewer

This Python script fetches and displays English Premier League (EPL) statistics using the Sportdata API. It allows users to select a season and view detailed statistics for their favorite teams.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Team Selection](#team-selection)
- [Team Stats](#team-stats)
- [Background Image](#background-image)

## Prerequisites

Make sure you have Python installed on your system.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/epl-stats-viewer.git
    ```

2. Install the required Python packages:

    ```bash
    pip install requests streamlit pandas Pillow
    ```

## How to Use

Run the script using the following command:

```bash
streamlit run epl_stats_viewer.py
```

This will launch a Streamlit web app where you can interact with the EPL statistics.

## Team Selection

Choose two teams from the sidebar dropdown menus to view their statistics. The team options are listed by their positions in the league.

## Team Stats

The script fetches the latest EPL standings for the selected season and displays the positions, points, and goals scored for the chosen teams.

## Background Image

The app has a background image featuring the Premier League logo. This provides a visually appealing backdrop for the statistics.
