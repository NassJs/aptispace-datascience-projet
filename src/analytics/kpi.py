def get_kpis(df):
    return {
        "avg_ai": df["Weekly_GenAI_Hours"].mean(),
        "avg_dependency": df["Perceived_AI_Dependency"].mean(),
        "avg_anxiety": df["Anxiety_Level_During_Exams"].mean(),
        "avg_gpa": df["Post_Semester_GPA"].mean(),
        "total_students": df.shape[0],
        "total_columns": df.shape[1],
    }