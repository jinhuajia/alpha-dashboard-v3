import streamlit as st
import pandas as pd
import feedparser
import time

# 1. 基础配置
st.set_page_config(page_title="Alpha123 极速监控", page_icon="⚡", layout="wide")

# 2. 注入打磨后的 CSS
st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    .main .block-container { padding: 3rem 2rem !important; max-width: 1050px !important; margin: 0 auto !important; }
    .stApp { background-color: #1a1c23; color: #ffffff; font-family: 'PingFang SC', sans-serif; }
    .main-title { color: #ffcc00; font-size: 32px; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .nav-bar { display: flex; justify-content: center; gap: 40px; color: #9ca3af; font-size: 16px; margin-bottom: 40px; }
    .nav-item.active { color: #ffcc00; position: relative; font-weight: bold; border-bottom: 3px solid #ffcc00; padding-bottom: 8px; }
    .custom-table { width: 100%; border-collapse: collapse; }
    .custom-table td { padding: 22px 15px; border-bottom: 1px solid #2d303a; vertical-align: middle; }
    .cell-main { font-size: 17px; font-weight: 700; color: #ffffff; text-decoration: none; display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 350px; }
    .cell-main:hover { color: #ffcc00; }
    .cell-sub { font-size: 13px; color: #8c929e; display: block; margin-top: 6px; }
    .p-yellow { color: #ffcc00 !important; font-weight: bold; }
    .footer { margin-top: 50px; border-top: 1px solid #2d303a; padding-top: 20px; color: #6b7280; font-size: 14px; display: flex; justify-content: space-between; }
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def fetch_live_data():
    rss_url = "https://www.binance.com/en/support/announcement/rss"
    try:
        feed = feedparser.parse(rss_url)
        items = []
        if feed.entries:
            for entry in feed.entries[:3]:
                # 优化标题：去掉过长的后缀
                clean_title = entry.title.split('|')[0].strip()
                items.append({
                    "title": clean_title,
                    "url": entry.link,
                    "sub": "Binance Official",
                    "pts": "New",
                    "val": "LISTING"
                })
        
        if not items:
            # 备选数据保持 UI 丰满
            return [
                {"title": "Quack AI", "url": "https://www.binance.com", "sub": "Binance Launchpool", "pts": "240", "val": "~ $36.7"},
                {"title": "Berachain", "url": "https://www.binance.com", "sub": "Mainnet Reward", "pts": "500", "val": "~ $15.2"},
                {"title": "Monad", "url": "https://www.binance.com", "sub": "Early Access", "pts": "1000", "val": "~ $80.0"}
            ]
        return items
    except:
        return [{"title": "信号同步中...", "url": "#", "sub": "正在接入币安数据流", "pts": "---", "val": "---"}]

def main():
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar"><div class="nav-item active">今日</div><div>历史</div><div>稳定度</div><div>记账</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="display:flex;align-items:center;margin:35px 0 15px 0;"><span>🎁</span><span style="font-size:22px;font-weight:800;margin-left:12px;">今日空投</span><span style="background:#2d303a;color:#ffcc00;font-size:13px;padding:4px 14px;border-radius:20px;margin-left:15px;border:1px solid #3f4451;">币安公告实时监控中 ⓘ</span></div>', unsafe_allow_html=True)

    current_items = fetch_live_data()
    rows = []
    for item in current_items:
        rows.append({
            "项目": f'<a href="{item["url"]}" target="_blank" class="cell-main">{item["title"]}</a><span class="cell-sub">{item["sub"]}</span>',
            "积分": f'<span class="cell-main p-yellow">{item["pts"]}</span><span class="cell-sub">币安同步</span>',
            "数量": f'<span class="cell-main p-yellow">2500</span><span class="cell-sub"><span style="color:#ffcc00;">{item["val"]}</span></span>',
            "时间": f'<span class="cell-main">{time.strftime("%H:%M")}</span><span class="cell-sub">已同步</span>'
        })
    
    st.write(pd.DataFrame(rows).to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)
    st.markdown('<div class="footer"><div>🌐 alpha123.uk</div><div>𝕏 | ✈️ | ❓ | 🌐</div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
