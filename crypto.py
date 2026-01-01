import streamlit as st
import pandas as pd

# 1. 基础配置
st.set_page_config(page_title="Alpha123 克隆版", page_icon="⚡", layout="wide")

# 2. 核心 CSS：强制瘦身与缓存穿透
st.markdown("""
<style>
    ::-webkit-scrollbar {display: none;}
    [data-testid="stHeader"], [data-testid="stToolbar"] {display: none !important;}
    
    /* 严格限制宽度：880px 是实现“两边留大白”的关键 */
    .main .block-container {
        padding: 4rem 1rem !important; 
        max-width: 880px !important; 
        margin: 0 auto !important;
        display: block !important;
    }
    
    .stApp { background-color: #1a1c23; color: #ffffff; font-family: 'PingFang SC', sans-serif; }
    
    /* 样式类名加后缀避免缓存 */
    .title-v4 { color: #ffcc00; font-size: 32px; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .nav-v4 { display: flex; justify-content: center; gap: 40px; color: #9ca3af; font-size: 16px; margin-bottom: 40px; }
    .active-v4 { color: #ffcc00; position: relative; font-weight: bold; }
    .active-v4::after { content: ""; position: absolute; bottom: -8px; left: 0; width: 100%; height: 3px; background: #ffcc00; }
    
    .table-v4 { width: 100%; border-collapse: collapse; }
    .table-v4 th { color: #6b7280; text-align: left; padding: 15px; border-bottom: 2px solid #2d303a; font-size: 14px; }
    .table-v4 td { padding: 22px 15px; border-bottom: 1px solid #2d303a; vertical-align: middle; }
    
    .cell-main { font-size: 17px; font-weight: 700; color: #ffffff; display: block; }
    .cell-sub { font-size: 13px; color: #8c929e; display: block; margin-top: 6px; }
    .p-yellow { color: #ffcc00 !important; }
</style>
""", unsafe_allow_html=True)

def main():
    # 顶部 - 严格还原原版文字
    st.markdown('<div class="title-v4">Alpha123空投日历</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-v4"><div class="active-v4">今日</div><div>历史</div><div>稳定度</div><div>记账</div></div>', unsafe_allow_html=True)
    
    # 今日空投板块
    st.markdown('<div style="display:flex;align-items:center;margin:30px 0 15px 0;"><span>🎁</span><span style="font-size:22px;font-weight:800;margin-left:12px;">今日空投</span><span style="background:#2d303a;color:#ffcc00;font-size:13px;padding:4px 14px;border-radius:20px;margin-left:15px;border:1px solid #3f4451;">Alpha活跃人数推荐 27.3 万 ⓘ</span></div>', unsafe_allow_html=True)
    
    # 仅保留原版的单条数据
    data = [{"项目": '<span class="cell-main">Q 📄</span><span class="cell-sub">Quack AI</span>',
             "积分": '<span class="cell-main p-yellow">240</span><span class="cell-sub">3.6万份</span>',
             "数量": '<span class="cell-main p-yellow">2500</span><span class="cell-sub"><span style="color:#ffcc00;">~ $36.7</span> / $36.7</span>',
             "时间": '<span class="cell-main">15:00</span><span class="cell-sub">已同步</span>'}]
    
    st.write(pd.DataFrame(data).to_html(escape=False, index=False, classes="table-v4"), unsafe_allow_html=True)

    # 空投预告
    st.markdown('<div style="margin-top:35px;display:flex;align-items:center;"><span>📅</span><span style="font-size:22px;font-weight:800;margin-left:12px;">空投预告</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#242731;padding:40px;border-radius:10px;text-align:center;color:#6b7280;margin-top:15px;border-top:2px solid #2d303a;">暂无数据</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
