import streamlit as st
import pandas as pd

# 1. 基础配置
st.set_page_config(page_title="Alpha123 精修版", page_icon="⚡", layout="wide")

# 2. 注入优化后的 CSS
st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    
    .main .block-container {
        padding: 3rem 2rem !important; 
        max-width: 1050px !important; 
        margin: 0 auto !important;
    }
    
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
    .price-yellow { color: #ffcc00 !important; font-weight: bold; }
    
    /* 底部导航栏样式 */
    .footer {
        margin-top: 60px;
        padding-top: 20px;
        border-top: 1px solid #2d303a;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #6b7280;
        font-size: 14px;
    }
    .footer-icons { display: flex; gap: 20px; font-size: 18px; }
</style>
""", unsafe_allow_html=True)

def main():
    # 顶部标题与导航
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar"><div class="nav-item active">今日</div><div>历史</div><div>稳定度</div><div>记账</div></div>', unsafe_allow_html=True)
    
    # 今日空投板块
    st.markdown('<div class="section-header"><span>🎁</span><span class="section-text">今日空投</span><span class="info-badge">Alpha活跃人数推荐 27.3 万 ⓘ</span></div>', unsafe_allow_html=True)
    
    # 严格保留 3 条核心数据
    core_data = [
        ["Q 📄", "Quack AI", "240", "3.6万份", "2500", "~ $36.7", "15:00"],
        ["Berachain 🐻", "BGT Reward", "500", "不限量", "100", "~ $15.2", "16:30"],
        ["Monad 🟣", "Early Access", "1000", "5000份", "50", "~ $80.0", "18:00"]
    ]
    
    rows = []
    for item in core_data:
        rows.append({
            "项目": f'<span class="cell-main">{item[0]}</span><span class="cell-sub">{item[1]}</span>',
            "积分": f'<span class="cell-main price-yellow">{item[2]}</span><span class="cell-sub">{item[3]}</span>',
            "数量": f'<span class="cell-main price-yellow">{item[4]}</span><span class="cell-sub"><span style="color:#ffcc00;">{item[5]}</span></span>',
            "时间": f'<span class="cell-main">{item[6]}</span><span class="cell-sub">已同步</span>'
        })
    st.write(pd.DataFrame(rows).to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)

    # 空投预告
    st.markdown('<div class="section-header"><span>📅</span><span class="section-text">空投预告</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#242731;padding:40px;border-radius:10px;text-align:center;color:#6b7280;margin-top:10px;">暂无数据</div>', unsafe_allow_html=True)

    # 推荐工具
    st.markdown('<div class="section-header"><span>⚔️</span><span class="section-text">推荐工具</span></div>', unsafe_allow_html=True)
    tools = [
        ("稳定度看板 (3秒更新) 📈", "识别当前时间相对稳定的项目，降低磨损风险"),
        ("模拟抢空投 (图片验证) 🎮", "每天练一练，模拟真实抢空投场景")
    ]
    for title, desc in tools:
        st.markdown(f'<div style="background:#242731; padding:20px; border-radius:10px; margin-bottom:12px; border-left:5px solid #ffcc00;"><div style="font-weight:bold; font-size:16px;">{title}</div><div style="font-size:13px; color:#9ca3af; margin-top:8px;">{desc}</div></div>', unsafe_allow_html=True)

    # --- 优化后的底部导航栏 ---
    st.markdown("""
    <div class="footer">
        <div>🌐 alpha123.uk</div>
        <div class="footer-icons">
            <span>𝕏</span>
            <span>✈️</span>
            <span>❓</span>
            <span>🌐</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
