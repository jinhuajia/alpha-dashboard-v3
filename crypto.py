import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Alpha123 像素级重制版",
    page_icon="⚡",
    layout="wide"
)

# 注入严谨打磨后的 CSS
st.markdown("""
<style>
    /* 1. 强制隐藏默认组件，提升纯净度 */
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    .main .block-container {
        padding: 3rem 1rem !important; 
        max-width: 1000px !important; 
        margin: 0 auto;
    }
    
    /* 2. 背景与全局字体 */
    .stApp { background-color: #1a1c23; color: #ffffff; font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; }
    
    /* 3. 顶部金色大标题 - 字体加粗加大 */
    .main-title {
        color: #ffcc00;
        font-size: 32px;
        font-weight: 900;
        text-align: center;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }
    
    /* 4. 导航栏 - 优化间距与丰满度 */
    .nav-bar {
        display: flex;
        justify-content: center;
        gap: 40px;
        color: #9ca3af;
        font-size: 16px;
        margin-bottom: 40px;
        font-weight: 500;
    }
    .nav-item.active { color: #ffcc00; position: relative; font-weight: bold; }
    .nav-item.active::after {
        content: "";
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 100%;
        height: 3px;
        background: #ffcc00;
    }
    
    /* 5. 板块头部样式 */
    .section-header {
        display: flex;
        align-items: center;
        margin: 30px 0 15px 0;
    }
    .section-icon { font-size: 26px; margin-right: 12px; }
    .section-text { font-size: 22px; font-weight: 800; color: #ffffff; }
    .info-badge {
        background: #2d303a;
        color: #ffcc00;
        font-size: 13px;
        padding: 4px 14px;
        border-radius: 20px;
        margin-left: 18px;
        border: 1px solid #3f4451;
    }
    
    /* 6. 表格细节：模仿原版行高与边框 */
    .custom-table { width: 100%; border-collapse: collapse; margin-top: 5px; }
    .custom-table th {
        color: #6b7280;
        text-align: left;
        padding: 15px;
        border-bottom: 2px solid #2d303a;
        font-size: 14px;
        font-weight: normal;
    }
    .custom-table td {
        padding: 20px 15px;
        border-bottom: 1px solid #2d303a;
        vertical-align: middle;
    }
    
    /* 7. 双行文字精准比例 */
    .cell-main { font-size: 17px; font-weight: 700; color: #ffffff; display: block; line-height: 1.4; }
    .cell-sub { font-size: 13px; color: #8c929e; display: block; margin-top: 6px; }
    .price-yellow { color: #ffcc00 !important; }
    
    /* 8. 推荐工具卡片 - 提升质感 */
    .tool-card {
        background: #242731;
        padding: 22px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 5px solid #ffcc00;
        transition: transform 0.2s;
    }
    .tool-title { font-size: 16px; font-weight: bold; color: #ffffff; }
    .tool-desc { font-size: 14px; color: #9ca3af; margin-top: 8px; }
</style>
""", unsafe_allow_html=True)

def main():
    # 顶部区域
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="nav-bar">
        <div class="nav-item active">今日</div>
        <div class="nav-item">历史</div>
        <div class="nav-item">稳定度</div>
        <div class="nav-item">记账</div>
    </div>
    """, unsafe_allow_html=True)

    # 今日空投
    st.markdown("""
    <div class="section-header">
        <span class="section-icon">🎁</span>
        <span class="section-text">今日空投</span>
        <span class="info-badge">Alpha活跃人数推荐 27.3 万 ⓘ</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 调整后的模拟数据
    today_data = {
        "项目": ["""<span class="cell-main">Q 📄</span><span class="cell-sub">Quack AI</span>"""],
        "积分": ["""<span class="cell-main price-yellow">240</span><span class="cell-sub">3.6万份</span>"""],
        "数量": ["""<span class="cell-main price-yellow">2500</span><span class="cell-sub"><span style="color:#ffcc00;">~ $36.7</span> / $36.7</span>"""],
        "时间": ["""<span class="cell-main">15:00</span><span class="cell-sub">已同步</span>"""]
    }
    df = pd.DataFrame(today_data)
    st.write(df.to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)

    # 空投预告
    st.markdown('<div class="section-header"><span class="section-icon">📅</span><span class="section-text">空投预告</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#242731; padding:40px; border-radius:10px; text-align:center; color:#6b7280; font-size:16px;">暂无数据</div>', unsafe_allow_html=True)

    # 推荐工具
    st.markdown('<div class="section-header"><span class="section-icon">⚔️</span><span class="section-text">推荐工具</span></div>', unsafe_allow_html=True)
    
    tools = [
        ("稳定度看板 (3秒更新) 📈", "识别当前时间相对稳定的项目，降低磨损风险"),
        ("模拟抢空投 (图片验证) 🎮", "每天练一练，模拟真实抢空投场景"),
        ("网站使用帮助与提示 ▤", "关于网站功能图标与术语解释说明")
    ]
    
    for title, desc in tools:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-title">{title}</div>
            <div class="tool-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
