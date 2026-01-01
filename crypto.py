import streamlit as st
import pandas as pd
import feedparser
import time
from datetime import datetime

# 1. 页面配置与律动风格 CSS
st.set_page_config(page_title="Alpha123 | 币安广场快讯", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    .main .block-container { padding: 2rem 1rem !important; max-width: 800px !important; margin: 0 auto !important; }
    .stApp { background-color: #0d0e12; color: #ffffff; font-family: 'PingFang SC', sans-serif; }
    
    /* 头部样式 */
    .header-box { border-bottom: 1px solid #1e2126; padding-bottom: 25px; margin-bottom: 40px; }
    .main-title { color: #ffcc00; font-size: 30px; font-weight: 800; }
    .sub-status { color: #5c6068; font-size: 14px; margin-top: 8px; display: flex; align-items: center; gap: 8px; }
    .live-dot { width: 8px; height: 8px; background: #00ff00; border-radius: 50%; display: inline-block; animation: blink 1.5s infinite; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

    /* 律动风格时间轴 [参考 blockbeats] */
    .news-container { position: relative; padding-left: 30px; border-left: 1px solid #1e2126; }
    .news-item { position: relative; margin-bottom: 40px; padding-bottom: 10px; }
    .news-dot { position: absolute; left: -35px; top: 6px; width: 10px; height: 10px; background: #ffcc00; border-radius: 50%; border: 2px solid #0d0e12; box-shadow: 0 0 8px #ffcc00; }
    .news-time { color: #5c6068; font-family: 'Courier New', monospace; font-size: 15px; font-weight: bold; margin-bottom: 8px; }
    .news-title { font-size: 19px; font-weight: 700; color: #ffffff; line-height: 1.5; margin-bottom: 10px; cursor: pointer; text-decoration: none; display: block; }
    .news-title:hover { color: #ffcc00; }
    .news-content { font-size: 15px; color: #a1a1a1; line-height: 1.7; }
    .news-tag { color: #ffcc00; font-weight: bold; margin-right: 8px; }
</style>
""", unsafe_allow_html=True)

# 2. 免费抓取逻辑：利用 RSSHub 镜像
@st.cache_data(ttl=300) # 每5分钟强制刷新
def fetch_binance_square():
    # 币安广场“要闻”的 RSS 中转源
    rss_url = "https://rsshub.app/binance/news/zh-CN" 
    try:
        feed = feedparser.parse(rss_url)
        news_items = []
        for entry in feed.entries[:10]: # 展示最新的10条快讯
            # 格式化时间
            dt = datetime.fromtimestamp(time.mktime(entry.published_parsed))
            news_items.append({
                "time": dt.strftime("%H:%M"),
                "title": entry.title,
                "summary": entry.summary[:150] + "...", # 截取部分摘要
                "link": entry.link
            })
        return news_items
    except:
        # 抓取失败时的演示数据
        return [
            {"time": "19:30", "title": "币安广场：比特币现货 ETF 昨日净流入超过 2 亿美元", "summary": "根据最新披露数据，机构投资者持续加码，比特币在
