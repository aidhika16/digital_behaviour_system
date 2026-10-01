import pandas as pd
import numpy as np
from datetime import date, timedelta


def generate_data(days=30):

    dates = [
        date.today() - timedelta(days=i)
        for i in range(days - 1, -1, -1)
    ]

    data = {

        "Date": dates,

        # Instagram
        "Instagram_Minutes": np.random.randint(20, 241, days),
        "Instagram_Reels": np.random.randint(10, 120, days),
        "Instagram_Messages": np.random.randint(0, 80, days),
        "Instagram_Posts_Liked": np.random.randint(0, 50, days),

        # YouTube
        "YouTube_Minutes": np.random.randint(15, 181, days),
        "YouTube_Videos": np.random.randint(1, 20, days),

        # WhatsApp
        "WhatsApp_Minutes": np.random.randint(10, 121, days),
        "WhatsApp_Messages": np.random.randint(5, 250, days),
        "WhatsApp_Person_A_Messages": np.random.randint(0, 100, days),
        "WhatsApp_Person_B_Messages": np.random.randint(0, 60, days),

        # LinkedIn
        "LinkedIn_Minutes": np.random.randint(0, 61, days),
        "LinkedIn_Posts_Viewed": np.random.randint(0, 50, days),

        # Study
        "Study_Minutes": np.random.randint(30, 361, days)
    }

    df = pd.DataFrame(data)

    df.to_csv("digital_behaviour.csv", index=False)

    print("Data generated successfully!")
    print("30 days of random data saved to digital_behaviour.csv")


if __name__ == "__main__":
    generate_data()