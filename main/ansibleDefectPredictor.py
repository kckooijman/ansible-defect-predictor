import joblib
import numpy as np
import sys
import yaml


from metrics import get_metrics_from_file

# metrics
"""
Call the script in the command line with
    python <path>/ansibleDefectPredictor.py <path-to-file>
"""
if __name__ == '__main__':
    # Get list of yaml files from repo
    file = sys.argv[1]

    # Calculate metrics:
    try:
        counts = get_metrics_from_file(file)
    except yaml.YAMLError as exc:
        print(exc)
        raise

    # Load classifier and classify file.
    clf = joblib.load('model/NaiveBayesOutliers.joblib')
    pred = clf.predict(np.fromiter(counts.values(), dtype=float).reshape(1, -1))

    if pred[0] == 0:
        print('File classified as sound!')
        print('File parameters: ', counts)
    else:
        print('Suspicious file found!')
        print('File parameters: ', counts)
