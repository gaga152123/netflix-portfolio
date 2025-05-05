# year_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def load_data(path_or_url):
    """CSV를 읽어와 DataFrame으로 반환"""
    df = pd.read_csv(path_or_url)
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    return df

def plot_year_trend(df, filename='year_trend.png'):
    """연도별 등록 수 lineplot을 그리고 파일로 저장"""
    year_counts = df['year_added'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    plt.plot(year_counts.index, year_counts.values, marker='o')
    plt.title("Yearly Netflix Content Registrations")
    plt.xlabel("Year")                          # X축 레이블 영어로 변경
    plt.ylabel("Number of Registrations")       # Y축 레이블 영어로 변경
    plt.grid(True)
    plt.savefig(filename, dpi=300)
    plt.close()

if __name__ == "__main__":
    # 1) 로컬 파일 혹은 GitHub raw URL 중 편한 쪽 사용
    url = "netflix_titles.csv"  # 직접 업로드했으면 이걸로
    # url = "https://raw.githubusercontent.com/abishek-as/Netflix-Movie-Recommendation/main/netflix_titles.csv"
    
    df = load_data(url)
    plot_year_trend(df)
    print("Year trend chart saved as year_trend.png")
