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

### Day 1:

### Day 2:

### Day 3:

### Day 4:

### Day 5:

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
