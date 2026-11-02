# 数据字典与指标定义 (Data Dictionary & Metrics)

本项目所用所有定量指标、计算公式及其统计口径定义如下：

---

## 1. 核心经济学与财务指标

| 字段名称 (Key) | 中文名称 | 数据类型 | 单位 | 定义与统计口径 | 权威数据源 |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `token_price_index` | 基础模型推理价格指数 | Float | 基数=100 (2020-Q1) | 跟踪每百万 Token（输入+输出加权）标准化基准报价的通缩轨迹。 | Epoch AI *The Plunging Price of Thought* |
| `frontier_training_cost_m` | 前沿大模型训练 Capex | Float | 百万美元 ($M) | 单个前沿基础大模型单次完整预训练所需的硬件折旧、电力与工程开销。 | Stanford HAI / SemiAnalysis |
| `hyperscaler_capex_b` | 四大云巨头资本开支总和 | Float | 十亿美元 ($B) | 微软、Alphabet、亚马逊、Meta 年度数据中心、AI 服务器及电网基建 Capex 累计值。 | SEC 10-K Filings & Apollo Sløk Model |
| `ai_software_arr_b` | 企业级增量 AI 软件 ARR | Float | 十亿美元 ($B) | 全球企业级软件中由生成式 AI / Agent 能力直接创造的新增年度经常性收入。 | Gartner / Apollo Research |
| `gap_b` | 自由现金流缺口 | Float | 十亿美元 ($B) | `hyperscaler_capex_b` 与 `ai_software_arr_b` 之间的剪刀差差额。 | Apollo Global Research |
| `inventor_share` | 发明者价值捕获率 | Float | 百分比 (%) | 基础通用技术发明人在整个产业生态创造的经济净盈余中所留存的价值份额。 | 经济史计量模型 / Nordhaus 2004 |
| `consumer_share` | 终端应用与消费者盈余 | Float | 百分比 (%) | 由通用技术引发的下游应用、产业链降本及全社会消费者享受的经济盈余份额。 | 经济史计量模型 / Nordhaus 2004 |

---

## 2. 劳动力与产业分层指标

| 字段名称 (Key) | 中文名称 | 数据类型 | 单位 | 定义与统计口径 | 权威数据源 |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `total_us_workforce_m` | 全美非农就业总人口 | Float | 百万人 (M) | 美国劳工统计局统计的全部非农就业总人数（约 1.68 亿人）。 | U.S. BLS (2025) |
| `total_whitecollar_m` | 全美广义知识工作者 | Float | 百万人 (M) | 管理、专业、金融、法律、技术等广义办公室知识工作者总规模。 | U.S. BLS CPS |
| `software_developers_m` | 全美软件开发与架构师 | Float | 百万人 (M) | 计算机程序设计、软件开发、系统分析师及架构师从业人口。 | U.S. BLS OEWS 15-1252 |
| `heavy_ai_users_actual_m` | 深度闭环高频 AI 白领实际规模 | Float | 百万人 (M) | 每日高频调用 AI 自动化完成核心工作流且由雇主规模化付费的重度白领人数。 | Census Bureau BTOS WP 26-25 |
| `viral_claim_ai_users_m` | 网络自媒体声称规模 | Float | 百万人 (M) | 社交媒体图文声称的“全美深度使用 AI 改变流程的白领人数”。 | 小红书原帖 (被核实为夸大) |
| `btos_enterprise_adoption_rate_pct` | 全美企业级 AI 部署率 | Float | 百分比 (%) | 在正式生产流程中使用生成式 AI 的美国企业比例（仅 5.4%）。 | U.S. Census Bureau BTOS |
| `top_10pct_power_user_token_ratio` | 前 10% 极客企业消耗倍数 | Float | 倍数 (x) | OpenAI 企业级数据中前 10% 顶尖极客开发者企业消耗 Token 相对中位数企业的倍数。 | OpenAI Enterprise Disclosures |

---

## 3. 离岸 IT 产业健康度指标

| 字段名称 (Key) | 中文名称 | 数据类型 | 单位 | 定义与统计口径 | 权威数据源 |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `tcs_operating_margin_pct` | 塔塔咨询 (TCS) 营业利润率 | Float | 百分比 (%) | 财年营业利润 (Operating Profit) 占营业收入比例。 | TCS Audited Financials |
| `infosys_margin_pct` | 印孚瑟斯 (Infosys) 营业利润率 | Float | 百分比 (%) | 财年营业利润占营业收入比例。 | Infosys Form 20-F |
| `industry_net_addition_k` | 印度 IT 外包净新增员工数 | Integer | 千人 (k) | 印度主要外包企业当期入职人数减去离职人数的净增量（FY25-26 转负）。 | Nasscom Quarterly Reports |
