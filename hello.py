import pandas as pd
import plotly.express as px
import preswald

df = pd.read_csv("data/university_mental_health_iot_dataset.csv")  # Make sure this file path is correct

df["sleep_quality_score"] = df["sleep_hours"] - (df["noise_level_db"] / 50) - (df["lighting_lux"] / 500)

fig = px.scatter(
    df,
    x="sleep_quality_score",
    y="mood_score",
    color="mental_health_status",
    size="stress_level",
    hover_data=["timestamp", "location_id", "sleep_hours", "noise_level_db", "lighting_lux"],
    title="Mood vs Sleep Quality Score",
    labels={
        "sleep_quality_score": "Sleep Quality Score",
        "mood_score": "Mood Score",
        "mental_health_status": "Mental Health"
    }
)
fig.update_traces(textposition="top center", marker=dict(size=12, color="lightblue"))
fig.update_layout(template="plotly_white")

preswald.text("# Sleep Quality vs Mood Analysis")
preswald.text("This visualization explores how environmental and behavioral factors during sleep affect mood.")
preswald.plotly(fig)
preswald.table(df[["timestamp", "sleep_hours", "noise_level_db", "lighting_lux", "sleep_quality_score", "mood_score", "mental_health_status"]])