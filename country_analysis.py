# country_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def load_data(path_or_url):
    """CSV를 읽어와 DataFrame으로 반환"""
    df = pd.read_csv(path_or_url)
    df['country'] = df['country'].fillna('Unknown')
    # 여러 국가가 쉼표로 나열된 경우 첫 번째 국가만 추출
    df['main_country'] = df['country'].apply(lambda x: x.split(',')[0].strip())
    return df

def plot_country_bar(df, top_n=10, filename='country_bar.png'):
    """상위 top_n개 국가 barplot을 그리고 파일로 저장"""
    country_counts = df['main_country'].value_counts().head(top_n)
    plt.figure(figsize=(10, 6))
    country_counts.plot(kind='bar')
    plt.title(f"Top {top_n} Countries by Netflix Content Count")
    plt.xlabel("Country")                       # X축 레이블 영어로 변경
    plt.ylabel("Content Count")                 # Y축 레이블 영어로 변경
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

if __name__ == "__main__":
    # 1) 로컬 파일 혹은 GitHub raw URL 중 편한 쪽 사용
    url = "netflix_titles.csv"
    # url = "https://raw.githubusercontent.com/abishek-as/Netflix-Movie-Recommendation/main/netflix_titles.csv"
    
    df = load_data(url)
    plot_country_bar(df)
    print("Country bar chart saved as country_bar.png")
