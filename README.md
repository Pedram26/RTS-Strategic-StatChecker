# RTS-Strategic-StatChecker
Visualize eSports pros playtime, and compare them with yourself or against other teams. This project tracks the number of games that eSports pros play in real time. You can also track individual users by simply adding their username to a database. It currently has support for the two popular startegic games of StarCraft and League of Legends.
![Image] (images/gallery.jpg)

## Inspiration
Simply, our love of games!

## Dependencies
- Python 3.5

## Installation and Usage
- `pip install requests`
- To run the program, run the main.py script.

## How We Built It
We started with a database of eSports players. We implemented requests from Blizzard and Riot Games API to pull data on games played by those players and update statistics including but not limited to associated region, number of games played, number of games played by region, if they have multiple account (smurfs). Plotly then takes this data to provide two graphs: a stacked bar graph showing how many games each player has played while highlighting games played across multiple accounts, as well as a grouped bar graph for comparing games played between each player on an eSports team sorted by role. This project is coded in plotly and Python, taking advantage of .csv databases.

## Authors
- Ariel Hirschberg
- Pedram Pourdavood
- Clayton Finney

