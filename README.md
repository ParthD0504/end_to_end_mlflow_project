# end_to_end_mlflow_project

## workflow

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py





# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/ParthD0504/end_to_end_mlflow_project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

import dagshub
dagshub.init(repo_owner='parthdeshmukh0504', repo_name='end_to_end_mlflow_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/parthdeshmukh0504/end_to_end_mlflow_project.mlflow

export MLFLOW_TRACKING_USERNAME=parthdeshmukh0504 

export MLFLOW_TRACKING_PASSWORD=d45615a048bb8f72fd3e758203721f6a117b8c9f

```
