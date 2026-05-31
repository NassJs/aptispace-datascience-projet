def get_burnout_stats(df):
    burnout_top = df["Burnout_Risk_Level"].value_counts().index[0]

    return {
        "burnout_top": burnout_top,
        "avg_anxiety": df["Anxiety_Level_During_Exams"].mean(),
        "high_burnout_count": df[df["Burnout_Risk_Level"] == "High"].shape[0],
        "low_burnout_count": df[df["Burnout_Risk_Level"] == "Low"].shape[0],
    }