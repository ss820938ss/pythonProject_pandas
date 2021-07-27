import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')  # tsv 파일이라 \t 를 써서 정렬, csv 는 자동정렬
print(df)