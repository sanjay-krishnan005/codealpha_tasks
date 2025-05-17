Spotify Music Recommendation System

A machine learning-based project that uses clustering (K-Means) to recommend similar songs based on a user's input. This project leverages Spotify's audio features to find tracks that match the input song's characteristics.

Features

Uses Spotify audio features such as danceability, energy, tempo, valence, etc.

Implements K-Means clustering to group similar songs.

Recommends tracks based on the cluster of a given song.

Preprocessed dataset of Spotify songs (2010–2020).

Requirements

Python 3.7+

pandas

numpy

scikit-learn

matplotlib (optional for visualization)

How it Works

Load and preprocess the dataset.

Normalize the audio feature columns.

Apply K-Means clustering to group similar songs.

Given an input song, find its cluster and recommend other songs from the same cluster.

License

This project is open-source and available under the MIT License.

