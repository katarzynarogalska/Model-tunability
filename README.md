# Model-tunability
(project desc)

## Data
We are using 6 dataframes from Kaggle with data about delayed flights or airlines ratings.
1. https://www.kaggle.com/datasets/gabrielluizone/us-domestic-flights-delay-prediction-2013-2018
2. https://www.kaggle.com/datasets/kappann/british-airways-reviews
3. https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations
4. https://www.kaggle.com/datasets/ulrikthygepedersen/airlines-delay
5. https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022?select=Combined_Flights_2022.csv
6. https://www.kaggle.com/datasets/mikhail1681/airline-quality-ratings

Dataframes are kept in /data folder and loaded + split in data_analysis notebook. 
## Preprocessing
Here you may find a quick description of preprocessing techniques used for this data.

**for categorical columns:**

* Drop low variance - we are dropping columns, where most of the rows have the same value 
* Drop high cardinality - we are dropping columns ,where most of the values are unique, as it doesn't provide any type of generalization
* Label encoding - as we realize that there may be no order in the data, OneHot encoding results in great dimention increase, which we want to avoid
* Missing values imputing - we chose 'most frequent' strategy for imputing missing values

**for numerical columns:**

* Binning - we are binning numerical columns based on kmeans strategy
* Missing values imputing - we chose 'median' strategy for imputing missng values

**all columns:**

* Drop >50% missing - we are dropping column that have more than 50% missing values
* Scaling -  we scale all columns using MinMaxScaler (after categorical encoding)