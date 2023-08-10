# Predicting MLB Arbitration Salaries with Keras Sequential Network


## Description
This project is an attempt to predict MLB arbitration salaries based on a bevy of factors. This repository includes Jupyter notebooks containing cleaning and model building procedures. All models were neural networks trained in Tensorflow Keras and evaluated on metrics including Mean Absolute Error and Mean Absolute Percentage Error. Also included are Python files containing helper functions used in the data cleaning and preprocessing sections. An article explaining this project can be found at my [Medium page](https://medium.com/@joshsalce).

### Packages and Tech Used
- Python
- Python Packages: [pandas](https://pandas.pydata.org/docs/), [numpy](https://numpy.org/doc/), [sklearn](https://scikit-learn.org/stable/index.html), [TensorFlow](https://tensorflow.org/), [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/)

## Table of Contents

| Component | Description |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [Data](https://github.com/joshsalce/arbitration_tensorflow/tree/main/Data)| CSV files of raw data to be cleaned. Includes custom Fangraphs data, scraped and collected arbitration data with further data collection. Includes 'Metadata' folder describing datasets | 
| [Predictions](https://github.com/joshsalce/arbitration_tensorflow/tree/main/Predictions) | Contains Excel file with test set true and predicted salaires in tables, pivot tables |
| [Train Test Data](https://github.com/joshsalce/arbitration_tensorflow/tree/main/Train%20Test%20Data) | Contains CSV files of data after cleaning process and splitting into training, test sets |
| [Visualizations](https://github.com/joshsalce/arbitration_tensorflow/tree/main/Visualizations) | Includes visualizations of histograms visualizing distributions of individual features, scatterplots for model predictions according to different groupings |
| [Data_Cleaning](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Data_Cleaning.ipynb) | Jupyter notebook for importing and cleaning data. Procedure includes standardizing names, positions, changing data types and values |
| [DNN_pitchers](https://github.com/joshsalce/arbitration_tensorflow/blob/main/DNN_pitchers.ipynb) | Jupyter notebook for importing, preprocessing data, training and evaluating Tensorflow Neural network for MLB pitchers. Training done on 2011-2022 pitchers, tested on 2023 pitchers |
| [DNN_players](https://github.com/joshsalce/arbitration_tensorflow/blob/main/DNN_players.ipynb) | Jupyter notebook for importing, preprocessing data, training and evaluating Tensorflow Neural network for MLB position players. Training done on 2011-2022 position players, tested on 2023 position players |
| [Helper Functions](https://github.com/joshsalce/arbitration_tensorflow/tree/main/Helper%20Functions) | Includes Python files containing written helper functions to scrape data, build histogram visuals, clean data |

## Visualizations- Descriptions
- Pitchers & Position Players: Visualizations of Model Evaluation/Prediction
  - [Histograms, Pitchers](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Pitchers/histograms.png), [Histograms, Position Players](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Position%20Players/histgrams.png)- Histograms for each dataset's continuous features
  - [MAE Loss, Pitchers](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Pitchers/mae_curve.png), [MAE Loss, Position Players](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Position%20Players/mae_curve.png)- MAE Learning Curves for each model
  - [MAPE Loss, Pitchers](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Pitchers/mape_curve.png), [MAPE Loss, Position Players](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Position%20Players/mape_curve.png)- MAPE Learning Curves for each model
  - [SHAP Values, Pitchers](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Pitchers/shap_values.png), [SHAP Values, Position Players](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Position%20Players/shap_values.png)- Horizontal barplots of features with most positive SHAP values
  - [True vs. Pred, Pitchers](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Pitchers/true_vs_pred.png), [True vs. Pred, Position Players](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Position%20Players/true_vs_pred.png)- Scatterplots of true 2023 salary vs. predicted 2023 salary
  - [True vs. Pred (Position), Pitchers](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Pitchers/true_vs_pred_position.png), [True vs. Pred (Position), Position Players](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Position%20Players/true_vs_pred_position.png)- Scatterplots of true 2023 salary vs. predicted 2023 salary, grouped by player position
  -  [True vs. Pred (Service Time), Pitchers](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Pitchers/true_vs_pred_time.png), [True vs. Pred (Service Time), Position Players](https://github.com/joshsalce/arbitration_tensorflow/blob/main/Visualizations/Position%20Players/true_vs_pred_time.png)- Scatterplots of true 2023 salary vs. predicted 2023 salary, grouped by service time
