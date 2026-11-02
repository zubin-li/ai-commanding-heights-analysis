import re

html_path = "/Users/ashan/.gemini/antigravity/scratch/ai-commanding-heights-analysis/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update <style> block with comprehensive Light (Default) and Dark themes
old_style_match = re.search(r"<style>[\s\S]*?</style>", html)
if not old_style_match:
    print("Error: <style> not found")
    exit(1)

new_style = """<style>
    /* 默认白天模式 (Light Mode by Default - McKinsey / BCG Executive Style) */
    :root, body.theme-light {
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-card: #ffffff;
      --bg-card-hover: #f1f5f9;
      --border-color: #e2e8f0;
      --border-subtle: #f1f5f9;
      --border-accent: #0284c7;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #94a3b8;
      --accent-cyan: #0284c7;
      --accent-blue: #2563eb;
      --accent-emerald: #059669;
      --accent-rose: #e11d48;
      --accent-amber: #d97706;
      --accent-purple: #7c3aed;
      --takeaway-bg: #fffbeb;
      --takeaway-border: #d97706;
      --takeaway-text: #1e293b;
      --metric-card-bg: #ffffff;
      --metric-card-hover: #f8fafc;
      --chart-box-bg: #ffffff;
      --card-sub-bg: #f8fafc;
      --table-header-bg: #f1f5f9;
      --table-hover-bg: #f8fafc;
      --drawer-item-bg: #ffffff;
      --controls-bg: rgba(255, 255, 255, 0.96);
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
      --shadow-lg: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --header-bg: rgba(255, 255, 255, 0.95);
      --modal-backdrop: rgba(15, 23, 42, 0.65);
      --tag-bg: rgba(2, 132, 199, 0.08);
      --tag-border: rgba(2, 132, 199, 0.25);
      --card-highlight-bg: linear-gradient(180deg, #f0f9ff 0%, #ffffff 100%);
      --card-warning-bg: linear-gradient(180deg, #fff1f2 0%, #ffffff 100%);
      --quote-box-bg: linear-gradient(135deg, #f0f9ff 0%, #e0e7ff 100%);
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    /* 可切换暗黑模式 (Dark Mode) */
    body.theme-dark {
      --bg-primary: #0a0e17;
      --bg-secondary: #111827;
      --bg-card: rgba(17, 24, 39, 0.9);
      --bg-card-hover: rgba(31, 41, 55, 0.95);
      --border-color: rgba(75, 85, 99, 0.4);
      --border-subtle: rgba(75, 85, 99, 0.25);
      --border-accent: rgba(56, 189, 248, 0.5);
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --text-dim: #6b7280;
      --accent-cyan: #38bdf8;
      --accent-blue: #3b82f6;
      --accent-emerald: #10b981;
      --accent-rose: #f43f5e;
      --accent-amber: #f59e0b;
      --accent-purple: #a855f7;
      --takeaway-bg: rgba(30, 41, 59, 0.7);
      --takeaway-border: #f59e0b;
      --takeaway-text: #e2e8f0;
      --metric-card-bg: rgba(31, 41, 55, 0.5);
      --metric-card-hover: rgba(31, 41, 55, 0.8);
      --chart-box-bg: rgba(17, 24, 39, 0.7);
      --card-sub-bg: rgba(17, 24, 39, 0.6);
      --table-header-bg: rgba(31, 41, 55, 0.9);
      --table-hover-bg: rgba(55, 65, 81, 0.3);
      --drawer-item-bg: rgba(31, 41, 55, 0.6);
      --controls-bg: rgba(17, 24, 39, 0.95);
      --shadow-sm: 0 2px 8px rgba(0,0,0,0.4);
      --shadow-lg: 0 12px 30px rgba(0,0,0,0.6);
      --header-bg: rgba(10, 14, 23, 0.92);
      --modal-backdrop: rgba(0, 0, 0, 0.85);
      --tag-bg: rgba(56, 189, 248, 0.1);
      --tag-border: rgba(56, 189, 248, 0.3);
      --card-highlight-bg: linear-gradient(180deg, rgba(14, 165, 233, 0.08) 0%, rgba(31, 41, 55, 0.6) 100%);
      --card-warning-bg: linear-gradient(180deg, rgba(244, 63, 94, 0.08) 0%, rgba(31, 41, 55, 0.6) 100%);
      --quote-box-bg: linear-gradient(135deg, rgba(2, 132, 199, 0.15) 0%, rgba(99, 102, 241, 0.15) 100%);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-primary);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      overflow-x: hidden;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      transition: background-color 0.25s ease, color 0.25s ease;
    }

    /* 顶部导航控制台 */
    .header-nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 64px;
      background: var(--header-bg);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
      z-index: 1000;
      transition: background 0.25s ease, border-color 0.25s ease;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-badge {
      background: linear-gradient(135deg, #0284c7, #6366f1);
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }

    .brand-title {
      font-size: 15px;
      font-weight: 600;
      color: var(--text-main);
      letter-spacing: -0.2px;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 13px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-main);
      text-decoration: none;
    }

    .btn:hover {
      background: var(--bg-card-hover);
      border-color: var(--accent-cyan);
      color: var(--accent-cyan);
    }

    .btn-primary {
      background: linear-gradient(135deg, #0284c7, #2563eb);
      border: none;
      color: #fff !important;
    }
    .btn-primary:hover {
      background: linear-gradient(135deg, #0369a1, #1d4ed8);
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.35);
    }

    .btn-active {
      background: var(--tag-bg);
      border-color: var(--accent-cyan);
      color: var(--accent-cyan);
    }

    /* 视图容器 */
    #deck-container {
      margin-top: 64px;
      padding-bottom: 80px;
    }

    /* 幻灯片模式：单页居中展示 */
    .slide-mode .slide-card {
      display: none;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.3s ease, transform 0.3s ease;
    }

    .slide-mode .slide-card.active {
      display: block;
      opacity: 1;
      transform: translateY(0);
      max-width: 1320px;
      margin: 24px auto;
      padding: 0 20px;
    }

    /* 报告长文模式：连续垂直排版 */
    .report-mode .slide-card {
      display: block !important;
      opacity: 1 !important;
      transform: none !important;
      max-width: 1200px;
      margin: 40px auto;
      padding: 0 24px;
      border-bottom: 1px dashed var(--border-color);
      padding-bottom: 48px;
    }

    /* 幻灯片外壳与内容框架 */
    .slide-inner {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 36px 44px;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
      transition: background 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }

    .slide-header {
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 18px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 20px;
    }

    .slide-number-tag {
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      color: var(--accent-cyan);
      background: var(--tag-bg);
      border: 1px solid var(--tag-border);
      padding: 4px 10px;
      border-radius: 4px;
      letter-spacing: 0.5px;
      white-space: nowrap;
    }

    .slide-title-wrap h2 {
      font-size: 24px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 6px;
      letter-spacing: -0.3px;
    }

    .slide-subtitle {
      font-size: 14px;
      color: var(--text-muted);
      font-weight: 400;
    }

    .takeaway-banner {
      background: var(--takeaway-bg);
      border-left: 4px solid var(--takeaway-border);
      padding: 12px 18px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 26px;
      font-size: 14.5px;
      line-height: 1.6;
      color: var(--takeaway-text);
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }
    .takeaway-banner strong {
      color: var(--accent-amber);
    }

    /* 栅格系统 */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }

    .grid-1-2 {
      display: grid;
      grid-template-columns: 1fr 1.6fr;
      gap: 24px;
    }

    .grid-2-1 {
      display: grid;
      grid-template-columns: 1.6fr 1fr;
      gap: 24px;
    }

    /* 分析卡片组件 */
    .metric-card {
      background: var(--metric-card-bg);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 20px;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }

    .metric-card:hover {
      border-color: var(--border-accent);
      background: var(--metric-card-hover);
      transform: translateY(-2px);
    }

    .metric-card.highlight {
      border-color: var(--border-accent);
      background: var(--card-highlight-bg);
    }

    .metric-card.warning {
      border-color: rgba(225, 29, 72, 0.4);
      background: var(--card-warning-bg);
    }

    .metric-label {
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      color: var(--text-muted);
      letter-spacing: 0.6px;
      margin-bottom: 6px;
    }

    .metric-value {
      font-size: 28px;
      font-weight: 800;
      color: var(--text-main);
      font-family: var(--font-mono);
      margin-bottom: 8px;
    }
    .metric-value.cyan { color: var(--accent-cyan); }
    .metric-value.rose { color: var(--accent-rose); }
    .metric-value.emerald { color: var(--accent-emerald); }
    .metric-value.amber { color: var(--accent-amber); }

    .metric-desc {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    /* 观点要点列表 */
    .bullet-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .bullet-item {
      display: flex;
      gap: 12px;
      align-items: flex-start;
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.55;
    }
    .bullet-item strong {
      color: var(--text-main);
    }

    .bullet-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--accent-cyan);
      margin-top: 7px;
      flex-shrink: 0;
    }
    .bullet-dot.rose { background: var(--accent-rose); }
    .bullet-dot.emerald { background: var(--accent-emerald); }
    .bullet-dot.amber { background: var(--accent-amber); }

    /* 图表外框 */
    .chart-box {
      background: var(--chart-box-bg);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 16px;
      position: relative;
      box-shadow: var(--shadow-sm);
    }

    .chart-box-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }

    .chart-box-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .chart-container {
      width: 100%;
      height: 330px;
    }

    .slide-footer {
      margin-top: 24px;
      padding-top: 14px;
      border-top: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      color: var(--text-dim);
    }

    .source-tag {
      font-family: var(--font-mono);
      background: var(--card-sub-bg);
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
    }

    /* 底部悬浮控制器 */
    .deck-controls {
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--controls-bg);
      backdrop-filter: blur(14px);
      border: 1px solid var(--border-color);
      border-radius: 40px;
      padding: 8px 18px;
      display: flex;
      align-items: center;
      gap: 16px;
      box-shadow: var(--shadow-lg);
      z-index: 1000;
    }

    .deck-controls .btn-icon {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      width: 34px;
      height: 34px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
      font-size: 14px;
    }

    .deck-controls .btn-icon:hover {
      background: var(--accent-cyan);
      color: #fff;
      border-color: var(--accent-cyan);
    }

    .slide-counter {
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
    }
    .slide-counter span {
      color: var(--accent-cyan);
    }

    .progress-bar-wrap {
      width: 140px;
      height: 6px;
      background: var(--border-color);
      border-radius: 3px;
      overflow: hidden;
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #0284c7, #6366f1);
      width: 8.33%;
      transition: width 0.3s ease;
    }

    /* 模态框与辅助面板 */
    .modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: var(--modal-backdrop);
      backdrop-filter: blur(8px);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .modal-backdrop.open {
      display: flex;
    }

    .modal-content {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      max-width: 1100px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 32px;
      box-shadow: var(--shadow-lg);
      position: relative;
      color: var(--text-main);
    }

    .modal-close {
      position: absolute;
      top: 20px;
      right: 20px;
      background: var(--card-sub-bg);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      font-size: 18px;
      width: 32px;
      height: 32px;
      border-radius: 6px;
      cursor: pointer;
    }
    .modal-close:hover {
      color: var(--accent-rose);
      border-color: var(--accent-rose);
    }

    /* 幻灯片抽屉预览 */
    .drawer-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 16px;
      margin-top: 20px;
    }

    .drawer-item {
      background: var(--drawer-item-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 14px;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }

    .drawer-item:hover, .drawer-item.active {
      border-color: var(--accent-cyan);
      background: var(--bg-card-hover);
      transform: translateY(-2px);
    }

    .drawer-item-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-main);
      margin-top: 6px;
      line-height: 1.4;
    }

    /* 印证台账表格 */
    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      margin-top: 14px;
    }

    .data-table th {
      background: var(--table-header-bg);
      color: var(--text-muted);
      text-align: left;
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-color);
      font-weight: 600;
    }

    .data-table td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-main);
      vertical-align: top;
    }

    .data-table tr:hover td {
      background: var(--table-hover-bg);
    }

    .badge-verified {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      background: rgba(5, 150, 105, 0.12);
      color: var(--accent-emerald);
      border: 1px solid rgba(5, 150, 105, 0.3);
    }

    .badge-warning {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      background: rgba(217, 119, 6, 0.12);
      color: var(--accent-amber);
      border: 1px solid rgba(217, 119, 6, 0.3);
    }

    /* 原图对比轮播模态框 */
    .source-gallery {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 16px;
      max-height: 70vh;
      overflow-y: auto;
      padding: 10px;
    }
    .source-card {
      border: 1px solid var(--border-color);
      border-radius: 8px;
      overflow: hidden;
      background: var(--bg-card);
      cursor: pointer;
      transition: transform 0.2s;
      box-shadow: var(--shadow-sm);
    }
    .source-card:hover {
      transform: scale(1.03);
      border-color: var(--accent-cyan);
    }
    .source-card img {
      width: 100%;
      height: 240px;
      object-fit: cover;
      display: block;
    }
    .source-card-label {
      padding: 6px 10px;
      font-size: 12px;
      color: var(--text-muted);
      text-align: center;
      background: var(--bg-card);
    }

    /* 模拟器表单控制器 */
    .sim-slider-row {
      margin-bottom: 16px;
    }
    .sim-slider-row label {
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      color: var(--text-main);
      margin-bottom: 6px;
    }
    .sim-slider {
      width: 100%;
      height: 6px;
      border-radius: 3px;
      background: var(--border-color);
      outline: none;
      -webkit-appearance: none;
    }
    .sim-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--accent-cyan);
      cursor: pointer;
      box-shadow: 0 0 8px rgba(2, 132, 199, 0.5);
    }

    /* 打印与 PDF 导出优化样式 (A4 / 16:9 横版完美导出) */
    @media print {
      body {
        background: #ffffff !important;
        color: #0f172a !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .header-nav, .deck-controls, .modal-backdrop, .no-print {
        display: none !important;
      }
      #deck-container {
        margin-top: 0 !important;
        padding-bottom: 0 !important;
      }
      .slide-card {
        display: block !important;
        opacity: 1 !important;
        transform: none !important;
        page-break-after: always !important;
        break-after: page !important;
        max-width: 100% !important;
        margin: 0 !important;
        padding: 12mm 10mm !important;
        height: 100vh !important;
        box-sizing: border-box !important;
      }
      .slide-inner {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        height: 100% !important;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: #ffffff !important;
      }
      .chart-container {
        height: 280px !important;
      }
    }

    @media (max-width: 900px) {
      .grid-2, .grid-3, .grid-1-2, .grid-2-1 {
        grid-template-columns: 1fr;
      }
      .slide-inner {
        padding: 24px 20px;
      }
      .slide-header {
        flex-direction: column;
      }
      .deck-controls {
        width: 92%;
        justify-content: space-between;
      }
      .progress-bar-wrap {
        display: none;
      }
    }
  </style>"""

html = html[:old_style_match.start()] + new_style + html[old_style_match.end():]

# 2. Update <body ...> to default to theme-light
html = re.sub(r'<body class="[^"]*">', '<body class="slide-mode theme-light">', html)

# 3. Add Theme Toggle button into .nav-actions
nav_target = '<button class="btn btn-active" id="btn-toggle-view"'
if 'id="btn-theme-toggle"' not in html:
    theme_btn_html = """<button class="btn" id="btn-theme-toggle" onclick="toggleTheme()" title="切换白天/暗黑模式 (T)">
        <span id="theme-icon">🌙</span>
        <span id="theme-text">暗黑模式</span>
      </button>
      <button class="btn btn-active" id="btn-toggle-view" """
    html = html.replace(nav_target, theme_btn_html, 1)

# 4. Clean up inline styles that forced dark backgrounds
# Slide 6 sub-boxes
html = html.replace("background: rgba(17, 24, 39, 0.5); border-left: 3px solid #64748b; border-radius: 4px;", "background: var(--card-sub-bg); border-left: 3px solid #64748b; border-radius: 4px;")
html = html.replace("background: rgba(17, 24, 39, 0.5); border-left: 3px solid #38bdf8; border-radius: 4px;", "background: var(--card-sub-bg); border-left: 3px solid var(--accent-cyan); border-radius: 4px;")
html = html.replace("background: rgba(17, 24, 39, 0.5); border-left: 3px solid #a855f7; border-radius: 4px;", "background: var(--card-sub-bg); border-left: 3px solid var(--accent-purple); border-radius: 4px;")
html = html.replace("background: rgba(17, 24, 39, 0.5); border-left: 3px solid #f43f5e; border-radius: 4px;", "background: var(--card-sub-bg); border-left: 3px solid var(--accent-rose); border-radius: 4px;")

# Slide 6 governance box
html = html.replace("background: rgba(0,0,0,0.3); padding: 8px; border-radius: 4px;", "background: var(--card-sub-bg); border: 1px solid var(--border-color); padding: 8px; border-radius: 4px;")

# Slide 9 history sub-boxes
html = html.replace("background: rgba(17, 24, 39, 0.6); border-radius: 6px;", "background: var(--card-sub-bg); border: 1px solid var(--border-color); border-radius: 6px;")

# Slide 11 calculation box
html = html.replace("background: rgba(0,0,0,0.3); border-radius: 6px;", "background: var(--card-sub-bg); border: 1px solid var(--border-color); border-radius: 6px;")

# Slide 12 concluding quote banner
html = html.replace('background: linear-gradient(135deg, rgba(2, 132, 199, 0.15) 0%, rgba(99, 102, 241, 0.15) 100%); border-color: rgba(56, 189, 248, 0.5);', 'background: var(--quote-box-bg); border-color: var(--border-accent);')

# Replace white text in sub-boxes
html = re.sub(r'<strong style="color: #fff;">', '<strong>', html)
html = re.sub(r'<div style="font-weight: 700; color: #fff;', '<div style="font-weight: 700; color: var(--text-main);', html)
html = re.sub(r'<h3 style="font-size: 17px; color: #fff;', '<h3 style="font-size: 17px; color: var(--text-main);', html)
html = re.sub(r'<h3 style="font-size: 20px; color: #fff;', '<h3 style="font-size: 20px; color: var(--text-main);', html)
html = re.sub(r'color: #e5e7eb;', 'color: var(--text-main);', html)

# 5. Update Javascript to support dynamic theme switching & ECharts palette updates
old_js_start = html.find("<!-- 交互脚本与 ECharts 渲染引擎 -->")
new_js = """<!-- 交互脚本与 ECharts 渲染引擎 -->
  <script>
    let currentSlide = 1;
    const totalSlides = 12;
    let isReportMode = false;
    let chartInstances = {};

    const slideTitles = [
      "颠覆华尔街假设：智能本身只是赠品",
      "商业史五百年镜鉴：发明的 7% 诅咒",
      "大模型创世纪深渊：价格雪崩与训练爆炸",
      "云巨头算力开支失衡：2027 死亡交叉",
      "全球白领就业 K 型撕裂与纸带防线",
      "企业第四次重构：中层瓦解与人格化资本",
      "终极定义：什么是真正的制高点？",
      "私募股权变局：从门票 VC 到存量改造",
      "巴菲特报业败局启示：AI 时代的 Android",
      "全网权威数据深度印证台账",
      "动态情景模拟器与敏感性推演",
      "终局资产配置指南与战略行动 Playbook"
    ];

    // 初始化页面 (默认白天模式)
    window.addEventListener('DOMContentLoaded', () => {
      // 保证默认白天模式
      document.body.classList.remove('theme-dark');
      document.body.classList.add('theme-light');

      initDrawerGrid();
      initSourceGallery();
      updateControls();

      // 初始化第一页图表
      ensureSlideChart(1);

      // 键盘导航快捷键
      window.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        if (e.key === 'ArrowRight' || e.key === 'Space') {
          e.preventDefault();
          nextSlide();
        } else if (e.key === 'ArrowLeft') {
          e.preventDefault();
          prevSlide();
        } else if (e.key === 'm' || e.key === 'M') {
          toggleViewMode();
        } else if (e.key === 'p' || e.key === 'P') {
          window.print();
        } else if (e.key === 'f' || e.key === 'F') {
          toggleFullscreen();
        } else if (e.key === 't' || e.key === 'T') {
          toggleTheme();
        }
      });

      // 窗口缩放自适应图表
      window.addEventListener('resize', () => {
        Object.values(chartInstances).forEach(c => c && c.resize());
      });
    });

    // 主题切换：白天 (默认) ⟷ 暗黑
    function toggleTheme() {
      const body = document.body;
      const isDark = body.classList.toggle('theme-dark');
      if (isDark) {
        body.classList.remove('theme-light');
        document.getElementById('theme-icon').innerText = '☀️';
        document.getElementById('theme-text').innerText = '白天模式';
      } else {
        body.classList.add('theme-light');
        document.getElementById('theme-icon').innerText = '🌙';
        document.getElementById('theme-text').innerText = '暗黑模式';
      }
      rebuildCharts();
    }

    function getChartTheme() {
      const isDark = document.body.classList.contains('theme-dark');
      return {
        isDark: isDark,
        text: isDark ? '#9ca3af' : '#475569',
        title: isDark ? '#f3f4f6' : '#0f172a',
        splitLine: isDark ? 'rgba(75, 85, 99, 0.25)' : 'rgba(226, 232, 240, 0.8)',
        axisLine: isDark ? 'rgba(75, 85, 99, 0.4)' : '#cbd5e1',
        tooltipBg: isDark ? '#1f2937' : '#ffffff',
        tooltipBorder: isDark ? '#374151' : '#cbd5e1',
        tooltipText: isDark ? '#f3f4f6' : '#0f172a',
        tooltipShadow: isDark ? '0 8px 24px rgba(0,0,0,0.5)' : '0 8px 24px rgba(0,0,0,0.08)',
        radarArea: isDark 
          ? ['rgba(31, 41, 55, 0.2)', 'rgba(31, 41, 55, 0.4)', 'rgba(31, 41, 55, 0.6)']
          : ['#f8fafc', '#f1f5f9', '#e2e8f0'],
        radarLabel: isDark ? '#e5e7eb' : '#1e293b'
      };
    }

    function rebuildCharts() {
      Object.keys(chartInstances).forEach(key => {
        if (chartInstances[key]) {
          chartInstances[key].dispose();
          delete chartInstances[key];
        }
      });
      if (isReportMode) {
        initChartHistory();
        initChartScissors();
        initChartCapex();
        initChartLabor();
        initChartRadar();
        initChartSimulation();
      } else {
        ensureSlideChart(currentSlide);
      }
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
          console.log('Fullscreen error:', err);
        });
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    }

    function showSlide(index) {
      if (index < 1 || index > totalSlides) return;
      currentSlide = index;

      document.querySelectorAll('.slide-card').forEach((slide, idx) => {
        if (idx + 1 === currentSlide) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });

      updateControls();
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // 确保当前幻灯片的图表完成初始化并自适应尺寸
      setTimeout(() => {
        ensureSlideChart(currentSlide);
        Object.values(chartInstances).forEach(c => c && c.resize());
      }, 60);
    }

    function ensureSlideChart(slideNum) {
      try {
        if (slideNum === 2 && !chartInstances.history) initChartHistory();
        else if (slideNum === 3 && !chartInstances.scissors) initChartScissors();
        else if (slideNum === 4 && !chartInstances.capex) initChartCapex();
        else if (slideNum === 5 && !chartInstances.labor) initChartLabor();
        else if (slideNum === 7 && !chartInstances.radar) initChartRadar();
        else if (slideNum === 11 && !chartInstances.simulation) initChartSimulation();

        Object.values(chartInstances).forEach(c => c && c.resize());
      } catch (err) {
        console.error('Chart resize error:', err);
      }
    }

    function nextSlide() {
      if (currentSlide < totalSlides) showSlide(currentSlide + 1);
    }

    function prevSlide() {
      if (currentSlide > 1) showSlide(currentSlide - 1);
    }

    function updateControls() {
      document.getElementById('cur-slide-num').innerText = currentSlide.toString().padStart(2, '0');
      const progressPercent = (currentSlide / totalSlides) * 100;
      document.getElementById('progress-bar').style.width = progressPercent + '%';

      // 更新抽屉激活状态
      document.querySelectorAll('.drawer-item').forEach((item, idx) => {
        if (idx + 1 === currentSlide) item.classList.add('active');
        else item.classList.remove('active');
      });
    }

    function toggleViewMode() {
      isReportMode = !isReportMode;
      const body = document.body;
      const btnText = document.getElementById('view-mode-text');
      const controls = document.querySelector('.deck-controls');

      if (isReportMode) {
        body.classList.remove('slide-mode');
        body.classList.add('report-mode');
        btnText.innerText = "切换幻灯片";
        controls.style.display = 'none';
        initChartHistory();
        initChartScissors();
        initChartCapex();
        initChartLabor();
        initChartRadar();
        initChartSimulation();
      } else {
        body.classList.remove('report-mode');
        body.classList.add('slide-mode');
        btnText.innerText = "幻灯片模式";
        controls.style.display = 'flex';
        showSlide(currentSlide);
      }
      setTimeout(() => {
        Object.values(chartInstances).forEach(c => c && c.resize());
      }, 200);
    }

    function openDrawer() {
      document.getElementById('drawer-modal').classList.add('open');
    }
    function closeDrawer() {
      document.getElementById('drawer-modal').classList.remove('open');
    }

    function openSourceModal() {
      document.getElementById('source-modal').classList.add('open');
    }
    function closeSourceModal() {
      document.getElementById('source-modal').classList.remove('open');
    }

    function openLedgerModal() {
      const modal = document.getElementById('ledger-modal');
      const container = document.getElementById('ledger-modal-content');
      const tableHtml = document.querySelector('#slide-10 .data-table').outerHTML;
      container.innerHTML = tableHtml;
      modal.classList.add('open');
    }
    function closeLedgerModal() {
      document.getElementById('ledger-modal').classList.remove('open');
    }

    function initDrawerGrid() {
      const container = document.getElementById('drawer-grid-items');
      container.innerHTML = slideTitles.map((title, idx) => `
        <div class="drawer-item ${idx + 1 === currentSlide ? 'active' : ''}" onclick="showSlide(${idx + 1}); closeDrawer();">
          <span class="slide-number-tag">SLIDE ${String(idx + 1).padStart(2, '0')}</span>
          <div class="drawer-item-title">${title}</div>
        </div>
      `).join('');
    }

    function initSourceGallery() {
      const gallery = document.getElementById('source-gallery-items');
      let html = '';
      for (let i = 1; i <= 19; i++) {
        html += `
          <div class="source-card" onclick="window.open('./images/${i}.jpg', '_blank')">
            <img src="./images/${i}.jpg" alt="Slide ${i}" loading="lazy">
            <div class="source-card-label">原贴第 ${i} 页 (点击放大)</div>
          </div>
        `;
      }
      gallery.innerHTML = html;
    }

    // ====================== ECharts 数据图表配置 ======================
    function initChartHistory() {
      const dom = document.getElementById('chart-history');
      if (!dom) return;
      const chart = echarts.init(dom);
      chartInstances.history = chart;
      const theme = getChartTheme();

      const option = {
        tooltip: { 
          trigger: 'axis', 
          axisPointer: { type: 'shadow' },
          backgroundColor: theme.tooltipBg,
          borderColor: theme.tooltipBorder,
          textStyle: { color: theme.tooltipText },
          extraCssText: `box-shadow: ${theme.tooltipShadow};`
        },
        legend: { textStyle: { color: theme.text }, top: 0 },
        grid: { left: '3%', right: '4%', bottom: '5%', top: '35px', containLabel: true },
        xAxis: {
          type: 'value',
          max: 100,
          axisLabel: { formatter: '{value}%', color: theme.text },
          splitLine: { lineStyle: { color: theme.splitLine } }
        },
        yAxis: {
          type: 'category',
          data: ['1890 铁路网络', '1947 晶体管革命', '1980 个人电脑', '2005 移动互联网', '2026 AI 智能革命 (预测)'],
          axisLabel: { color: theme.title, fontSize: 12 },
          axisLine: { lineStyle: { color: theme.axisLine } }
        },
        series: [
          {
            name: '底层技术发明者留存',
            type: 'bar',
            stack: 'total',
            itemStyle: { color: '#e11d48' },
            data: [7, 4, 12, 8, 5]
          },
          {
            name: '流通通道与制高点垄断者',
            type: 'bar',
            stack: 'total',
            itemStyle: { color: '#059669', borderRadius: [0, 4, 4, 0] },
            data: [93, 96, 88, 92, 95]
          }
        ]
      };
      chart.setOption(option);
    }

    function initChartScissors() {
      const dom = document.getElementById('chart-scissors');
      if (!dom) return;
      const chart = echarts.init(dom);
      chartInstances.scissors = chart;
      const theme = getChartTheme();

      const years = ['2020 (GPT-3)', '2021', '2022', '2023 (GPT-4)', '2024', '2025', '2026 (当前)', '2027 (预测)', '2028 (预测)'];
      const tokenPrices = [20.0, 10.0, 4.0, 1.5, 0.4, 0.08, 0.02, 0.005, 0.001];
      const trainingCosts = [4.6, 12.0, 35.0, 100.0, 300.0, 650.0, 1200.0, 3500.0, 10000.0];

      const option = {
        tooltip: { 
          trigger: 'axis',
          backgroundColor: theme.tooltipBg,
          borderColor: theme.tooltipBorder,
          textStyle: { color: theme.tooltipText },
          extraCssText: `box-shadow: ${theme.tooltipShadow};`
        },
        legend: { textStyle: { color: theme.text }, top: 0 },
        grid: { left: '3%', right: '5%', bottom: '5%', top: '40px', containLabel: true },
        xAxis: {
          type: 'category',
          data: years,
          axisLabel: { color: theme.text, rotate: 20 },
          axisLine: { lineStyle: { color: theme.axisLine } }
        },
        yAxis: [
          {
            type: 'log',
            name: '百万 Token 推理单价 ($)',
            nameTextStyle: { color: '#0284c7' },
            position: 'left',
            axisLabel: { color: '#0284c7', formatter: '${value}' },
            splitLine: { lineStyle: { color: theme.splitLine } }
          },
          {
            type: 'log',
            name: '单次前沿训练支出 ($M)',
            nameTextStyle: { color: '#e11d48' },
            position: 'right',
            axisLabel: { color: '#e11d48', formatter: '${value}M' },
            splitLine: { show: false }
          }
        ],
        series: [
          {
            name: '基准推理单价 (每季-47%)',
            type: 'line',
            yAxisIndex: 0,
            data: tokenPrices,
            smooth: true,
            lineStyle: { width: 3, color: '#0284c7' },
            itemStyle: { color: '#0284c7' },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgba(2, 132, 199, 0.35)' },
                { offset: 1, color: 'rgba(2, 132, 199, 0.0)' }
              ])
            }
          },
          {
            name: '单次前沿训练支出 (年增 3.5x)',
            type: 'line',
            yAxisIndex: 1,
            data: trainingCosts,
            smooth: true,
            lineStyle: { width: 3, color: '#e11d48' },
            itemStyle: { color: '#e11d48' }
          }
        ]
      };
      chart.setOption(option);
    }

    function initChartCapex() {
      const dom = document.getElementById('chart-capex');
      if (!dom) return;
      const chart = echarts.init(dom);
      chartInstances.capex = chart;
      const theme = getChartTheme();

      const years = ['2023', '2024', '2025', '2026E', '2027E', '2028E', '2029E', '2030E'];
      const capex = [148, 225, 410, 780, 1020, 1150, 1180, 1200];
      const ocf = [210, 260, 320, 395, 485, 595, 740, 920];
      const fcf = ocf.map((val, idx) => val - capex[idx]);

      const option = {
        tooltip: { 
          trigger: 'axis', 
          axisPointer: { type: 'cross' },
          backgroundColor: theme.tooltipBg,
          borderColor: theme.tooltipBorder,
          textStyle: { color: theme.tooltipText },
          extraCssText: `box-shadow: ${theme.tooltipShadow};`
        },
        legend: { textStyle: { color: theme.text }, top: 0 },
        grid: { left: '3%', right: '4%', bottom: '5%', top: '40px', containLabel: true },
        xAxis: { 
          type: 'category', 
          data: years, 
          axisLabel: { color: theme.text },
          axisLine: { lineStyle: { color: theme.axisLine } }
        },
        yAxis: {
          type: 'value',
          name: '十亿美元 ($B)',
          nameTextStyle: { color: theme.text },
          axisLabel: { color: theme.text },
          splitLine: { lineStyle: { color: theme.splitLine } }
        },
        series: [
          {
            name: '四大云巨头 Capex 算力开支',
            type: 'bar',
            data: capex,
            itemStyle: { color: '#0284c7', borderRadius: [4, 4, 0, 0] }
          },
          {
            name: '经营现金流 (OCF)',
            type: 'line',
            data: ocf,
            lineStyle: { width: 3, color: '#059669' },
            itemStyle: { color: '#059669' }
          },
          {
            name: '自由现金流缺口 (FCF 赤字)',
            type: 'line',
            data: fcf,
            lineStyle: { width: 3, color: '#e11d48', type: 'dashed' },
            itemStyle: { color: '#e11d48' },
            markPoint: {
              data: [
                { name: '死亡交叉', value: '死亡交叉 -$535B', coord: ['2027E', -535] }
              ]
            }
          }
        ]
      };
      chart.setOption(option);
    }

    function initChartLabor() {
      const dom = document.getElementById('chart-labor');
      if (!dom) return;
      const chart = echarts.init(dom);
      chartInstances.labor = chart;
      const theme = getChartTheme();

      const quarters = ['FY23 Q1', 'FY23 Q3', 'FY24 Q1', 'FY24 Q3', 'FY25 Q1', 'FY25 Q3', 'FY26 Q1', 'FY26 Q4 (现时)'];
      const headcountChange = [14.2, 5.8, -1.8, -5.7, -8.3, -12.1, -18.5, -23.46];
      const profitGrowth = [4.1, 5.0, 5.8, 6.2, 6.9, 7.2, 7.4, 7.5];

      const option = {
        tooltip: { 
          trigger: 'axis',
          backgroundColor: theme.tooltipBg,
          borderColor: theme.tooltipBorder,
          textStyle: { color: theme.tooltipText },
          extraCssText: `box-shadow: ${theme.tooltipShadow};`
        },
        legend: { textStyle: { color: theme.text }, top: 0 },
        grid: { left: '3%', right: '5%', bottom: '5%', top: '40px', containLabel: true },
        xAxis: { 
          type: 'category', 
          data: quarters, 
          axisLabel: { color: theme.text, rotate: 20 },
          axisLine: { lineStyle: { color: theme.axisLine } }
        },
        yAxis: [
          {
            type: 'value',
            name: '全职员工累计净增减 (千人)',
            nameTextStyle: { color: '#e11d48' },
            position: 'left',
            axisLabel: { color: '#e11d48' },
            splitLine: { lineStyle: { color: theme.splitLine } }
          },
          {
            type: 'value',
            name: '调整后营业利润增速 (%)',
            nameTextStyle: { color: '#059669' },
            position: 'right',
            axisLabel: { color: '#059669', formatter: '{value}%' },
            splitLine: { show: false }
          }
        ],
        series: [
          {
            name: '员工规模净减员 (千人)',
            type: 'bar',
            yAxisIndex: 0,
            data: headcountChange,
            itemStyle: {
              color: function(params) {
                return params.value < 0 ? '#e11d48' : '#0284c7';
              }
            }
          },
          {
            name: '营业利润逆势增长率 (%)',
            type: 'line',
            yAxisIndex: 1,
            data: profitGrowth,
            smooth: true,
            lineStyle: { width: 3, color: '#059669' },
            itemStyle: { color: '#059669' }
          }
        ]
      };
      chart.setOption(option);
    }

    function initChartRadar() {
      const dom = document.getElementById('chart-radar');
      if (!dom) return;
      const chart = echarts.init(dom);
      chartInstances.radar = chart;
      const theme = getChartTheme();

      const option = {
        tooltip: {
          backgroundColor: theme.tooltipBg,
          borderColor: theme.tooltipBorder,
          textStyle: { color: theme.tooltipText },
          extraCssText: `box-shadow: ${theme.tooltipShadow};`
        },
        legend: { textStyle: { color: theme.text }, top: 0 },
        radar: {
          indicator: [
            { name: '边际网络效应与抽税力', max: 100 },
            { name: '资本防稀释与抗填平能力', max: 100 },
            { name: '法定签名与合规护城河', max: 100 },
            { name: '真实业务闭环靶场壁垒', max: 100 },
            { name: '客户切换成本与黏性', max: 100 },
            { name: '长周期暴利持续时间', max: 100 }
          ],
          shape: 'circle',
          splitArea: {
            areaStyle: {
              color: theme.radarArea
            }
          },
          axisLine: { lineStyle: { color: theme.axisLine } },
          splitLine: { lineStyle: { color: theme.splitLine } },
          axisName: { color: theme.radarLabel, fontSize: 11.5 }
        },
        series: [{
          name: '制高点特征透视',
          type: 'radar',
          data: [
            {
              value: [25, 20, 15, 30, 25, 30],
              name: '伪制高点 (燃气轮机/芯片租赁/套壳SaaS)',
              itemStyle: { color: '#e11d48' },
              areaStyle: { color: 'rgba(225, 29, 72, 0.22)' }
            },
            {
              value: [95, 90, 85, 92, 95, 98],
              name: '真制高点 (分发入口/清算轨道/专有RL靶场)',
              itemStyle: { color: '#059669' },
              areaStyle: { color: 'rgba(5, 150, 105, 0.28)' }
            }
          ]
        }]
      };
      chart.setOption(option);
    }

    function initChartSimulation() {
      const dom = document.getElementById('chart-sim');
      if (!dom) return;
      const chart = echarts.init(dom);
      chartInstances.simulation = chart;
      renderSimulationChart();
    }

    function updateSimulation() {
      const def = parseInt(document.getElementById('slider-deflation').value);
      const cap = parseInt(document.getElementById('slider-capex').value);
      const bpo = parseInt(document.getElementById('slider-bpo').value);

      document.getElementById('val-deflation').innerText = `-${def}% / 季`;
      document.getElementById('val-capex').innerText = `+${cap}% / 年`;
      document.getElementById('val-bpo').innerText = `${bpo}% 替代`;

      const margin = Math.max(2, (45 - (def * 0.75))).toFixed(1);
      const gap = Math.round(250 + (cap * 3.0));
      const layoff = Math.round(bpo * 0.85);

      document.getElementById('res-margin').innerText = margin + '%';
      document.getElementById('res-gap').innerText = `$${gap} 亿美元`;
      document.getElementById('res-layoff').innerText = layoff + '%';

      renderSimulationChart(def, cap, bpo);
    }

    function renderSimulationChart(def = 47, cap = 70, bpo = 45) {
      if (!chartInstances.simulation) return;
      const theme = getChartTheme();

      const years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030'];
      const marginSeries = [35, 26, 18, Math.max(3, 14 - def*0.1), Math.max(2, 8 - def*0.08), 5, 4];
      const gapSeries = [120, 240, 390, Math.round(cap * 6.5), Math.round(cap * 6.0), Math.round(cap * 4.5), 200];

      const option = {
        tooltip: { 
          trigger: 'axis',
          backgroundColor: theme.tooltipBg,
          borderColor: theme.tooltipBorder,
          textStyle: { color: theme.tooltipText },
          extraCssText: `box-shadow: ${theme.tooltipShadow};`
        },
        legend: { textStyle: { color: theme.text }, top: 0 },
        grid: { left: '3%', right: '5%', bottom: '5%', top: '35px', containLabel: true },
        xAxis: { 
          type: 'category', 
          data: years, 
          axisLabel: { color: theme.text },
          axisLine: { lineStyle: { color: theme.axisLine } }
        },
        yAxis: [
          {
            type: 'value',
            name: '模型层平均毛利率 (%)',
            nameTextStyle: { color: '#e11d48' },
            position: 'left',
            axisLabel: { color: '#e11d48', formatter: '{value}%' },
            splitLine: { lineStyle: { color: theme.splitLine } }
          },
          {
            type: 'value',
            name: '累计自由现金流缺口 ($B)',
            nameTextStyle: { color: '#0284c7' },
            position: 'right',
            axisLabel: { color: '#0284c7', formatter: '${value}B' },
            splitLine: { show: false }
          }
        ],
        series: [
          {
            name: '模型层平均毛利率',
            type: 'line',
            yAxisIndex: 0,
            data: marginSeries,
            smooth: true,
            lineStyle: { width: 3, color: '#e11d48' },
            itemStyle: { color: '#e11d48' }
          },
          {
            name: '云巨头现金流缺口',
            type: 'bar',
            yAxisIndex: 1,
            data: gapSeries,
            itemStyle: { color: '#0284c7', borderRadius: [4, 4, 0, 0] }
          }
        ]
      };
      chartInstances.simulation.setOption(option);
    }
  </script>
</body>
</html>"""

html = html[:old_js_start] + new_js

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully with default Light mode & Dark mode toggle!")
