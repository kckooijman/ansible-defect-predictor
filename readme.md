![Model Diagram](https://github.com/kckooijman/ansible-defect-predictor/blob/master/images/Prediction_Model_Diagram.png)

A tool that reads Ansible files from your repository, derives metrics from the files, and returns a prediction about possible defects in each file.

### ansible-metrics
  A repository to extract 50 different metrics from Ansible files.
  See the [Ansible Metric Extractor](https://github.com/stefanodallapalma/ansible-metrics) for more info and documentation.
  
### Using the script

```
pip3 install -r requirements.txt
python3 ansibleDefectPredictor.py <path-to-ansible-file>
```
  
### main/ansibleDefectPredictor.py
  Script that opens file the file in the specified path, extracts the metrics:
  - Average Task Size
  - Depth
  - Entropy
  - Occurrences of Deprecated Keywords
  - Occurrences of Deprecated Modules

  The Number of:
  - Blank Lines of Code
  - Blocks
  - Blocks Error Handling
  - 'Command' Commands
  - Commented Lines of Code
  - Deprecated Keywords
  - Deprecated Modules
  - Inline Conditions
  - Ignore Errors
  - Import Roles
  - Import Tasks
  - Includes
  - Include Roles
  - Include Tasks
  - Include Variables
  - Lines of Code
  - Lookups
  - Logic Operands
  - Loops
  - Modules
  - Names With Variable
  - Shell Commands
  - Tasks with No Name

  
  The Relative Number of:
  - Blank Lines of Code
  - Blocks Error Handling
  - Commented Lines of Code
  - External Modules
  - Names with No Variable
  - Names With Variable
  - Tasks with a Unique Name
  - Unique Names
  
Using the ansible-metrics tool. Based on the values of these metrics, a Naive Bayes classifier classifies the file as sound or suspicious. The tool returns the classification and the calculated metrics. 


