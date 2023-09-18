import pandas as pd


#  -------extracting tables from websites----------
# one_piece = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
# print(one_piece[0])

# -------------extracting CSV files from websites---------
results = pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')
# renaming columns
results.rename(columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)
print(results)