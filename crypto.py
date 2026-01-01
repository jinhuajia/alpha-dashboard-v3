import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# 1. 基础配置
st.set_page_config(page_title="Alpha123 动态监控", page_icon="⚡", layout="wide")

# 2. CSS 样式 (保持你最满意的 UI)
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
    .cell-main { font-size: 17px; font-weight: 700; color: #ffffff; display: block; text-decoration: none; }
    .cell-main:hover { color: #ffcc00; } /* 鼠标悬停变色 */
    .cell-sub { font-size: 13px; color: #8c929e; display: block; margin-top: 6px; }
    .p-yellow { color: #ffcc00 !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. 币安公告抓取逻辑 (增强版)
@st.cache_data(ttl=300)
def fetch_real_data():
    # 币安新币公告频道
    url = "https://www.binance.com/zh-CN/support/announcement/c-48"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        items = []
        # 寻找公告列表中的所有链接
        links = soup.find_all('a')
        
        for link in links:
            text = link.get_text().strip()
            # 过滤核心关键词
            if any(k in text for k in ["上线", "推出", "Launchpool", "Megadrop"]):
                href = link.get('href')
                full_url = f"https://www.binance.com{href}" if href.startswith('/') else href
                items.append({
                    "title": text[:30],
                    "url": full_url,
                    "sub": "币安官方公告",
                    "pts": "New",
                    "val": "Listing"
                })
        
        if not items:
            # 演示数据，也加上链接方便你测试跳转效果
            return [
                {"title": "Quack AI", "url": "https://www.binance.com/zh-CN/support/announcement/", "sub": "演示项目 A", "pts": "240", "val": "~ $36.7"},
                {"title": "Berachain", "url": "https://www.binance.com/zh-CN/support/announcement/", "sub": "演示项目 B", "pts": "500", "val": "~ $15.2"},
                {"title": "Monad", "url": "https://www.binance.com/zh-CN/support/announcement/", "sub": "演示项目 C", "pts": "1000", "val": "~ $80.0"}
            ]
        return items[:3]
    except:
        return [{"title": "网络请求受限", "url": "#", "sub": "请稍后重试", "pts": "---", "val": "---"}]

def main():
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar"><div class="nav-item active">今日</div><div>历史</div><div>稳定度</div><div>记账</div></div>', unsafe_allow_html=True)
    
    current_data = fetch_real_data()
    
    rows = []
    for item in current_data:
        # 将项目名称包装在 <a> 标签中实现跳转
        rows.append({
            "项目": f'<a href="{item["url"]}" target="_blank" class="cell-main">{item["title"]}</a><span class="cell-sub">{item["sub"]}</span>',
            "积分": f'<span class="cell-main p-yellow">{item["pts"]}</span><span class="cell-sub">币安实时</span>',
            "数量": f'<span class="cell-main p-yellow">2500</span><span class="cell-sub"><span style="color:#ffcc00;">{item["val"]}</span></span>',
            "时间": f'<span class="cell-main">{time.strftime("%H:%M")}</span><span class="cell-sub">已同步</span>'
        })
    
    st.write(pd.DataFrame(rows).to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)

    # 底部版权
    st.markdown('<div style="margin-top:50px; border-top:1px solid #2d303a; padding-top:20px; color:#6b7280; font-size:14px; display:flex; justify-content:space-between;"><div>🌐 alpha123.uk</div><div>𝕏 | ✈️ | ❓</div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
