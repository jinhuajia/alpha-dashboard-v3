import streamlit as st
import pandas as pd

# 页面基础配置
st.set_page_config(
    page_title="Alpha123 极速版",
    page_icon="⚡",
    layout="wide"
)

# 注入打磨后的像素级 CSS
st.markdown("""
<style>
    /* 强制隐藏 Streamlit 所有的默认边距和头部 */
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    .main .block-container {padding: 1rem 2rem !important; max-width: 900px !important; margin: 0 auto;}
    
    .stApp { background-color: #1a1c23; color: #ffffff; }
    
    /* 顶部金色标题 */
    .main-title {
        color: #ffcc00;
        font-size: 26px;
        font-weight: 800;
        text-align: center;
        margin-top: 10px;
    }
    
    /* 仿制水平导航栏 */
    .nav-bar {
        display: flex;
        justify-content: center;
        gap: 30px;
        color: #9ca3af;
        font-size: 15px;
        margin: 15px 0 30px 0;
        font-weight: 500;
    }
    .nav-item.active { color: #ffcc00; border-bottom: 2px solid #ffcc00; padding-bottom: 5px; }
    
    /* 模块标题与小标签 */
    .section-header {
        display: flex;
        align-items: center;
        margin: 25px 0 15px 0;
    }
    .section-icon { font-size: 22px; margin-right: 10px; }
    .section-text { font-size: 18px; font-weight: bold; }
    .info-badge {
        background: #374151;
        color: #ffcc00;
        font-size: 11px;
        padding: 2px 10px;
        border-radius: 20px;
        margin-left: 15px;
        border: 1px solid #4b5563;
    }
    
    /* 精修表格排版 */
    .custom-table { width: 100%; border-collapse: collapse; }
    .custom-table th {
        color: #6b7280;
        text-align: left;
        padding: 12px;
        border-bottom: 2px solid #2d303a;
        font-size: 13px;
    }
    .custom-table td {
        padding: 15px 12px;
        border-bottom: 1px solid #2d303a;
        vertical-align: middle;
    }
    
    /* 文字双行显示逻辑 */
    .cell-main { font-size: 15px; font-weight: 600; color: #ffffff; display: block; }
    .cell-sub { font-size: 11px; color: #6b7280; display: block; margin-top: 4px; }
    .price-yellow { color: #ffcc00; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

def main():
    # 顶部标题与导航
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="nav-bar">
        <div class="nav-item active">今日</div>
        <div class="nav-item">历史</div>
        <div class="nav-item">稳定度</div>
        <div class="nav-item">记账</div>
    </div>
    """, unsafe_allow_html=True)

    # 今日空投板块
    st.markdown("""
    <div class="section-header">
        <span class="section-icon">🎁</span>
        <span class="section-text">今日空投</span>
        <span class="info-badge">Alpha活跃人数推荐 27.3 万 ⓘ</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 构造像素级模拟数据
    today_data = {
        "项目": ["""<span class="cell-main">Q 📄</span><span class="cell-sub">Quack AI</span>"""],
        "积分": ["""<span class="cell-main price-yellow">240</span><span class="cell-sub">3.6万份</span>"""],
        "数量": ["""<span class="cell-main price-yellow">2500</span><span class="cell-sub"><span style="color:#ffcc00;">~ $34.3</span> / $34.4</span>"""],
        "时间": ["""<span class="cell-main">15:00</span><span class="cell-sub">已同步</span>"""]
    }
    df = pd.DataFrame(today_data)
    st.write(df.to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)

    # 推荐工具
    st.markdown('<div class="section-header"><span class="section-icon">⚔️</span><span class="section-text">推荐工具</span></div>', unsafe_allow_html=True)
    
    tools = [
        ("稳定度看板 (3秒更新) 📈", "识别当前时间相对稳定的项目，降低磨损风险"),
        ("模拟抢空投 (图片验证) 🎮", "每天练一练，模拟真实抢空投场景"),
        ("网站使用帮助与提示 ▤", "关于网站功能图标与术语解释说明")
    ]
    
    for title, desc in tools:
        st.markdown(f"""
        <div style="background:#242731; padding:15px; border-radius:8px; margin-bottom:12px; border-left:3px solid #ffcc00;">
            <div style="font-weight:bold; font-size:14px;">{title}</div>
            <div style="font-size:12px; color:#6b7280; margin-top:5px;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
