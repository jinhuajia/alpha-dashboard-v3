import streamlit as st
import pandas as pd

# 1. 页面基础配置：暗黑模式风格
st.set_page_config(
    page_title="Alpha123 仿制版 | 加密货币空投日历",
    page_icon="🎁",
    layout="wide"
)

# 2. 注入 Alpha123 像素级 CSS
st.markdown("""
<style>
    /* 全局深色背景 */
    .stApp { background-color: #1a1c23; color: #ffffff; }
    
    /* 顶部大标题：金色字体 */
    .main-title {
        color: #ffcc00;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-nav {
        color: #9ca3af;
        text-align: center;
        font-size: 14px;
        margin-bottom: 30px;
    }
    
    /* 模块标题样式：带图标 */
    .section-title {
        display: flex;
        align-items: center;
        color: #ffffff;
        font-size: 20px;
        font-weight: bold;
        margin: 20px 0;
    }
    
    /* 卡片容器 */
    .crypto-card {
        background-color: #242731;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 4px solid #ffcc00;
    }
    
    /* 自定义表格样式 */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        color: #d1d5db;
    }
    .custom-table th {
        color: #6b7280;
        text-align: left;
        padding: 10px;
        border-bottom: 1px solid #374151;
        font-size: 12px;
    }
    .custom-table td {
        padding: 15px 10px;
        border-bottom: 1px solid #374151;
    }
    
    /* 价格和积分高亮 */
    .highlight-yellow { color: #ffcc00; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

def main():
    # --- 头部 ---
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-nav">今日 &nbsp;&nbsp; 历史 &nbsp;&nbsp; 稳定度 &nbsp;&nbsp; 记账</div>', unsafe_allow_html=True)

    # --- 今日空投模块 ---
    st.markdown('<div class="section-title">🎁 今日空投 <span style="font-size:12px; background:#374151; padding:2px 8px; border-radius:10px; margin-left:10px; color:#ffcc00;">Alpha活跃人数推荐 27.3 万 ⓘ</span></div>', unsafe_allow_html=True)
    
    # 模拟截图中的数据
    today_data = {
        "项目": ["Q 📄<br><span style='font-size:10px; color:#6b7280;'>Quack AI</span>"],
        "积分": ["<span class='highlight-yellow'>240</span><br><span style='font-size:10px;'>3.6万份</span>"],
        "数量": ["<span class='highlight-yellow'>2500</span><br><span style='color:#ffcc00;'>~ $34.3</span><br><span style='font-size:10px;'>$34.4</span>"],
        "时间": ["15:00"]
    }
    df_today = pd.DataFrame(today_data)
    
    # 渲染今日空投表格
    st.write(df_today.to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)

    # --- 空投预告模块 ---
    st.markdown('<div class="section-title">📅 空投预告</div>', unsafe_allow_html=True)
    st.markdown('<div class="crypto-card" style="text-align:center; color:#6b7280;">暂无数据</div>', unsafe_allow_html=True)

    # --- 推荐工具模块 ---
    st.markdown('<div class="section-title">🛠️ 推荐工具</div>', unsafe_allow_html=True)
    
    tools = [
        {"title": "稳定度看板 (3秒更新) 📈", "desc": "识别当前时间相对稳定的项目，降低磨损风险"},
        {"title": "模拟抢空投 (图片验证) 🎮", "desc": "每天练一练，模拟真实抢空投场景，提升反应速度和成功率"},
        {"title": "网站使用帮助与提示 ▤", "desc": "关于网站功能图标与术语解释说明"}
    ]
    
    for tool in tools:
        with st.container():
            st.markdown(f"""
            <div style="margin-bottom:15px;">
                <div style="font-weight:bold; color:#ffffff;">{tool['title']}</div>
                <div style="font-size:12px; color:#6b7280;">{tool['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
