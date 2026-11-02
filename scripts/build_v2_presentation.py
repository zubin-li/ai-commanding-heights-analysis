# Script to generate the comprehensive, master-grade Consulting Slide Deck & Report V2
import re

html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI 时代的「制高点」之战：大模型商品化危机、终极暴利重构与现实可行性批判</title>
  <!-- ECharts 5 离线优先加载，兼顾 CDN 降级 -->
  <script src="./echarts.min.js"></script>
  <script>
    if (!window.echarts) {
      document.write('<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"><\\/script>');
    }
  </script>
  <style>
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
      --critique-bg: #fef2f2;
      --critique-border: #e11d48;
      --critique-text: #881337;
      --future-bg: #f0fdf4;
      --future-border: #059669;
      --future-text: #064e3b;
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
      --critique-bg: rgba(153, 27, 27, 0.25);
      --critique-border: #f43f5e;
      --critique-text: #fecdd3;
      --future-bg: rgba(6, 78, 59, 0.25);
      --future-border: #10b981;
      --future-text: #a7f3d0;
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
      font-size: 14.5px;
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
      padding: 34px 42px;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
      transition: background 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }

    .slide-header {
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 16px;
      margin-bottom: 22px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 20px;
    }

    .slide-number-tag {
      font-family: var(--font-mono);
      font-size: 12.5px;
      font-weight: 700;
      color: var(--accent-cyan);
      background: var(--tag-bg);
      border: 1px solid var(--tag-border);
      padding: 3px 9px;
      border-radius: 4px;
      letter-spacing: 0.5px;
      white-space: nowrap;
    }

    .slide-title-wrap h2 {
      font-size: 23px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 6px;
      letter-spacing: -0.3px;
    }

    .slide-subtitle {
      font-size: 13.5px;
      color: var(--text-muted);
      font-weight: 400;
    }

    .takeaway-banner {
      background: var(--takeaway-bg);
      border-left: 4px solid var(--takeaway-border);
      padding: 12px 18px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 22px;
      font-size: 14px;
      line-height: 1.6;
      color: var(--takeaway-text);
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }
    .takeaway-banner strong {
      color: var(--accent-amber);
    }

    .critique-banner {
      background: var(--critique-bg);
      border-left: 4px solid var(--critique-border);
      padding: 12px 18px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 22px;
      font-size: 14px;
      line-height: 1.6;
      color: var(--critique-text);
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }
    .critique-banner strong {
      color: var(--accent-rose);
    }

    .future-banner {
      background: var(--future-bg);
      border-left: 4px solid var(--future-border);
      padding: 12px 18px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 22px;
      font-size: 14px;
      line-height: 1.6;
      color: var(--future-text);
      border-top: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }
    .future-banner strong {
      color: var(--accent-emerald);
    }

    /* 栅格系统 */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 22px;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }

    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }

    .grid-1-2 {
      display: grid;
      grid-template-columns: 1fr 1.6fr;
      gap: 22px;
    }

    .grid-2-1 {
      display: grid;
      grid-template-columns: 1.6fr 1fr;
      gap: 22px;
    }

    /* 分析卡片组件 */
    .metric-card {
      background: var(--metric-card-bg);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 18px;
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
      font-size: 26px;
      font-weight: 800;
      color: var(--text-main);
      font-family: var(--font-mono);
      margin-bottom: 6px;
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
      font-size: 13.5px;
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
      margin-top: 22px;
      padding-top: 12px;
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
      width: 6.67%;
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
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
      gap: 14px;
      margin-top: 18px;
    }

    .drawer-item {
      background: var(--drawer-item-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px;
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
      font-size: 12.5px;
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
      padding: 11px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-main);
      vertical-align: top;
      line-height: 1.5;
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
      white-space: nowrap;
    }

    .badge-error {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      background: rgba(225, 29, 72, 0.12);
      color: var(--accent-rose);
      border: 1px solid rgba(225, 29, 72, 0.3);
      white-space: nowrap;
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
      white-space: nowrap;
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
      .grid-2, .grid-3, .grid-4, .grid-1-2, .grid-2-1 {
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
  </style>
</head>
<body class="slide-mode theme-light">

  <!-- 顶部导航栏 -->
  <header class="header-nav no-print">
    <div class="brand">
      <span class="brand-badge">Intelligence Deck</span>
      <span class="brand-title">AI 时代的「制高点」之战：商业史铁律、数据实证审计与可行性全景批判</span>
    </div>
    <div class="nav-actions">
      <!-- 默认白天模式，支持切换暗黑 -->
      <button class="btn" id="btn-theme-toggle" onclick="toggleTheme()" title="切换白天/暗黑模式 (快捷键 T)">
        <span id="theme-icon">🌙</span>
        <span id="theme-text">暗黑模式</span>
      </button>
      <button class="btn btn-active" id="btn-toggle-view" onclick="toggleViewMode()" title="切换幻灯片/长文模式 (快捷键 M)">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg>
        <span id="view-mode-text">幻灯片模式</span>
      </button>
      <button class="btn" onclick="openDrawer()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        全览目录 (15P)
      </button>
      <button class="btn" onclick="openSourceModal()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        原帖切片 (19P)
      </button>
      <button class="btn" onclick="openLedgerModal()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
        交叉核验台账
      </button>
      <button class="btn" onclick="toggleFullscreen()" title="全屏演示 (快捷键 F)">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
        全屏
      </button>
      <button class="btn btn-primary" onclick="window.print()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
        导出 PDF / 打印
      </button>
    </div>
  </header>

  <!-- 幻灯片与报告主容器 -->
  <main id="deck-container">
__SLIDES_PLACEHOLDER__
  </main>

  <!-- 底部悬浮控制器 -->
  <footer class="deck-controls no-print">
    <button class="btn-icon" onclick="prevSlide()" title="上一页 (←)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
    </button>
    <div class="slide-counter">
      SLIDE <span id="cur-slide-num">01</span> / 15
    </div>
    <div class="progress-bar-wrap">
      <div class="progress-bar-fill" id="progress-bar"></div>
    </div>
    <button class="btn-icon" onclick="nextSlide()" title="下一页 (→)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
    </button>
  </footer>

  <!-- 抽屉导航模态框 -->
  <div class="modal-backdrop" id="drawer-modal" onclick="closeDrawer(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeDrawer()">&times;</button>
      <h3 style="font-size: 20px; color: var(--text-main); margin-bottom: 4px;">📑 研报幻灯片全览导航 (15 Slides)</h3>
      <div style="font-size: 13px; color: var(--text-muted);">点击任意卡片即可直接跳转至对应战略篇章</div>
      <div class="drawer-grid" id="drawer-grid-items"></div>
    </div>
  </div>

  <!-- 原帖图片对照模态框 -->
  <div class="modal-backdrop" id="source-modal" onclick="closeSourceModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeSourceModal()">&times;</button>
      <h3 style="font-size: 20px; color: var(--text-main); margin-bottom: 4px;">🖼️ 小红书原贴 19 张核心长图完整对照</h3>
      <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">点击任意图片可查看高清大图，逐页比对原始素材内容与实证核查结论</div>
      <div class="source-gallery" id="source-gallery-items"></div>
    </div>
  </div>

  <!-- 权威印证台账全屏模态框 -->
  <div class="modal-backdrop" id="ledger-modal" onclick="closeLedgerModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeLedgerModal()">&times;</button>
      <h3 style="font-size: 20px; color: var(--text-main); margin-bottom: 4px;">🔍 全网数据印证与交叉事实核查台账 (Audit Ledger)</h3>
      <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">比对原始报告核心陈述、权威数据来源、学术依据及偏差研判</div>
      <div id="ledger-modal-content"></div>
    </div>
  </div>

__JAVASCRIPT_PLACEHOLDER__
</body>
</html>
"""

print("Template ready, preparing slides data...")
