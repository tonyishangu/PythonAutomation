import pandas as pd
import camelot

#  -------extracting tables from websites----------
one_piece = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
print(one_piece[0])

# -------------extracting CSV files from websites---------
results = pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')
# renaming columns
results.rename(columns={'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)
print(results)

# ---------------extract tables from PDFs----------------
tables = camelot.read_pdf('nameofpdf', pages='page you want')
# export to csv
tables.export('nameoffile.csv', f='csv', compress=True)
tables[0].to_csv('nameoffile.csv')      #export the first table