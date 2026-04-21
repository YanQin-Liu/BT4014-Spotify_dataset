# BT4014 - Spotify Song Recommendation with Contextual Bandits

Final project for BT4014 (NUS, AY2025/26 Sem 2). Frames Spotify song recommendation as a contextual bandit: each round a user arrives, the algorithm picks a song cluster, and receives a taste-match reward. Compares 12 algorithms (2 baselines, 8 non-contextual, 2 contextual) over N=10 simulations of T=50,000 steps.

## Notebooks (run in order)

1. [01_data_preparation.ipynb](01_data_preparation.ipynb) - clean the raw song dataset; extract user playlists.
2. [02_feature_diagnostics.ipynb](02_feature_diagnostics.ipynb) - VIF and mutual information to select 7 audio features.
3. [03_feature_engineering.ipynb](03_feature_engineering.ipynb) - build 805 user taste profiles (playlist-mean of features); export tempo normalisation params.
4. [04_parameter_tuning.ipynb](04_parameter_tuning.ipynb) - pick reward function, K for K-means, and all 7 bandit hyperparameters; paired t-tests and window-sensitivity checks.
5. [05_bandit_experiments.ipynb](05_bandit_experiments.ipynb) - run all 12 algorithms and produce the final comparison.

## Folders

- [data/](data/) - raw inputs (song catalog + playlists).
- [outputs/](outputs/) - cleaned data and intermediate artifacts passed between notebooks.
- [archive/](archive/) - earlier iterations kept for reference.

## Data sources

- Kaggle - Spotify Music Analytics Dataset 2015-2025: https://www.kaggle.com/datasets/rohiteng/spotify-music-analytics-dataset-20152025
- Gigasheet - Spotify sample dataset: https://www.gigasheet.com/sample-data/spotify-dataset

## References

- Li, L., Chu, W., Langford, J., & Schapire, R. E. (2010). A contextual-bandit approach to personalized news article recommendation. *WWW '10*.
- Agrawal, S., & Goyal, N. (2013). Thompson sampling for contextual bandits with linear payoffs. *ICML*.
- Eckles, D., & Kaptein, M. (2014). Thompson sampling with the online bootstrap. *arXiv:1410.4009*.
- Bouneffouf, D., Rish, I., & Aggarwal, C. (2020). Survey on applications of multi-armed and contextual bandits. *IEEE CEC*.
