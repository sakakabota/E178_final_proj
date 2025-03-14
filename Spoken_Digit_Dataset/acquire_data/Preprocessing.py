import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Find the recordings
recordings_path = "/Users/sakakabota/Desktop/SPRING\ \'25/E178/final_proj/Spoken_Digit_Dataset/recordings "

digit_counts = Counter()

for file in os.listdir(recordings_path):
    digit = file[0]

digit
