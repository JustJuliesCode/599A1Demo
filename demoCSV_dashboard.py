import pandas as pd

def generate_html(df):
    average = df['score'].mean()
    rows = "\n".join([f"<tr><td>{r['name']}</td><td>{r['score']}</td></tr>" for _, r in df.iterrows()])
    html = f"""
    <html>
    <head><title>Score Dashboard</title></head>
    <body>
        <h1>Average Score: {average:.2f}</h1>
        <table border="1">
            <tr><th>Name</th><th>Score</th></tr>
            {rows}
        </table>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    html = generate_html(df)
    with open("output/dashboard.html", "w") as f:
        f.write(html)
    print("Dashboard generated.")
