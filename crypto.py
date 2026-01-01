import streamlit as st
import pandas as pd
import requests
import time

# 1. 基础 UI 配置
st.set_page_config(page_title="Alpha123 极简实时版", page_icon="⚡", layout="wide")
st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    .main .block-container { padding: 3rem 2rem !important; max-width: 1050px !important; margin: 0 auto !important; }
    .stApp { background-color: #1a1c23; color: #ffffff; font-family: 'PingFang SC', sans-serif; }
    .main-title { color: #ffcc00; font-size: 32px; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .nav-bar { display: flex; justify-content: center; gap: 40px; color: #9ca3af; font-size: 16px; margin-bottom: 40px; }
    .nav-item.active { color: #ffcc00; font-weight: bold; border-bottom: 3px solid #ffcc00; padding-bottom: 8px; }
    .custom-table { width: 100%; border-collapse: collapse; }
    .custom-table td { padding: 22px 15px; border-bottom: 1px solid #2d303a; vertical-align: middle; }
    .cell-main { font-size: 17px; font-weight: 700; color: #ffffff; display: block; }
    .cell-sub { font-size: 13px; color: #8c929e; display: block; margin-top: 6px; }
    .p-yellow { color: #ffcc00 !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 2. 实时抓取函数（去掉缓存，确保每次刷新都是最新的）
def fetch_now():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    try:
        # 增加随机参数防止浏览器缓存
        response = requests.get(f"{url}?t={int(time.time())}", timeout=5)
        data = response.json()
        # 获取最后上线的 3 个资产
        symbols = data['symbols'][-3:] 
        items = []
        for s in symbols:
            items.append({
                "name": s['baseAsset'],
                "sub": f"Status: {s['status']}",
                "pts": "New",
                "val": f"Pair: {s['quoteAsset']}"
            })
        return items, "✅ API 链接正常"
    except Exception as e:
        # 兜底数据
        return [
            {"name": "Quack AI", "sub": "Binance Launchpad", "pts": "240", "val": "~ $36.7"},
            {"name": "Berachain", "sub": "BGT Reward", "pts": "500", "val": "~ $15.2"},
            {"name": "Monad", "sub": "Early Access", "pts": "1000", "val": "~ $80.0"}
        ], f"⚠️ 链接超时: {str(e)}"

def main():
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar"><div class="nav-item active">今日</div><div>历史</div><div>稳定度</div><div>记账</div></div>', unsafe_allow_html=True)
    
    # 动态数据获取
    items, status_msg = fetch_now()
    
    st.markdown(f'<div style="display:flex;align-items:center;margin:30px 0 15px 0;"><span>🎁</span><span style="font-size:22px;font-weight:800;margin-left:12px;">今日空投</span><span style="background:#2d303a;color:#ffcc00;font-size:12px;padding:4px 14px;border-radius:20px;margin-left:15px;border:1px solid #3f4451;">{status_msg} | {time.strftime("%H:%M:%S")}</span></div>', unsafe_allow_html=True)

    rows = []
    for it in items:
        rows.append({
            "项目": f'<span class="cell-main">{it["name"]}</span><span class="cell-sub">{it["sub"]}</span>',
            "积分": f'<span class="cell-main p-yellow">{it["pts"]}</span><span class="cell-sub">币安同步</span>',
            "数量": f'<span class="cell-main p-yellow">2500</span><span class="cell-sub"><span style="color:#ffcc00;">{it["val"]}</span></span>',
            "时间": f'<span class="cell-main">{time.strftime("%H:%M")}</span><span class="cell-sub">自动刷新</span>'
        })
    st.write(pd.DataFrame(rows).to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)
    
    # 底部版权
    st.markdown('<div style="margin-top:60px; border-top:1px solid #2d303a; padding-top:20px; color:#6b7280; font-size:14px; display:flex; justify-content:space-between;"><div>🌐 alpha123.uk</div><div>𝕏 | ✈️ | ❓ | 🌐</div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
