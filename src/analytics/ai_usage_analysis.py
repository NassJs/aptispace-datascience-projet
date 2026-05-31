def get_ai_usage_stats(df):
    return {
        "high_usage": df[df["Weekly_GenAI_Hours"] >= 20].shape[0],
        "medium_usage": df[
            (df["Weekly_GenAI_Hours"] >= 10) &
            (df["Weekly_GenAI_Hours"] < 20)
        ].shape[0],
        "low_usage": df[df["Weekly_GenAI_Hours"] < 10].shape[0],
        "top_major_ai": (
            df.groupby("Major_Category")["Weekly_GenAI_Hours"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )
    }