import os

# Create assets directory
os.makedirs('assets', exist_ok=True)

# 1. header-animation.svg
header_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="850" height="200" viewBox="0 0 850 200">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&amp;family=Inter:wght@900&amp;display=swap');
      .title { font-family: 'Inter', sans-serif; font-size: 55px; font-weight: 900; fill: #ffffff; text-anchor: middle; }
      .subtitle { font-family: 'Fira Code', monospace; font-size: 22px; font-weight: 700; fill: #c481ff; text-anchor: middle; letter-spacing: 2px; }
      .glow { filter: drop-shadow(0 0 10px rgba(196, 129, 255, 0.8)); }
      
      @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
      }
      .animated { animation: float 4s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="100%" height="100%" fill="transparent"/>
  <g class="animated">
    <text x="425" y="90" class="title glow">SANDIPAN CHAKRABORTY</text>
    <text x="425" y="140" class="subtitle">AI BACKEND &amp; SYSTEMS ENGINEER</text>
  </g>
</svg>"""
with open('assets/header-animation.svg', 'w', encoding='utf-8') as f: f.write(header_svg)

# 2. terminal-intro.svg
terminal_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="700" height="250" viewBox="0 0 700 250">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&amp;display=swap');
      .term-bg { fill: #0d1117; stroke: #30363d; stroke-width: 1; rx: 10; ry: 10; }
      .term-header { fill: #161b22; }
      .btn-r { fill: #ff5f56; } .btn-y { fill: #ffbd2e; } .btn-g { fill: #27c93f; }
      .txt { font-family: 'Fira Code', monospace; font-size: 15px; fill: #c9d1d9; }
      .prompt { fill: #79c0ff; font-weight: 600; }
      .highlight { fill: #c481ff; font-weight: 600; }
      .comment { fill: #8b949e; font-style: italic; }
      
      @keyframes type1 { 0% { opacity: 0; } 10% { opacity: 1; } 100% { opacity: 1; } }
      @keyframes type2 { 0% { opacity: 0; } 40% { opacity: 1; } 100% { opacity: 1; } }
      @keyframes type3 { 0% { opacity: 0; } 70% { opacity: 1; } 100% { opacity: 1; } }
      .line1 { animation: type1 5s infinite; }
      .line2 { animation: type2 5s infinite; }
      .line3 { animation: type3 5s infinite; }
    </style>
  </defs>
  <rect x="10" y="10" width="680" height="230" class="term-bg"/>
  <path d="M10 20 C10 14.477 14.477 10 20 10 L680 10 C685.523 10 690 14.477 690 20 L690 40 L10 40 Z" class="term-header"/>
  <circle cx="30" cy="25" r="6" class="btn-r"/>
  <circle cx="50" cy="25" r="6" class="btn-y"/>
  <circle cx="70" cy="25" r="6" class="btn-g"/>
  <text x="350" y="29" font-family="'Fira Code', monospace" font-size="12" fill="#8b949e" text-anchor="middle">sid0803@macbook ~ zsh</text>
  
  <g transform="translate(30, 80)">
    <g class="line1">
      <text y="0" class="txt"><tspan class="prompt">?</tspan> <tspan class="highlight">~</tspan> ./whoami.sh</text>
      <text y="30" class="txt">Loading AI Backend Engineer profile...</text>
    </g>
    <g class="line2">
      <text y="70" class="txt"><tspan class="prompt">?</tspan> <tspan class="highlight">~</tspan> cat status.txt</text>
      <text y="100" class="txt">Architecting low-latency AI pipelines (<tspan class="highlight">&lt; 200ms p95</tspan>)</text>
      <text y="125" class="txt">and distributed systems that scale.</text>
    </g>
    <g class="line3">
      <text y="165" class="txt"><tspan class="prompt">?</tspan> <tspan class="highlight">~</tspan> <tspan class="comment">¦</tspan></text>
    </g>
  </g>
</svg>"""
with open('assets/terminal-intro.svg', 'w', encoding='utf-8') as f: f.write(terminal_svg)

# 3. divider.svg
divider_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="10" viewBox="0 0 900 10">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#c481ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0d1117;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="900" height="2" y="4" fill="url(#grad)" rx="1"/>
</svg>"""
with open('assets/divider.svg', 'w', encoding='utf-8') as f: f.write(divider_svg)

# Function to create section headers
def create_section(filename, icon, text):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="300" height="40" viewBox="0 0 300 40">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@800&amp;display=swap');
      .txt {{ font-family: 'Inter', sans-serif; font-size: 20px; font-weight: 800; fill: #ffffff; letter-spacing: 1px; }}
      .icon {{ font-size: 22px; }}
    </style>
  </defs>
  <text x="0" y="28" class="icon">{icon}</text>
  <text x="35" y="26" class="txt">{text}</text>
</svg>"""
    with open(f'assets/{filename}.svg', 'w', encoding='utf-8') as f: f.write(svg)

create_section('section-about', '??', 'ABOUT ME')
create_section('section-trophy', '??', 'ACHIEVEMENTS')
create_section('section-stats', '??', 'GITHUB ANALYTICS')
create_section('section-tech', '?', 'TECH STACK')
create_section('section-connect', '??', 'CONNECT WITH ME')

# Footer
footer_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="100" viewBox="0 0 800 100">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@600&amp;display=swap');
      .txt { font-family: 'Fira Code', monospace; font-size: 16px; font-weight: 600; fill: #8b949e; text-anchor: middle; }
      .heart { fill: #ff5f56; animation: beat .5s infinite alternate; transform-origin: center; }
      @keyframes beat{ to { transform: scale(1.2); } }
    </style>
  </defs>
  <text x="400" y="50" class="txt">Built with <tspan class="heart">??</tspan> by Sandipan Chakraborty</text>
</svg>"""
with open('assets/footer.svg', 'w', encoding='utf-8') as f: f.write(footer_svg)

print("SVGs generated successfully.")
