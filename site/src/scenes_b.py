from lib import *

# ======================= Scene 3: Password manager =======================
# You can read the leaked password, and you can see it on every door it fits.

LEAK = "Sunset2019!"
SITES = [("CLOUD", "k7#Vq2mXr9L"), ("PAYMENTS", "Tz4!pW8nE3s"), ("CODE", "9hR@c6YbQ2f"), ("DESIGN", "xM3$j8KtU5w")]
YS3 = [40, 100, 160, 220]
assert all(len(p) == len(LEAK) for _, p in SITES)


def s3():
    sid = "s3"
    rows = []
    for i, ((n, pw), y) in enumerate(zip(SITES, YS3)):
        last = " last-without" if i == 3 else ""
        rows.append(
            f'<g class="s3-t s3-t{i}"><rect class="obj box{last}" x="176" y="{y}" width="212" height="40" rx="6"/>'
            f'{text(186, y + 25, n, "f12")}'
            f'<rect class="s3-pill" x="258" y="{y + 10}" width="100" height="20" rx="4"/>'
            f'{text(263, y + 25, LEAK, "f13 s3-pw only-without")}{text(263, y + 25, pw, "f13 only-with")}</g>')
    checks = "".join(check(374, y + 20, 9, f"s3-ck s3-ck{i} only-with") for i, y in enumerate(YS3))
    # The safe's lines fan from one point on its right edge to each row's left edge.
    vlines = "".join(f'<line class="thin" x1="144" y1="196" x2="176" y2="{y + 20}"/>' for y in YS3)
    # The leaked chip is drawn at its final place, above DESIGN; the sequences move it in from the forum.
    cy = YS3[3] - 19
    svg = f'''<svg viewBox="0 0 400 300" role="img" aria-labelledby="s3-alt-with">
<g class="s3-forum"><rect class="obj box" x="12" y="40" width="148" height="60" rx="6"/>
{text(22, 62, "OLD FORUM", "f13")}
<rect class="s3-pill" x="18" y="70" width="104" height="20" rx="4"/>{text(24, 85, LEAK, "f13")}</g>
<path class="crack s3-crack" pathLength="1" d="M128 100 L134 88 L141 94 L147 78 L153 84 L160 66"/>
{text(12, 118, "BREACHED", "f12 bd s3-br")}
{token(28, 170, 14, "T")}{text(12, 200, "THEO", "f12")}
<g class="only-with">{vlines}
<rect class="obj s3-safe" x="60" y="150" width="84" height="92" rx="6"/>
<rect class="safe-door" x="66" y="156" width="72" height="80" rx="3"/>
<circle class="dial" cx="128" cy="196" r="5"/><line class="dial-t" x1="128" y1="196" x2="128" y2="192"/>
{text(60, 262, "1PASSWORD", "f12")}</g>
{"".join(rows)}
{checks}
<g class="s3-leak last-with"><g class="s3-chip">
<rect class="s3-lchip" x="258" y="{cy}" width="100" height="18" rx="4"/>
{text(263, cy + 13, LEAK, "f13 bd")}
{text(252, cy + 13, "LEAKED", "f12 bd", "end")}</g></g>
</svg>'''
    css('''.s3-pill{fill:var(--sunk);stroke:transparent;stroke-width:1.5}
.s3-lchip{fill:var(--surface);stroke:var(--bad);stroke-width:1.5}
.s3-safe{stroke:var(--accent);stroke-width:3}
#s3 .s3-forum .box{stroke:var(--bad);fill:var(--bad-tint)}
#s3[data-state="without"] .s3-t .box{stroke:var(--bad);fill:var(--bad-tint)}
#s3[data-state="without"] .s3-t .s3-pill{stroke:var(--bad)}
#s3[data-state="without"] .s3-pw{fill:var(--bad)}
#s3[data-state="with"] .s3-leak{opacity:.35}''')
    KF.append("@keyframes s3pill{from{stroke:transparent}}")
    # The chip's stops, as offsets from its final place above DESIGN. It pops in the gap above the forum
    # (LEAKED, 6 units to its left, would leave the stage if it sat on the forum's own pill).
    FORUM = (-202, -180)
    above = [(0, y - YS3[3]) for y in YS3]
    tr = lambda p: f"transform:translate({p[0]}px,{p[1]}px);opacity:1;animation-timing-function:{EI}"

    def chip(name, moves):
        fr = [(800, f"transform:translate({FORUM[0]}px,{FORUM[1]}px) scale(.4);opacity:0;animation-timing-function:{EO}"),
              (960, tr(FORUM))]
        prev = FORUM
        for p, (t0, t1) in zip(above, moves):
            fr += [(t0, tr(prev)), (t1, tr(p))]
            prev = p
        return steps(name, fr)

    for st in ("without", "with"):
        A(sid, st, ".s3-crack", a("draw", 400, 300))
        A(sid, st, ".s3-forum .box", a("fromplain", 250, 400))
        A(sid, st, ".s3-br", a("in", 200, 500))
    # Without, 3.35s: the chip stops above each row in turn, and each row turns crimson.
    moves = [(1000, 1450), (1750, 2000), (2300, 2550), (2850, 3100)]
    A(sid, "without", ".s3-chip", chip("s3chipA", moves))
    for k, (_, t1) in enumerate(moves):
        A(sid, "without", f".s3-t{k} .s3-pill", a("s3pill", 125, t1))
        A(sid, "without", f".s3-t{k} .s3-pw", a("fromtext", 125, t1))
        A(sid, "without", f".s3-t{k} .box", a("fromplain", 125, t1 + 125))
    # With, 3.45s: the strings differ, so each row gets a check; then the chip fades where it is.
    moves = [(1000, 1450), (1700, 1950), (2200, 2450), (2700, 2950)]
    A(sid, "with", ".s3-chip", chip("s3chipB", moves))
    for k, (_, t1) in enumerate(moves):
        A(sid, "with", f".s3-ck{k}", a("pop", 160, t1, EO))
    A(sid, "with", ".s3-leak", a("undim", 250, 3200))
    return svg


# ======================= Scene 4: Hardware key =======================
# A password and a code are text, and text travels. The key stays in Maya's hand.

def finger(cx, cy, r, cls):
    """A fingertip: r is half its width; it comes in from the lower right and runs off the stage."""
    tx = cx - r / 3
    return (f'<g class="rot" transform="rotate(35 {cx} {cy})"><g class="finger {cls}"><path class="fpath" d="M{tx:.1f} {cy - r} H{tx + 260:.1f} V{cy + r} H{tx:.1f} A{r} {r} 0 0 1 {tx:.1f} {cy - r} Z"/>'
            f'<rect class="nail" x="{tx - r * .65:.1f}" y="{cy - r / 2}" width="{r * 1.5}" height="{r}" rx="{r / 2}"/></g></g>')


def ykey(x, y, cls=""):
    """The library key at full size, body 46 x 18 at (x, y): the contact on the left, the touch pad at the body's
    centre, the ring hole at the right end with a key ring through it."""
    return (f'<g class="ykey {cls}"><circle class="key-ring" cx="{x + 49}" cy="{y + 9}" r="9"/>'
            f'<rect class="key-c" x="{x - 10}" y="{y + 4}" width="10" height="10"/>'
            f'<rect class="key-b" x="{x}" y="{y}" width="46" height="18" rx="5"/>'
            f'<circle class="key-h" cx="{x + 40}" cy="{y + 9}" r="2.6"/>'
            f'<circle class="key-pad" cx="{x + 23}" cy="{y + 9}" r="6"/></g>')


def packet(label, w, cls):
    """A chip riding the relay, drawn at the relay's midpoint (224, 124)."""
    return (f'<g class="s4-pk {cls}"><rect class="pk" x="{224 - w / 2}" y="117" width="{w}" height="14" rx="3"/>'
            f'{text(224, 128, label, "f12 bd", "middle")}</g>')


def s4():
    sid = "s4"
    dots = lambda n, x, step, cy, r, cls: "".join(
        f'<circle class="pdot {cls}{i}{" only-without" if i >= 6 else ""}" cx="{x + i * step}" cy="{cy}" r="{r}"/>' for i in range(n))
    code = "".join(f'<tspan class="s4-c{i}">{ch}</tspan>' for i, ch in enumerate("481 920"))
    svg = f'''<svg viewBox="0 -30 400 300" role="img" aria-labelledby="s4-alt-with">
{token(20, 56, 10, "M")}{text(36, 61, "MAYA", "f12")}
<rect class="obj" x="8" y="76" width="184" height="120" rx="6"/>
<path class="topbar" d="M9 82 a5 5 0 0 1 5 -5 h172 a5 5 0 0 1 5 5 v20 h-182 Z"/>
<path class="obj" d="M2 196 H198 L190 206 H10 Z"/>
<rect class="port" x="178" y="198" width="10" height="5"/>
<rect class="pill" x="14" y="82" width="172" height="16" rx="6"/>
<text class="f12 s4-addr" x="19" y="94">goog1e-login.example</text>
<line class="s4-ul only-without last-without" pathLength="1" x1="19" y1="98" x2="66" y2="98"/>
<text class="say b" x="18" y="120">Sign in</text>
<rect class="field" x="18" y="128" width="120" height="18" rx="3"/>
<text class="say f13 mu s4-ph1" x="24" y="141">Password</text>
{dots(8, 26, 9, 137, 2.6, "s4-d")}
<g class="only-without"><rect class="field" x="18" y="154" width="120" height="18" rx="3"/>
<text class="say f13 mu s4-ph2" x="24" y="167">Code</text>
<text class="f13 s4-code" x="24" y="167">{code}</text></g>
<text class="say f14 s4-touch only-with" x="18" y="168">Touch your key</text>
{text(256, 61, "A STRANGER", "f12 bd")}
<rect class="badobj" x="256" y="76" width="132" height="96" rx="6"/>
<path class="badobj" d="M250 172 H394 L388 180 H256 Z"/>
<rect class="port" x="350" y="174" width="10" height="5"/>
<text class="say b f14" x="264" y="96">Google</text>
<rect class="field" x="264" y="104" width="100" height="16" rx="3"/>
<g class="s4-sd">{dots(8, 272, 8, 112, 2.2, "s4-e")}</g>
<g class="only-without"><rect class="field" x="264" y="126" width="100" height="16" rx="3"/>
{text(270, 138, "481 920", "f13 s4-sc")}
<text class="say f13 s4-in" x="264" y="162">Signed in</text>
{text(256, 200, "IN MAYA’S MAIL", "f12 bd s4-out")}</g>
<text class="say f13 s4-touch2 only-with" x="264" y="139">Touch your key</text>
<line class="atk s4-relay" x1="192" y1="137" x2="256" y2="112"/>
{packet("•••", 34, "s4-pk1")}
<g class="only-without">{packet("481 920", 60, "s4-pk2")}</g>
<g class="only-with">
{cross(224, 124, 9, "s4-rx")}
<rect class="s4-empty s4-ek" x="360" y="169.5" width="28" height="14" rx="3.5"/>
{cross(374, 158, 7, "s4-ex")}
{text(256, 200, "NO KEY HERE", "f12 okc s4-nk last-with")}
{text(188, 228, "WRONG SITE", "f12 mu s4-ws")}
{ykey(188, 192, "s4-key")}
{finger(211, 201, 7, "s4-tip")}
{text(130, 262, "MAYA’S KEY", "f12 mu s4-mk")}
</g>
</svg>'''
    css('''.topbar{fill:var(--sunk)}
.pill{fill:var(--surface);stroke:var(--line);stroke-width:1}
#s4[data-state="without"] .s4-addr{fill:var(--bad)}
.s4-ul{stroke:var(--bad);stroke-width:2;stroke-dasharray:1}
.field{fill:var(--sunk)}
.pdot{fill:var(--text)}
.port{fill:var(--text)}
.s4-ph1,.s4-ph2{opacity:0}
.badobj{fill:var(--bg);stroke:var(--bad);stroke-width:2;stroke-linecap:round}
.pk{fill:var(--surface);stroke:var(--bad);stroke-width:1.5}
.s4-pk{opacity:0}
.s4-empty{fill:var(--bad-tint);stroke:var(--bad);stroke-width:2;stroke-dasharray:3 2}
.key-ring{fill:none;stroke:var(--text);stroke-width:1.5}
.key-c{fill:var(--text)}.key-b{fill:var(--accent)}
.key-h{fill:var(--surface)}
.key-pad{fill:var(--key-dark);stroke:var(--key-dark);stroke-width:.6}
.fpath{fill:var(--text);fill-opacity:.35;stroke:var(--text);stroke-opacity:.6;stroke-width:1.5;stroke-linejoin:round}
.finger{opacity:0}
.nail{fill:none;stroke:var(--surface);stroke-width:1.2;opacity:.7}
#s4 .rot{transform-box:view-box;transform-origin:0 0}
@media (max-width:40rem){#s4 .s4-addr{letter-spacing:0}}
.s4-mk{opacity:0}''')
    KF.append("@keyframes tin{from{fill-opacity:0}}")
    pk = lambda t0, t1: steps(f"s4pk{t0}", [
        (t0, f"opacity:1;transform:translate(-28px,11px);animation-timing-function:{EI}"),
        (t1 - 40, "opacity:1;transform:translate(28px,-11px)"), (t1, "opacity:0;transform:translate(28px,-11px)")])
    # Without, 4.0s
    A(sid, "without", ".s4-ph1", a("out", 60, 240))
    for i in range(8):
        A(sid, "without", f".s4-d{i}", a("pop", 80, 300 + i * 60, EO))
    A(sid, "without", ".s4-relay", a("wr", 450, 850, EI))
    A(sid, "without", ".s4-pk1", pk(850, 1300))
    A(sid, "without", ".s4-sd", a("in", 100, 1300))
    A(sid, "without", ".s4-ph2", a("out", 60, 1340))
    for i, ch in enumerate("481 920"):
        if ch != " ":
            A(sid, "without", f".s4-c{i}", a("tin", 60, 1400 + (i if i < 3 else i - 1) * 80))
    A(sid, "without", ".s4-pk2", pk(1950, 2400))
    A(sid, "without", ".s4-sc", a("in", 100, 2400))
    A(sid, "without", ".s4-in", a("in", 400, 2500))
    A(sid, "without", ".s4-out", a("in", 400, 3000))
    # The reveal, and only now: the address was wrong all along.
    A(sid, "without", ".s4-addr", a("fromtext", 250, 3500))
    A(sid, "without", ".s4-ul", a("draw", 500, 3500, EO))
    # With, 4.1s. The key starts on its ring, below the laptop, and goes into the port.
    A(sid, "with", ".s4-key", (f"mv 450ms {EI} 300ms", "--fx:-58px;--fy:34px"))
    A(sid, "with", ".s4-mk", steps("s4mk", [(0, "opacity:1"), (300, "opacity:1"), (450, "opacity:0")]))
    A(sid, "with", ".s4-ph1", a("out", 60, 740))
    for i in range(6):
        A(sid, "with", f".s4-d{i}", a("pop", 80, 800 + i * 74, EO))
    A(sid, "with", ".s4-relay", a("wr", 450, 1350, EI))
    A(sid, "with", ".s4-pk1", pk(1350, 1800))
    A(sid, "with", ".s4-sd", a("in", 100, 1800))
    A(sid, "with", ".s4-touch", a("in", 200, 1900))
    A(sid, "with", ".s4-touch2", a("in", 200, 2150))
    # The fingertip comes in and rests on the pad; the pad stays dark. Then it leaves.
    A(sid, "with", ".s4-tip", steps("s4tip", [
        (2450, f"opacity:0;transform:translate(14px,0);animation-timing-function:{EO}"),
        (2610, "opacity:1;transform:translate(0,0)"), (2650, "opacity:1;transform:translate(0,0)"),
        (2900, "opacity:0;transform:translate(0,0)")]))
    A(sid, "with", ".s4-ws", a("in", 250, 2650))
    A(sid, "with", ".s4-rx", a("pop", 160, 3000, EO))
    A(sid, "with", ".s4-ek", a("in", 250, 3300))
    A(sid, "with", ".s4-ex", a("pop", 160, 3550, EO))
    A(sid, "with", ".s4-nk", a("in", 300, 3800))
    return svg
