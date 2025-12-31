import streamlit as st
import requests
import pandas as pd
import feedparser
from datetime import datetime
import time
from typing import List, Dict, Optional

# 页面配置
st.set_page_config(
    page_title="加密货币情报站 | Alpha123 Clone",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 初始化session_state - 必须在最开始
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = '热门项目'

# 高质量备用数据（Fallback Data）- 包含标签信息
FALLBACK_AIRDROPS = [
    {
        "项目": "LayerZero",
        "参与方式": "跨链交互 + 社交媒体任务",
        "状态": "进行中",
        "链接": "https://layerzero.network",
        "标签": "主网"
    },
    {
        "项目": "Starknet",
        "参与方式": "链上交互 + 生态项目参与",
        "状态": "进行中",
        "链接": "https://starknet.io",
        "标签": "主网"
    },
    {
        "项目": "zkSync Era",
        "参与方式": "跨链桥接 + DeFi交互",
        "状态": "进行中",
        "链接": "https://zksync.io",
        "标签": "主网"
    },
    {
        "项目": "Linea",
        "参与方式": "测试网任务 + 主网交互",
        "状态": "进行中",
        "链接": "https://linea.build",
        "标签": "测试网"
    },
    {
        "项目": "Scroll",
        "参与方式": "测试网交互 + 生态参与",
        "状态": "进行中",
        "链接": "https://scroll.io",
        "标签": "测试网"
    },
    {
        "项目": "Base",
        "参与方式": "链上交互 + NFT铸造",
        "状态": "进行中",
        "链接": "https://base.org",
        "标签": "主网"
    },
    {
        "项目": "Blast",
        "参与方式": "跨链桥接 + 质押",
        "状态": "进行中",
        "链接": "https://blast.io",
        "标签": "主网"
    },
    {
        "项目": "Celestia",
        "参与方式": "测试网节点运行",
        "状态": "即将开始",
        "链接": "https://celestia.org",
        "标签": "测试网"
    },
    {
        "项目": "EigenLayer",
        "参与方式": "再质押 + 节点运营",
        "状态": "进行中",
        "链接": "https://eigenlayer.xyz",
        "标签": "主网"
    },
    {
        "项目": "Sui Network",
        "参与方式": "链上交互 + NFT交易",
        "状态": "进行中",
        "链接": "https://sui.io",
        "标签": "主网"
    },
    {
        "项目": "Arbitrum",
        "参与方式": "DeFi协议交互",
        "状态": "进行中",
        "链接": "https://arbitrum.io",
        "标签": "主网"
    },
    {
        "项目": "Optimism",
        "参与方式": "生态项目参与",
        "状态": "进行中",
        "链接": "https://optimism.io",
        "标签": "主网"
    },
    {
        "项目": "Polygon zkEVM",
        "参与方式": "测试网交互",
        "状态": "进行中",
        "链接": "https://polygon.technology",
        "标签": "测试网"
    },
    {
        "项目": "Manta Network",
        "参与方式": "零撸任务",
        "状态": "进行中",
        "链接": "https://manta.network",
        "标签": "零撸"
    },
    {
        "项目": "Taiko",
        "参与方式": "测试网交互",
        "状态": "进行中",
        "链接": "https://taiko.xyz",
        "标签": "测试网"
    },
    {
        "项目": "Berachain",
        "参与方式": "测试网任务",
        "状态": "进行中",
        "链接": "https://berachain.com",
        "标签": "测试网"
    },
    {
        "项目": "Sei Network",
        "参与方式": "主网交互",
        "状态": "进行中",
        "链接": "https://www.sei.io",
        "标签": "主网"
    }
]

# RSS源配置
RSS_FEEDS = {
    "Binance": "https://www.binance.com/en/support/announcement",
    "OKX": "https://www.okx.com/support/hc/en-us",
    "Coinbase": "https://blog.coinbase.com/feed",
    "Bybit": "https://announcements.bybit.com/en-US/",
}

def get_project_tag(project_name: str, participation: str) -> str:
    """根据项目名称和参与方式智能推断标签"""
    participation_lower = participation.lower() if pd.notna(participation) else ""
    project_lower = project_name.lower()
    
    # 根据参与方式判断
    if '测试网' in participation or 'testnet' in participation_lower:
        return '测试网'
    elif '零撸' in participation or 'freemint' in participation_lower:
        return '零撸'
    elif '主网' in participation or 'mainnet' in participation_lower:
        return '主网'
    elif 'defi' in participation_lower or 'deFi' in participation:
        return 'DeFi'
    elif 'nft' in participation_lower:
        return 'NFT'
    else:
        # 默认根据项目名称判断
        if 'testnet' in project_lower or 'test' in project_lower:
            return '测试网'
        else:
            return '主网'

def get_airdrops_data() -> pd.DataFrame:
    """
    获取今日热门空投数据
    优先从Alpha123 API获取，失败则使用备用数据
    """
    api_url = "https://alpha123.uk/api/airdrops/today"
    
    try:
        # 尝试从API获取数据
        response = requests.get(api_url, timeout=5, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            data = response.json()
            
            # 如果API返回的是列表格式
            if isinstance(data, list):
                df = pd.DataFrame(data)
            # 如果API返回的是字典格式，包含data字段
            elif isinstance(data, dict) and 'data' in data:
                df = pd.DataFrame(data['data'])
            else:
                df = pd.DataFrame(data)
            
            # 确保必要的列存在
            required_columns = ['项目', '参与方式', '状态', '链接']
            if all(col in df.columns for col in required_columns):
                # 如果API返回的数据没有标签列，自动生成
                if '标签' not in df.columns:
                    df['标签'] = df.apply(
                        lambda row: get_project_tag(
                            row.get('项目', ''),
                            row.get('参与方式', '')
                        ),
                        axis=1
                    )
                return df
            else:
                st.warning("API返回数据格式不完整，使用备用数据")
                return pd.DataFrame(FALLBACK_AIRDROPS)
        else:
            st.warning(f"API请求失败 (状态码: {response.status_code})，使用备用数据")
            return pd.DataFrame(FALLBACK_AIRDROPS)
            
    except requests.exceptions.RequestException as e:
        st.warning(f"网络请求失败: {str(e)}，使用备用数据")
        return pd.DataFrame(FALLBACK_AIRDROPS)
    except Exception as e:
        st.warning(f"数据解析失败: {str(e)}，使用备用数据")
        return pd.DataFrame(FALLBACK_AIRDROPS)

def get_announcements_data() -> pd.DataFrame:
    """
    聚合多个交易所的RSS公告数据
    """
    all_announcements = []
    
    # Binance公告（使用官方API）
    try:
        binance_url = "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query"
        binance_params = {
            "type": "1",
            "pageNo": "1",
            "pageSize": "20"
        }
        response = requests.get(binance_url, params=binance_params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'catalogs' in data['data']:
                for catalog in data['data']['catalogs']:
                    if 'articles' in catalog:
                        for article in catalog['articles']:
                            all_announcements.append({
                                "交易所": "Binance",
                                "标题": article.get('title', 'N/A'),
                                "发布时间": article.get('releaseDate', 'N/A'),
                                "链接": f"https://www.binance.com/en/support/announcement/{article.get('id', '')}"
                            })
    except Exception as e:
        st.warning(f"Binance数据获取失败: {str(e)}")
    
    # OKX公告（尝试RSS或API）
    try:
        okx_url = "https://www.okx.com/api/v5/announcement/public"
        response = requests.get(okx_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                for item in data['data'][:10]:  # 限制数量
                    all_announcements.append({
                        "交易所": "OKX",
                        "标题": item.get('title', 'N/A'),
                        "发布时间": item.get('publishTime', 'N/A'),
                        "链接": item.get('link', 'https://www.okx.com')
                    })
    except Exception as e:
        st.warning(f"OKX数据获取失败: {str(e)}")
    
    # 备用RSS数据
    if len(all_announcements) == 0:
        fallback_announcements = [
            {
                "交易所": "Binance",
                "标题": "Binance Launchpool新项目上线",
                "发布时间": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "链接": "https://www.binance.com"
            },
            {
                "交易所": "OKX",
                "标题": "OKX Jumpstart新项目公告",
                "发布时间": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "链接": "https://www.okx.com"
            },
            {
                "交易所": "Coinbase",
                "标题": "Coinbase新币上线公告",
                "发布时间": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "链接": "https://www.coinbase.com"
            }
        ]
        all_announcements = fallback_announcements
    
    df = pd.DataFrame(all_announcements)
    
    # 按发布时间排序（最新的在前）
    if '发布时间' in df.columns:
        try:
            df['发布时间'] = pd.to_datetime(df['发布时间'], errors='coerce')
            df = df.sort_values('发布时间', ascending=False)
            df['发布时间'] = df['发布时间'].dt.strftime('%Y-%m-%d %H:%M')
        except:
            pass
    
    return df

def get_tag_class(tag: str) -> str:
    """根据标签类型返回对应的CSS类"""
    tag_mapping = {
        '测试网': 'tag-testnet',
        '主网': 'tag-mainnet',
        '零撸': 'tag-freemint',
        'DeFi': 'tag-defi',
        'NFT': 'tag-nft'
    }
    return tag_mapping.get(tag, 'tag-testnet')

def format_project_name(project_name: str, status: str, tag: str = None) -> str:
    """格式化项目名称，添加圆点图标和标签"""
    status_lower = status.lower()
    if '进行中' in status or 'active' in status_lower or 'ongoing' in status_lower:
        dot_class = "status-dot active"
    elif '即将' in status or 'upcoming' in status_lower or 'soon' in status_lower:
        dot_class = "status-dot upcoming"
    elif '结束' in status or 'ended' in status_lower or 'closed' in status_lower:
        dot_class = "status-dot ended"
    else:
        dot_class = "status-dot ended"
    
    tag_html = ""
    if tag and pd.notna(tag):
        tag_class = get_tag_class(tag)
        tag_html = f'<span class="project-tag {tag_class}">{tag}</span>'
    
    return f'<div class="project-name"><span class="{dot_class}"></span><span>{project_name}</span>{tag_html}</div>'

def format_status(status: str) -> str:
    """格式化状态显示"""
    status_lower = status.lower()
    if '进行中' in status or 'active' in status_lower or 'ongoing' in status_lower:
        return f'<span class="status-active">进行中</span>'
    elif '即将' in status or 'upcoming' in status_lower or 'soon' in status_lower:
        return f'<span class="status-upcoming">即将开始</span>'
    elif '结束' in status or 'ended' in status_lower or 'closed' in status_lower:
        return f'<span class="status-ended">已结束</span>'
    else:
        return status

def render_custom_table(df: pd.DataFrame) -> str:
    """渲染自定义表格HTML，去除索引列，添加悬停效果"""
    html = '<table class="custom-table">'
    
    # 表头
    html += '<thead><tr>'
    for col in df.columns:
        if col != '标签':  # 标签列不显示在表头，但显示在内容中
            html += f'<th>{col}</th>'
    html += '</tr></thead>'
    
    # 表体
    html += '<tbody>'
    for idx, row in df.iterrows():
        html += '<tr>'
        for col in df.columns:
            if col != '标签':  # 标签已整合到项目名称中
                html += f'<td>{row[col]}</td>'
        html += '</tr>'
    html += '</tbody>'
    
    html += '</table>'
    return html

def main():
    # 整合所有CSS到main()函数顶部
    st.markdown("""
    <style>
        /* 隐藏Streamlit默认元素 */
        #MainMenu {visibility: hidden !important; display: none !important;}
        footer {visibility: hidden !important; display: none !important;}
        header {visibility: hidden !important; display: none !important;}
        .stDeployButton {display: none !important;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* 全屏布局 */
        .stApp {
            background-color: #F9FAFB;
        }
        
        .main .block-container {
            padding: 24px;
            max-width: 100%;
        }
        
        /* 精确字体 */
        * {
            font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, sans-serif !important;
            -webkit-font-smoothing: antialiased;
        }
        
        /* 自定义Tab样式 - 背景透明、文字深灰、选中项带蓝色下划线 */
        .stTabs [data-baseweb="tab-list"] {
            background-color: transparent !important;
            border-bottom: 1px solid #E5E7EB;
            gap: 0;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: transparent !important;
            color: #6B7280 !important;
            font-weight: 500;
            padding: 12px 20px;
        }
        
        .stTabs [aria-selected="true"] {
            color: #374151 !important;
            font-weight: 600;
            border-bottom: 2px solid #0066cc;
        }
        
        /* 标题样式 */
        h1 {
            font-size: 18px;
            font-weight: 700;
            color: #374151;
            margin-bottom: 16px;
        }
        
        /* 搜索框样式 */
        .stTextInput > div > div > input {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 6px;
            padding: 10px 14px;
            font-size: 13px;
        }
        
        /* 金融级表格 */
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
        }
        
        .custom-table thead th {
            background-color: #F3F4F6 !important;
            font-weight: 700 !important;
            color: #6B7280 !important;
            padding: 10px 16px;
            border-bottom: 1px solid #E5E7EB;
            font-size: 11px;
            text-transform: uppercase;
        }
        
        .custom-table tbody td {
            padding: 10px 16px;
            border-bottom: 1px solid #E5E7EB;
            color: #1F2937;
            line-height: 1.4;
        }
        
        .custom-table tbody tr:nth-child(odd) {
            background-color: #FFFFFF;
        }
        
        .custom-table tbody tr:nth-child(even) {
            background-color: #FAFAFA;
        }
        
        .custom-table tbody tr:hover {
            background-color: #F3F4F6 !important;
        }
        
        /* 项目名称带圆点 */
        .project-name {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            flex-shrink: 0;
        }
        
        .status-dot.active {
            background-color: #10B981;
            animation: pulse 2s infinite;
        }
        
        .status-dot.upcoming {
            background-color: #F59E0B;
        }
        
        .status-dot.ended {
            background-color: #6B7280;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.7; transform: scale(1.1); }
        }
        
        /* 状态标签 */
        .status-active {
            background-color: #D1FAE5;
            color: #065F46;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
            display: inline-block;
        }
        
        .status-upcoming {
            background-color: #FEF3C7;
            color: #92400E;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
            display: inline-block;
        }
        
        .status-ended {
            background-color: #F3F4F6;
            color: #4B5563;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
            display: inline-block;
        }
        
        /* 详情链接 */
        .detail-link {
            color: #0066cc;
            text-decoration: none;
            font-size: 13px;
            font-weight: 500;
        }
        
        .detail-link:hover {
            color: #0052a3;
        }
        
        /* Tag标签 */
        .project-tag {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 11px;
            font-weight: 500;
            margin-left: 6px;
        }
        
        .tag-testnet { background-color: #DBEAFE; color: #1E40AF; }
        .tag-mainnet { background-color: #D1FAE5; color: #065F46; }
        .tag-freemint { background-color: #FEF3C7; color: #92400E; }
        .tag-defi { background-color: #E9D5FF; color: #6B21A8; }
        .tag-nft { background-color: #FCE7F3; color: #9F1239; }
    </style>
    """, unsafe_allow_html=True)
    
    # 使用st.tabs确保功能稳定
    tab1, tab2, tab3 = st.tabs(["🔥 热门项目", "📅 空投日历", "📢 实时快讯"])
    
    # Tab 1: 热门项目
    with tab1:
        st.title("今日热门空投")
        
        # 显示加载状态
        with st.spinner("正在获取最新空投数据..."):
            airdrops_df = get_airdrops_data()
        
        if not airdrops_df.empty:
            # 搜索框
            search_query = st.text_input(
                "",
                placeholder="搜索项目...",
                key="airdrop_search",
                label_visibility="collapsed"
            )
            
            # 应用搜索过滤
            if search_query:
                mask = airdrops_df['项目'].str.contains(search_query, case=False, na=False)
                filtered_df = airdrops_df[mask].copy()
            else:
                filtered_df = airdrops_df.copy()
            
            if not filtered_df.empty:
                # 确保有标签列，如果没有则智能生成
                if '标签' not in filtered_df.columns:
                    filtered_df['标签'] = filtered_df.apply(
                        lambda row: get_project_tag(
                            row.get('项目', ''),
                            row.get('参与方式', '')
                        ),
                        axis=1
                    )
                
                # 格式化项目名称（添加圆点图标和标签）
                if '项目' in filtered_df.columns and '状态' in filtered_df.columns:
                    filtered_df['项目'] = filtered_df.apply(
                        lambda row: format_project_name(
                            row['项目'], 
                            row['状态'],
                            row.get('标签', None)
                        ), 
                        axis=1
                    )
                
                # 格式化状态列
                if '状态' in filtered_df.columns:
                    filtered_df['状态'] = filtered_df['状态'].apply(format_status)
                
                # 格式化链接列为详情按钮
                if '链接' in filtered_df.columns:
                    filtered_df['链接'] = filtered_df['链接'].apply(
                        lambda x: f'<a href="{x}" target="_blank" class="detail-link clickable">🔗 详情</a>' if pd.notna(x) else ''
                    )
                
                # 显示表格（无卡片包装，直接显示）
                html_table = render_custom_table(filtered_df)
                st.markdown(html_table, unsafe_allow_html=True)
                
                # 显示数据统计
                st.markdown(
                    f'<div style="color: #6B7280; font-size: 13px; margin-top: 16px;">'
                    f'共找到 <strong>{len(filtered_df)}</strong> 个热门空投项目'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                st.info("未找到匹配的项目")
        else:
            st.error("暂无空投数据")
    
    # Tab 2: 空投日历
    with tab2:
        st.title("空投日历")
        st.info("空投日历功能开发中，敬请期待...")
    
    # Tab 3: 实时快讯
    with tab3:
        st.title("最新公告")
        
        # 显示加载状态
        with st.spinner("正在聚合交易所公告..."):
            announcements_df = get_announcements_data()
        
        if not announcements_df.empty:
            # 搜索框
            search_query = st.text_input(
                "",
                placeholder="搜索公告...",
                key="announcement_search",
                label_visibility="collapsed"
            )
            
            # 应用搜索过滤
            if search_query:
                mask = announcements_df['标题'].str.contains(search_query, case=False, na=False)
                filtered_df = announcements_df[mask].copy()
            else:
                filtered_df = announcements_df.copy()
            
            if not filtered_df.empty:
                # 格式化链接列为详情按钮
                if '链接' in filtered_df.columns:
                    filtered_df['链接'] = filtered_df['链接'].apply(
                        lambda x: f'<a href="{x}" target="_blank" class="detail-link clickable">🔗 详情</a>' if pd.notna(x) else ''
                    )
                
                # 显示表格（无卡片包装，直接显示）
                html_table = render_custom_table(filtered_df)
                st.markdown(html_table, unsafe_allow_html=True)
                
                # 显示数据统计
                st.markdown(
                    f'<div style="color: #6B7280; font-size: 13px; margin-top: 16px;">'
                    f'共找到 <strong>{len(filtered_df)}</strong> 条最新公告'
                    f'</div>',
                    unsafe_allow_html=True
                )
            else:
                st.info("未找到匹配的公告")
        else:
            st.error("暂无公告数据")

if __name__ == "__main__":
    main()

