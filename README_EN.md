[中文](README.md) · [English](README_EN.md)

# AI Commanding Heights: Profitability and Value-Capture Analysis

[![Live research deck](https://img.shields.io/badge/GitHub_Pages-Live-0969da?logo=github)](https://zubin-li.github.io/ai-commanding-heights-analysis/)
[![Methodology](https://img.shields.io/badge/Research-Methods_and_sources-005ea8)](docs/methodology.md)
[![License: MIT](https://img.shields.io/badge/Code-MIT-yellow.svg)](LICENSE)

A bilingual interactive research deck that examines the thesis that economic rent may shift toward industry bottlenecks as foundation models become more interchangeable. It separates the source report, social-media retellings, external evidence, scenario assumptions, and author interpretation, and includes an adjustable sensitivity simulator.

**Live site:** <https://zubin-li.github.io/ai-commanding-heights-analysis/>

**Full research text:** [`docs/strategic_report.md`](docs/strategic_report.md)

## Research questions

- Does a falling unit price for model inference necessarily prevent the model layer from capturing value?
- How large could the return gap between AI-infrastructure capital expenditure and attributable revenue become?
- Which bottlenecks in data, energy, distribution, workflow, and legal accountability may retain bargaining power?
- Which claims in social-media summaries are reproducible, and which are inference or misinterpretation?
- How sensitive are scenario results to assumptions about inference prices, capital expenditure, and enterprise adoption?

The site is a continuous vertical research deck. It defaults to English and a light theme and provides Chinese, a dark theme, 15 sections, interactive charts, a source gallery, an evidence ledger, and a three-parameter sensitivity simulator.

## How to read the evidence

| Layer | Meaning | Appropriate use |
| --- | --- | --- |
| Source fact | Traceable to a listed public source or company disclosure | Check the original link, definition, and publication date |
| External estimate | A third party's estimate or model output | Preserve its assumptions and uncertainty |
| Project scenario | Parameters set by this repository for sensitivity analysis | Compare directions; do not treat as a forecast |
| Author interpretation | Analysis of value capture and industry or career effects | Treat as a thesis to test, not an established fact |

> [!CAUTION]
> This project is not investment advice. Future-year values, capital gaps, sector rankings, and simulator outputs can depend on assumptions. “Checked” should mean that cited evidence supports a specific statement—not that the entire argument has been proven. Read [`docs/citations.md`](docs/citations.md), [`docs/data_dictionary.md`](docs/data_dictionary.md), and [`docs/methodology.md`](docs/methodology.md) before relying on a conclusion.

## Run locally

Python 3 is required; there is no frontend build step.

```bash
git clone https://github.com/zubin-li/ai-commanding-heights-analysis.git
cd ai-commanding-heights-analysis
python3 server.py
```

Open <http://127.0.0.1:8080>. You can also run `npm run serve` or `./run.sh`. Serving the project over HTTP is recommended instead of opening `index.html` directly.

## Verification

```bash
npm test
```

This checks project files, structured data, i18n keys, and key page contracts. It is not automated proof of visual quality or factual truth. Real-browser acceptance should additionally cover desktop and mobile viewports, both languages, both themes, charts, dialogs, keyboard behavior, and observable simulator state changes.

To rebuild structured data:

```bash
npm run data:build
```

## Repository map

| Path | Purpose |
| --- | --- |
| `index.html`, `i18n.js` | Continuous research deck, interactions, and bilingual copy |
| `data/` | Chart inputs, evidence ledger, and scenario inputs |
| `docs/strategic_report.md` | Long-form research report |
| `docs/methodology.md` | Research method, evidence levels, and limitations |
| `docs/citations.md` | Sources and citation information |
| `docs/data_dictionary.md` | Metrics, units, and calculation definitions |
| `images/` | The 19-page source material being analysed |
| `tests/` | Project contract and regression checks |
| `scripts/` | Data and page generation scripts |

## Known limitations

- The project starts from one report and a specific set of retellings; it is not a complete systematic review of the AI industry.
- Sources may use different years, units, and definitions and should not be compared without normalisation.
- The simulator is for sensitivity analysis; its parameter ranges and output are not probabilistic forecasts.
- Transactions, financial disclosures, and adoption metrics change over time. Recheck dates and primary documents before citing a conclusion.
- Career and sector recommendations are analytical opinions and require independent judgement.

For citation, calculation, or interface defects, open a [GitHub issue](https://github.com/zubin-li/ai-commanding-heights-analysis/issues) with the section, data field, and reproduction steps.

## Maintainers and contributions

- [Zubin Li](https://github.com/zubin-li) — project lead, research framework, and data architecture
- Antigravity — AI development assistant; frontend implementation and quality checks

## License and citation

Code is released under the [MIT License](LICENSE). Source material and images remain subject to their original rights. Use [`CITATION.cff`](CITATION.cff) to cite the project; cite the corresponding primary source for individual factual claims.
