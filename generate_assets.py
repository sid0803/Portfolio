import os

# Create assets directory
os.makedirs('assets', exist_ok=True)

# Colors (Tokyonight + Cyberpunk)
BG = "transparent" # Or "#0d1117"
PURPLE = "#c481ff"
BLUE = "#79c0ff"
GREEN = "#27c93f"
RED = "#ff5f56"
YELLOW = "#ffbd2e"
TEXT = "#c9d1d9"
COMMENT = "#8b949e"

# 1. header-animation.svg
header_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="850" height="220" viewBox="0 0 850 220">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&amp;family=Outfit:wght@800;900&amp;display=swap');
      .title {{ font-family: 'Outfit', sans-serif; font-size: 58px; font-weight: 900; fill: #ffffff; text-anchor: middle; }}
      .subtitle {{ font-family: 'Fira Code', monospace; font-size: 20px; font-weight: 700; fill: {PURPLE}; text-anchor: middle; letter-spacing: 3px; }}
      .glow {{ filter: drop-shadow(0 0 15px rgba(196, 129, 255, 0.9)); }}
      .blue-glow {{ filter: drop-shadow(0 0 10px rgba(121, 192, 255, 0.7)); }}
      
      @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-8px); }}
      }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 0.8; transform: scale(1); }}
        50% {{ opacity: 1; transform: scale(1.05); }}
      }}
      .animated-text {{ animation: float 5s ease-in-out infinite; }}
      .pulse-obj {{ animation: pulse 4s ease-in-out infinite; transform-origin: center; }}
    </style>
    <radialGradient id="orb1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{PURPLE}" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="{PURPLE}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="orb2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="{BLUE}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  
  <rect width="100%" height="100%" fill="{BG}"/>
  
  <!-- Animated Background Orbs -->
  <circle cx="200" cy="110" r="180" fill="url(#orb1)" class="pulse-obj">
    <animate attributeName="cx" values="100;750;100" dur="20s" repeatCount="indefinite" />
  </circle>
  <circle cx="650" cy="110" r="150" fill="url(#orb2)" class="pulse-obj">
    <animate attributeName="cx" values="750;100;750" dur="25s" repeatCount="indefinite" />
    <animate attributeName="cy" values="50;180;50" dur="15s" repeatCount="indefinite" />
  </circle>

  <!-- Foreground Text -->
  <g class="animated-text">
    <text x="425" y="110" class="title glow">SANDIPAN CHAKRABORTY</text>
    <text x="425" y="155" class="subtitle blue-glow">AI BACKEND &amp; SYSTEMS ENGINEER</text>
  </g>
</svg>"""
with open('assets/header-animation.svg', 'w', encoding='utf-8') as f: f.write(header_svg)

# 2. terminal-intro.svg
terminal_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="750" height="280" viewBox="0 0 750 280">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&amp;display=swap');
      .term-bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 12; ry: 12; }}
      .term-header {{ fill: #161b22; rx: 12; ry: 12; }}
      .btn-r {{ fill: {RED}; }} .btn-y {{ fill: {YELLOW}; }} .btn-g {{ fill: {GREEN}; }}
      .txt {{ font-family: 'Fira Code', monospace; font-size: 15px; fill: {TEXT}; font-weight: 500; }}
      .prompt {{ fill: {GREEN}; font-weight: 700; }}
      .server {{ fill: {BLUE}; font-weight: 700; }}
      .cmd {{ fill: {PURPLE}; font-weight: 700; }}
      .arg {{ fill: #ff9e64; }}
      .comment {{ fill: {COMMENT}; font-style: italic; }}
      .cursor {{ fill: {PURPLE}; animation: blink 1s step-end infinite; }}
      
      @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
      @keyframes type1 {{ 0% {{ opacity: 0; }} 5% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
      @keyframes type2 {{ 0% {{ opacity: 0; }} 30% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
      @keyframes type3 {{ 0% {{ opacity: 0; }} 65% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
      
      .line1 {{ animation: type1 8s infinite; }}
      .line2 {{ animation: type2 8s infinite; }}
      .line3 {{ animation: type3 8s infinite; }}
    </style>
  </defs>
  
  <rect x="5" y="5" width="740" height="270" class="term-bg"/>
  <path d="M5 17 C5 10.373 10.373 5 17 5 L733 5 C739.627 5 745 10.373 745 17 L745 40 L5 40 Z" class="term-header"/>
  
  <circle cx="25" cy="22" r="6" class="btn-r"/>
  <circle cx="45" cy="22" r="6" class="btn-y"/>
  <circle cx="65" cy="22" r="6" class="btn-g"/>
  <text x="375" y="27" font-family="'Fira Code', monospace" font-size="13" fill="{COMMENT}" text-anchor="middle">sid0803@ai-core ~ zsh</text>
  
  <g transform="translate(25, 80)">
    <g class="line1">
      <text y="0" class="txt"><tspan class="prompt">sid0803</tspan>@<tspan class="server">ai-core</tspan> ~ <tspan class="cmd">python3</tspan> <tspan class="arg">init_pipeline.py</tspan></text>
      <text y="30" class="txt comment">[INFO] Booting neural interface...</text>
      <text y="55" class="txt comment">[INFO] Establishing sub-200ms latency connections...</text>
      <text y="80" class="txt" fill="{GREEN}">[SUCCESS] AI Backend Node Active.</text>
    </g>
    
    <g class="line2">
      <text y="130" class="txt"><tspan class="prompt">sid0803</tspan>@<tspan class="server">ai-core</tspan> ~ <tspan class="cmd">cat</tspan> <tspan class="arg">status.log</tspan></text>
      <text y="160" class="txt">Currently architecting <tspan fill="{PURPLE}" font-weight="700">production voice AI systems</tspan></text>
      <text y="185" class="txt">and scaling <tspan fill="{BLUE}" font-weight="700">distributed microservices</tspan>.</text>
    </g>
    
    <g class="line3">
      <text y="235" class="txt"><tspan class="prompt">sid0803</tspan>@<tspan class="server">ai-core</tspan> ~ <tspan class="cursor">█</tspan></text>
    </g>
  </g>
</svg>"""
with open('assets/terminal-intro.svg', 'w', encoding='utf-8') as f: f.write(terminal_svg)

# 3. divider.svg
divider_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="20" viewBox="0 0 900 20">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:1" />
      <stop offset="15%" style="stop-color:{BLUE};stop-opacity:1" />
      <stop offset="50%" style="stop-color:{PURPLE};stop-opacity:1" />
      <stop offset="85%" style="stop-color:{BLUE};stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0d1117;stop-opacity:1" />
    </linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="3" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <style>
      .dash {{ stroke-dasharray: 10, 10; animation: dashAnim 20s linear infinite; }}
      @keyframes dashAnim {{ from {{ stroke-dashoffset: 1000; }} to {{ stroke-dashoffset: 0; }} }}
    </style>
  </defs>
  <line x1="0" y1="10" x2="900" y2="10" stroke="url(#grad)" stroke-width="2" class="dash" filter="url(#glow)" />
</svg>"""
with open('assets/divider.svg', 'w', encoding='utf-8') as f: f.write(divider_svg)

# 4. Section Headers
def create_section(filename, icon, text):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="350" height="50" viewBox="0 0 350 50">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&amp;display=swap');
      .txt {{ font-family: 'Fira Code', monospace; font-size: 22px; font-weight: 700; fill: #ffffff; letter-spacing: 1px; }}
      .bracket {{ fill: {PURPLE}; }}
      .icon {{ font-size: 24px; }}
      .glow {{ filter: drop-shadow(0 0 8px rgba(196, 129, 255, 0.6)); }}
    </style>
  </defs>
  <text x="5" y="35" class="txt glow">
    <tspan class="bracket">[</tspan> {icon} {text} <tspan class="bracket">]</tspan>
  </text>
</svg>"""
    with open(f'assets/{{filename}}.svg', 'w', encoding='utf-8') as f: f.write(svg)

create_section('section-about', '👤', 'ABOUT_ME')
create_section('section-trophy', '🏆', 'ACHIEVEMENTS')
create_section('section-stats', '📊', 'GITHUB_ANALYTICS')
create_section('section-tech', '⚡', 'TECH_STACK')
create_section('section-connect', '🌐', 'CONNECT')

# Footer
footer_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="100" viewBox="0 0 800 100">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@500;700&amp;display=swap');
      .txt {{ font-family: 'Fira Code', monospace; font-size: 16px; font-weight: 500; fill: {COMMENT}; text-anchor: middle; }}
      .highlight {{ fill: {PURPLE}; font-weight: 700; }}
      .heart {{ fill: {RED}; animation: beat 1s infinite alternate; transform-origin: center; display: inline-block; }}
      @keyframes beat{{ 0% {{ transform: scale(1); }} 100% {{ transform: scale(1.3); }} }}
    </style>
  </defs>
  <text x="400" y="50" class="txt">SYSTEM ARCHITECTED WITH <tspan class="heart">❤</tspan> BY <tspan class="highlight">SANDIPAN</tspan></text>
</svg>"""
with open('assets/footer.svg', 'w', encoding='utf-8') as f: f.write(footer_svg)

print("Premium SVGs generated successfully.")
