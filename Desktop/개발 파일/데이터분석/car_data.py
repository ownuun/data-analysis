#자동차 데이터 불러오는 코드
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("yaminh/german-car-insights")

df = pd.read_csv(path + '/gcar_data.csv')
print(df)