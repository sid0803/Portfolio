import os

os.makedirs('assets', exist_ok=True)

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
    with open(f'assets/{filename}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

create_section('section-about', '👤', 'ABOUT ME')
create_section('section-trophy', '🏆', 'ACHIEVEMENTS')
create_section('section-stats', '📊', 'GITHUB ANALYTICS')
create_section('section-tech', '⚡', 'TECH STACK')
create_section('section-connect', '🌐', 'CONNECT WITH ME')
create_section('section-game', '🎮', 'CONTRIBUTIONS')

footer = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="100" viewBox="0 0 800 100">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@600&amp;display=swap');
      .txt { font-family: 'Fira Code', monospace; font-size: 16px; font-weight: 600; fill: #8b949e; text-anchor: middle; }
      .heart { fill: #ff5f56; animation: beat .5s infinite alternate; transform-origin: center; }
      @keyframes beat{ to { transform: scale(1.2); } }
    </style>
  </defs>
  <text x="400" y="50" class="txt">Built with <tspan class="heart">❤️</tspan> by Sandipan Chakraborty</text>
</svg>"""
with open('assets/footer.svg', 'w', encoding='utf-8') as f:
    f.write(footer)

print("Generated successfully.")
