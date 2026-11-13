"""Helpers for generating the Seven Walls v2 page: SVG shapes and animation CSS."""
EO = "cubic-bezier(.2,.7,.2,1)"
EI = "cubic-bezier(.45,0,.25,1)"

KF = []   # scene keyframes
CSS = []  # scene CSS (base poses and animation bindings)


def css(s):
    CSS.append(s)


def A(sid, state, sel, *anims):
    """Bind animations to a selector while stage `sid` plays `state`."""
    parts, vs = [], ""
    for x in anims:
        if isinstance(x, tuple):
            x, v = x
            vs += v + ";"
        parts.append(x + " backwards")
    sels = ",".join(f'#{sid}[data-play="{state}"] {s.strip()}' for s in sel.split(","))
    CSS.append(f"{sels}{{{vs}animation:{','.join(parts)}}}")


def a(name, dur, delay, ease="linear"):
    return f"{name} {dur}ms {ease} {delay}ms"


def steps(name, frames, ease="linear"):
    """frames: [(t_ms, 'decls'), ...] in absolute time. Returns an animation value."""
    t0, t1 = frames[0][0], frames[-1][0]
    d = t1 - t0
    body = "".join(f"{(t - t0) / d * 100:.2f}%{{{decl}}}" for t, decl in frames)
    KF.append(f"@keyframes {name}{{{body}}}")
    return f"{name} {d}ms {ease} {t0}ms"


def mv(fx, fy, dur, delay, ease=EI):
    """An object travelling into its base pose from an offset (fx, fy)."""
    return f"mv {dur}ms {ease} {delay}ms", f"--fx:{fx}px;--fy:{fy}px"


# ---------- shapes ----------

def text(x, y, s, cls="", anchor=None, extra=""):
    an = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text class="{cls}" x="{x}" y="{y}"{an}{extra}>{s}</text>'


def token(cx, cy, r, ch, cls=""):
    fs = round(r * 1.125, 1)
    return (f'<g class="tok {cls}"><circle class="obj" cx="{cx}" cy="{cy}" r="{r}"/>'
            f'<text class="ini" x="{cx}" y="{cy + fs * 0.36:.1f}" text-anchor="middle" style="font-size:{fs}px">{ch}</text></g>')


def anon(cx, cy, r=16, cls=""):
    return (f'<g class="anon {cls}"><circle class="obj anon-c" cx="{cx}" cy="{cy}" r="{r}"/>'
            f'<circle class="glyph" cx="{cx}" cy="{cy - 5}" r="4"/>'
            f'<path class="glyph" d="M{cx - 7} {cy + 9} a7 6 0 0 1 14 0"/></g>')


def check(cx, cy, r=11, cls=""):
    s = round(max(1.6, 2.5 * r / 11), 2)
    return (f'<g class="ck {cls}"><circle class="ckc" cx="{cx}" cy="{cy}" r="{r}"/>'
            f'<path class="ckp" style="stroke-width:{s}" d="M{cx - r * .45:.1f} {cy + r * .02:.1f} '
            f'L{cx - r * .1:.1f} {cy + r * .36:.1f} L{cx + r * .45:.1f} {cy - r * .34:.1f}"/></g>')


def cross(cx, cy, r=11, cls=""):
    s = round(max(1.6, 2.5 * r / 11), 2)
    k = r * .36
    return (f'<g class="xk {cls}"><circle class="xkc" cx="{cx}" cy="{cy}" r="{r}"/>'
            f'<path class="ckp" style="stroke-width:{s}" d="M{cx - k:.1f} {cy - k:.1f} L{cx + k:.1f} {cy + k:.1f} '
            f'M{cx + k:.1f} {cy - k:.1f} L{cx - k:.1f} {cy + k:.1f}"/></g>')


def keyglyph(x, y, cls=""):
    """The hardware key at 40%: means 'signs in with a key only'. 22 x 7."""
    return (f'<g class="kg {cls}"><rect class="kg-glow" x="{x - 4}" y="{y - 4}" width="30" height="15" rx="4"/>'
            f'<rect class="kg-c" x="{x}" y="{y + 1.5}" width="4" height="4"/>'
            f'<rect class="kg-b" x="{x + 3.5}" y="{y}" width="18.5" height="7" rx="2"/>'
            f'<circle class="kg-h" cx="{x + 18.5}" cy="{y + 3.5}" r="1.6"/></g>')


def envelope(x, y, w, h, cls="", flapcls="flap"):
    return (f'<g class="env {cls}"><rect class="obj" x="{x}" y="{y}" width="{w}" height="{h}" rx="2"/>'
            f'<path class="{flapcls}" d="M{x} {y} L{x + w / 2} {y + h * .55:.1f} L{x + w} {y}"/></g>')


def doc(x, y, w=18, h=22, cls=""):
    lines = "".join(f'<line class="docl" x1="{x + 4}" y1="{y + 6 + i * 5}" x2="{x + w - 4}" y2="{y + 6 + i * 5}"/>' for i in range(3))
    return f'<g class="doc {cls}"><rect class="obj" x="{x}" y="{y}" width="{w}" height="{h}" rx="2"/>{lines}</g>'


def switch(x, y, s=1.0, cls=""):
    """Switch shown ON (orange) at base. 40 x 20 at s=1."""
    w, h, r = 40 * s, 20 * s, 7 * s
    return (f'<g class="sw {cls}"><rect class="sw-t" x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}"/>'
            f'<circle class="sw-k" cx="{x + w - h / 2}" cy="{y + h / 2}" r="{r}"/></g>')
