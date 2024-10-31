
# 📰 Hacker News Scraper

🚀 A web scraping project designed to extract and display the top news from [Hacker News](https://news.ycombinator.com/), store it in MongoDB, and provide a web interface for users to view the latest, most-upvoted articles!

## 📌 Features
- Scrapes top Hacker News articles from multiple pages.
- Extracts and stores Title, URL, and Upvotes for each article.
- Saves data to MongoDB and periodically refreshes to stay updated.
- Provides a web interface to view and interact with the latest news.

## 📂 Project Structure
| File              | Description |
|-------------------|-------------|
| `app.py`          | Main application file - sets up Flask server, connects to MongoDB, and runs data scraping with periodic refresh. |
| `scrap.py`        | Handles the web scraping logic, fetching top articles and storing them in MongoDB. |
| `create_csv.py`   | Generates a CSV file to save scraped data for local reference. |
| `top_three.py`    | Calculates and returns the top three most-upvoted articles. |

## 🛠️ Installation Guide
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/hacker-news-scraper.git
   cd hacker-news-scraper
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Start MongoDB**:
   ```bash
   mongod --dbpath /path-to-your-data-directory
   ```

## ▶️ Usage
1. **Run the app**:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000/` to view the news articles.

## 📈 Example Output
<details>
<summary>Show sample output</summary>

### Latest Hacker News Articles
| Title | URL | Upvotes |
|-------|-----|---------|
| Sample Article | https://sample-url.com | 120 |
| Sample Article | https://sample-url.com | 98 |
| Sample Article | https://sample-url.com | 75 |

</details>

## 🧰 Dependencies
- `Flask`
- `pandas`
- `pymongo`
- `requests`
- `BeautifulSoup4`

## 🎯 Future Improvements
- Enhance scraping to retrieve more data points.
- Add more data visualizations on the web interface.
- Implement notifications for top trending articles.

## 📜 License
This project is licensed under the MIT License.
