# Project description

This is a simple data exploration of publically avilable FDA drug adverse reaction data (https://open.fda.gov/apis/drug/event/)

## Installation
All code is in Python3.10 and the dependencies are specified in requirements.txt
```
pip install requirements.txt
```

## Folder structure

There are two notebooks used for analysis and visualization:

- Basic_EDA.ipynb is using OpenFDA available API to extract basic statistics from the database, relying on `count` feature
- download_data.py is used to download part of the data locally
- Drug_Reaction_exploration.ipynb is exploring some relations of the drug type, drug indication and adverse event.



