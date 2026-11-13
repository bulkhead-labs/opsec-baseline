from lib import *

# ======================= Scene 0: the opening hull =======================

def s0():
    sid = "s0"
    cx = [12 + i * 46 for i in range(7)]          # compartment x (42 wide)
    walls = "".join(f'<rect class="s0-wall s0-w{i} only-with" x="{54 + i * 46}" y="20" width="4" height="80"/>' for i in range(6))
    bow = "M334 20 C362.8 20 377.2 41.8 391.6 60 C377.2 78.2 362.8 100 334 100 Z"
    crack = "M113 100 L118 93 L124 101 L130 92 L137 100"
    svg = f'''<svg viewBox="0 0 400 120" role="img" aria-labelledby="s0-alt-with">
<g class="s0-hull">
<rect class="s0-water only-without" x="12" y="20" width="318" height="80"/>
<path class="s0-bowwater only-without" d="{bow}"/>
<rect class="s0-water3 only-with" x="104" y="20" width="42" height="80"/>
{walls}
<rect class="s0-out last-without" x="12" y="20" width="318" height="80" rx="3"/>
<path class="s0-out" d="{bow}"/>
<rect class="s0-c3 only-with last-with" x="104" y="20" width="42" height="80"/>
<path class="s0-crack crack" pathLength="1" d="{crack}"/>
</g></svg>'''
    css('''.s0-water,.s0-water3,.s0-bowwater{fill:var(--bad-tint)}
.s0-water{transform-origin:35.5% 50%}
.s0-water3{transform-origin:50% 50%}
.s0-wall{fill:var(--text);transform-origin:50% 0}
.s0-out{fill:none;stroke:var(--text);stroke-width:2.5;stroke-linejoin:round}
.s0-c3{fill:none;stroke:var(--bad);stroke-width:2.5}
#s0[data-state="without"] .s0-out{stroke:var(--bad)}
#s0[data-state="without"] .s0-hull{opacity:.55}''')
    KF.append("@keyframes s0wall{0%{transform:scaleY(0);fill:var(--accent)}40%{transform:scaleY(1);fill:var(--accent)}100%{fill:var(--text)}}")
    KF.append("@keyframes scalex{from{transform:scaleX(0)}}")
    KF.append("@keyframes s0c3{0%{opacity:0}28%{opacity:1}100%{opacity:1}}")
    # Without, 3.2s
    A(sid, "without", ".s0-crack", a("draw", 300, 400))
    A(sid, "without", ".s0-water", a("scalex", 2000, 700, EI))
    A(sid, "without", ".s0-bowwater", a("in", 500, 2700))
    A(sid, "without", ".s0-out", a("fromstroke", 500, 2700))
    A(sid, "without", ".s0-hull", a("undim", 500, 2700))
    # With, 2.4s
    for i in range(6):
        A(sid, "with", f".s0-w{i}", a("s0wall", 350, i * 60, EO))
    A(sid, "with", ".s0-crack", a("draw", 300, 600))
    A(sid, "with", ".s0-water3", a("scalex", 600, 900, EI))
    A(sid, "with", ".s0-c3", a("s0c3", 900, 1500))
    return svg


# ======================= Scene 1: Wren Street diagram =======================

def s1():
    people = []
    k = 0
    named = {0: "M", 1: "T", 2: "P"}
    for r in range(3):
        for c in range(3):
            x, y = 64 + c * 28, 32 + r * 28
            if k in named:
                people.append(f'<g class="ws-p" style="--i:{k}">{token(x, y, 10, named[k])}</g>')
            else:
                people.append(f'<circle class="ws-p ws-dot" style="--i:{k}" cx="{x}" cy="{y}" r="7"/>')
            k += 1
    tools = []
    k = 0
    for r in range(5):
        for c in range(8):
            tools.append(f'<rect class="ws-t" style="--i:{k}" x="{220 + c * 17}" y="{20 + r * 17}" width="12" height="12" rx="2"/>')
            k += 1
    return (f'<svg class="ws-dia" viewBox="0 0 400 120" role="img" aria-label="Nine people and forty online tools.">'
            + "".join(people) + "".join(tools) + "</svg>")


# ======================= Scene 2: Sign in with Google =======================

def s2():
    sid = "s2"
    names = ["MAIL", "DRIVE", "DOCS", "SALES", "SUPPORT", "CHAT"]
    ys = [36, 76, 116, 156, 196, 236]
    lines = "".join(f'<line class="ln s2-l s2-l{i}" x1="146" y1="160" x2="278" y2="{y + 15}"/>' for i, y in enumerate(ys))
    setb = "".join(f'<line class="atk s2-b s2-b{i} only-without" x1="48" y1="160" x2="278" y2="{ys[i] + 15}"/>' for i in (3, 4, 5))
    tiles = []
    for i, (n, y) in enumerate(zip(names, ys)):
        g = (f'<g class="s2-g only-with"><circle class="gb" cx="358" cy="{y + 15}" r="8"/>'
             f'<text class="gch" x="358" y="{y + 19}" text-anchor="middle">G</text></g>')
        d = "".join(f'<circle class="pw" cx="{352 + j * 6}" cy="{y + 15}" r="1.6"/>' for j in range(3))
        if i < 3:
            badge = g.replace(" only-with", "")
        else:
            badge = f'<g class="only-without">{d}</g>' + g
        tiles.append(f'<g class="s2-t s2-t{i}"><rect class="obj box" x="278" y="{y}" width="96" height="30" rx="6"/>'
                     f'{text(288, y + 20, n, "f13")}{badge}</g>')
    svg = f'''<svg viewBox="0 0 400 300" role="img" aria-labelledby="s2-alt-with">
<rect class="bnd" x="64" y="14" width="326" height="272" rx="12"/>
{text(76, 32, "WREN STREET", "f12 mu")}
<g class="only-with s2-list"><rect class="list" x="80" y="40" width="120" height="66" rx="6"/>
{text(90, 58, "OFFBOARDING", "f13 mu")}
<rect class="box10" x="90" y="67" width="10" height="10" rx="1"/>{text(108, 77, "SALES", "f13")}
<path class="tick s2-k1" pathLength="1" d="M91.5 72 L94.5 75 L99 68.5"/>
<rect class="box10" x="90" y="86" width="10" height="10" rx="1"/>{text(108, 96, "CHAT", "f13")}
<path class="tick s2-k2" pathLength="1" d="M91.5 91 L94.5 94 L99 87.5"/></g>
{lines}{setb}
{"".join(tiles)}
<g class="s2-lead">{anon(32, 160)}
{text(32, 192, "SALES", "f12 mu", "middle")}{text(32, 206, "LEAD", "f12 mu", "middle")}
{text(32, 224, "LAST DAY", "f12 s2-day", "middle")}{text(32, 224, "LEFT", "f12 s2-left", "middle")}</g>
<circle class="ring s2-ring" cx="96" cy="250" r="18"/>
{token(96, 250, 14, "P")}
<g class="sw s2-sw"><rect class="sw-t" x="124" y="240" width="40" height="20" rx="10"/><circle class="sw-k" cx="134" cy="250" r="7"/></g>
{text(124, 280, "COMPANY ACCOUNT", "f12")}{text(172, 254, "ON", "f12 s2-on")}{text(172, 254, "OFF", "f12 s2-off")}
{check(64, 160, 11, "s2-ck only-with")}
{text(278, 280, "STILL OPEN", "f13 bd s2-open only-without last-without")}
{text(278, 280, "ALL CLOSED", "f13 okc s2-closed only-with last-with")}
</svg>'''
    css('''.s2-l{opacity:0}
#s2 .s2-t0,#s2 .s2-t1,#s2 .s2-t2{opacity:.3}
#s2[data-state="without"] :is(.s2-t3,.s2-t4,.s2-t5) .box{stroke:var(--bad);fill:var(--bad-tint)}
#s2[data-state="with"] :is(.s2-t3,.s2-t4,.s2-t5){opacity:.3}
.s2-day,.s2-on{opacity:0}
.s2-sw .sw-t{fill:var(--line)}
.s2-sw .sw-k{fill:var(--surface);stroke:var(--muted);stroke-width:1}''')
    KF.append("@keyframes s2track{from{fill:var(--accent)}}")
    for st in ("without", "with"):
        A(sid, st, ".s2-ring", a("in", 160, 300))
        A(sid, st, ".s2-sw .sw-k", mv(20, 0, 240, 460))
        A(sid, st, ".s2-sw .sw-t", a("s2track", 240, 460))
        A(sid, st, ".s2-on", a("out", 150, 460))
        A(sid, st, ".s2-off", a("in", 150, 560))
    # Without, 3.4s
    for i in range(3):
        A(sid, "without", f".s2-t{i}", a("undim", 250, 700 + i * 60))
        A(sid, "without", f".s2-l{i}", a("out", 250, 700 + i * 60))
    A(sid, "without", ".s2-lead", mv(98, 0, 450, 1250))
    A(sid, "without", ".s2-day", a("out", 150, 1500))
    A(sid, "without", ".s2-left", a("in", 150, 1500))
    A(sid, "without", ".s2-l3,.s2-l4,.s2-l5", a("out", 250, 1250))
    for k, i in enumerate((3, 4, 5)):
        A(sid, "without", f".s2-b{i}", a("wr", 500, 1700 + k * 80, EO))
        A(sid, "without", f".s2-t{i} .box", a("fromplain", 250, 2150 + k * 80))
    A(sid, "without", ".s2-open", a("in", 300, 2500))
    # With, 3.9s
    for k, i in enumerate((0, 1, 2, 4)):
        A(sid, "with", f".s2-t{i}", a("undim", 250, 700 + k * 60))
        A(sid, "with", f".s2-l{i}", a("out", 250, 700 + k * 60))
    A(sid, "with", ".s2-k1", a("draw", 160, 1300))
    A(sid, "with", ".s2-t3", a("undim", 300, 1550))
    A(sid, "with", ".s2-l3", a("out", 300, 1550))
    A(sid, "with", ".s2-k2", a("draw", 160, 2000))
    A(sid, "with", ".s2-t5", a("undim", 300, 2250))
    A(sid, "with", ".s2-l5", a("out", 300, 2250))
    A(sid, "with", ".s2-lead", mv(98, 0, 450, 2700))
    A(sid, "with", ".s2-day", a("out", 150, 2950))
    A(sid, "with", ".s2-left", a("in", 150, 2950))
    A(sid, "with", ".s2-ck", a("pop", 160, 3300, EO))
    A(sid, "with", ".s2-closed", a("in", 400, 3500))
    return svg
