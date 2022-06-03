Imersão de Dados Alura - 2022
==============================
The <i>Imersão Dados</i> is a event promoted by [Alura](https://www.alura.com.br/), an online school that provides courses for different technologies, focused in presenting the principal tools of a data scientist and in developing a data science project. The event consists in 5 days of lives, where experts in the field show how to perform common activities related to data science, and then some practical task are proposed to the audiance.
<br><br>
In the edition of 2022, the project was about developing a machine learning model to predict the prices of houses in São Paulo city. For this, it was used a [database](https://www.kaggle.com/datasets/kaggleshashankk/house-price-data-of-sao-paulo) with some information about houses in São Paulo, together with their prices. A great part of the time was spend in cleaning and exploring this database. To make the machine learning models more accurate, it was proposed to use external data from [IBGE](https://www.ibge.gov.br/) (Brazilian Institute of Geography and Statistics) concerning the socio-economic data from different regions of the city. This was the most challenging step of the project, and to make the connection between the original database and this external database from IBGE, it was necessary to use other two databases. But in the end it was worth it, since there was a great improviment in the prediction of prices after adding this external data.
<br><br>
Some of the libraries used in this project were **Numpy**, **Pandas**, **Matplotlib**, **Seaborn**, **Plotly**, **Geopandas** and **Sklearn**.
<br><br>
In what follows, I will briefly describe the main tasks done in each day of the event.

## Description

### Days 1 and 2: 
The first two days were dedicated to exploring and processing the database of house prices in São Paulo. We began by cleaning the data. Some rows in the price column had strings in the entries, and this had to be corrected before converting this column to a numeric type. Also, some of the rows were related to renting prices, and we decided to delete them. We also explored the data getting statistical information, using different kinds of graphs and by dividing the data by the districts of São Paulo. I learned how to personalize my graphs using **matplotlib** and **seaborn** and how to create interative plots with **plotly**.

### Days 3 and 4:
Some of the processing of the prices database still had to be done. I investigated the outliers in the database, and, after noticing that they were distrobing a lot the statistical data, I decided to remove some of them. But the main task of these two days was to get the socio-economic data from IBGE and merge it with our original database. The first step was to clean IBGE data. The data from IBGE divides the city of São Paulo in different sector (which do not necessarily coincide with the districts), and it has data related to the mean income of the resisdents in each of these sectors. To connect the two datasets, we had to relate the houses addresses with the IBGE sectors. But this task was not trivial. First, we used another database to relate the addresses with the CEP (Brazillian ZIP code), longitude and latitude informations. Another dataset was used together with **geopandas** to relate the latitude and longitude with the IBGE sector. Then, we could finally merge our original data with IBGE data. We also analyzed which of the columns from IBGE had the most correlation of the price, and selected these columns for use in the machine learning models.

### Day 5:
Finally, we were now able to construct our machine learning models to predict the prices of houses in São Paulo. I decided to use three different approaches: **Linear Regression**, **Decision Trees**, and **Random Forests**. First, I built a model for each of these algorithms using only the original data. These models were used as baseline to compare if the addition of IBGE data brought any improvement to the predictions. So the next step was to built the machine learning models using the original dataset plus data from IBGE. These showed a significat improvement in the R2 and Mean Absolute Error metrics when compared to those. So having all the effort to add IBGE information was worth it! All the metrics were calculated taking the mean values of the scores after 30 different rounds of **5-fold cross validation** for each of the models. The best model was a Random Forest with 50 predictors and using IBGE data.
<br><br>
Another task proposed in the event was to verify what happen when we include the price per square foot into the features. This would be a **data leakage**, since this feature were calculated dividing the price (our target) by the footage. As expected, even without considering IBGE data, our models were much better than before. The Mean Ablosute Errors were much smaller, and R2 metrics were close to one. Of course, in a real application the price per square foot wouldn't be available.
<br><br>
To close this project, I tested the best model obtained in real external data from [Zap Imóveis](https://www.zapimoveis.com.br/), a site to buy and sell houses. I selected 5 houses in São Paulo, used my model to predict their prices, and compared with the real value. Unfortunatelly, the predictions weren't good, showing that my model has not generalized to external data.

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
