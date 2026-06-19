from fastapi import FastAPI
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from fastapi.responses import FileResponse
from pathlib import Path


app = FastAPI(title="Financial Analysis Service")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/technical-analysis")
def technical_analysis(symbol: str = None):
    prices = pd.read_csv("./notebooks/data/prices.csv")
    available_symbols = prices["Symbol"].unique().tolist()
    if symbol is None:
        return {"message": f"Please choose a symbol from the available symbols: {available_symbols}"}

    message, url = generate_plot(symbol)

    image = Path(url)

    return FileResponse(path=image, media_type="image/png", filename=f"{symbol}_macd.png")
    

def generate_plot(symbol: str):
    prices = pd.read_csv("./notebooks/data/prices.csv")
    df = prices[prices["Symbol"] == symbol].copy()
    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()

    fig, ax = plt.subplots(figsize=(10,6))
    df["Close"].plot(ax=ax, color='#374151', alpha=0.2, secondary_y=True)
    macd.plot(ax=ax, color='blue')
    signal.plot(ax=ax, color='red')

    ax.set_title(f"MACD and Signal for {symbol}")
    ax.set_xlabel("Date")
    ax.set_ylabel("MACD")
    ax.right_ax.set_ylabel("Close Price")

    # Guardar la figura en un archivo temporal con timestamp
    timestamp = pd.Timestamp.now().strftime("%Y%m%d%H%M%S")
    plt.savefig(f"./outputs/{symbol}_macd_{timestamp}.png")

    return {
        "message": f"MACD and Signal plot for {symbol} saved as ./outputs/{symbol}_macd_{timestamp}.png",
        "url": f"./outputs/{symbol}_macd_{timestamp}.png"
    }