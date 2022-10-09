# API de scoring

# Project
Projet 7 OpenClassRooms

# Data 
Sourced from: https://www.kaggle.com/c/home-credit-default-risk/data

# Objective 
Return a score given customer features

# Model part
- LGB model
- Le modèle est chargé en parallèle de la base de donnée client
- Il est appelé pour simplement retourner un score compris entre 0 et 1 reflétant le risque de non remboursement

# Characteristics
- Using Flask and Python
- Build for 2 version of dataframe smal or large (XL), not used at the moment

# Deployed on Heroku at :
https://appp7fd.herokuapp.com/predict



