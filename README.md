
## Problem Statement: Generate a Multiclass Classification Model and Web-App that Accurately Predicts Clothing Size using Age, Weight, and Height as Inputs.

### Data source: 
Data for "Clothes-Size-Prediction" was published by Sarvesh Dubey on Kaggle, October 2020. https://www.kaggle.com/tourist55/clothessizeprediction/metadata  
The CSV file contains 119218 rows of data and 4 columns which include weight, age, height, and size.


### Data Dictionary:
|Column|Type|Description|
|---|---|---|---|
|Weight | int | Weight in Kilograms (kg) range from 22 to 136 kg, modified for modeling |
|Age| float | Ages in decimal format range from 0 to 117, modified for modeling |
|Height| float | Height in centimeters (cm) and decimal format |
|Size| object | Includes sizes XXS - XXXL, hard coded to integer values (1-7) |

### EDA:
Weight is recorded in kilograms (kg), height in centimeters (cm), age spans from 0 to 117 years, and sizes include XXS, S, M, L, XL, XXL, XXXL. There are no XS. 

After loading the csv file into Jupyter, I did a brief scan of the data using numPy  dtypes, describe, and nunique attributes to see just what I would be working with. All of which were in good shaping, needing only a few adjustments. I got rid of 587 null values which is less than 1 percent of my total data. I also found that the age columns contained ages spanning from 0 to 117 which seemed to be input errors. I filtered my age column by only keeping ages between 18 and 80 (inclusive). Similarly, I filtered the weight column to include weights between 41 kg and 136 kg. The lowest weight value in my dataset was 22 kg which also seemed very unlikely. The ranges I chose to be my new minimum and maximum for the columns mentioned above were personal choices due to my own knowledge of physiology and sizing. After cleaning, I dropped a total of 892, still less than 1 percent of my total data. I also hard coded the sizes which were objects to integers using the python map function and using small size: small number, big size: big number logic. 

I copied the original dataframe and created two new dataframes (new_df and dummy_df) for analysis. The original df was used for EDA, the new_df was used for modeling, and dummy_df was used to briefly look at correlations. 

My exploratory data analysis provides a thorough look into each column’s distribution and its relationship to the other variables. Age is concentrated between 25 and 40 years with an average of 34 years.  Weight is concentrated between 50 and 70 kg with an average of 61.8 kg. Height is concentrated between 160 and 170 cm with an average of 165.8 cm. Correlations are moderate to strong between weight and size, and height and weight. However, age has a weak correlation predicting height, size, or weight. 

### Findings: 
I began with baseline accuracy scores of: XXS: 0.083114, S: 0.183247, M: 0.247781, L: 0.147199, XL: 0.160057, XXL: 0.000539, XXXL: 0.178064. Size medium was the most recurring size and size extra extra large was the least recurring size. 
I generated several models, including Logistic Regression, K-Nearest Neighbors (KNN), Random Forest, Extra Tree, as well as, boosting models such as AdaBoost, Gradient Boost, and a Voting Classifier. All scores were around 50%. These models are predicting clothing sizes 30% more accurately than the baseline accuracy scores. The logistic Regression model performed slightly better than the others and was used in the final Web-App to predict user size, given user inputs. The model was pickled to be quickly referenced and used in the Python’s Streamlit tool where the interactive clothing size predictor could be put to the test. 


### Conclusions: 
Accuracy below 90 percent seems to be the norm for multiclass classification. There are many  clothing sizes with only small variations between them. However, the models were still able to score well above the baseline accuracy. 
Age is not a great indicator for predicting clothing size and weight is the best indicator. The data provided no other details besides age, height, and weight so it is not clear whether the sizes were male, female, or unisex. Using the web-app created to predict size, I inputted a few standard male measurements, however, the predicted sizes were not aligned with the typical male size for an individual of the given height and weight. Using conventional female height and weight, such as my own, the model was also slightly off in some cases. However, it is important to note that everyone carries their weight differently, and the models did not take into account an individual’s fitness level or body shape. The country origin of the data is also unclear. Many East Asian countries tend to make clothing much smaller to fit their demographic and culture, and clothing sizes vary in other parts of the world as well. For future analysis, I would be interested to work with a dataset that includes information about the collection of the data, and other measurements such as waist, breast, and hip measurements, along with gender specifications and the standard age, weight, and height. I believe that would increase my model’s accuracy tenfolds. 
