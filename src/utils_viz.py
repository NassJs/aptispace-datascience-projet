import matplotlib.pyplot as plt
import seaborn as sns


def set_custom_style(theme="light"):
    if theme == "dark":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")

    sns.set_theme(style="whitegrid")


def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution de {column}")
    plt.show()


def plot_boxplot(df, x, y):
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f"{y} selon {x}")
    plt.xticks(rotation=45)
    plt.show()


def plot_correlation_matrix(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation")
    plt.show()