# GDELT Shipping Market Impact POC

This is a proof of concept (POC) project that demonstrates how to use the GDELT Project API for real-time country-specific news exploration, and forms a data source concept for a downstream shipping market impact prediction model.

## 🧠 Project goal

- Fetch recent worldwide news using GDELT `doc` API
- Fetch large article batches for feature engineering in POC (count, intensity, tone, topics)
- Cache/handle rate limits with retry + exponential backoff
- Print the latest 5 articles as a fast signal preview
- Serve as an upstream event stream for machine-learning features (e.g., sentiment, event intensity, risk scoring) impacting shipping/logistics markets

## 📁 Files

- `GDELT.py` - main script:
  - `build_gdelt_query_parameters()`
  - `fetch_gdelt_articles_with_retries()`
  - `extract_articles_from_gdelt_response()`
  - `print_news_articles()`
  - `main()`
- `README.md` - this document

## ⚙️ Setup

1. Create and activate a virtual environment (recommended):
   - Windows:
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

   If you don't have `requirements.txt`, install dependencies directly:
   ```powershell
   pip install requests
   ```

## ▶️ Usage

Run the script:

```powershell
python GDELT.py
```

Output is the latest 5 shipping/logistics-related news articles from worldwide sources according to GDELT.

## 💡 Notes

- GDELT enforces rate limits (`429`). The script has retry+backoff to handle this.
- For a production POC, extend with:
  - local cache storage (`JSON`, `Parquet`, DB)
  - NLP sentiment and event classification
  - time-series feature aggregation for shipping risk models
  - periodic scheduling (cron, Airflow, etc.)

## 📈 Next steps toward shipping market ML

1. Collect historical daily event batch from GDELT timeseries (country-level, themes).
2. Generate signal features:
   - Media event count, tone, and intensity
   - Trade corridor / port location references
   - Policy changes, strikes, weather/hurricane, geopolitical actions
3. Join with shipping datasets:
   - fixture rates (e.g., Baltic Indices, freight rates)
   - AIS vessel movement, port throughput
   - S&P logistics labels or market indexes
4. Build model forecasting short-term freight rate impacts or risk spikes.

---

*This README explains the POC as requested, suited for `sandbox/GDELT`.*