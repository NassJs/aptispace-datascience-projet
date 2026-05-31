def get_academic_stats(df):
    gpa_gain = df["Post_Semester_GPA"].mean() - df["Pre_Semester_GPA"].mean()

    return {
        "avg_pre_gpa": df["Pre_Semester_GPA"].mean(),
        "avg_post_gpa": df["Post_Semester_GPA"].mean(),
        "gpa_gain": gpa_gain,
        "best_major_gpa": (
            df.groupby("Major_Category")["Post_Semester_GPA"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )
    }