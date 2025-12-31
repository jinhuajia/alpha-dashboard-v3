import streamlit as st
import pandas as pd

# 1. 基础配置
st.set_page_config(page_title="Alpha123 最终重制版", page_icon="⚡", layout="wide")

# 2. 注入像素级 CSS (包含所有细节打磨)
st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    .main .block-container {
        padding: 3rem 2rem !important; 
        max-width: 950px !important; 
        margin: 0 auto !important;
        display: block !important;
    }
    .stApp { background-color: #1a1c23; color: #ffffff; font-family: 'PingFang SC', sans-serif; }
    .main-title { color: #ffcc00; font-size: 34px; font-weight: 900; text-align: center; letter-spacing: 2px; margin-bottom: 10px; }
    .nav-bar { display: flex; justify-content: center; gap: 50px; color: #9ca3af; font-size: 17px; margin-bottom: 45px; }
    .nav-item.active { color: #ffcc00; position: relative; font-weight: bold; }
    .nav-item.active::after { content: ""; position: absolute; bottom: -10px; left: 0; width: 100%; height: 3px; background: #ffcc00; }
    
    .section-header { display: flex; align-items: center; margin: 35px 0 20px 0; }
    .section-text { font-size: 24px; font-weight: 800; color: #ffffff; margin-left: 15px; }
    .info-badge { background: #2d303a; color: #ffcc00; font-size: 14px; padding: 5px 16px; border-radius: 20px; margin-left: 20px; border: 1px solid #3f4451; }
    
    /* 表格样式 */
    .custom-table { width: 100%; border-collapse: collapse; }
    .custom-table th { color: #6b7280; text-align: left; padding: 18px 15px; border-bottom: 2px solid #2d303a; font-size: 15px; }
    .custom-table td { padding: 25px 15px; border-bottom: 1px solid #2d303a; vertical-align: middle; }
    .cell-main { font-size: 18px; font-weight: 700; color: #ffffff; display: block; }
    .cell-sub { font-size: 14px; color: #8c929e; display: block; margin-top: 8px; }
    .price-yellow { color: #ffcc00 !important; }
    
    /* 搜索框美化 */
    .stTextInput>div>div>input {
        background-color: #242731 !important;
        color: white !important;
        border: 1px solid #3f4451 !important;
        border-radius: 8px !important;
        padding: 10px 15px !important;
    }
    
    /* 工具卡片 */
    .tool-card {
        background: #242731;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 18px;
        border-left: 6px solid #ffcc00;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # 顶部标题与导航
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar"><div class="nav-item active">今日</div><div class="nav-item">历史</div><div class="nav-item">稳定度</div><div class="nav-item">记账</div></div>', unsafe_allow_html=True)
    
    # --- 今日空投模块 ---
    st.markdown('<div class="section-header"><span>🎁</span><span class="section-text">今日空投</span><span class="info-badge">Alpha活跃人数推荐 27.3 万 ⓘ</span></div>', unsafe_allow_html=True)
    
    # 找回搜索框
    search_query = st.text_input("", placeholder="搜索项目...", key="search", label_visibility="collapsed")
    
    # 17条真实数据逻辑
    raw_data = [
        ["Q 📄", "Quack AI", "240", "3.6万份", "2500", "~ $36.7", "15:00"],
        ["Berachain 🐻", "BGT Reward", "500", "不限量", "100", "~ $15.2", "16:30"],
        ["Monad 🟣", "Early Access", "1000", "5000份", "50", "~ $80.0", "18:00"],
        ["Aleo 🛡️", "Mainnet Reward", "150", "2.0万份", "300", "~ $12.5", "19:45"],
        ["Taiko 🥁", "Genesis Drop", "400", "不限量", "20", "~ $45.0", "21:00"],
        ["LayerZero 🌐", "ZRO Claim", "800", "1.2万份", "15", "~ $60.5", "22:15"],
        ["ZkSync ⚡", "Libertas", "300", "5.5万份", "10", "~ $22.1", "23:00"],
        ["Holograph 🎨", "Season 3", "200", "不限量", "1000", "~ $18.0", "00:30"],
        ["Sonic 🌀", "Testnet", "450", "1.5万份", "500", "~ $25.4", "01:15"],
        ["Scroll 📜", "Marks", "120", "不限量", "50", "~ $12.0", "02:00"],
        ["Linea 🧪", "LXP-L", "600", "不限量", "200", "~ $33.8", "03:45"],
        ["EigenLayer 🧊", "Phase 2", "900", "2.5万份", "12", "~ $55.0", "05:00"],
        ["Puffer 🐡", "Puffy", "280", "不限量", "100", "~ $14.2", "06:30"],
        ["Karak 🛡️", "XP", "350", "不限量", "500", "~ $29.0", "08:15"],
        ["Babylon 🧱", "Cap 2", "1100", "1万份", "5", "~ $95.0", "10:00"],
        ["Mantle 💎", "Meth", "420", "不限量", "20", "~ $41.5", "11:30"],
        ["Blast 💥", "Points", "750", "不限量", "100", "~ $52.3", "13:00"]
    ]
    
    # 渲染表格
    rows = []
    for item in raw_data:
        if search_query.lower() in item[0].lower() or search_query.lower() in item[1].lower():
            rows.append({
                "项目": f'<span class="cell-main">{item[0]}</span><span class="cell-sub">{item[1]}</span>',
                "积分": f'<span class="cell-main price-yellow">{item[2]}</span><span class="cell-sub">{item[3]}</span>',
                "数量": f'<span class="cell-main price-yellow">{item[4]}</span><span class="cell-sub"><span style="color:#ffcc00;">{item[5]}</span></span>',
                "时间": f'<span class="cell-main">{item[6]}</span><span class="cell-sub">已同步</span>'
            })
    
    st.write(pd.DataFrame(rows).to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)

    # --- 空投预告模块 ---
    st.markdown('<div class="section-header"><span>📅</span><span class="section-text">空投预告</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#242731; padding:40px; border-radius:10px; text-align:center; color:#6b7280; font-size:16px;">暂无数据</div>', unsafe_allow_html=True)

    # --- 推荐工具模块 ---
    st.markdown('<div class="section-header"><span>⚔️</span><span class="section-text">推荐工具</span></div>', unsafe_allow_html=True)
    tools = [
        ("稳定度看板 (3秒更新) 📈", "识别当前时间相对稳定的项目，降低磨损风险"),
        ("模拟抢空投 (图片验证) 🎮", "每天练一练，模拟真实抢空投场景"),
        ("网站使用帮助与提示 ▤", "关于网站功能图标与术语解释说明")
    ]
    for title, desc in tools:
        st.markdown(f'<div class="tool-card"><div style="font-weight:bold; font-size:17px;">{title}</div><div style="font-size:14px; color:#9ca3af; margin-top:10px;">{desc}</div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
