# JOTBhackaton
Team 2  hackaton submission

# Project goal

The goal of our project is to create a model able to predict solar energy generation based on weather forcast. 
This would allow owner of solar panels to better plan their energy consumption based on what the predicted generation for next day is.
Simple app combining weather and solar power output could be build to provide this data in accessible and easy to understand form.

# Data model

We used simple solar power generation data set:
https://www.kaggle.com/datasets/pythonafroz/solar-powe-generation-data

It provdes information about  irradiation, temperature, humidity and wind velocity for each hour during year time period. We have chosen this model because all this values can be obtained using publicly available weather APIs, for example https://openweathermap.org 
We modified this data set by splitting the date into month and hour copoment that were loaded into separate database columns. 

# Training set


