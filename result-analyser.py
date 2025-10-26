import pandas as pd
import matplotlib.pyplot as plt
def load_data(filename):
    """
    Load student marks from a CSV file.
    Example CSV format:
    Name,Math,Science,English,Computer
    Ravi,85,90,78,92
    Anjali,88,76,85,80
    Raj,70,65,60,75
    """
    try:
        df = pd.read_csv(filename)
        print("\n✅ Data loaded successfully!\n")
        print(df.head())
        return df
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the file path.")
        return None
    

def show_statistics(df):
    print("\n📊 Overall Statistics:")
    print(df.describe())

    df["Total"] = df.iloc[:, 1:].sum(axis=1)
    df["Average"] = df["Total"] / (len(df.columns) - 1)

    topper = df.loc[df["Total"].idxmax(), "Name"]
    print(f"\n🏆 Top Performer: {topper} with {df['Total'].max()} total marks")

    print("\n📈 Class Average (per subject):")
    print(df.iloc[:, 1:-2].mean())


def plot_subject_average(df):
    subject_averages = df.iloc[:, 1:-2].mean()
    plt.figure(figsize=(8, 4))
    subject_averages.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("📘 Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_student_comparison(df):
    df.set_index("Name", inplace=True)
    df.iloc[:, :-2].plot(kind='bar', figsize=(10, 5))
    plt.title("📊 Student Performance Comparison")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.legend(title="Subjects")
    plt.tight_layout()
    plt.show()


def main():
    print("🎓 Student Result Analyzer\n")
    filename = input("📂 Enter CSV file name (e.g., results.csv): ")

    df = load_data(filename)
    if df is not None:
        show_statistics(df)
        plot_subject_average(df)
        plot_student_comparison(df)

if _name_ == "_main_":
    main()