from lib import *

# ======================= Scene 5: Separate admin accounts =======================
# Two accounts side by side, and what each can do.

DOMAIN = "wrenstreet.example"   # reserved (RFC 2606): wrenstreet.com is a real, registered domain
ROWS5 = ["MAIL AND LINKS", "DOCS AND TOOLS", "ADD PEOPLE", "CHANGE SETTINGS"]
RY = [136, 158, 180, 202]


def card(x, local, roles, can, cls, under=""):
    """An account card at (x, 36), 176 x 184. roles: [(text, only-class)]; can: per state, which rows it can do."""
    head = (f'{text(x + 12, 62, local, "f16")}{text(x + 12, 80, DOMAIN, "f12 mu s5-dom")}'
            + "".join(text(x + 12, 102, r, "f12 " + c) for r, c in roles)
            + f'<line class="thin" x1="{x + 12}" y1="114" x2="{x + 164}" y2="114"/>')
    rows = ""
    for i, (label, y) in enumerate(zip(ROWS5, RY)):
        for st, rows_can in can.items():
            on = i in rows_can
            mark = (f'<rect class="m-can" x="{x + 14}" y="{y - 8}" width="8" height="8"/>' if on
                    else f'<rect class="m-not" x="{x + 13}" y="{y - 5}" width="10" height="2"/>')
            rows += f'<g class="only-{st}">{mark}{text(x + 30, y, label, "f12" + ("" if on else " mu"))}</g>'
    return f'<g class="{cls}"><rect class="obj card5" x="{x}" y="36" width="176" height="184" rx="6"/>{under}{head}{rows}</g>'


def s5():
    sid = "s5"
    bands = "".join(f'<rect class="band5 s5-b{i}{" only-without" if i >= 2 else ""}" x="10" y="{y - 14}" width="168" height="20"/>'
                    for i, y in enumerate(RY))
    a_card = card(6, "maya@", [("EVERYDAY + ADMIN", "only-without"), ("EVERYDAY", "only-with")],
                  {"without": {0, 1, 2, 3}, "with": {0, 1}}, "s5-a", bands)
    b_card = card(218, "maya-admin@", [("ADMIN ONLY", "")], {"with": {2, 3}}, "s5-bc only-with")
    svg = f'''<svg viewBox="0 0 400 300" role="img" aria-labelledby="s5-alt-with">
{a_card}
<line class="atk s5-atk" x1="94" y1="8" x2="94" y2="36"/>
<g class="only-without"><rect class="ph5" x="218" y="36" width="176" height="184" rx="6"/>
{text(306, 124, "NO ADMIN", "f12 mu", "middle")}{text(306, 142, "ACCOUNT", "f12 mu", "middle")}
{text(8, 250, "THE WHOLE COMPANY", "f13 bd s5-whole last-without")}</g>
{b_card}
<g class="only-with">{keyglyph(360, 95)}
<rect class="glowr s5-glow" x="188" y="36" width="24" height="184"/>
<rect class="wallbar" x="196" y="36" width="8" height="184"/>
<line class="atk s5-hit" x1="182" y1="191" x2="196" y2="191"/>
{check(384, 40, 11, "s5-ck")}
{text(8, 250, "ALSO: theo-admin@", "f12 mu s5-t1")}
{text(8, 270, "BREAK-GLASS: 2 KEYS, 2 PLACES", "f12 mu s5-t2 last-with")}</g>
</svg>'''
    css('''.stage .f16{font-size:17px;font-weight:600}
.stage .s5-dom{letter-spacing:-.03em}
.m-can{fill:var(--text)}.m-not{fill:var(--muted)}
.band5{fill:var(--bad-tint)}
#s5 .s5-a .card5{stroke:var(--bad)}
.ph5{fill:none;stroke:var(--line);stroke-width:1.5;stroke-dasharray:4 4}
.glowr{fill:var(--accent-tint);opacity:0}
.wallbar{fill:var(--accent)}''')
    for st in ("without", "with"):
        A(sid, st, ".s5-atk", a("wd", 400, 300, EO))
        A(sid, st, ".s5-a .card5", a("fromstroke", 250, 700))
        A(sid, st, ".s5-b0", a("in", 250, 1000))
        A(sid, st, ".s5-b1", a("in", 250, 1300))
    # Without, 2.7s: the slip reaches every row, and there is no admin account beside it.
    A(sid, "without", ".s5-b2", a("in", 250, 1600))
    A(sid, "without", ".s5-b3", a("in", 250, 1900))
    A(sid, "without", ".s5-whole", a("in", 400, 2300))
    # With, 3.2s: it reaches mail and docs, then the wall.
    A(sid, "with", ".s5-hit", a("wr", 250, 1650, EO))
    A(sid, "with", ".s5-glow", a("flash", 250, 1900))
    A(sid, "with", ".s5-ck", a("pop", 160, 2250, EO))
    A(sid, "with", ".s5-t1", a("in", 300, 2550))
    A(sid, "with", ".s5-t2", a("in", 300, 2900))
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
{text(16, 292, "NEXT LOOK: APRIL", "f12 okc s6-next only-with last-with")}
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
