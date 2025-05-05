# netflix_pie_chart.py

import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    """
    로컬에 업로드된 CSV 파일을 읽어와 DataFrame으로 반환
    """
    df = pd.read_csv(path)
    df['country'].fillna('Unknown', inplace=True)
    return df

def prepare_pie_data(df):
    """
    'United States' 대 'Others' 그룹으로 집계
    """
    df['country_group'] = df['country'].apply(
        lambda x: 'United States' if 'United States' in x else 'Others'
    )
    return df['country_group'].value_counts()

def plot_and_save_pie(pie_data, filename='netflix_pie_chart.png'):
    """
    Pie Chart를 그려서 파일로 저장
    """
    plt.figure(figsize=(8, 8))
    plt.pie(
        pie_data,
        labels=pie_data.index,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Netflix Content: United States vs Others")
    plt.axis('equal')  # 원형 유지
    plt.savefig(filename, dpi=300)
    plt.close()

if __name__ == "__main__":
    # Colab이나 로컬에 업로드한 CSV 파일 이름을 지정하세요
    csv_path = 'netflix_titles.csv'
    
    # 데이터 로드
    df = load_data(csv_path)
    
    # Pie Chart용 데이터 준비
    pie_data = prepare_pie_data(df)
    print(pie_data)
    
    # 차트 그려서 파일로 저장
    plot_and_save_pie(pie_data)
    print("Pie chart saved as netflix_pie_chart.png")
