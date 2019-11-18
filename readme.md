A tool that reads Ansible files from your repository, derives metrics from the files, and returns a prediction about possible defects in each file.

### ansible-metrics
  A repository to extract 50 different metrics from Ansible files.
  See https://github.com/stefanodallapalma/ansible-metrics for more info and documentation.
  
### main/ansibleDefectPredictor.py
  Script that opens file the file in the specified path, extracts the metrics:
  - Lines of Code
  - Average Task Size
  - Entropy
  - Number of Filters
  - Number of Loops
  - Number of Modules
  - Number of Tasks with No Name
  - Relative Number of External Modules
  - Relative Number of Unique Names
  
Using the ansible-metrics tool. Based on the values of these metrics, a Naive Bayes classifier classifies the file as sound or suspicious. The tool returns the classification and the calculated metrics. 

### Using the script

```
pip3 install -r requirements.txt
python3 ansibleDefectPredictor.py <path-to-ansible-file>
```
