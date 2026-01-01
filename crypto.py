import streamlit as st
import pandas as pd
import requests
import time

# 1. 律动风格 CSS 注入
st.set_page_config(page_title="Alpha123 | 实时快讯", page_icon="⚡", layout="wide")
st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    .main .block-container { padding: 2rem 1rem !important; max-width: 850px !important; margin: 0 auto !important; }
    .stApp { background-color: #0d0e12; color: #ffffff; }
    
    /* 标题区域 */
    .header-box { text-align: left; margin-bottom: 40px; border-bottom: 1px solid #1e2126; padding-bottom: 20px; }
    .main-title { color: #ffcc00; font-size: 28px; font-weight: 800; display: flex; align-items: center; gap: 10px; }
    
    /* 快讯流样式 */
    .news-item { display: flex; gap: 20px; margin-bottom: 35px; position: relative; }
    .news-time { color: #5c6068; font-family: 'Courier New', monospace; font-size: 16px; font-weight: bold; min-width: 60px; padding-top: 2px; }
    .news-dot { width: 8px; height: 8px; background: #ffcc00; border-radius: 50%; position: absolute; left: 74px; top: 8px; box-shadow: 0 0 10px #ffcc00; }
    .news-content { padding-left: 25px; border-left: 1px solid #1e2126; }
    .news-title { font-size: 18px; font-weight: 700; color: #ffffff; margin-bottom: 8px; line-height: 1.4; transition: 0.3s; cursor: pointer; text-decoration: none; display: block; }
    .news-title:hover { color: #ffcc00; }
    .news-desc { font-size: 14px; color: #8c929e; line-height: 1.6; }
    .tag { background: #1e2126; color: #ffcc00; font-size: 11px; padding: 2px 8px; border-radius: 4px; margin-right: 8px; }
</style>
""", unsafe_allow_html=True)

# 2. 模拟币安广场数据抓取 (由于Square无公开API，我们通过RSS中转或模拟)
def fetch_newsflash():
    # 模拟从 binance.com/square/news 实时获取的数据结构
    # 真实版本可以通过 RSSHub 或特定爬虫接口接入
    news_data = [
        {
            "time": "19:25", 
            "title": "币安广场：BTC 突破历史高点，空投板块活跃度上升 27%", 
            "desc": "根据币安广场最新要闻，随着 BTC 波动加大，Layer 2 协议的交互成本下降，建议关注...",
            "tag": "要闻"
        },
        {
            "time": "19:02", 
            "title": "新项目预告：Monad 官方确认将于本季度开启内部测试网", 
            "desc": "Monad 开发者在广场发帖称，目前的测试进度符合预期，早期参与者将获得特殊勋章...",
            "tag": "空投"
        },
        {
            "time": "18:40", 
            "title": "币安将上线新一期 Launchpool 项目，支持 BNB 质押", 
            "desc": "本次活动持续 5 天，预计年化收益率保持在 15% 左右，详细规则请参考公告详情...",
            "tag": "新币"
        }
    ]
    return news_data

def main():
    # 头部设计
    st.markdown("""
    <div class="header-box">
        <div class="main-title"><span>⚡</span> Alpha123 快讯</div>
        <div style="color: #5c6068; font-size: 14px; margin-top: 10px;">聚合币安广场、律动等全球加密快讯 ⓘ</div>
    </div>
    """, unsafe_allow_html=True)

    # 快讯渲染逻辑
    news_list = fetch_newsflash()
    
    for item in news_list:
        st.markdown(f"""
        <div class="news-item">
            <div class="news-time">{item['time']}</div>
            <div class="news-dot"></div>
            <div class="news-content">
                <a class="news-title" href="#">{item['title']}</a>
                <div class="news-desc">
                    <span class="tag">{item['tag']}</span>
                    {item['desc']}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 底部版权
    st.markdown("""
    <div style="margin-top:80px; text-align:center; color:#2d303a; font-size:12px;">
        © 2026 ALPHA123 NEWSFLASH | SOURCE: BINANCE SQUARE
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
