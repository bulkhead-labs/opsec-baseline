from lib import *

# ======================= Scene 5: Separate admin accounts =======================

def gear(cx, cy):
    """A plain cog: eight square teeth and a hole."""
    import math
    pts = []
    for k in range(8):
        a = k * math.pi / 4
        for da, r in ((-0.36, 9), (-0.2, 12.5), (0.2, 12.5), (0.36, 9)):
            pts.append(f"{cx + r * math.cos(a + da):.1f} {cy + r * math.sin(a + da):.1f}")
    d = "M" + " L".join(pts) + " Z"
    return (f'<g class="gear s5-q s5-q9"><path d="{d}"/>'
            f'<circle class="gear-h" cx="{cx}" cy="{cy}" r="3.5"/></g>')


def s5():
    sid = "s5"
    sq = []
    k = 0
    for r in range(3):
        for c in range(3):
            sq.append(f'<rect class="obj acct s5-q s5-q{k}" x="{242 + c * 24}" y="{54 + r * 24}" width="18" height="18" rx="3"/>')
            k += 1
    svg = f'''<svg viewBox="0 0 400 300" role="img" aria-labelledby="s5-alt-with">
<line class="atk s5-in" x1="2" y1="58" x2="24" y2="58"/>
<rect class="obj s5-maya" x="24" y="40" width="120" height="36" rx="6"/>
<text class="f14 lc" x="34" y="63">maya@</text>
<g class="only-without"><rect class="badge" x="104" y="32" width="46" height="16" rx="3"/>{text(127, 44, "ADMIN", "f11 onfill", "middle")}</g>
{text(24, 92, "MAYA · EVERYDAY", "f12 mu")}
<g class="only-with"><rect class="chipr" x="24" y="100" width="106" height="18" rx="3"/>{text(77, 113, "MAIL AND DOCS", "f11", "middle")}</g>
<line class="ln" x1="144" y1="58" x2="232" y2="58"/>
<line class="badln s5-o1 only-without" pathLength="1" x1="144" y1="58" x2="232" y2="58"/>
<line class="badln s5-o2 only-with" pathLength="1" x1="144" y1="58" x2="184" y2="58"/>
<rect class="bnd" x="232" y="24" width="150" height="130" rx="12"/>
{text(244, 44, "EVERY ACCOUNT", "f12 mu")}
{"".join(sq)}
{gear(350, 84)}{text(350, 114, "SETTINGS", "f12", "middle")}
<g class="only-without">
<g class="s5-n1"><rect class="newq" x="252" y="164" width="18" height="18" rx="3"/>{text(261, 196, "NEW?", "f11 bd", "middle")}</g>
<g class="s5-n2 last-without"><rect class="newq" x="300" y="164" width="18" height="18" rx="3"/>{text(309, 196, "NEW?", "f11 bd", "middle")}</g></g>
<g class="only-with">
<rect class="glowr s5-glow" x="176" y="24" width="24" height="70"/>
<rect class="wallbar" x="184" y="24" width="8" height="70"/>
{check(382, 24, 11, "s5-ck")}
<path class="adminpath" d="M340 214 H368 V154"/><circle class="adminend" cx="368" cy="154" r="3"/>
<rect class="obj safe s5-safe" x="60" y="162" width="280" height="130" rx="8"/>
<rect class="safe-door s5-door" x="68" y="170" width="264" height="114" rx="4"/>
<circle class="dial" cx="322" cy="227" r="9"/><line class="dial-t" x1="322" y1="227" x2="322" y2="220"/>
{text(78, 186, "ADMIN ACCOUNTS", "f12 mu")}
{text(78, 206, "MAYA · ADMIN", "f12")}{keyglyph(200, 199, "s5-k1")}
{text(78, 226, "THEO · ADMIN", "f12")}{keyglyph(200, 219, "s5-k2")}
{text(78, 246, "SPARE", "f12")}{keyglyph(200, 239, "s5-k3")}
<line class="thin" x1="250" y1="235" x2="250" y2="251"/>{keyglyph(282, 239, "s5-k4")}
{text(78, 262, "BREAK-GLASS · 2 KEYS, 2 PLACES", "f12 mu s5-t1")}
{text(78, 276, "TESTED QUARTERLY", "f12 mu s5-t2 last-with")}
</g>
</svg>'''
    css('''#s5 .s5-maya{stroke:var(--bad);fill:var(--bad-tint)}
.badge{fill:var(--text)}.onfill{fill:var(--surface)}
.chipr{fill:var(--bg);stroke:var(--text);stroke-width:1.5}
.badln{stroke:var(--bad);stroke-width:2.5;stroke-dasharray:1;stroke-linecap:round}
.gear{fill:var(--bg);stroke:var(--text);stroke-width:2;stroke-linejoin:round}
.gear-h{fill:var(--surface)}
.adminpath{fill:none;stroke:var(--text);stroke-width:1.5}
.adminend{fill:var(--text)}
#s5[data-state="without"] .acct{stroke:var(--bad);fill:var(--bad-tint)}
#s5[data-state="without"] .gear{stroke:var(--bad);fill:var(--bad-tint)}
.newq{fill:none;stroke:var(--bad);stroke-width:1.5;stroke-dasharray:3 3}
.glowr{fill:var(--accent-tint);opacity:0}
.wallbar{fill:var(--accent)}
.safe{stroke-width:3}
.kg-glow{fill:var(--accent-tint);opacity:0}''')
    KF.append("@keyframes s5door{0%{stroke:var(--line)}50%{stroke:var(--accent)}100%{stroke:var(--line)}}")
    for st in ("without", "with"):
        A(sid, st, ".s5-in", a("wr", 350, 300, EO))
        A(sid, st, ".s5-maya", a("fromplain", 250, 600))
    # Without, 3.4s
    A(sid, "without", ".s5-o1", a("draw", 400, 900, EO))
    for k in range(10):
        A(sid, "without", f".s5-q{k}", a("fromplain", 250, 1300 + k * 110))
    A(sid, "without", ".s5-n1", a("in", 300, 2600))
    A(sid, "without", ".s5-n2", a("in", 300, 2900))
    # With, 4.2s
    A(sid, "with", ".s5-o2", a("draw", 300, 900, EO))
    A(sid, "with", ".s5-glow", a("flash", 250, 1200))
    A(sid, "with", ".s5-ck", a("pop", 160, 1500, EO))
    A(sid, "with", ".s5-door", a("s5door", 400, 1900))
    for k, t in enumerate((1950, 2350, 2750, 3050)):
        A(sid, "with", f".s5-k{k + 1} .kg-glow", a("flash", 350, t))
    A(sid, "with", ".s5-t1", a("in", 600, 3300))
    A(sid, "with", ".s5-t2", a("in", 600, 3600))
    return svg


# ======================= Scene 6: Admin audit =======================

ROWS = ["GOOGLE", "CODE", "CHAT", "CLOUD", "PAYMENTS", "DOMAIN", "SUPPORT", "SALES", "DESIGN"]
SEATS = [[0, 1], [0, 1, 2, 5], [0, 1, 2, 4, 6], [0, 2, 6], [0, 1, 2, 9], [0, 1, 2], [1, 2, 3], [0, 2, 4], [0, 1, 2, 3]]
KEEP = [[0, 1], [1, 2], [0, 2], [0, 2], [0, 2], [0, 2], [1, 2], [0, 2], [1, 2]]


def s6():
    sid = "s6"
    col = lambda c: 128 + c * 26
    rowy = lambda r: 80 + r * 24
    heads = [token(col(0), 56, 9, "M"), token(col(1), 56, 9, "T"), token(col(2), 56, 9, "P")]
    heads += [f'<circle class="mdot" cx="{col(c)}" cy="56" r="4"/>' for c in range(3, 9)]
    labels = "".join(text(16, rowy(r) + 5, n, "f13" + (" s6-pl" if n == "PAYMENTS" else "")) for r, n in enumerate(ROWS))
    dots, n = [], 0
    removed = []
    for r, cols in enumerate(SEATS):
        for c in cols:
            keep = c in KEEP[r]
            cls = "s6-ex" if c == 9 else ""
            inner = f'<circle class="dot s6-d{n} {cls}" cx="{col(c)}" cy="{rowy(r)}" r="6"/>'
            if keep:
                dots.append(inner)
            else:
                removed.append((r, c, n))
                dots.append(f'<g class="rm s6-r{n}">{inner}</g>')
            n += 1
    assert n == 31 and len(removed) == 13
    # removal order: the ex-contractor first, then the rest in reading order
    removed.sort(key=lambda x: (x[1] != 9, x[0], x[1]))
    checks = "".join(check(388, rowy(r), 7, f"s6-ck s6-ck{r} only-with") for r in range(9))
    svg = f'''<svg viewBox="0 0 400 300" role="img" aria-labelledby="s6-alt-with">
<rect class="s6-band only-without last-without" x="8" y="{rowy(4) - 12}" width="384" height="24" rx="4"/>
<rect class="obj" x="16" y="12" width="92" height="26" rx="6"/>{text(62, 30, "ASSISTANT", "f13", "middle")}
<circle class="ring s6-ring only-with" cx="130" cy="25" r="16"/>
{token(130, 25, 12, "P")}{text(150, 30, "PRIYA", "f12")}
<text class="s6-count" x="388" y="31" text-anchor="end"><tspan class="c31 only-with">31 → </tspan><tspan class="cnum">18</tspan><tspan class="f12" dx="6">ADMIN SEATS</tspan></text>
{text(388, 46, "NEXT LOOK: APRIL", "f12 okc s6-next only-with last-with", "end")}
{"".join(heads)}
<g class="s6-col10"><circle class="exhead" cx="{col(9)}" cy="56" r="6"/>{text(392, 292, "EX-CONTRACTOR", "f12 bd", "end")}</g>
{cross(col(9), 56, 7, "s6-exx only-with")}
{labels}
<circle class="s6-exring only-without" cx="{col(9)}" cy="{rowy(4)}" r="10"/>
<line class="atk s6-atk only-without" x1="398" y1="{rowy(4)}" x2="370" y2="{rowy(4)}"/>
{"".join(dots)}
{checks}
</svg>'''
    css('''.dot{fill:var(--text)}
.mdot{fill:var(--muted)}
.exhead{fill:none;stroke:var(--bad);stroke-width:1.5;stroke-dasharray:3 2}
.s6-count .cnum,.s6-count .c31{font-family:var(--f-head);font-weight:800;font-size:22px;letter-spacing:0}
#s6[data-state="without"] .s6-ex{fill:var(--bad)}
.s6-exring{fill:var(--bad-tint)}
.s6-band{fill:var(--bad-tint)}
#s6[data-state="without"] .s6-pl{fill:var(--bad)}
#s6[data-state="with"] .rm .dot{fill:transparent;stroke:var(--line);stroke-width:2}''')
    KF.append("@keyframes shrink{0%{fill:var(--text);stroke-width:0;transform:scale(1)}45%{fill:var(--text);stroke-width:0;transform:scale(.4)}46%{fill:transparent;stroke-width:2;transform:scale(.4)}}")
    KF.append("@keyframes fin{from{fill-opacity:0}}")
    # Without, 3.6s
    ex = [n for (r, c, n) in removed if c == 9][0]
    for i in range(31):
        if i != ex:
            A(sid, "without", f".s6-d{i}", a("pop", 160, 200 + i * 50, EO))
    A(sid, "without", ".s6-ex", a("pop", 160, 200 + ex * 50, EO), a("fromtext", 250, 1900))
    A(sid, "without", ".s6-exring", a("in", 400, 1900))
    A(sid, "without", ".s6-atk", a("wl", 500, 2400, EO))
    A(sid, "without", ".s6-band", a("in", 700, 2900))
    A(sid, "without", ".s6-pl", a("fromtext", 250, 2900))
    # With, 4.4s
    cut = {n: 1500 + k * 140 for k, (r, c, n) in enumerate(removed)}
    for i in range(31):
        if i in cut:  # shrink listed first so the pop owns the transform while it runs
            A(sid, "with", f".s6-d{i}", a("shrink", 300, cut[i]), a("pop", 160, i * 30, EO))
        else:
            A(sid, "with", f".s6-d{i}", a("pop", 160, i * 30, EO))
    A(sid, "with", ".s6-ring", a("in", 300, 1100))
    A(sid, "with", ".c31", a("fin", 250, 1500))
    A(sid, "with", ".s6-exx", a("pop", 160, 1600, EO))
    for r in range(9):
        A(sid, "with", f".s6-ck{r}", a("pop", 160, 3400 + r * 40, EO))
    A(sid, "with", ".s6-next", a("in", 500, 3900))
    return svg
