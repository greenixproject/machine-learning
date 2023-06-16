# machine-learning
Machine Learning Deployment

## Folder Structure
### Food_Greenix
Food_Greenix contain the dataset used for training. This folder also contains the code for generating the dataset.
The folder also contain the model food used machine learning with format .h5 and .json. The model generated from the dataset is stored in this folder.

### Vehicle_Greenix
Food_Greenix contain the dataset used for training. This folder also contains the code for generating the dataset.
The folder also contain the model transportation used machine learning with format .h5 and .json. The model generated from the dataset is stored in this folder.


## Minimum Requirements
- Nodejs
- TensorflowJs
- express

## Installation instructions
Fork and clone the forked repository:
```shell
git clone git://github.com/<your_fork>/API-ML
```
Install requirement libraries:
```shell
npm install
```
Run **server.js**:
```shell
node server.js
```

## Usage
Predicting the data food:
```
curl --location 'https://<YOUR-IP>:8081/predict-minyak' \
--data '{
    "num_people": 5,
    "consumption": 4
}'
```
Example response:
```
{
  "error": false,
  "message": "Predict Success",
  "predictResult": [
    41.858848571777344
  ]
}
```

predicting the data transportation:

```
curl --location 'https://<YOUR-IP>:8081/predict-mobil' \
--data '{
    "distance" : 15
}'
```
Example response:
```
{
    "distance" : 15
}
```

##Repository API ML Deployment
[repository API ML](https://github.com/greenixproject/API-ML)
