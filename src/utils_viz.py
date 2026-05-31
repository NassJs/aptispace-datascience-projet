import matplotlib.pyplot as plt
import seaborn as sns


def set_custom_style(theme="light"):
    """
    Applique un style graphique simple.
    """
    if theme == "dark":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")

    sns.set_theme(style="whitegrid")


def plot_generic_trends(df, x_col, y_col, group_col=None):
    """
    Trace une courbe d'évolution entre deux colonnes.
    """
    plt.figure(figsize=(10, 5))

    if group_col:
        sns.lineplot(data=df, x=x_col, y=y_col, hue=group_col)
    else:
        sns.lineplot(data=df, x=x_col, y=y_col)

    plt.title(f"{y_col} selon {x_col}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt


def plot_correlation_matrix(df):
    """
    Affiche la matrice de corrélation des colonnes numériques.
    """
    numeric_df = df.select_dtypes(include="number")

    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation")
    plt.tight_layout()

    return plt


def plot_bivariate_scatter(df, x_col, y_col, hue_col=None):
    """
    Trace un nuage de points entre deux variables.
    """
    plt.figure(figsize=(8, 5))

    if hue_col:
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col)
    else:
        sns.scatterplot(data=df, x=x_col, y=y_col)

    plt.title(f"Relation entre {x_col} et {y_col}")
    plt.tight_layout()

    return plt


def plot_histogram(df, column):
    """
    Trace un histogramme pour une colonne numérique.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution de {column}")
    plt.tight_layout()

    return plt


def plot_boxplot(df, x_col, y_col):
    """
    Trace un boxplot pour comparer une variable numérique selon une catégorie.
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x=x_col, y=y_col)
    plt.title(f"{y_col} selon {x_col}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt
def plot_bivariate_scatter(df, x_col, y_col, color_col=None):
    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x=x_col,
        y=y_col,
        hue=color_col
    )

    plt.title(f"{y_col} vs {x_col}")
    plt.tight_layout()

    return plt