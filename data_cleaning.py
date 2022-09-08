import pandas as pd
import numpy as np


X = pd.Series([2.1, 2.2, 4.5, 2.2, 2.3])


# Median based anomaly detection
def median_based_anomaly_detection(series, threshold):  # Set a range/threshold
    " Range for normal data: |data - median| <= threshold "
    outliers = []
    for i in series:
        if abs(i - np.median(series)) > threshold:
            outliers.append(i)
    return outliers


def mean_based_anomaly_detection(series):
    " Range for normal data: (mean - std) <= data <= (mean + std) "
    outliers = []
    for i in series:
        if i < (np.mean(series) - np.std(series)) or i > (np.mean(series) + np.std(series)):
            outliers.append(i)
    return outliers


def z_score_anomaly_detection(series, threshold):  # Z-Score is a statistical measure that shows how many standard deviations a value is from the mean.
    " Range for normal data: z-score = |data - mean| / std <= threshold "
    outliers = []
    for i in series:
        z_score = abs(np.mean(series) - i) / np.std(series)
        if z_score > threshold:
            outliers.append(i)
    return outliers


def interquatile_anomaly_detection(series):  # interquatile (IQR), between 1st and 3rd quatile (Q1 & Q3)
    " Range for normal data: Q1 - 1.5*IQR <= data <= Q3 + 1.5*IQR "
    Q1, Q3 = np.percentile(series, [25, 75])  # np.percentile(list, [percentage1, percentage2, ...])
    IQR = Q3 - Q1
    outliers = []
    for i in series:
        if i < Q1 - 1.5*IQR or i > Q3 + 1.5*IQR:
            outliers.append(i)
    return outliers


print(median_based_anomaly_detection(X, 2))
print(mean_based_anomaly_detection(X))
print(z_score_anomaly_detection(X, 1.5))
print(interquatile_anomaly_detection(X))
