import pandas as pd
import matplotlib.pyplot as plt
import os


df = pd.read_csv("data/app_metrics.csv")
df["day"] = pd.to_datetime(df["day"])


os.makedirs("docs/images", exist_ok=True)

def plot_daily_trend():
    plt.figure(figsize=(8,5))
    plt.plot(df["day"], df["active_users"], marker="o", color="blue")
    plt.title("Daily Trend of Active Users")
    plt.xlabel("Date")
    plt.ylabel("Active Users")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("docs/images/daily_trend.png")
    plt.show()

def plot_minutes_per_user():
    plt.figure(figsize=(8,5))
    plt.plot(df["day"], df["minutes_per_user"], marker="o", color="green")
    plt.title("Daily Trend of Minutes per User")
    plt.xlabel("Date")
    plt.ylabel("Minutes per User")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("docs/images/minutes_per_user.png")
    plt.show()

def plot_installs_retention():
    plt.figure(figsize=(8,5))
    plt.plot(df["day"], df["installs"], marker="o", color="blue", label="Installs")
    plt.plot(df["day"], df["retention"], marker="s", color="orange", label="Retention Rate")
    plt.title("Installs and Retention Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("docs/images/installs_retention.png")
    plt.show()

def plot_growth_rate_moving_avg():
    df["growth_rate"] = df["active_users"].pct_change() * 100
    df["moving_avg"] = df["active_users"].rolling(window=3).mean()

    plt.figure(figsize=(8,5))
    plt.plot(df["day"], df["growth_rate"], marker="o", color="red", label="Daily Growth Rate (%)")
    plt.plot(df["day"], df["moving_avg"], marker="s", color="purple", label="3-Day Moving Average")
    plt.title("Active Users Growth Rate and Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("docs/images/growth_rate_moving_avg.png")
    plt.show()

if __name__ == "__main__":
    plot_daily_trend()
    plot_minutes_per_user()
    plot_installs_retention()
    plot_growth_rate_moving_avg()
