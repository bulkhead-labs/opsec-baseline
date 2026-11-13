from lib import *

# ======================= Scene 3: Password manager =======================

# Each pattern is a password: four bars, tall (14) or short (5), on a 60 x 20 chip.
PATTERNS = [
    [(5, 14), (17, 5), (33, 14), (47, 5)],
    [(7, 5), (21, 14), (32, 14), (45, 14)],
    [(4, 14), (15, 14), (28, 5), (48, 14)],
    [(9, 5), (22, 5), (36, 14), (47, 14)],
    [(6, 14), (19, 5), (30, 5), (42, 14)],
]


def pchip(x, y, p, cls=""):
    bars = "".join(f'<rect class="bar" x="{x + ox}" y="{y + 3 + (14 - h)}" width="6" height="{h}" rx="1"/>' for ox, h in PATTERNS[p])
    return f'<g class="pchip {cls}"><rect class="chipbg" x="{x}" y="{y}" width="60" height="20" rx="3"/>{bars}</g>'


YS3 = [30, 88, 146, 204]


def s3():
    sid = "s3"
    sites = ["CLOUD", "PAYMENTS", "CODE", "ANALYTICS"]
    ys = YS3
    tiles = []
    for i, (n, y) in enumerate(zip(sites, ys)):
        tiles.append(
            f'<g class="s3-t s3-t{i}"><rect class="obj box" x="236" y="{y}" width="140" height="48" rx="6"/>'
            f'{text(246, y + 17, n, "f13")}'
            f'{pchip(246, y + 23, 0, "only-without")}{pchip(246, y + 23, i + 1, "only-with")}'
            f'{text(314, y + 39, "OPEN", "f12 bd s3-o s3-o" + str(i) + " only-without")}'
            f'<rect class="door" x="360" y="{y + 8}" width="10" height="32"/></g>')
    crosses = "".join(cross(276, y + 33, 8, f"s3-x s3-x{i} only-with") for i, y in enumerate(ys))
    checks = "".join(check(386, y + 24, 9, f"s3-ck s3-ck{i} only-with" + (" last-with" if i == 3 else "")) for i, y in enumerate(ys))
    vlines = "".join(f'<line class="thin" x1="185" y1="215" x2="236" y2="{y + 24}"/>' for y in ys)
    svg = f'''<svg viewBox="0 0 400 300" role="img" aria-labelledby="s3-alt-with">
<g class="only-with">{vlines}
<rect class="obj s3-safe" x="120" y="200" width="65" height="75" rx="4"/>
<rect class="safe-door" x="124" y="204" width="57" height="67" rx="3"/>
<circle class="dial" cx="172" cy="237.5" r="4.5"/><line class="dial-t" x1="172" y1="237.5" x2="172" y2="234"/>
{text(152.5, 292, "1PASSWORD", "f12", "middle")}</g>
<g class="s3-forum"><rect class="obj box" x="24" y="30" width="120" height="48" rx="6"/>
{text(34, 47, "OLD FORUM", "f13")}{pchip(34, 53, 0)}</g>
<path class="crack s3-crack" pathLength="1" d="M100 76 L108 66 L117 72 L127 60 L136 67 L143 57"/>
{text(24, 96, "BREACHED", "f12 bd s3-br")}
{"".join(tiles)}
{crosses}
<g class="s3-leak last-without">{pchip(246, 227, 0, "leak")}{text(246, 268, "LEAKED", "f12 bd s3-lk")}</g>
{checks}
{token(50, 250, 16, "T")}{text(50, 284, "THEO", "f12", "middle")}
</svg>'''
    css('''.chipbg{fill:var(--sunk)}
.bar{fill:var(--text)}
.leak .chipbg{stroke:var(--bad);stroke-width:1.5}
.door{fill:var(--text);transform-origin:100% 50%}
.s3-safe{stroke:var(--accent);stroke-width:3}
#s3 .s3-forum .box{stroke:var(--bad);fill:var(--bad-tint)}
#s3[data-state="without"] .s3-t .box{stroke:var(--bad);fill:var(--bad-tint)}
#s3[data-state="without"] .door{transform:scaleX(.2)}
#s3[data-state="with"] .s3-leak{transform:translate(-20px,0);opacity:.3}
.s3-x{opacity:0}''')
    KF.append("@keyframes dooropen{from{transform:scaleX(1)}}")
    for st in ("without", "with"):
        A(sid, st, ".s3-crack", a("draw", 500, 300))
        A(sid, st, ".s3-forum .box", a("fromplain", 250, 500))
        A(sid, st, ".s3-br", a("in", 200, 650))
        # leaked chip path, in offsets from its base at (246, 229)
    F, L, W = (-212, -174), (-212, -184), (-66, -174)
    tr = lambda p, o=1: f"transform:translate({p[0]}px,{p[1]}px);opacity:{o};animation-timing-function:{EI}"
    stops = [(0, y + 23 - 227) for y in YS3]
    fr = [(800, tr(F, 0)), (900, tr(L)), (1200, tr(W))]
    arrive = [1450, 1900, 2350, 2800]
    for k, (p, t) in enumerate(zip(stops, arrive)):
        fr.append((t, tr(p)))
        fr.append((t + 200, tr(p)))
    fr.append((3400, tr(stops[-1])))
    A(sid, "without", ".s3-leak", steps("s3leakA", fr))
    A(sid, "without", ".s3-lk", a("in", 200, 3000))
    for k, t in enumerate(arrive):
        A(sid, "without", f".s3-t{k} .door", a("dooropen", 200, t))
        A(sid, "without", f".s3-t{k} .box", a("fromplain", 200, t))
        A(sid, "without", f".s3-o{k}", a("in", 200, t))
    fr = [(800, tr(F, 0)), (900, tr(L)), (1200, tr(W))]
    t = 1200
    xs = []
    for k, p in enumerate(stops):
        fr.append((t + 150, tr(p)))
        xs.append(t + 150)
        fr.append((t + 350, tr((p[0] - 20, p[1]))))
        t += 350
    fr.append((2700, tr((-20, 0))))
    fr.append((3000, f"transform:translate(-20px,0);opacity:.3"))
    A(sid, "with", ".s3-leak", steps("s3leakB", fr))
    A(sid, "with", ".s3-lk", a("in", 300, 2700))
    for k, t in enumerate(xs):
        A(sid, "with", f".s3-x{k}", a("flash", 200, t))
        A(sid, "with", f".s3-ck{k}", a("pop", 160, 3000 + k * 80, EO))
    return svg


# ======================= Scene 4: Hardware key =======================

# The finger: 24 wide, its tip a half-circle of r 12 (half the width), centred just past the pad so the
# rounded end shows over the key body; the finger runs off the stage to the right.
def finger(cx, cy, cls):
    r, tx = 12, cx - 4
    return (f'<g class="rot" transform="rotate(35 {cx} {cy})"><g class="finger {cls}"><path class="fpath" d="M{tx} {cy - r} H{tx + 200} V{cy + r} H{tx} A{r} {r} 0 0 1 {tx} {cy - r} Z"/>'
            f'<rect class="nail" x="{tx - 8}" y="{cy - 6}" width="18" height="12" rx="6"/></g></g>')


def s4():
    sid = "s4"
    dots8 = "".join(f'<circle class="pdot s4-d{i}{" only-without" if i >= 6 else ""}" cx="{44 + i * 12}" cy="105" r="2.5"/>' for i in range(8))
    fake = f'''<g class="s4-fake">
<rect class="pill s4-pill" x="30" y="46" width="200" height="14" rx="6"/>
<text class="f12 s4-addr" x="36" y="57">goog1e-login.example</text>
<line class="s4-ul only-without last-without" pathLength="1" x1="36" y1="61" x2="80" y2="61"/>
<text class="say b" x="34" y="84">Sign in</text>
<g class="s4-field"><rect class="field" x="34" y="96" width="150" height="18" rx="3"/>{dots8}</g>
<text class="say f14 s4-touch only-with" x="34" y="109">Touch your key</text>
<rect class="s4-next" x="34" y="124" width="52" height="18" rx="3"/>
<text class="say f13 s4-nextt" x="60" y="137" text-anchor="middle">Next</text></g>'''
    real = f'''<g class="s4-real only-with">
<rect class="pill s4-pill2" x="30" y="46" width="200" height="14" rx="6"/>
<text class="f12" x="36" y="57">accounts.google.com</text>
<text class="say b" x="34" y="84">Sign in</text>
<text class="say f14 s4-touch2" x="34" y="109">Touch your key</text>
{check(48, 112, 14, "s4-ok")}
<text class="say s4-in last-with" x="70" y="117">Signed in</text></g>'''
    # The key at 1.8x, drawn in its own units: contact 10 x 10, body 46 x 18, touch pad r 6, a small outlined ring hole.
    # In the port: contact over the port at (222, 182), body pointing right. Pad centre on the stage: (268.8, 185.2).
    key = f'''<g class="s4-key only-with"><g class="keyin" transform="translate(222 169) scale(1.8)">
<circle class="key-halo" cx="26" cy="9" r="13"/>
<rect class="key-c" x="0" y="4" width="10" height="10"/>
<rect class="key-b" x="8" y="0" width="46" height="18" rx="5"/>
<circle class="key-h" cx="48" cy="9" r="1.6"/>
<circle class="key-glow" cx="26" cy="9" r="10"/>
<circle class="key-pad" cx="26" cy="9" r="6"/></g>
{text(278, 228, "DAILY", "f12", "middle")}</g>'''
    svg = f'''<svg viewBox="0 0 400 300" role="img" aria-labelledby="s4-alt-with">
<rect class="obj" x="20" y="40" width="220" height="140" rx="6"/>
<path class="topbar" d="M21 46 a5 5 0 0 1 5 -5 h208 a5 5 0 0 1 5 5 v18 h-218 Z"/>
<path class="obj" d="M14 180 H246 L238 192 H22 Z"/>
<rect class="port" x="220" y="182" width="18" height="8" rx="1"/>
{fake}
{real}
<g class="only-without">
<rect class="obj s4-g" x="284" y="40" width="100" height="30" rx="6"/>{text(292, 60, "REAL GOOGLE", "f12")}
<g class="s4-mail"><rect class="obj" x="284" y="100" width="100" height="30" rx="6"/><rect class="tint" x="284" y="100" width="100" height="30" rx="6"/></g>{text(292, 120, "MAYA'S MAIL", "f12")}
<line class="atk s4-a1" x1="240" y1="105" x2="284" y2="55"/>
<g class="s4-pk"><rect class="pk" x="272" y="49" width="24" height="12" rx="6"/>
<circle class="pkd" cx="278" cy="55" r="1.6"/><circle class="pkd" cx="284" cy="55" r="1.6"/><circle class="pkd" cx="290" cy="55" r="1.6"/></g>
<line class="atk s4-a2" x1="238" y1="198" x2="292" y2="70"/>
<line class="ln s4-gm" pathLength="1" x1="334" y1="70" x2="334" y2="100"/>
<line class="atk s4-a3" x1="364" y1="130" x2="364" y2="158"/>
<g class="s4-str"><rect class="badobj" x="344" y="158" width="40" height="22" rx="3"/>
<path class="badobj" d="M338 184 H390"/>{text(392, 202, "A STRANGER", "f12 bd", "end")}</g>
<rect class="obj" x="176" y="198" width="64" height="90" rx="10"/>
<rect class="s4-scr" x="180" y="202" width="56" height="82" rx="7"/>
<rect class="notch" x="201" y="205" width="14" height="3" rx="1"/>
<g class="s4-ask"><text class="say f14" x="208" y="230" text-anchor="middle">Is this</text>
<text class="say f14" x="208" y="246" text-anchor="middle">you?</text>
<rect class="s4-yes" x="188" y="254" width="40" height="18" rx="4"/>
<text class="say f13 s4-yest" x="208" y="267" text-anchor="middle">Yes</text></g>
<circle class="tip s4-tipy" cx="208" cy="263" r="14"/>
</g>
{key}
<g class="only-with">
<g class="s4-tag"><rect class="tagpill" x="250" y="136" width="40" height="22" rx="4"/>
<text class="f14 s4-q" x="270" y="152" text-anchor="middle">?</text>
{cross(270, 147, 7, "s4-tx")}{check(270, 147, 7, "s4-tk")}</g>
<line class="acl s4-acl" pathLength="1" x1="258" y1="136" x2="232" y2="60"/>
{finger(269, 185, "s4-tip1")}
{finger(269, 185, "s4-tip2")}
<g class="s4-card"><rect class="card" x="20" y="220" width="196" height="56" rx="6"/>
<rect class="mini" x="28" y="232" width="40" height="30" rx="3"/><line class="miniline" x1="28" y1="239" x2="68" y2="239"/>
{cross(48, 251, 7)}
{text(76, 244, "LOOK-ALIKE", "f12 mu")}{text(76, 262, "KEY STAYED DARK", "f12 mu")}</g>
</g>
</svg>'''
    css('''.topbar{fill:var(--sunk)}
.pill{fill:var(--surface);stroke:var(--line);stroke-width:1}
#s4[data-state="with"] .pill{stroke:var(--accent);stroke-width:1.5}
#s4[data-state="without"] .s4-addr{fill:var(--bad)}
.s4-ul{stroke:var(--bad);stroke-width:2;stroke-dasharray:1}
.field{fill:var(--sunk)}
.pdot{fill:var(--text)}
.s4-next{fill:var(--text)}.s4-nextt{fill:var(--surface)}
.port{fill:var(--text)}
#s4[data-state="with"] .s4-fake{opacity:0;transform-origin:0 0}
#s4[data-state="with"] .s4-field{opacity:0}
.s4-touch2{opacity:0}
.badobj{fill:var(--bg);stroke:var(--bad);stroke-width:2;stroke-linecap:round}
.tint{fill:var(--bad-tint);stroke:var(--bad);stroke-width:2}
.pk{fill:var(--bg);stroke:var(--bad);stroke-width:1.5}.pkd{fill:var(--bad)}
.s4-pk{opacity:0}
.s4-scr{fill:var(--surface)}
.notch{fill:var(--text)}
.s4-yes{fill:var(--text);stroke:var(--text);stroke-width:1.5}.s4-yest{fill:var(--surface)}
.tip,.fpath{fill:var(--text);fill-opacity:.35}
.fpath{stroke:var(--text);stroke-opacity:.6;stroke-width:1.5;stroke-linejoin:round}.tip,.finger{opacity:0}
.nail{fill:none;stroke:var(--surface);stroke-width:1.5;opacity:.7}
#s4 .keyin,#s4 .rot{transform-box:view-box;transform-origin:0 0}
#s4 .finger{transform-origin:14px 50%}
.key-c{fill:var(--text)}.key-b{fill:var(--accent)}
.key-h{fill:var(--accent);stroke:var(--key-dark);stroke-width:.8}
.key-pad{fill:var(--key-lit);stroke:var(--key-dark);stroke-width:.6}
.key-glow{fill:var(--key-glow)}
.key-halo{fill:var(--accent);opacity:.3}
.tagpill{fill:var(--accent-tint);stroke:var(--accent);stroke-width:1.5}
.s4-q,.s4-tx{opacity:0}
#s4 .s4-q{fill:var(--text);font-family:var(--f-mono);font-size:14px;font-weight:600}
.acl{fill:none;stroke:var(--accent);stroke-width:1.5;stroke-dasharray:1}
.card{fill:var(--bg);stroke:var(--line);stroke-width:1.5}
.mini{fill:var(--surface);stroke:var(--muted);stroke-width:1.5}.miniline{stroke:var(--muted);stroke-width:1.5}''')
    # A press: the fingertip arrives, presses in (scale 1 -> .9), holds, lets go, leaves.
    def press(t_in, t_press, t_release, t_out):
        return [(t_in - 200, f"opacity:0;transform:translate(60px,0);animation-timing-function:{EO}"),
                (t_in, f"opacity:1;transform:translate(0,0);animation-timing-function:{EI}"),
                (t_press, "opacity:1;transform:scale(.9)"),
                (t_release, f"opacity:1;transform:scale(.9);animation-timing-function:{EI}"),
                (t_release + 100, "opacity:1;transform:scale(1)"),
                (t_out, "opacity:0;transform:translate(60px,0)")]
    # Without, 3.8s
    for i in range(8):
        A(sid, "without", f".s4-d{i}", a("pop", 120, 300 + i * 80, EO))
    A(sid, "without", ".s4-a1", a("wr", 500, 1000, EO))
    A(sid, "without", ".s4-pk", steps("s4pk", [
        (1000, f"opacity:1;transform:translate(-44px,50px);animation-timing-function:{EI}"),
        (1500, "opacity:1;transform:translate(0,0)"), (1600, "opacity:0;transform:translate(0,0)")]))
    KF.append("@keyframes s4dark{from{fill:var(--sunk)}}")
    A(sid, "without", ".s4-scr", a("s4dark", 250, 1550))
    A(sid, "without", ".s4-ask", a("in", 250, 1550))
    A(sid, "without", ".s4-tipy", steps("s4tipy", [
        (1800, "opacity:0;transform:scale(1.3)"), (1960, "opacity:1;transform:scale(1)"),
        (2060, "opacity:1;transform:scale(.9)"), (2350, "opacity:1;transform:scale(.9)"), (2550, "opacity:0;transform:scale(1)")]))
    KF.append("@keyframes s4yes{from{fill:var(--bg)}}")
    KF.append("@keyframes s4yest{from{fill:var(--text)}}")
    A(sid, "without", ".s4-yes", a("s4yes", 120, 2060))
    A(sid, "without", ".s4-yest", a("s4yest", 120, 2060))
    A(sid, "without", ".s4-a2", a("wu", 250, 2300, EO))
    A(sid, "without", ".s4-gm", a("draw", 200, 2500))
    A(sid, "without", ".s4-mail .tint", a("in", 200, 2600))
    A(sid, "without", ".s4-a3", a("wd", 350, 2800, EO))
    A(sid, "without", ".s4-str", a("in", 250, 2900))
    # The reveal, and only now: the address was wrong all along.
    A(sid, "without", ".s4-addr", a("fromtext", 250, 3300))
    A(sid, "without", ".s4-ul", a("draw", 300, 3500, EO))
    # With, 4.6s
    # The key rests clear of the port (70 right, 40 below) for 300ms, then is plugged in: up to the port's
    # height, then straight in.
    A(sid, "with", ".s4-key", steps("s4key", [
        (0, "transform:translate(70px,40px)"), (300, f"transform:translate(70px,40px);animation-timing-function:{EI}"),
        (600, f"transform:translate(24px,0);animation-timing-function:{EO}"), (750, "transform:translate(0,0)")]))
    for i in range(6):
        A(sid, "with", f".s4-d{i}", a("pop", 120, 800 + i * 80, EO))
    A(sid, "with", ".s4-field", a("out", 250, 1350))
    A(sid, "with", ".s4-touch", a("in", 250, 1350))
    # First touch, on the look-alike: the finger presses and holds; the pad stays dark.
    A(sid, "with", ".s4-tip1", steps("s4tip1", press(1650, 1780, 2700, 2950)))
    A(sid, "with", ".s4-tag", a("in", 160, 1810))
    # The tag asks on each page: the look-alike gets an x; once it has left the screen, the tag is back to ? until
    # the real page's touch answers.
    A(sid, "with", ".s4-q", steps("s4q", [(1810, "opacity:1"), (2199, "opacity:1"), (2200, "opacity:0"),
                                         (3149, "opacity:0"), (3150, "opacity:1"), (3709, "opacity:1"), (3710, "opacity:0")]))
    A(sid, "with", ".s4-acl", a("draw", 250, 1900, EO))
    KF.append("@keyframes s4pill{from{stroke:var(--line);stroke-width:1}}")
    A(sid, "with", ".s4-pill", a("s4pill", 250, 2150))
    A(sid, "with", ".s4-tx", steps("s4tx", [(2200, "opacity:0;transform:scale(.4)"), (2360, "opacity:1;transform:scale(1)"),
                                           (3149, "opacity:1;transform:scale(1)"), (3150, "opacity:0")]))
    # The look-alike shrinks straight into the card's thumbnail (28, 232): the fill-box origin is its top left
    # (30, 46), so it lands at (30 - 2, 46 + 186) at a fifth of its size: 40 wide, the thumbnail's width.
    A(sid, "with", ".s4-fake", steps("s4fake", [(0, "opacity:1;transform:none"), (2850, f"opacity:1;transform:none;animation-timing-function:{EI}"),
                                               (3150, "opacity:1;transform:translate(-2px,186px) scale(.2)"),
                                               (3250, "opacity:0;transform:translate(-2px,186px) scale(.2)")]))
    A(sid, "with", ".s4-card", a("in", 200, 3100))
    A(sid, "with", ".s4-real", a("in", 300, 3250))
    A(sid, "with", ".s4-touch2", a("out", 200, 4300))
    # Second touch, on the real page: the press comes first, then the pad answers.
    A(sid, "with", ".s4-tip2", steps("s4tip2", press(3480, 3600, 4150, 4400)))
    A(sid, "with", ".s4-tk", a("pop", 160, 3710, EO))
    lit, dark = "fill:var(--key-lit)", "fill:var(--key-dark)"
    pad, glow = [(0, dark)], [(0, "opacity:0")]
    t = 3710
    for k in range(3):
        pad += [(t, dark), (t + 1, lit), (t + 120, lit)]
        glow += [(t, "opacity:0"), (t + 1, "opacity:1"), (t + 120, "opacity:1")]
        if k < 2:
            pad += [(t + 121, dark)]
            glow += [(t + 121, "opacity:0")]
        t += 220
    A(sid, "with", ".key-pad", steps("s4pad", pad))
    A(sid, "with", ".key-glow", steps("s4glow", glow))
    A(sid, "with", ".key-halo", steps("s4halo", [(f, d.replace("opacity:1", "opacity:.3")) for f, d in glow]))
    A(sid, "with", ".s4-ok", a("pop", 160, 4300, EO))
    A(sid, "with", ".s4-in", a("in", 300, 4300))
    return svg
