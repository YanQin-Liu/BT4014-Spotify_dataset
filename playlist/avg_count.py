import pandas as pd

df = pd.read_csv('dataset/output.csv')
avg_songs_per_playlist = df.groupby('pid').size().mean()
print(f'Average number of songs per playlist: {avg_songs_per_playlist:.2f}')
