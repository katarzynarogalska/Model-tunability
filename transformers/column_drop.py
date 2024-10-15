from sklearn.base import BaseEstimator,TransformerMixin

class DropMissing(BaseEstimator,TransformerMixin): #drop columns that have >50% NaN
    def __init__(self, threshold=0.5):
        self.threshold = threshold
        self.columns_missing =[]
    def fit(self,X,y=None):
        self.columns_missing = [col for col in X.columns if X[col].isna().mean() > self.threshold] 
        return self
    def transform(self, X, y=None):
        return X.drop(columns= self.columns_missing)
    
class DropLowVarianceCategorical(BaseEstimator, TransformerMixin): #drop categorical columns that have 95% one value 
    def __init__(self, threshold=0.95):
        self.threshold=threshold
        self.columns_to_drop=[]
    def fit(self,X,y=None):
        for col in X.select_dtypes(include=['object','category']).columns:
            top_cat_percentage = X[col].value_counts(normalize=True).max() 
            if top_cat_percentage > self.threshold:
                self.cols_to_drop_.append(col)
        return self
    def transform(self,X,y=None):
        return X.drop(columns = self.columns_to_drop)
    
class DropHighCardinality(BaseEstimator,TransformerMixin): #drop columns that have >50% unique values
    def __init__(self, threshold=0.5):
        self.threshold=threshold
        self.columns_to_drop=[]
    def fit(self,X,y=None):
        for col in X.columns:
            unique_count = X[col].nunique()
            total_count = X['col'].count() 
            unique_percentage = unique_count/total_count
            if unique_percentage > self.threshold:
                self.columns_to_drop.append(col)
        return self
    def transform(self,X,y=None):
        return X.drop(columns=self.columns_to_drop)
