import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

def sort_dataset(dataset_df):
	#TODO:
	data_df = dataset_df.sort_values(by='year')
	return data_df

def split_dataset(dataset_df):	
	#TODO:
	y_data = dataset_df[['salary']]
	y_data = (y_data*0.001)
	y_data = y_data.astype(int)
	x_data = dataset_df.drop('salary',axis=1)
	y_train = y_data[:1718]
	x_train = x_data[:1718]
	y_test = y_data[1718:]
	x_test = x_data[1718:]
	return x_train,x_test,y_train,y_test

def extract_numerical_cols(dataset_df):
	#TODO:
	nummeric_data = ['age','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','HBP','SO','GDP','fly','war']
	dataset_df = dataset_df[nummeric_data]
	return dataset_df

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO:
	dt_cls=DecisionTreeRegressor()
	dt_cls.fit(X_train,Y_train)
	return dt_cls.predict(X_test)

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO:
	rf_cls=RandomForestRegressor()
	rf_cls.fit(X_train,Y_train)
	return rf_cls.predict(X_test)

def train_predict_svm(X_train, Y_train, X_test):
	#TODO:
	svm_cls = make_pipeline(
		StandardScaler(),
		SVR()
	)
	svm_cls.fit(X_train,Y_train)
	return svm_cls.predict(X_test)

def calculate_RMSE(labels, predictions):
	#TODO:
	return mean_squared_error(labels,predictions,squared=False)

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))