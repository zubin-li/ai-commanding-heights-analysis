[中文](README.md) · [English](README_EN.md)

# AI 制高点：盈利能力与价值捕获分析

[![在线研究演示](https://img.shields.io/badge/GitHub_Pages-在线访问-0969da?logo=github)](https://zubin-li.github.io/ai-commanding-heights-analysis/)
[![研究方法](https://img.shields.io/badge/研究-方法与来源-005ea8)](docs/methodology.md)
[![License: MIT](https://img.shields.io/badge/代码许可-MIT-yellow.svg)](LICENSE)

一个中英文交互式研究演示，用于检验“大模型商品化后，经济租将转移到产业瓶颈”这一命题。项目把原始报告、社交媒体二次传播、外部数据、情景假设和作者判断分开呈现，并提供可调参数的敏感性模拟器。

**在线访问：** <https://zubin-li.github.io/ai-commanding-heights-analysis/>

**完整研究文本：** [`docs/strategic_report.md`](docs/strategic_report.md)

## 研究问题

- 基础模型的单位推理价格下降，是否必然意味着模型层无法捕获价值？
- AI 基础设施资本开支与可归因收入之间可能存在多大的回报缺口？
- 数据、能源、分发、工作流和法律责任中，哪些瓶颈更可能保留议价权？
- 社交媒体对原报告的哪些表述可以复核，哪些属于推断或误读？
- 当关键假设改变时，情景结果对推理价格、资本开支和企业采用率有多敏感？

网页采用连续纵向研究演示形式，默认英文和亮色主题；支持中文、暗色主题、15 个章节、交互图表、来源图集、核查台账以及三参数敏感性模拟器。

## 证据阅读规则

| 层级 | 含义 | 应如何使用 |
| --- | --- | --- |
| 来源事实 | 可追溯到已列明的公开来源或公司披露 | 检查原始链接、统计口径和发布日期 |
| 外部估计 | 第三方研究机构的估算或模型结果 | 保留其假设与不确定性 |
| 项目情景 | 仓库为敏感性分析设置的参数 | 用于比较方向，不是预测 |
| 作者判断 | 对价值捕获和职业/产业影响的解释 | 作为待检验观点，不是已证事实 |

> [!CAUTION]
> 本项目不是投资建议。未来年份的数值、资本缺口、行业排名和模拟输出均可能依赖假设；“已核查”只应表示列明证据支持特定表述，不代表整份论证已被证明。阅读结论前请先查看 [`docs/citations.md`](docs/citations.md)、[`docs/data_dictionary.md`](docs/data_dictionary.md) 和 [`docs/methodology.md`](docs/methodology.md)。

## 本地运行

需要 Python 3，无需前端构建步骤。

```bash
git clone https://github.com/zubin-li/ai-commanding-heights-analysis.git
cd ai-commanding-heights-analysis
python3 server.py
```

打开 <http://127.0.0.1:8080>。也可以运行 `npm run serve` 或 `./run.sh`。建议通过 HTTP 服务访问，而不是直接打开 `index.html`。

## 验证

```bash
npm test
```

该命令检查项目文件、结构化数据、国际化键和关键页面契约。它不是视觉回归或事实真伪的自动证明；真实浏览器验收还应覆盖桌面/移动视口、中英文、主题切换、图表、弹窗、键盘操作和模拟器状态变化。

如需重建结构化数据：

```bash
npm run data:build
```

## 目录导航

| 路径 | 用途 |
| --- | --- |
| `index.html`, `i18n.js` | 连续研究演示、交互和双语文案 |
| `data/` | 图表、核查台账与情景输入 |
| `docs/strategic_report.md` | 长篇研究报告 |
| `docs/methodology.md` | 研究方法、证据分层与限制 |
| `docs/citations.md` | 来源和引用信息 |
| `docs/data_dictionary.md` | 指标、单位和计算口径 |
| `images/` | 被分析的 19 页原始传播材料 |
| `tests/` | 项目契约与回归检查 |
| `scripts/` | 数据与页面生成脚本 |

## 已知边界

- 本项目基于一个特定报告及其传播材料，不是 AI 产业的完整系统综述。
- 不同来源的年份、统计单位和定义可能不一致，不能在缺少归一化时直接比较。
- 模拟器用于敏感性分析；参数分布和输出不代表概率预测。
- 公司交易、财报和采用率会随时间变化，引用结论应重新核对发布日期与原始文件。
- 职业和产业建议属于分析观点，应结合个人情况与独立研究判断。

发现引用、计算或界面问题时，请在 [GitHub Issues](https://github.com/zubin-li/ai-commanding-heights-analysis/issues) 中提供具体章节、数据字段和复现步骤。

## 维护者与贡献

- [Zubin Li](https://github.com/zubin-li) — 项目负责人、研究框架与数据架构
- Antigravity — AI 开发助手，参与前端实现与质量检查

## 许可与引用

代码使用 [MIT License](LICENSE)。来源材料和图片仍受其原权利人的许可约束。引用项目时可使用 [`CITATION.cff`](CITATION.cff)，引用具体事实时应优先引用相应原始来源。
