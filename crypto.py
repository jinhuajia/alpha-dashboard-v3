import streamlit as st
import pandas as pd

# 1. 基础页面设置
st.set_page_config(page_title="Alpha123 克隆版", page_icon="⚡", layout="wide")

# 2. 暴力 CSS：不再调整原生容器，而是直接重写整个页面的展示逻辑
st.markdown("""
<style>
    /* 彻底隐藏原生组件和多余空间 */
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    
    /* 【核心修正】彻底接管原生容器的布局 */
    /* 我们把原生容器设为透明，并强制让它不再限制宽度 */
    .main .block-container {
        max-width: 100% !important;
        padding: 0 !important;
    }

    /* 创建一个绝对居中、宽度锁死在 850px 的内层容器 */
    .custom-container {
        max-width: 850px !important;
        margin: 0 auto !important;
        padding: 4rem 1rem !important;
        background-color: #1a1c23;
        min-height: 100vh;
    }

    /* 全局背景色强行覆盖 */
    .stApp { background-color: #1a1c23 !important; }

    /* 样式细节还原 */
    .main-title { color: #ffcc00; font-size: 32px; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .nav-bar { display: flex; justify-content: center; gap: 40px; color: #9ca3af; font-size: 16px; margin-bottom: 40px; }
    .nav-item.active { color: #ffcc00; position: relative; font-weight: bold; }
    .nav-item.active::after { content: ""; position: absolute; bottom: -8px; left: 0; width: 100%; height: 3px; background: #ffcc00; }
    
    .section-header { display: flex; align-items: center; margin: 30px 0 15px 0; }
    .section-text { font-size: 22px; font-weight: 800; color: #ffffff; margin-left: 12px; }
    .info-badge { background: #2d303a; color: #ffcc00; font-size: 13px; padding: 4px 14px; border-radius: 20px; margin-left: 15px; border: 1px solid #3f4451; }
    
    /* 表格样式：完全透传背景 */
    .custom-table { width: 100%; border-collapse: collapse; background-color: transparent !important; }
    .custom-table td { padding: 22px 15px; border-bottom: 1px solid #2d303a; vertical-align: middle; }
    .cell-main { font-size: 17px; font-weight: 700; color: #ffffff; display: block; }
    .cell-sub { font-size: 13px; color: #8c929e; display: block; margin-top: 6px; }
    .p-yellow { color: #ffcc00 !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

def main():
    # 使用 custom-container 强行包裹所有内容，实现物理留白
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    
    # 顶部
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar"><div class="nav-item active">今日</div><div>历史</div><div>稳定度</div><div>记账</div></div>', unsafe_allow_html=True)
    
    # 今日空投
    st.markdown('<div class="section-header"><span>🎁</span><span class="section-text">今日空投</span><span class="info-badge">Alpha活跃人数推荐 27.3 万 ⓘ</span></div>', unsafe_allow_html=True)
    
    # 纯净版数据展示
    data = [{"项目": '<span class="cell-main">Q 📄</span><span class="cell-sub">Quack AI</span>',
             "积分": '<span class="cell-main p-yellow">240</span><span class="cell-sub">3.6万份</span>',
             "数量": '<span class="cell-main p-yellow">2500</span><span class="cell-sub"><span style="color:#ffcc00;">~ $36.7</span> / $36.7</span>',
             "时间": '<span class="cell-main">15:00</span><span class="cell-sub">已同步</span>'}]
    st.write(pd.DataFrame(data).to_html(escape=False, index=False, classes="custom-table"), unsafe_allow_html=True)

    # 空投预告
    st.markdown('<div class="section-header"><span>📅</span><span class="section-text">空投预告</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#242731;padding:40px;border-radius:10px;text-align:center;color:#6b7280;margin-top:15px;border-top:2px solid #2d303a;">暂无数据</div>', unsafe_allow_html=True)

    # 推荐工具
    st.markdown('<div class="section-header"><span>⚔️</span><span class="section-text">推荐工具</span></div>', unsafe_allow_html=True)
    tools = [
        ("稳定度看板 (3秒更新) 📈", "识别当前时间相对稳定的项目，降低磨损风险"),
        ("模拟抢空投 (图片验证) 🎮", "每天练一练，模拟真实抢空投场景"),
        ("网站使用帮助与提示 ▤", "关于网站功能图标与术语解释说明")
    ]
    for title, desc in tools:
        st.markdown(f'''
        <div style="background:#242731; padding:20px; border-radius:10px; margin-bottom:15px; border-left:5px solid #ffcc00;">
            <div style="font-weight:bold; font-size:16px;">{title}</div>
            <div style="font-size:13px; color:#9ca3af; margin-top:8px;">{desc}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True) # 闭合自定义容器

if __name__ == "__main__":
    main()
