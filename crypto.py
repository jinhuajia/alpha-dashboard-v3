import streamlit as st
import pandas as pd
import time

# 1. 基础配置
st.set_page_config(page_title="Alpha123 自动化版", page_icon="⚡", layout="wide")

# 2. 核心 CSS (保持你满意的 UI)
st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    .main .block-container { padding: 3rem 2rem !important; max-width: 1050px !important; margin: 0 auto !important; }
    .stApp { background-color: #1a1c23; color: #ffffff; font-family: 'PingFang SC', sans-serif; }
    .main-title { color: #ffcc00; font-size: 32px; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .nav-bar { display: flex; justify-content: center; gap: 40px; color: #9ca3af; font-size: 16px; margin-bottom: 40px; }
    .nav-item.active { color: #ffcc00; position: relative; font-weight: bold; border-bottom: 3px solid #ffcc00; padding-bottom: 8px; }
    .section-header { display: flex; align-items: center; margin: 35px 0 15px 0; }
    .section-text { font-size: 22px; font-weight: 800; color: #ffffff; margin-left: 12px; }
    .info-badge { background: #2d303a; color: #ffcc00; font-size: 13px; padding: 4px 14px; border-radius: 20px; margin-left: 15px; border: 1px solid #3f4451; }
    .custom-table { width: 100%; border-collapse: collapse; }
    .custom-table td { padding: 22px 15px; border-bottom: 1px solid #2d303a; vertical-align: middle; }
    .cell-main { font-size: 17px; font-weight: 700; color: #ffffff; display: block; }
    .cell-sub { font-size: 13px; color: #8c929e; display: block; margin-top: 6px; }
    .p-yellow { color: #ffcc00 !important; font-weight: bold; }
    .footer { margin-top: 60px; padding-top: 20px; border-top: 1px solid #2d303a; display: flex; justify-content: space-between; color: #6b7280; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# 3. 核心功能：数据抓取模拟器 (未来这里会替换成真正的爬虫)
@st.cache_data(ttl=60) # 每 60 秒自动强制过期，触发重新抓取
def fetch_binance_announcements():
    # 模拟从币安抓取到的最新 3 条数据
    # 在真实版本中，我们会使用 requests.get("https://www.binance.com/zh-CN/support/announcement/...")
    mock_data = [
        {"icon": "Q 📄", "name": "Quack AI", "points": "240", "copies": "3.6万份", "amount": "2500", "val": "~ $36.7", "time": "15:00"},
        {"icon": "B 🐻", "name": "Berachain", "points": "500", "copies": "不限量", "amount": "100", "val": "~ $15.2", "time": "16:30"},
        {"icon": "M 🟣", "name": "Monad", "points": "1000", "copies": "5000份", "amount": "50", "val": "~ $80.0", "time": "18:00"},
    ]
    return mock_data

def main():
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar"><div class="nav-item active">今日</div><div>历史</div><div>稳定度</div><div>记账</div></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header"><span>🎁</span><span class="section-text">今日空投</span><span class="info-badge">已开启币安公告监控 ⓘ</span></div>', unsafe_allow_html=True)
    
    # 获取“实时”数据
    latest_items = fetch_binance_announcements()
    
    rows = []
    for item in latest_items:
        rows.append({
            "项目": f'<span class="cell-main">{item["icon"]}</span><span class="cell-sub">{item["name"]}</span>',
            "积分": f'<span class="cell-main p-yellow">{item["points"]}</span><span class="cell-sub">{item["copies"]}</span>',
            "数量": f'<span class="cell-main p-yellow">{item["amount"]}</span><span class="cell-sub"><span style="color:#ffcc00;">{item["val"]}</span></span>',
            "时间": f'<span class="cell-main">{item["time"]}</span><span class="cell-sub">自动刷新中</span>'
        })
    st.write(pd.DataFrame(rows).to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)

    st.markdown('<div class="footer"><div>🌐 alpha123.uk</div><div>𝕏 | ✈️ | ❓</div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
