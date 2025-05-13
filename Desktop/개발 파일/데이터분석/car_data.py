#자동차 데이터 불러오는 코드
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("yaminh/german-car-insights")

df = pd.read_csv(path + '/gcar_data.csv')

pd.set_option('display.max_columns', None)       # 열 전체 보이기
pd.set_option('display.max_rows', None)          # 행 전체 보이기
pd.set_option('display.max_colwidth', None)      # 문자열 잘리지 않게
pd.set_option('display.expand_frame_repr', False)  # 옆으로 길게 출력

# 🔍 전체 출력 (예: 상위 50행)
df['price_in_euro'] = (
    pd.to_numeric(
        df['price_in_euro']
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.extract(r'(\d+\.?\d*)')[0],   # 숫자만 추출
        errors='coerce'  # 변환 안 되는 값은 NaN 처리
    )
)


df2 = df.groupby('brand')['price_in_euro'].mean().sort_values(ascending=False)
print(df2['ferrari'])

