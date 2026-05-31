def get_correlations(df):
    return {
        "ai_gpa_corr": df["Weekly_GenAI_Hours"].corr(df["Post_Semester_GPA"]),
        "dependency_anxiety_corr": df["Perceived_AI_Dependency"].corr(
            df["Anxiety_Level_During_Exams"]
        ),
        "ai_dependency_corr": df["Weekly_GenAI_Hours"].corr(
            df["Perceived_AI_Dependency"]
        ),
    }