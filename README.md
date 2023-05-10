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

# Training and validation sets

All the columns in data set are relevant for the model (hour of the day as well as month have impact on power generation) so we cannot split the data set based on values in specific columns. Instead, we split the data into training (70%) and validation (30%) set by selecting rows at random.

# Results

## With radiation
We trained first model using all columns form the data set.
After testing it we noticed that the radiation value had the heaviest influence on the predicted values. 
We removed radiation from the data set and created another model.

## Witout radiation

Even after removing radiation from the dataset the predictions were correlated with the value in validation data.
The correlation chart can be found in file chart1.png.
