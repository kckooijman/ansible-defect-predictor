import joblib
import numpy as np
import os
import re
import sys
import yaml

from io import StringIO

# metrics
from ansiblemetrics.general import etp, loc, nfl, nlo, nun
from ansiblemetrics.tasks import atss, nmd, nlp, ntnn, nemd


def list_yaml_files(repository):
    yaml_files = []
    for root, dirs, files in os.walk(repository):
        for file in files:
            if file.endswith(".yml"):
                # print(os.path.join("repository", file))
                rel_dir = os.path.relpath(root, repository)
                rel_file = os.path.join(rel_dir, file)
                path = os.path.join(repository, rel_file)
                yaml_files.append(path)
    return yaml_files


def load(path):
    """ Returns a StringIO object representing the content of the file at <path>, if any; None otherwise """
    if not os.path.isfile(path):
        return None

    content = StringIO()
    with open(path, 'r') as file:
        for line in file.readlines():
            content.write(re.sub(r'\s{2,2}', '\\t', line).expandtabs(2))

    return content


"""
Call the script in the command line with
    python <path>/ansibleDefectPredictor.py <path-to-file>
"""
if __name__ == '__main__':
    # Get list of yaml files from repo
    file = sys.argv[1]

    # Calculate metrics:
    try:
        counts = {'loc_count': loc.LOC(load(file)).count(),
                  'atss_count': atss.ATSS(load(file)).count(),
                  'etp_count': etp.ETP(load(file)).count(),
                  'nfl_count': nfl.NFL(load(file)).count(),
                  'nlo_count': nlo.NLO(load(file)).count(),
                  'nmd_count': nmd.NMD(load(file)).count(),
                  'nlp_count': nlp.NLP(load(file)).count(),
                  'ntnn_count': ntnn.NTNN(load(file)).count(),
                  'nemd_count_rel': nemd.NEMD(load(file)).count(relative=True),
                  'nun_count_rel': nun.NUN(load(file)).count(relative=True)}
    except yaml.YAMLError as exc:
        print(exc)
        raise

    # Load classifier and classify file.
    clf = joblib.load('model/NaiveBayes.joblib')
    pred = clf.predict(np.fromiter(counts.values(), dtype=float).reshape(1, -1))

    if pred[0] == 0:
        print('File classified as sound!')
        print('File parameters: ', counts)
    else:
        print('Suspicious file found!')
        print('File parameters: ', counts)
