# Model-tunability
 ## Project overview
 The aim of this project is to measure ML models tunability, which is defined based on [this paper](https://jmlr.org/papers/volume20/18-444/18-444.pdf). We used two sampling techniques: Grid Search and Bayes Search to finds best parameters, calculate defaults and finally measure tunability of each of the following algorithms:
 
 * KNN
 * XGBoost
 * Logistic Regression

 In the  sections below you may find more implementation details.

### Notebooks order
1. data_analysis.ipynb
2. preprocessing.ipynb
3. model_optimisation.ipynb
4. tunability.ipynb
## Data
We are using 5 dataframes for binary classification from Kaggle with data about delayed flights or airlines ratings.
1. https://www.kaggle.com/datasets/gabrielluizone/us-domestic-flights-delay-prediction-2013-2018
2. https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations
3. https://www.kaggle.com/datasets/ulrikthygepedersen/airlines-delay
4. https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022?select=Combined_Flights_2022.csv
5. https://www.kaggle.com/datasets/mikhail1681/airline-quality-ratings

Dataframes are kept in /data folder and loaded + split in data_analysis notebook. 
## Preprocessing
Here you may find a quick description of preprocessing techniques used for chosen dataframes.

**for categorical columns:**

* Drop low variance - we are dropping columns, where most of the rows have the same value 
* Drop high cardinality - we are dropping columns ,where most of the values are unique, as it doesn't provide any type of generalization
* Label encoding - as we realize that there may be no order in the data, OneHot encoding results in great dimention increase, which we want to avoid
* Missing values imputing - we chose 'most frequent' strategy for imputing missing values

**for numerical columns:**
* Missing values imputing - we chose 'median' strategy for imputing missng values

**all columns:**

* Drop >50% missing - we are dropping column that have more than 50% missing values
* Scaling -  we scale all columns using MinMaxScaler (after categorical encoding)

## Optimisation
In notebooks model_optimisation_naive.ipynb and model_optimisation_bayes.ipynb you can find implementation of Grid Search and Bayes Search performed on every model and for every dataset. Results of every iteration of this sampling methods are saved in json format in /raport folder. 

For each dataframe, we used the same parameter space to calculate the default parameters (as defined in the paper linked above). The rationale behind the selection of parameter values is discussed in several papers linked within these notebooks.

## Default parameters
The first step after obtaining Grid Search results was calculating default parameter sets $\theta_{d}$  for each model. It is defined as the set that gives the highest average score (AUC) among all datasets for each model.  Here are calculated defaults:

### KNN
| Parameter | Value |
|------------|------------|
| algorithm  | ball tree  | 
| leaf size  | 50  |
| metric  | manhattan |
| n_neighbors | 50 |
|weights | distance |

### XGBoost
| Parameter | Value |
|------------|------------|
| eval_metric  | logloss  | 
| gamma  | 0.15  |
| learning_rate | 0.01 |
| max_depth | 10 |
| min_child_weight | 10 |
| n_estimators| 100| 

### Logistic Regression

| Parameter | Value |
|------------|------------|
| C  | 1291.549665  | 
| class_weight  | balanced  |
| fit_intercept | True |
| max_iter | 50000 |
| tol | 0.001 |


## Tunability
Tunability is an aggregation of the differences in model performance on best parameter set and model performance on default set (AUC on $\theta_{best}$ - AUC on $\theta_{d}$). As we only had 5 dataframes it's not enough to draw hard conclusions. In our experiment the results are on the following plots:

![Opis obrazu](/saved_plots/GSTunab.png)

![Opis obrazu](/saved_plots/BSTunab.png)

We can see that conclusions are very simiar for both Grid Search and Bayes Search.

## Methods stability
We also checked how both of the sampling methods differ. How many iterations do they need to find the best parameters? How long does it take to search through the param grid ? How each method finds the parameters? Plots below show max AUC found so far vs the number of iterations for every model and sampling method. We can see that while GS need around 20-100 iterations to achieve the best AUC, BS needs only 4-10.

![Opis obrazu](/saved_plots/1.png)
![Opis obrazu](/saved_plots/2.png)
![Opis obrazu](/saved_plots/3.png)

We were also interested in how each iteration works in GS and BS. As we didn't notice any differences for most of the datasets, here are 2 plots that were more interesting:

![Opis obrazu](/saved_plots/4.png)
![Opis obrazu](/saved_plots/5.png)

From these plots, we can see that Bayes Search indeed spent less 'time' searching through parameter combinations that resulted in low AUC, while Grid Search explored every possible combination.

As mentioned earlier, 'time' refers to the number of iterations, which does not necessarily imply that Bayes Search was faster, as it has limited multi-threading capabilities.

## Results on default parameters
The last thing we cheked was the difference between AUC in each iteration of GS and BS vs AUC achieved on default parameters (AUC on every $\theta$ - AUC on $\theta_{d}$). Plots below ilustrate that for most of the cases default parameters give better results than randomly chosen ones. It suggests that maybe for those algorithms it is worth to use the defaults insted of randomly setting hyperparameters.

![Opis obrazu](/saved_plots/7.png)


## Conclusions
As we take into consideration that 5 dataframes are not enough to make conclusions, we can see the following aspects of our experiment:

* Bayes Search requires fewer iterations to find the best parameters.

* KNN appears to be less sensitive to parameter changes, while XGBoost and Logistic Regression can improve their performance by up to 2%.

* Results with default parameters are often better than those with randomly set parameters.

* The conclusions regarding tunability and defaults are similar for both Grid Search and Bayes Search.

* While we didn’t observe significant differences for most datasets, there are a few that show Bayes Search finds the best parameters in a different way than Grid Search.