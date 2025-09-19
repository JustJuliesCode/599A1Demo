import pandas as pd

def process():
    df = pd.read_csv('demo2_data.csv')
    avg = df['score'].mean()
    print(f"Average score: {avg:.2f}")

if __name__ == "__main__":
    process()
