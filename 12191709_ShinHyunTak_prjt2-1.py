import pandas as pd

def func1(data):
    for year in [2015,2016,2017,2018]:
        year_data=data[data['year']==year]
        for section in ['H','avg','HR','OBP']:
            print_data=year_data[['batter_name',section,'year']]
            print(year, section)
            print(print_data.sort_values(by=section,ascending=False)[:10])
            print()

def func2(data):
    data_2018=data[data['year']==2018]
    for position in ['포수','1루수','2루수','3루수','유격수','좌익수','중견수','우익수']:
        cp_data_2018 = data_2018[data_2018['cp']==position]
        print_data = cp_data_2018[['batter_name','war']]
        print(position)
        print(print_data.sort_values(by='war', ascending=False)[:1])
    print()

def func3(data):
    data_corr=data[['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']]
    data_corr = data_corr.corrwith(data_corr.salary)
    data_corr = data_corr.drop('salary')
    print(data_corr)
    print("Most realtion : ",data_corr.sort_values(ascending=False)[:1])

if __name__=='__main__':
    data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
    print("Q1")
    func1(data)
    print("Q2")
    func2(data)
    print("Q3")
    func3(data)