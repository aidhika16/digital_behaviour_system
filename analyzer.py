import pandas as pd
import numpy as np


df = pd.read_csv("digital_behaviour.csv")


def time_format(minutes):

    hours = int(minutes // 60)
    mins = int(minutes % 60)

    if hours > 0:
        return f"{hours}h {mins}m"

    return f"{mins}m"


print("\n" + "=" * 55)
print("           DIGITAL BEHAVIOUR REPORT")
print("=" * 55)


# -----------------------------------
# APP TIME
# -----------------------------------

instagram_time = df["Instagram_Minutes"].sum()
youtube_time = df["YouTube_Minutes"].sum()
whatsapp_time = df["WhatsApp_Minutes"].sum()
linkedin_time = df["LinkedIn_Minutes"].sum()
study_time = df["Study_Minutes"].sum()


print("\nAPP USAGE")
print("-" * 55)

print(
    f"Instagram : {time_format(instagram_time)}"
)

print(
    f"YouTube   : {time_format(youtube_time)}"
)

print(
    f"WhatsApp  : {time_format(whatsapp_time)}"
)

print(
    f"LinkedIn  : {time_format(linkedin_time)}"
)

print(
    f"Study     : {time_format(study_time)}"
)


# -----------------------------------
# INSTAGRAM
# -----------------------------------

print("\nINSTAGRAM")
print("-" * 55)

print(
    "Time spent:",
    time_format(df["Instagram_Minutes"].sum())
)

print(
    "Reels watched:",
    df["Instagram_Reels"].sum()
)

print(
    "Messages sent:",
    df["Instagram_Messages"].sum()
)

print(
    "Posts liked:",
    df["Instagram_Posts_Liked"].sum()
)


# -----------------------------------
# YOUTUBE
# -----------------------------------

print("\nYOUTUBE")
print("-" * 55)

print(
    "Time spent:",
    time_format(df["YouTube_Minutes"].sum())
)

print(
    "Videos watched:",
    df["YouTube_Videos"].sum()
)


# -----------------------------------
# WHATSAPP
# -----------------------------------

print("\nWHATSAPP")
print("-" * 55)

print(
    "Time spent:",
    time_format(df["WhatsApp_Minutes"].sum())
)

print(
    "Messages sent:",
    df["WhatsApp_Messages"].sum()
)

print(
    "Messages with Person A:",
    df["WhatsApp_Person_A_Messages"].sum()
)

print(
    "Messages with Person B:",
    df["WhatsApp_Person_B_Messages"].sum()
)


# -----------------------------------
# LINKEDIN
# -----------------------------------

print("\nLINKEDIN")
print("-" * 55)

print(
    "Time spent:",
    time_format(df["LinkedIn_Minutes"].sum())
)

print(
    "Posts viewed:",
    df["LinkedIn_Posts_Viewed"].sum()
)


# -----------------------------------
# STUDY
# -----------------------------------

print("\nSTUDY")
print("-" * 55)

print(
    "Total study time:",
    time_format(df["Study_Minutes"].sum())
)


# -----------------------------------
# DAILY AVERAGE
# -----------------------------------

print("\nDAILY AVERAGE")
print("-" * 55)

print(
    "Instagram:",
    time_format(df["Instagram_Minutes"].mean())
)

print(
    "YouTube:",
    time_format(df["YouTube_Minutes"].mean())
)

print(
    "WhatsApp:",
    time_format(df["WhatsApp_Minutes"].mean())
)

print(
    "LinkedIn:",
    time_format(df["LinkedIn_Minutes"].mean())
)

print(
    "Study:",
    time_format(df["Study_Minutes"].mean())
)


# -----------------------------------
# MOST USED APP
# -----------------------------------

app_usage = {

    "Instagram": instagram_time,
    "YouTube": youtube_time,
    "WhatsApp": whatsapp_time,
    "LinkedIn": linkedin_time
}

most_used_app = max(
    app_usage,
    key=app_usage.get
)

print("\nMOST USED APP")
print("-" * 55)

print(
    most_used_app,
    "with",
    time_format(app_usage[most_used_app])
)


# -----------------------------------
# NUMPY STATISTICS
# -----------------------------------

print("\nNUMPY STATISTICS")
print("-" * 55)

instagram_array = df["Instagram_Minutes"].to_numpy()

print(
    "Instagram maximum:",
    np.max(instagram_array),
    "minutes in a day"
)

print(
    "Instagram minimum:",
    np.min(instagram_array),
    "minutes in a day"
)

print(
    "Instagram standard deviation:",
    round(np.std(instagram_array), 2)
)


print("\n" + "=" * 55)