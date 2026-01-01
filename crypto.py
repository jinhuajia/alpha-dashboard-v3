import streamlit as st
import pandas as pd

# 1. 基础配置
st.set_page_config(page_title="Alpha123 克隆版", page_icon="⚡", layout="wide")

# 2. 强制 CSS 注入（使用 !important 盾牌）
st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    
    /* 核心宽度调整：严格收缩至 880px 并在大屏下保持居中 */
    .main .block-container {
        padding: 4rem 1rem !important; 
        max-width: 880px !important; 
        margin: 0 auto !important;
        display: block !important;
    }
    
    .stApp { background-color: #1a1c23; color: #ffffff; font-family: 'PingFang SC', sans-serif; }
    
    /* 顶部导航细节 */
    .main-title { color: #ffcc00; font-size: 32px; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .nav-bar { display: flex; justify-content: center; gap: 40px; color: #9ca3af; font-size: 16px; margin-bottom: 40px; }
    .nav-item.active { color: #ffcc00; position: relative; font-weight: bold; }
    .nav-item.active::after { content: ""; position: absolute; bottom: -8px; left: 0; width: 100%; height: 3px; background: #ffcc00; }
    
    /* 表格布局打磨 */
    .table-v2 { width: 100%; border-collapse: collapse; }
    .table-v2 th { color: #6b7280; text-align: left; padding: 15px; border-bottom: 2px solid #2d303a; font-size: 14px; }
    .table-v2 td { padding: 22px 15px; border-bottom: 1px solid #2d303a; vertical-align: middle; }
    
    .cell-main { font-size: 17px; font-weight: 700; color: #ffffff; display: block; }
    .cell-sub { font-size: 13px; color: #8c929e; display: block; margin-top: 6px; }
    .p-yellow { color: #ffcc00 !important; }
    
    .tool-card-v2 { background: #242731; padding: 20px; border-radius: 10px; margin-bottom: 15px; border-left: 5px solid #ffcc00; }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<div class="main-title">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-bar"><div class="nav-item active">今日</div><div class="nav-item">历史</div><div class="nav-item">稳定度</div><div class="nav-item">记账</div></div>', unsafe_allow_html=True)
    
    # 今日空投
    st.markdown('<div style="display:flex;align-items:center;margin:30px 0 15px 0;"><span>🎁</span><span style="font-size:22px;font-weight:800;margin-left:12px;">今日空投</span><span style="background:#2d303a;color:#ffcc00;font-size:13px;padding:4px 14px;border-radius:20px;margin-left:15px;border:1px solid #3f4451;">Alpha活跃人数推荐 27.3 万 ⓘ</span></div>', unsafe_allow_html=True)
    
    raw_data = [
        ["Q 📄", "Quack AI", "240", "3.6万份", "2500", "~ $36.7", "15:00"],
        ["Berachain 🐻", "BGT Reward", "500", "不限量", "100", "~ $15.2", "16:30"],
        ["Monad 🟣", "Early Access", "1000", "5000份", "50", "~ $80.0", "18:00"],
        ["Aleo 🛡️", "Mainnet Reward", "150", "2.0万份", "300", "~ $12.5", "19:45"],
        ["Taiko 🥁", "Genesis Drop", "400", "不限量", "20", "~ $45.0", "21:00"],
        ["LayerZero 🌐", "ZRO Claim", "800", "1.2万份", "15", "~ $60.5", "22:15"],
        ["ZkSync ⚡", "Libertas", "300", "5.5万份", "10", "~ $22.1", "23:00"]
    ]
    
    rows = []
    for item in raw_data:
        rows.append({
            "项目": f'<span class="cell-main">{item[0]}</span><span class="cell-sub">{item[1]}</span>',
            "积分": f'<span class="cell-main p-yellow">{item[2]}</span><span class="cell-sub">{item[3]}</span>',
            "数量": f'<span class="cell-main p-yellow">{item[4]}</span><span class="cell-sub"><span style="color:#ffcc00;">{item[5]}</span></span>',
            "时间": f'<span class="cell-main">{item[6]}</span><span class="cell-sub">已同步</span>'
        })
    
    st.write(pd.DataFrame(rows).to_html(escape=False, index=False, classes="table-v2"), unsafe_allow_html=True)

    # 空投预告与工具（保持原版简洁）
    st.markdown('<div style="margin-top:30px;font-size:22px;font-weight:800;">📅 空投预告</div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#242731;padding:40px;border-radius:10px;text-align:center;color:#6b7280;margin-top:15px;">暂无数据</div>', unsafe_allow_html=True)

    st.markdown('<div style="margin-top:30px;font-size:22px;font-weight:800;">⚔️ 推荐工具</div>', unsafe_allow_html=True)
    tools = [("稳定度看板 (3秒更新) 📈", "识别当前时间相对稳定的项目，降低磨损风险"), ("模拟抢空投 (图片验证) 🎮", "每天练一练，模拟真实抢空投场景")]
    for title, desc in tools:
        st.markdown(f'<div class="tool-card-v2"><div style="font-weight:bold;font-size:16px;">{title}</div><div style="font-size:13px;color:#9ca3af;margin-top:8px;">{desc}</div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
