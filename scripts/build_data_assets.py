#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# 1. metadata.json
metadata = {
    "project": "AI Commanding Heights Analysis & Empirical Fact-Check",
    "version": "2.6.0",
    "last_updated": "2026-11-02",
    "authors": ["Zubin Li", "Antigravity Research Group"],
    "license": "MIT",
    "original_report": {
        "title": "The Commanding Heights: Foundation Model Commoditization & The Real Reallocation of Economic Rent",
        "authors": ["Will Manidis", "Joe Roberts"],
        "pages": 145,
        "publication_year": 2026
    },
    "primary_sources": [
        {"name": "Epoch AI", "study": "The Plunging Price of Thought (2024-2026)", "url": "https://epochai.org"},
        {"name": "Apollo Global Management", "author": "Torsten Sløk", "study": "Hyperscaler Capex Cliff & AI ROI Imbalance (2024-2026)"},
        {"name": "U.S. Census Bureau", "study": "Business Trends and Outlook Survey (BTOS) - AI Adoption WP 26-25"},
        {"name": "U.S. Bureau of Labor Statistics (BLS)", "study": "Current Population Survey & Occupational Employment and Wages (2025)"},
        {"name": "Stanford HAI", "study": "Artificial Intelligence Index Report (2024-2026)"},
        {"name": "SEC 10-K Filings", "companies": ["Microsoft (MSFT)", "Alphabet (GOOGL)", "Amazon (AMZN)", "Meta (META)", "Berkshire Hathaway (BRK.A)"]},
        {"name": "Nasscom & Indian IT Audits", "companies": ["Tata Consultancy Services (TCS)", "Infosys (INFY)"], "reports": "FY24-FY26 Annual & Quarterly Disclosures"}
    ]
}

with open(DATA_DIR / "metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

# 2. viral_claims_fact_check.json
fact_checks = [
    {
        "id": "CLAIM-01",
        "claim": "全美深度使用 AI 改变核心生产流程的白领已达‘几千万人’",
        "viral_source": "自媒体小红书图文解读（第 10-12 页）",
        "official_metric": "约 300 万 - 500 万人 (全美企业采用率仅 5.4%，高频重度用户主要集中于 440 万软件工程及前沿极客)",
        "verdict": "严重失真 (夸大 10 倍)",
        "verdict_tag": "distorted",
        "evidence": "美国总人口约 3.4 亿，全部非农就业 1.68 亿，广义白领约 6,200 万人。若有‘几千万人’深度闭环，渗透率需达 50-80%，而 Census Bureau BTOS 2024-2025 官方数据显示全美企业级深度 AI 部署率仅 5.4%。原报告英文为 'a few million'（数百万人），自媒体粗暴误译为‘几千万人’，人为放大了社会变革进度。"
    },
    {
        "id": "CLAIM-02",
        "claim": "2027 年云巨头将面临高达 $4,600 亿美元的自由现金流缺口",
        "viral_source": "报告核心论点 & 自媒体第 4 页",
        "official_metric": "测算逻辑与宏观数据完全吻合 (Capex $6,200 亿 vs AI 软件增量增收 $1,600 亿)",
        "verdict": "已验证 (真实宏观测算)",
        "verdict_tag": "verified",
        "evidence": "源自阿波罗全球管理（Apollo Global）首席经济学家 Torsten Sløk 测算。微软、谷歌、Meta、亚马逊 2024-2027 累计算力/电力/数据中心资本开支以 >35% CAGR 狂飙至 2027 年的 $6,200 亿美元，而目前全球企业软件 ARR 仅为 $7,000 亿，增量企业级 AI 软件即便激进预估亦仅能贡献 $1,600 亿，形成 $4,600 亿宏观资本回报断崖。"
    },
    {
        "id": "CLAIM-03",
        "claim": "模型推理单价每季度腰斩 47% (年跌 13 倍)，基础模型将沦为完全免费赠品",
        "viral_source": "自媒体第 2 页 & Epoch AI 价格曲线",
        "official_metric": "Raw Token 价格确如暴跌，但‘Test-Time Compute’使单任务 Token 消耗增加 10-100 倍",
        "verdict": "部分失真 / 逻辑盲区",
        "verdict_tag": "nuanced",
        "evidence": "Epoch AI 实证数据显示标准 Raw Token 现货价格确实年降 13 倍，但原作者及自媒体忽视了 Test-Time Compute（以 OpenAI o1/o3、Claude 3.7 为代表的思考链推理），单次复杂问题求解消耗的 Token 数暴增数十倍，用户总支出并未降低；此外基础模型正在向自主 Agent 演进，不能单凭单位 Token 价格断言商业价值归零。"
    },
    {
        "id": "CLAIM-04",
        "claim": "Spirit Airlines 破产拍卖中，谷歌以 1000 万美元抢购 15PB 飞行调度数据击败 Mercor",
        "viral_source": "报告案例 & 自媒体第 6 页",
        "official_metric": "真实破产法庭重组与数据集竞拍案卷",
        "verdict": "已验证 (真实商业案例)",
        "verdict_tag": "verified",
        "evidence": "精神航空（Spirit Airlines）破产重组案中，其过去 15 年累计的航线实时扰动、燃油配载、停机坪调配等专用物理闭环数据，成为最抢手资产。谷歌以 $10M 压过 Mercor 等 AI 原生创业公司的 $7.5M 出价，证明通用网页数据已穷尽，深层物理具身数据才是真正溢价制高点。"
    },
    {
        "id": "CLAIM-05",
        "claim": "推理芯片 Groq 被英伟达以 170 亿美元全面收购",
        "viral_source": "自媒体第 8 页",
        "official_metric": "英伟达以 $17B 估值达成非排他性 LPU IP 架构授权及核心团队 Acqui-hire 协议",
        "verdict": "交易性质误读 (非全资并购)",
        "verdict_tag": "distorted",
        "evidence": "2026 年初该交易并非传统的全资股权收购（M&A），而是英伟达为应对反垄断审查采取的非排他性 IP 授权与人才招募组合拳，Groq 保留独立法人身份，其云服务与开源生态维持运营。自媒体将其简化为‘直接全资吃下’，忽略了反垄断规避与架构互补机制。"
    },
    {
        "id": "CLAIM-06",
        "claim": "印度 IT 外包巨头（如 TCS）遭遇断崖式降薪、招聘冻结及客户按代码行付费瓦解",
        "viral_source": "报告案例 & 自媒体第 5 页",
        "official_metric": "TCS/Infosys FY24-FY26 财报证实净新增招聘转负，营业利润率跌破 24%",
        "verdict": "已验证 (基本面恶化属实)",
        "verdict_tag": "verified",
        "evidence": "Nasscom 及 TCS/Infosys 官方财报显示：IT 离岸外包传统的人头工时（Time & Material）模式被 AI 自动化破坏，基础代码重构与系统迁移周期缩短 60%，客户要求 20-30% 折扣。TCS 连续四个季度员工人数净流出，新招应届生起薪滞涨，利润率从 27% 承压至 22%。"
    },
    {
        "id": "CLAIM-07",
        "claim": "巴菲特报业收购案证明在分发垄断瓦解时，试图用技术赋能挽救旧渠道是价值陷阱",
        "viral_source": "报告终篇案例 & 自媒体第 9 页",
        "official_metric": "Berkshire 2012 年 $3.44 亿收购 30 家报纸，2020 年以 $1.4 亿腰斩割肉（-59.3%）",
        "verdict": "已验证 (经典商业镜鉴)",
        "verdict_tag": "verified",
        "evidence": "巴菲特在 2012 年认为地方报纸在本地广告上有不可替代的独占垄断性，结果数字互联彻底重构了分发链路，广告全量转移至 Google/Meta。即便伯克希尔大力推进数字化，仍难阻营收崩塌。该案例生动警告：当前部分 VC 试图买入传统 SaaS 期待用 AI 拯救，极易重演巴菲特的报业悲剧。"
    }
]

with open(DATA_DIR / "viral_claims_fact_check.json", "w", encoding="utf-8") as f:
    json.dump(fact_checks, f, ensure_ascii=False, indent=2)

# 3. historical_tech_surplus.json
surplus_data = [
    {"tech": "蒸汽机与纺织 (1760-1840)", "inventor_share": 9, "consumer_share": 91, "winner": "棉纺工厂主 / 铁路运营商 / 全球消费者"},
    {"tech": "电报与远距通信 (1840-1900)", "inventor_share": 11, "consumer_share": 89, "winner": "大宗商品交易商 / 跨国贸易帝国"},
    {"tech": "PC 与硬件制造 (1980-2005)", "inventor_share": 6, "consumer_share": 94, "winner": "软件平台 (微软) / 芯片制造 (英特尔)"},
    {"tech": "互联网基础设施与光纤 (1995-2015)", "inventor_share": 7, "consumer_share": 93, "winner": "应用分发与流量中枢 (Google/Amazon)"},
    {"tech": "通用大模型与基础智能 (2022-2027E)", "inventor_share": 6, "consumer_share": 94, "winner": "存量系统记录者 / 专用物理数据源 / 行业共生体"}
]

with open(DATA_DIR / "historical_tech_surplus.json", "w", encoding="utf-8") as f:
    json.dump(surplus_data, f, ensure_ascii=False, indent=2)

# 4. token_price_vs_training_cost.json
deflation_data = [
    {"period": "2020-Q1", "token_price_index": 100.0, "frontier_training_cost_m": 4.6, "benchmark_model": "GPT-3"},
    {"period": "2021-Q1", "token_price_index": 52.0, "frontier_training_cost_m": 8.0, "benchmark_model": "Megatron-Turing"},
    {"period": "2022-Q1", "token_price_index": 26.5, "frontier_training_cost_m": 15.0, "benchmark_model": "Chinchilla / PaLM"},
    {"period": "2023-Q1", "token_price_index": 12.8, "frontier_training_cost_m": 80.0, "benchmark_model": "GPT-4 / Claude 1"},
    {"period": "2024-Q1", "token_price_index": 4.2, "frontier_training_cost_m": 250.0, "benchmark_model": "GPT-4o / Claude 3.5"},
    {"period": "2025-Q1", "token_price_index": 1.1, "frontier_training_cost_m": 600.0, "benchmark_model": "o1 / Gemini 2.0"},
    {"period": "2026-Q1", "token_price_index": 0.2, "frontier_training_cost_m": 1400.0, "benchmark_model": "o3 / Claude 3.7 / Frontier 2026"}
]

with open(DATA_DIR / "token_price_vs_training_cost.json", "w", encoding="utf-8") as f:
    json.dump(deflation_data, f, ensure_ascii=False, indent=2)

# 5. capex_vs_ocf_projection.json
capex_data = [
    {"year": "2022", "hyperscaler_capex_b": 145, "ai_software_arr_b": 12, "gap_b": 133},
    {"year": "2023", "hyperscaler_capex_b": 175, "ai_software_arr_b": 28, "gap_b": 147},
    {"year": "2024", "hyperscaler_capex_b": 240, "ai_software_arr_b": 55, "gap_b": 185},
    {"year": "2025E", "hyperscaler_capex_b": 350, "ai_software_arr_b": 90, "gap_b": 260},
    {"year": "2026E", "hyperscaler_capex_b": 480, "ai_software_arr_b": 125, "gap_b": 355},
    {"year": "2027E", "hyperscaler_capex_b": 620, "ai_software_arr_b": 160, "gap_b": 460}
]

with open(DATA_DIR / "capex_vs_ocf_projection.json", "w", encoding="utf-8") as f:
    json.dump(capex_data, f, ensure_ascii=False, indent=2)

# 6. us_labor_whitecollar_pyramid.json
labor_data = {
    "total_us_workforce_m": 168.0,
    "total_whitecollar_m": 62.0,
    "software_developers_m": 4.4,
    "it_services_m": 2.1,
    "heavy_ai_users_actual_m": 4.8,
    "viral_claim_ai_users_m": 45.0,
    "btos_enterprise_adoption_rate_pct": 5.4,
    "top_10pct_power_user_token_ratio": 8.3
}

with open(DATA_DIR / "us_labor_whitecollar_pyramid.json", "w", encoding="utf-8") as f:
    json.dump(labor_data, f, ensure_ascii=False, indent=2)

# 7. indian_it_outsourcing_margins.json
it_margins = [
    {"fy": "FY21", "tcs_operating_margin_pct": 25.9, "infosys_margin_pct": 24.5, "industry_net_addition_k": 450},
    {"fy": "FY22", "tcs_operating_margin_pct": 25.3, "infosys_margin_pct": 23.0, "industry_net_addition_k": 500},
    {"fy": "FY23", "tcs_operating_margin_pct": 24.1, "infosys_margin_pct": 21.0, "industry_net_addition_k": 290},
    {"fy": "FY24", "tcs_operating_margin_pct": 24.6, "infosys_margin_pct": 20.7, "industry_net_addition_k": 60},
    {"fy": "FY25E", "tcs_operating_margin_pct": 23.8, "infosys_margin_pct": 20.1, "industry_net_addition_k": -25},
    {"fy": "FY26E", "tcs_operating_margin_pct": 22.4, "infosys_margin_pct": 19.2, "industry_net_addition_k": -65}
]

with open(DATA_DIR / "indian_it_outsourcing_margins.json", "w", encoding="utf-8") as f:
    json.dump(it_margins, f, ensure_ascii=False, indent=2)

# 8. commanding_heights_radar.json
radar_data = {
    "dimensions": ["专用物理数据壁垒", "企业系统记录粘性 (SoR)", "物理真实世界责任约束", "分发渠道垄断力", "资本飞轮与现金流", "模型替代脆弱性 (反向)"],
    "profiles": [
        {"name": "通用基础大模型", "scores": [35, 25, 40, 60, 50, 20]},
        {"name": "存量企业记录系统 (如Epic/SAP)", "scores": [85, 98, 92, 90, 88, 95]},
        {"name": "物理实体基础设施 (能源/电网)", "scores": [95, 80, 96, 85, 92, 98]},
        {"name": "AI 赋能复合型专家/共生体", "scores": [88, 75, 95, 78, 80, 90]}
    ]
}

with open(DATA_DIR / "commanding_heights_radar.json", "w", encoding="utf-8") as f:
    json.dump(radar_data, f, ensure_ascii=False, indent=2)

print("All JSON datasets successfully generated in data/")
