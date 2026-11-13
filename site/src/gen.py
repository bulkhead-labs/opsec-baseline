"""Generate site/story.html for Seven Walls. Edit the scenes here, not story.html: python3 site/build.py runs this first."""
import sys
from pathlib import Path
from lib import KF, CSS, END
import scenes_a, scenes_b, scenes_c, scenes_d

OUT = Path(__file__).resolve().parent.parent / "story.html"
MOD = "https://github.com/bulkhead-labs/opsec-baseline/blob/main/modules/"
SITE = "https://bulkhead-labs.github.io/opsec-baseline/"
DESC = ("Seven security basics a small team can set up itself, told as one year at an invented nine-person company. "
        "No security background needed.")
CARD_ALT = "The Bulkhead Labs mark: a hull seen from above, cut into compartments, one lit orange."
# Icon and manifest paths are relative, so they resolve under the /opsec-baseline/ project path. The og:image is
# absolute and read only by link unfurlers, never by the page.
HEAD = f'''<title>Seven Walls · Bulkhead Labs</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{SITE}">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#ECEFF2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#15191D" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bulkhead Labs">
<meta property="og:title" content="Seven Walls: security basics for small teams">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{CARD_ALT}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image:alt" content="{CARD_ALT}">'''

BASE_CSS = r'''
/* ---------- Tokens (v1's, plus three tints and the motion tokens) ---------- */
:root {
  --bg: #ECEFF2; --surface: #FFFFFF; --sunk: #E1E5E9;
  --text: #111417; --muted: #535B63; --line: #C9D0D6; --rule: #111417;
  --accent: #EC5A20; --accent-ink: #B23C0C; --ok: #1E7A46; --bad: #B4235A;
  --f-stencil: "Big Shoulders Stencil Display", "Arial Narrow", Impact, sans-serif;
  --f-head: "Big Shoulders Display", "Arial Narrow", Impact, sans-serif;
  --f-body: "Atkinson Hyperlegible Next", system-ui, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  /* Tints are literal rgba, never color-mix: a fill animated toward a color-mix() value flashes yellow in Chromium. */
  --bad-tint: rgba(180, 35, 90, .16); --ok-tint: rgba(30, 122, 70, .16); --accent-tint: rgba(236, 90, 32, .16);
  /* Light: a narrower, stronger bar, so it reads orange, never the peach-pink of the crimson tint. */
  --hl: rgba(236, 90, 32, .74); --hl-top: 64%; --ring0: rgba(236, 90, 32, .55); --ring1: rgba(236, 90, 32, 0);
  --key-dark: #2A1A12; --key-lit: #FFFFFF; --key-glow: rgba(255, 196, 160, .9);
  --ease-out: cubic-bezier(.2, .7, .2, 1);
  --ease-inout: cubic-bezier(.45, 0, .25, 1);
  --t-pop: 160ms; --t-fade: 250ms; --t-move: 450ms; --t-draw: 500ms;
  --gutter-l: max(16px, env(safe-area-inset-left, 0px));
  --gutter-r: max(16px, env(safe-area-inset-right, 0px));
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #15191D; --surface: #1E2328; --sunk: #101316;
    --text: #E8EBEE; --muted: #9AA3AB; --line: #2E353C; --rule: #E8EBEE;
    --accent: #FF6B35; --accent-ink: #FF8A5C; --ok: #4CC07E; --bad: #F06A8A;
    --bad-tint: rgba(240, 106, 138, .16); --ok-tint: rgba(76, 192, 126, .16); --accent-tint: rgba(255, 107, 53, .16);
    --hl: rgba(255, 107, 53, .45); --hl-top: 58%; --ring0: rgba(255, 107, 53, .6); --ring1: rgba(255, 107, 53, 0);
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #15191D; --surface: #1E2328; --sunk: #101316;
  --text: #E8EBEE; --muted: #9AA3AB; --line: #2E353C; --rule: #E8EBEE;
  --accent: #FF6B35; --accent-ink: #FF8A5C; --ok: #4CC07E; --bad: #F06A8A;
  --bad-tint: rgba(240, 106, 138, .16); --ok-tint: rgba(76, 192, 126, .16); --accent-tint: rgba(255, 107, 53, .16);
  --hl: rgba(255, 107, 53, .45); --hl-top: 58%; --ring0: rgba(255, 107, 53, .6); --ring1: rgba(255, 107, 53, 0);
  color-scheme: dark;
}

/* ---------- Page and scenes ---------- */
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-snap-type: y proximity; scroll-padding-top: 0; }
@media (min-width: 64rem) and (min-height: 760px) { html { scroll-snap-type: y mandatory; } }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
@media (prefers-reduced-motion: reduce) { html { scroll-snap-type: y proximity; } }
/* Without JS, snapping fights the browser's own jump to an anchor and lands past it: no snapping then. */
html.no-js { scroll-snap-type: none; }
body { margin: 0; background: var(--bg); color: var(--text); font-family: var(--f-body); font-size: 1.125rem; line-height: 1.5; overflow-x: clip; }
@media (min-width: 64rem) { body { font-size: 1.25rem; } }
p, h1, h2, h3, figure, dl, dd, ol { margin: 0; }
a { color: inherit; text-decoration-color: var(--accent); text-decoration-thickness: 2px; text-underline-offset: 3px; }
a:hover { color: var(--accent-ink); }
a:focus-visible, button:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 2px; }
.vh { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
.scene {
  min-height: 100vh; min-height: 100svh; scroll-snap-align: start;
  display: grid; align-content: center; grid-template-columns: minmax(0, 1fr);
  padding: 56px var(--gutter-r) 16px var(--gutter-l);
}
.wrap { width: 100%; max-width: 72rem; margin: 0 auto; }
@media (min-width: 64rem) { .scene { padding: 64px 32px 20px; } }

.meta { font-family: var(--f-mono); font-size: 15px; text-transform: uppercase; letter-spacing: .06em; color: var(--accent-ink); }
.name {
  font-family: var(--f-head); font-weight: 800; text-transform: uppercase; line-height: .9;
  font-size: clamp(3rem, 11vw, 5.75rem); letter-spacing: .005em; text-wrap: balance; hyphens: manual;
}
.hook { font-size: 1.1875rem; line-height: 1.4; max-width: 36ch; }
.head { display: flex; flex-direction: column; gap: 12px; }
.takeaway { font-weight: 700; font-size: 1.25rem; line-height: 1.3; max-width: 30ch; }
@media (min-width: 40rem) { .hook { font-size: 1.375rem; } .takeaway { font-size: 1.5rem; } }

.next, .back {
  font-family: var(--f-mono); font-size: 15px; text-transform: uppercase; letter-spacing: .06em;
  color: var(--muted); text-decoration: none; display: inline-flex; align-items: center; min-height: 44px; align-self: flex-start;
}
.next:hover, .back:hover { color: var(--text); }
/* Next: lit once the reader has seen the scene. The border is always there, so lighting it moves nothing. */
.next { border: 1.5px solid transparent; border-radius: 4px; padding: 0 14px; margin-left: -14px; transition: color 400ms linear, border-color 400ms linear; }
.next.is-ready { color: var(--text); border-color: var(--accent); }
.arr { display: inline-block; }
.is-ready .arr { animation: nudge 700ms var(--ease-inout) 400ms 2; }
@keyframes nudge { 50% { transform: translateY(3px); } }
@media (prefers-reduced-motion: reduce) { .next, .start { transition: none; } .is-ready .arr { animation: none; } }

/* What the wall does: plain sentences, the same in every mode. */
.what { font-size: 1.125rem; line-height: 1.45; color: var(--text); max-width: 38ch; }
@media (min-width: 64rem) { .what { font-size: 1.25rem; } }
/* Key phrases are bold. Only the opening phrase of the right column sits on the orange highlighter bar: one per wall.
   The text keeps --text, so contrast holds in both themes. */
.kb { font-weight: 700; }
.k { font-weight: 700; background: linear-gradient(transparent var(--hl-top), var(--hl) var(--hl-top), var(--hl) 92%, transparent 92%);
  -webkit-box-decoration-break: clone; box-decoration-break: clone; padding: 0 .12em; margin: 0 -.12em; }
@media (forced-colors: active) { .k { background: none; text-decoration: underline; } }
.addr { font-family: var(--f-mono); font-size: .9em; letter-spacing: 0; white-space: nowrap; }

/* ---------- The hull bar ---------- */
.hullbar {
  position: fixed; top: 0; left: 0; right: 0; height: 48px; z-index: 10;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
  transition: opacity 200ms, visibility 0s;
}
.hullbar .in { max-width: calc(72rem + 64px); margin: 0 auto; height: 100%; display: flex; align-items: center; gap: 14px; padding: 0 var(--gutter-r) 0 var(--gutter-l); }
@media (min-width: 64rem) { .hullbar .in { padding: 0 32px; } }
/* 202px on touch screens: each compartment's link is then 24px wide and 44px tall. */
.hullnav { display: block; width: 202px; height: auto; overflow: visible; }
@media (min-width: 64rem) { .hullnav { width: 168px; } }
.hullnav .hit { fill: transparent; }
.hullnav .c, .hullnav .bow { fill: none; stroke: var(--line); stroke-width: 1.5; transition: fill 250ms ease-out, stroke 250ms ease-out; }
.hullnav .done { fill: var(--text); stroke: var(--text); }
.hullnav .lit { fill: var(--accent); stroke: var(--accent); }
.hullnav a:focus-visible { outline: none; }
.hullnav a:focus-visible .c, .hullnav a:focus-visible .bow { stroke: var(--accent); stroke-width: 2.5; }
.hullnav a:hover .c, .hullnav a:hover .bow { stroke: var(--text); }
.hb-label { font-family: var(--f-mono); font-size: 14px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); white-space: nowrap; }
.hb-name { display: none; }
@media (min-width: 40rem) { .hb-name { display: inline; } }
.hullbar.is-wren .hb-name { display: inline; }
.js .hullbar.is-hidden { opacity: 0; visibility: hidden; pointer-events: none; transition: opacity 200ms, visibility 0s 200ms; }

/* ---------- Wall scene layout ---------- */
.body { display: flex; flex-direction: column; gap: 14px; margin-top: 12px; }
.stagecol { display: flex; flex-direction: column; gap: 10px; min-width: 0; }
.side { display: flex; flex-direction: column; gap: 12px; min-width: 0; }
@media (min-width: 64rem) {
  .body { display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: 48px; margin-top: 20px; }
  .side { align-self: end; gap: 16px; }
  .stagecol { gap: 12px; }
  .wall .stage { max-width: var(--stage-w, 600px); }
  .wall .control, .wall .caption { max-width: var(--stage-w, 600px); }
}

/* ---------- The stage ---------- */
.stage { display: flex; flex-direction: column; gap: 8px; width: 100%; }
.stage svg { display: block; width: 100%; height: auto; background: var(--surface); border: 1px solid var(--line); border-radius: 6px; box-shadow: inset 0 4px 0 var(--sc, var(--ok)); transition: box-shadow 250ms linear; }
/* Phones: the stage runs edge to edge. No SVG label is under 14 units anywhere. */
@media (max-width: 40rem) {
  .stage > svg { width: calc(100% + var(--gutter-l) + var(--gutter-r)); max-width: none; margin-left: calc(-1 * var(--gutter-l)); border-left: 0; border-right: 0; border-radius: 0; }
  .stage svg text { letter-spacing: .01em; }
}
.stage[data-state="without"] { --sc: var(--bad); }
.stage[data-state="with"] { --sc: var(--ok); }
.state-tag { font-family: var(--f-mono); font-size: 14px; text-transform: uppercase; letter-spacing: .06em; font-weight: 600; display: flex; align-items: center; gap: 8px; }
.state-tag::before { content: ""; width: 8px; height: 8px; background: var(--sc); }
.state-tag .st-without { color: var(--bad); }
.state-tag .st-with { color: var(--ok); }
.stage[data-state="with"] .st-without, .stage[data-state="without"] .st-with { display: none; }
.stage[data-state="with"] .only-without, .stage[data-state="without"] .only-with { display: none; }
.stage[data-state="with"] .legend .only-without, .stage[data-state="without"] .legend .only-with { display: inline; visibility: hidden; }
.legend { font-family: var(--f-mono); font-size: 14px; color: var(--muted); letter-spacing: .02em; display: flex; flex-wrap: wrap; gap: 4px 18px; align-items: center; }
.legend .gl { display: inline-grid; place-items: center; width: 16px; height: 16px; border: 1.5px solid var(--text); border-radius: 50%; font: 700 10px/1 var(--f-body); color: var(--text); margin-right: 4px; vertical-align: -3px; }
.stage .legend svg { display: inline-block; width: 8px; height: 16px; vertical-align: -3px; margin-right: 6px; background: none; border: 0; border-radius: 0; box-shadow: none; }

/* ---------- The control ---------- */
.control { display: flex; align-items: center; gap: 6px; }
.seg { display: flex; gap: 6px; min-width: 0; }
.control button {
  min-height: 44px; border: 1.5px solid var(--line); border-radius: 4px; background: transparent; color: var(--muted);
  font: 600 17px/1.1 var(--f-body); padding: 0 12px; display: inline-flex; align-items: center; gap: 7px; cursor: pointer; white-space: nowrap;
}
.control button:hover { color: var(--text); }
.seg .dot { width: 8px; height: 8px; border-radius: 50%; border: 1.5px solid currentColor; flex: none; }
/* Pressed: outline, tint and coloured text. Only a pressed button has a fill. */
.seg .b-without[aria-pressed="true"] { border-color: var(--bad); color: var(--bad); background: var(--bad-tint); }
.seg .b-with[aria-pressed="true"] { border-color: var(--ok); color: var(--ok); background: var(--ok-tint); }
.seg [aria-pressed="true"] .dot { background: currentColor; }
.seg .go { display: none; width: 14px; margin: 0 -3px; font: 700 15px/1 var(--f-body); color: var(--accent-ink); justify-content: center; flex: none; }
/* The invitation: a few seconds into Without, With gets an orange outline, a pulsing ring and an arrow for its dot.
   No fill and the text stays grey, so it never looks more "on" than the pressed button. Three beats, then still. */
.seg .b-with { transition: border-color 300ms linear, background-color 300ms linear, color 300ms linear; }
.seg .b-with.is-invite { border-color: var(--accent); animation: invite 1100ms var(--ease-inout) 3; }
.seg .b-with.is-invite .dot { display: none; }
.seg .b-with.is-invite .go { display: inline-flex; }
@keyframes invite { 0% { box-shadow: 0 0 0 0 var(--ring0); } 100% { box-shadow: 0 0 0 9px var(--ring1); } }
@media (prefers-reduced-motion: reduce) { .seg .b-with { transition: none; } .seg .b-with.is-invite { animation: none; } }
.replay { margin-left: auto; }
/* The third button: Pause while the stage cycles, Replay otherwise. Both faces share one grid cell, so the button
   keeps one size and swapping faces moves nothing. */
.control .replay { display: inline-grid; }
.replay .face { grid-area: 1 / 1; display: inline-flex; align-items: center; justify-content: center; gap: 7px; }
.replay .f-pause, .replay.is-pause .f-replay { visibility: hidden; }
.replay.is-pause .f-pause { visibility: visible; }
.replay .bars { display: block; width: 10px; height: 12px; fill: currentColor; }
.replay .glyph { font-size: 18px; line-height: 1; }
.btn-short { display: none; }
@media (max-width: 40rem) {
  .replay .rl { display: none; } .replay { width: 44px; justify-content: center; padding: 0; }
  .control button { font-size: 16px; padding: 0 9px; gap: 6px; }
}
@media (max-width: 379px) { .btn-long { display: none; } .btn-short { display: inline; } }
.no-js .control { display: none; }
@media (prefers-reduced-motion: reduce) { .control .replay { display: none; } }

/* ---------- Caption ---------- */
.caption { display: flex; flex-direction: column; gap: 8px; font-size: 1.125rem; line-height: 1.4; }
@media (min-width: 64rem) { .caption { font-size: 1.1875rem; } }
.cap { display: block; padding-left: 12px; border-left: 3px solid var(--ok); }
.cap-without { border-left-color: var(--bad); }
.cap[hidden] { display: none; }
/* With JS, both captions sit in one grid cell and the hidden one keeps its space: nothing above the stage moves on a toggle. */
.js .caption { display: grid; }
.js .caption .cap { grid-area: 1 / 1; }
.js .caption .cap[hidden] { display: block; visibility: hidden; }
.cap-tag { display: block; font-family: var(--f-mono); font-size: 14px; letter-spacing: .06em; font-weight: 600; }
.cap-without .cap-tag { color: var(--bad); }
.cap-with .cap-tag { color: var(--ok); }
.js .cap-tag { display: none; }

/* ---------- Chips ---------- */
.chips { display: grid; grid-template-columns: 1fr; gap: 2px 16px; background: var(--sunk); border-radius: 4px; padding: 12px 14px; }
.chips dt { font-family: var(--f-mono); font-size: 14px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); padding-top: 2px; }
.chips dd { font-size: 16px; line-height: 1.4; margin-bottom: 6px; }
@media (min-width: 64rem) { .chips dd { font-size: 17px; } }
.chips dd:last-child { margin-bottom: 0; }
@media (min-width: 64rem) { .chips { grid-template-columns: max-content 1fr; } .chips dd { margin-bottom: 0; } }
.modlink { font-weight: 600; font-size: 17px; align-self: flex-start; display: inline-flex; align-items: center; min-height: 32px; }

/* ---------- SVG drawing conventions ---------- */
.stage svg *, .dia * { transform-box: fill-box; transform-origin: center; }
.stage :where(text), .ws-dia :where(text), .tok64 :where(text) { font-family: var(--f-mono); font-size: 15px; letter-spacing: .02em; fill: var(--text); }
.stage .f11, .stage .f12 { font-size: 14px; } .stage .f13 { font-size: 15px; } .stage .f14 { font-size: 16px; }
.stage .say { font-family: var(--f-body); letter-spacing: 0; font-size: 16px; }
.stage .say.f13 { font-size: 14px; } .stage .say.f14 { font-size: 15px; }
.stage .say.b { font-weight: 700; }
.stage .ls0 { letter-spacing: 0; }
.stage .mu { fill: var(--muted); } .stage .bd { fill: var(--bad); } .stage .okc { fill: var(--ok); }
text.ini, .stage text.ini, .tok64 text.ini { font-family: var(--f-head); font-weight: 800; letter-spacing: 0; fill: var(--text); }
.gch { font-family: var(--f-body) !important; font-weight: 700; font-size: 14px !important; letter-spacing: 0 !important; }
.obj { fill: var(--bg); stroke: var(--text); stroke-width: 2; }
.ln { fill: none; stroke: var(--text); stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }
.thin { stroke: var(--line); stroke-width: 1.5; }
.atk { fill: none; stroke: var(--bad); stroke-width: 1.5; stroke-dasharray: 6 5; stroke-linecap: round; }
.bnd { fill: none; stroke: var(--muted); stroke-width: 1.5; stroke-dasharray: 4 4; }
.ring { fill: none; stroke: var(--accent); stroke-width: 2; }
.anon-c { stroke: var(--muted); }
.glyph { fill: none; stroke: var(--muted); stroke-width: 1.5; stroke-linecap: round; }
.ckc { fill: var(--ok); } .xkc { fill: var(--bad); }
.ckp { fill: none; stroke: var(--surface); stroke-linecap: round; stroke-linejoin: round; }
.crack { fill: none; stroke: var(--bad); stroke-width: 2.5; stroke-linejoin: round; stroke-linecap: round; stroke-dasharray: 1; }
.tick { fill: none; stroke: var(--ok); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 1; }
.ln[pathLength] { stroke-dasharray: 1; }
.list { fill: var(--bg); stroke: var(--muted); stroke-width: 1.5; }
.box10 { fill: none; stroke: var(--text); stroke-width: 1.5; }
.gb { fill: none; stroke: var(--text); stroke-width: 1.5; }
.pw { fill: var(--text); }
.sw-t { fill: var(--accent); } .sw-k { fill: var(--surface); }
.safe-door { fill: none; stroke: var(--line); stroke-width: 1.5; }
.dial { fill: var(--bg); stroke: var(--text); stroke-width: 1.5; } .dial-t { stroke: var(--text); stroke-width: 1.5; stroke-linecap: round; }
.kg-c { fill: var(--text); } .kg-b { fill: var(--accent); } .kg-h { fill: var(--surface); }
.docl { stroke: var(--line); stroke-width: 1.5; }

/* ---------- Motion: shared keyframes (each describes only where a thing comes from) ---------- */
@keyframes in { from { opacity: 0; } }
@keyframes out { 0% { opacity: 1; } 100% { opacity: 0; } }
@keyframes undim { from { opacity: 1; } }
@keyframes pop { from { opacity: 0; transform: scale(.4); } }
@keyframes draw { from { stroke-dashoffset: 1; } }
@keyframes mv { from { transform: translate(var(--fx, 0px), var(--fy, 0px)); } }
@keyframes fromplain { from { stroke: var(--text); fill: var(--bg); } }
@keyframes fromtext { from { fill: var(--text); } }
@keyframes fromstroke { from { stroke: var(--text); } }
@keyframes flash { 0% { opacity: 0; } 30% { opacity: 1; } 70% { opacity: 1; } 100% { opacity: 0; } }
@keyframes wr { from { clip-path: inset(-30px 100% -30px -30px); } to { clip-path: inset(-30px -30px -30px -30px); } }
@keyframes wl { from { clip-path: inset(-30px -30px -30px 100%); } to { clip-path: inset(-30px -30px -30px -30px); } }
@keyframes wd { from { clip-path: inset(-30px -30px 100% -30px); } to { clip-path: inset(-30px -30px -30px -30px); } }
@keyframes wu { from { clip-path: inset(100% -30px -30px -30px); } to { clip-path: inset(-30px -30px -30px -30px); } }
.paused *, .paused *::before, .paused *::after { animation-play-state: paused !important; }
'''

PAGE_CSS = r'''
/* ---------- Scene 0: opening ---------- */
.opening .wrap { display: flex; flex-direction: column; gap: 18px; }
.top { display: flex; justify-content: space-between; align-items: center; gap: 12px 20px; flex-wrap: wrap; }
.top .logo { display: block; width: 150px; }
.top .logo svg { display: block; width: 100%; height: auto; }
.top nav { display: flex; gap: 4px 20px; flex-wrap: wrap; }
.top nav a { font-family: var(--f-mono); font-size: 14px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); text-decoration: none; min-height: 32px; display: inline-flex; align-items: center; }
.top nav a:hover { color: var(--text); }
.opening.scene { padding-top: 16px; align-content: stretch; }
.no-js .opening.scene { padding-top: 56px; }
.opening .wrap { min-height: calc(100svh - 44px); gap: 12px; }
.open-body { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 12px; }
.eyebrow { font-family: var(--f-mono); font-size: 14px; text-transform: uppercase; letter-spacing: .04em; color: var(--muted); }
@media (min-width: 40rem) { .eyebrow { font-size: 15px; letter-spacing: .06em; } }
.title { font-family: var(--f-stencil); font-weight: 900; text-transform: uppercase; font-size: clamp(4rem, 16vw, 9rem); line-height: .86; letter-spacing: .01em; }
.lead { font-size: 1.375rem; line-height: 1.35; max-width: 30ch; }
@media (min-width: 40rem) { .lead { font-size: 1.5rem; } }
.opening .stagecol { max-width: 640px; margin-top: 6px; }
.after { font-size: 1.1875rem; color: var(--muted); max-width: 40ch; }
@media (min-width: 64rem) { .after { font-size: 1.25rem; } }
.start {
  align-self: flex-start; font-family: var(--f-mono); font-size: 15px; text-transform: uppercase; letter-spacing: .06em; font-weight: 600;
  text-decoration: none; border: 1.5px solid var(--text); border-radius: 4px; padding: 0 16px; min-height: 44px; display: inline-flex; align-items: center;
}
.start:hover, .start.is-ready { border-color: var(--accent); }
.start { transition: border-color 400ms linear; }

/* ---------- Scene 1: Wren Street ---------- */
.cast { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.cast li { display: flex; flex-direction: column; gap: 4px; min-width: 0; }
.tok64 { width: 48px; height: 48px; }
.tok64 .obj { stroke-width: 2.5; }
.cast .cn { font-family: var(--f-head); font-weight: 800; font-size: 1.5rem; text-transform: uppercase; line-height: 1; }
.cast .cr { font-size: 16px; line-height: 1.35; color: var(--muted); }
@media (min-width: 64rem) {
  .cast { gap: 32px; }
  .cast li { border-top: 1px solid var(--line); padding-top: 14px; display: grid; grid-template-columns: 64px 1fr; column-gap: 14px; align-items: center; }
  .tok64 { width: 64px; height: 64px; grid-row: span 2; }
  .cast .cn { font-size: 1.75rem; align-self: end; }
  .cast .cr { font-size: 18px; align-self: start; }
}
.ws-dia { display: block; width: 100%; max-width: 560px; height: auto; }
.ws-dot { fill: var(--muted); }
.ws-t { fill: none; stroke: var(--line); stroke-width: 1.5; }
.ws-dia .obj { stroke-width: 2; }
.ws-dia text.ini { font-size: 11px; }
.trigger { font-size: 1.25rem; line-height: 1.4; max-width: 34ch; }
@media (min-width: 40rem) { .trigger { font-size: 1.375rem; } }
.small { font-size: 1.125rem; color: var(--muted); max-width: 40ch; }
.wren .wrap { display: flex; flex-direction: column; gap: 18px; }
@media (min-width: 64rem) {
  .wren .two { display: grid; grid-template-columns: minmax(0, 6fr) minmax(0, 5fr); gap: 48px; align-items: center; }
}
.wren .two { display: flex; flex-direction: column; gap: 18px; }
@media (min-width: 64rem) { .wren .two { display: grid; } }
.wren .words { display: flex; flex-direction: column; gap: 12px; }
.ws-dia.is-playing .ws-p { animation: in 250ms linear calc(var(--i) * 40ms) backwards; }
.ws-dia.is-playing .ws-t { animation: in 200ms linear calc(400ms + var(--i) * 25ms) backwards; }

/* ---------- Scene 9: the year ---------- */
.year .wrap { display: flex; flex-direction: column; gap: 16px; }
.year .grid { display: flex; flex-direction: column; gap: 20px; }
@media (min-width: 64rem) { .year .grid { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 48px; align-items: start; } }
.year .left { display: flex; flex-direction: column; gap: 16px; }
.year .line { font-size: 1.25rem; line-height: 1.4; max-width: 34ch; }
@media (min-width: 40rem) { .year .line { font-size: 1.375rem; } }
.year .hull { display: block; width: 100%; max-width: 560px; height: auto; }
.hull .c { fill: none; stroke: var(--line); stroke-width: 1.5; }
.hull .c.done { fill: var(--text); stroke: var(--text); }
.hull .c.lit { fill: var(--accent); stroke: var(--accent); }
.hull .bow { fill: none; stroke: var(--line); stroke-width: 1.5; }
.hull .bow.done { fill: var(--text); stroke: var(--text); }
.ledger { list-style: none; padding: 0; border-top: 1px solid var(--line); }
.ledger li { border-bottom: 1px solid var(--line); }
.ledger a { display: grid; grid-template-columns: 5.5rem minmax(0, 1fr); grid-template-areas: "m w" "m h"; column-gap: 12px; padding: 8px 0; text-decoration: none; }
.ledger a:hover .lh { color: var(--accent-ink); }
.ledger .lm { grid-area: m; font-family: var(--f-mono); font-size: 14px; letter-spacing: .06em; color: var(--accent-ink); padding-top: 3px; }
.ledger .lw { grid-area: w; font-size: 17px; line-height: 1.3; }
.ledger .lh { grid-area: h; font-family: var(--f-head); font-weight: 800; font-size: 1.25rem; text-transform: uppercase; line-height: 1.1; }
@media (min-width: 64rem) {
  .ledger a { grid-template-columns: 6rem minmax(0, 1fr) minmax(0, 1fr); grid-template-areas: "m w h"; align-items: baseline; padding: 9px 0; }
  .ledger .lw { font-size: 18px; } .ledger .lh { font-size: 1.375rem; }
}
.costs h3 { font-family: var(--f-mono); font-size: 14px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); font-weight: 600; margin-bottom: 6px; }
.costs ul { margin: 0; padding-left: 1.1rem; display: flex; flex-direction: column; gap: 3px; font-size: 17px; line-height: 1.4; }
.year.is-playing .hull .c { animation: yfill 250ms linear backwards; }
.year.is-playing .ledger li { animation: rowin 250ms var(--ease-out) backwards; }
.year.is-playing .hull .bow { animation: yfill 250ms linear 1260ms backwards; }
.year.is-playing .hull .c:nth-of-type(7) { animation: y7 700ms linear 1080ms backwards; }
@keyframes yfill { from { fill: transparent; stroke: var(--line); } }
@keyframes y7 { 0% { fill: transparent; stroke: var(--line); } 1% { fill: var(--accent); stroke: var(--accent); } 64% { fill: var(--accent); stroke: var(--accent); } }
@keyframes rowin { from { opacity: 0; transform: translateY(6px); } }
STAGGER

/* ---------- Scene 10: build your own ---------- */
.build .wrap { display: flex; flex-direction: column; gap: 20px; }
.ways { display: grid; grid-template-columns: 1fr; gap: 20px; }
@media (min-width: 48rem) { .ways { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px; } }
.ways > div { border-top: 2px solid var(--text); padding-top: 12px; display: flex; flex-direction: column; gap: 8px; }
.ways > div.us { border-top-color: var(--accent); }
.ways .wl { font-family: var(--f-mono); font-size: 14px; text-transform: uppercase; letter-spacing: .06em; font-weight: 600; }
.ways a { font-weight: 600; align-self: flex-start; min-height: 32px; display: inline-flex; align-items: center; }
footer { border-top: 1px solid var(--line); padding-top: 16px; margin-top: 12px; color: var(--muted); font-size: 16px; display: flex; flex-direction: column; gap: 8px; }
footer .logo { display: block; width: 140px; margin-top: 6px; }
footer .logo svg { display: block; width: 100%; height: auto; }
'''


def stagger():
    out = []
    for i in range(1, 8):
        out.append(f".year.is-playing .hull .c:nth-of-type({i}) {{ animation-delay: {(i - 1) * 180}ms; }}")
        out.append(f".year.is-playing .ledger li:nth-child({i}) {{ animation-delay: {(i - 1) * 180}ms; }}")
    out.append(".year.is-playing .hull .c:nth-of-type(7) { animation-delay: 1080ms; }")
    return "\n".join(out)


def arr(label):
    """A Next link's label, its arrow wrapped so the highlight can nudge it."""
    assert label.endswith(" ↓")
    return label[:-2] + '&nbsp;<span class="arr" aria-hidden="true">↓</span>'


def control():
    return '''<div class="control">
<div class="seg" role="group" aria-label="Compare">
<button type="button" class="b-without" data-set="without" aria-pressed="false"><span class="dot" aria-hidden="true"></span><span class="btn-long">Without the wall</span><span class="btn-short">Without</span></button>
<button type="button" class="b-with" data-set="with" aria-pressed="true"><span class="dot" aria-hidden="true"></span><span class="go" aria-hidden="true">→</span><span class="btn-long">With the wall</span><span class="btn-short">With</span></button>
</div>
<button type="button" class="replay" aria-label="Replay"><span class="face f-replay" aria-hidden="true"><span class="glyph">↻</span><span class="rl">Replay</span></span><span class="face f-pause" aria-hidden="true"><svg class="bars" viewBox="0 0 10 12"><rect x="0" y="0" width="3" height="12"/><rect x="7" y="0" width="3" height="12"/></svg><span class="rl">Pause</span></span></button>
</div>'''


def stagecol(sid, svg, cap_without, cap_with, alt_without, alt_with, legend=""):
    lg = f'<div class="legend">{legend}</div>' if legend else ""
    return f'''<div class="stagecol">
<figure class="stage" id="{sid}" data-state="with">
<p class="state-tag" aria-hidden="true"><span class="st-without">Without the wall</span><span class="st-with">With the wall</span></p>
{svg}
{lg}
<p class="vh" id="{sid}-alt-without">{alt_without}</p>
<p class="vh" id="{sid}-alt-with">{alt_with}</p>
</figure>
{control()}
<p class="caption" aria-live="polite"><span class="cap cap-without"><span class="cap-tag">WITHOUT THE WALL</span>{cap_without}</span><span class="cap cap-with"><span class="cap-tag">WITH THE WALL</span>{cap_with}</span></p>
</div>'''


WALLS = [
    dict(id="work-email", n=1, sid="s2", meta="WALL 1 OF 7 · JUNE", name="Sign in with Google",
         hook="Friday is the sales lead’s last day. Priya does the offboarding.",
         cw="[[Three tools stay open.]] They were signed up with a personal email.",
         ch="[[One switch closes most doors.]] A short list closes the rest.",
         take="You can’t take back access [[the company never handed out]].",
         what="[[Turn off one account.]] When everyone signs in to every tool with their company Google account, that one switch stops a leaver signing in anywhere. A short list closes the few tools that keep them signed in.",
         time="Half a day for the admin; 30 minutes per person",
         pay="A Google Workspace Business Starter seat per person",
         legend='<span><span class="gl" aria-hidden="true">G</span>= signs in with Google</span><span>••• = its own password</span>',
         nxt="NEXT: PASSWORD MANAGER ↓", nxt_id="password-manager",
         aw="The sales lead leaves Wren Street. Turning off their company account closes mail, drive and docs, but three tools signed up with a personal email stay open.",
         ah="Every tool signs in with the company account. Priya turns it off, ticks two tools on a short offboarding list, and the sales lead leaves with nothing still open."),
    dict(id="password-manager", n=2, sid="s3", meta="WALL 2 OF 7 · AUGUST", name="Password manager",
         hook="A cycling forum Theo forgot about was breached. His old password leaked.",
         cw="[[Sunset2019! on every site.]] One leak opens them all.",
         ch="[[A different random password on each site.]] The leak opens only the old forum.",
         what="[[A different password for every site.]] 1Password makes each one long and random, and fills it in. When one site leaks, that password opens nothing else. Theo remembers one password; 1Password remembers the rest.",
         take="Leaks happen on sites you don’t control. [[Unique passwords keep them there.]]",
         time="2 hours for the admin; 30–60 minutes per person",
         pay="A 1Password Business subscription per person",
         nxt="NEXT: HARDWARE KEY ↓", nxt_id="hardware-keys",
         aw="An old forum is breached and Theo’s password, Sunset2019!, leaks. He used it everywhere, so it opens his cloud, payments, code and design accounts.",
         ah="An old forum leaks Theo’s old password, Sunset2019!. His cloud, payments, code and design accounts each have their own random password from 1Password, so the leaked one opens none of them."),
    dict(id="hardware-keys", n=3, sid="s4", meta="WALL 3 OF 7 · OCTOBER", name="Hardware key",
         hook="Maya gets a perfect fake: “Storage full. Sign in to keep your mail.”",
         cw="[[Password and code are just text.]] The fake page passes both on.",
         ch="[[The stranger needs her key.]] The fake gets her password, but the key stays on Maya’s keychain.",
         take="Anything typed can be passed on. [[A key has to be in your hand.]]",
         what="[[The key never leaves your hand.]] A six-digit code is just text: a fake page can pass it on, and a code kept in the vault falls with the password. A key’s secret can’t be copied, and it answers only the real site.",
         time="2 hours for the admin; 30 minutes per person",
         pay="Two security keys per person (YubiKey 5C NFC)",
         nxt="NEXT: SEPARATE ADMIN ACCOUNTS ↓", nxt_id="admin-split",
         aw="On a look-alike Google page, Maya types her password and the six-digit code from her app. The page passes both to a stranger, who signs in to her mail.",
         ah="Maya’s key is plugged into her laptop. The look-alike page passes on her password, but on the wrong site her key stays dark and nothing from it crosses. The stranger is asked to touch a key they don’t have."),
    dict(id="admin-split", n=4, sid="s5", meta="WALL 4 OF 7 · THE SAME OCTOBER EMAIL", name="Separate admin accounts",
         hook="What if that fake had caught the account that runs the company?",
         cw="[[One account does everything.]] Catch it, and you catch the company.",
         ch="[[<span class=\"addr\">maya@</span> holds no admin.]] Admin lives on <span class=\"addr\">maya-admin@</span>, behind a key.",
         what="[[Two accounts, two jobs.]] Maya’s everyday account reads mail and holds no admin, so catching it gets a stranger her inbox, not the company. Her admin account signs in only with her key and does nothing else.",
         take="Keep the power to change everything [[off the account that clicks links]].",
         time="2 hours for the admins; 15 minutes each quarter",
         pay="A Workspace seat per admin account, the spare included, and two keys for the spare",
         nxt="NEXT: ADMIN AUDIT ↓", nxt_id="admin-audit",
         aw="Maya has one account, maya@wrenstreet.example, for mail and for running the company. A fake sign-in catches it, and with it her mail, her docs, adding people and changing settings: the whole company.",
         ah="Maya has two accounts side by side. maya@ reads mail and holds no admin; maya-admin@ only does admin and signs in with a key. A fake sign-in catches maya@ and gets her mail and docs, but stops at the wall. Theo has an admin account too, and a break-glass account has two keys kept in two places."),
    dict(id="admin-audit", n=5, sid="s6", meta="WALL 5 OF 7 · JANUARY", name="Admin audit",
         hook="Priya asks the assistant: who is an admin of what?",
         cw="[[31 admin seats for nine people.]] One is held by a contractor long gone.",
         ch="[[Two admins per tool.]] The assistant drafts the table; Priya cuts it, one seat at a time.",
         take="[[Every extra admin]] is one more account worth stealing.",
         what="[[List every admin, then cut.]] Admin rights pile up, on people who left and on tools nobody checks. The audit keeps each role to the few who need it, and is checked again each quarter.",
         time="2–3 hours for an admin, with the assistant; 30 minutes each quarter",
         pay="Nothing to buy, unless a smaller Google role needs another admin seat",
         legend='<span>● = an admin seat</span>',
         nxt="NEXT: PHONE NUMBER LOCK ↓", nxt_id="phone-sim",
         aw="A table of nine tools and Wren Street’s people shows 31 admin seats. One, on the payments tool, belongs to a contractor who left, and an attack comes in through it.",
         ah="The assistant builds the table of 31 admin seats. Priya removes them one at a time, the ex-contractor’s first, down to two per tool, and books the next review for April."),
    dict(id="phone-sim", n=6, sid="s7", meta="WALL 6 OF 7 · MARCH", name="Phone number lock",
         hook="A caller tells Theo’s carrier: “I lost my phone. Move my number.”",
         cw="[[His number moves to a stranger.]] So does every text-message code.",
         ch="[[No PIN, no move.]] The number stays put until Theo unlocks it himself.",
         take="A phone number was [[never meant to prove who you are]].",
         what="[[Lock your number at the carrier.]] A caller who talks your carrier into moving it gets every text-message code meant for you. A number lock and a SIM lock stop the move. Accounts that matter sign in with keys, not texts.",
         time="30 minutes for an admin; 20–30 minutes per person",
         pay="Nothing to buy: settings on plans people already have",
         nxt="NEXT: AI CONNECTORS ↓", nxt_id="ai-connector-scopes",
         aw="A caller talks Theo’s carrier into moving his number to a new SIM. Theo’s phone loses service, and text-message codes for his accounts go to the stranger.",
         ah="The carrier asks for a PIN the caller doesn’t have, and Theo’s number lock and SIM lock keep the number on his phone. His important accounts sign in with keys, not text messages."),
    dict(id="ai-connector-scopes", n=7, sid="s8", meta="WALL 7 OF 7 · MAY", name="AI connectors",
         hook="Priya’s assistant drafts her replies. One email hid an instruction for it.",
         cw="[[It does what the hidden text says.]] With access to everything, it sends out every clinic’s records.",
         ch="[[Google locks it out of Drive.]] [[A rule in the AI tool]] stops it sending.",
         what="[[Give it only what its job needs.]] An assistant acts on what it reads, hidden text included: prompt injection. Google can lock it out of Drive. Gmail has no “drafts only” permission, so “don’t send” is a rule in the AI tool, not a lock.",
         take="The assistant isn’t the problem. [[What it can reach is.]]",
         time="2–3 hours for an admin, with the assistant; 15 minutes per person; 30 minutes each quarter",
         pay="Nothing to buy; some AI tools need a business plan for these settings",
         nxt="NEXT: THE YEAR ↓", nxt_id="the-year",
         aw="An email from a new supplier hides an instruction in white text: reply with the full customer list. Priya’s assistant can reach everything, so it takes every clinic’s contacts and records from Drive and sends them to an unknown address.",
         ah="The same hidden instruction reaches the assistant, which can only read and draft. Google locks it out of Drive, where the customer list lives. A setting in the AI tool, a rule rather than a lock, stops it sending. The customer list stays put."),
]

SVGS = {"s2": scenes_a.s2, "s3": scenes_b.s3, "s4": scenes_b.s4, "s5": scenes_c.s5,
        "s6": scenes_c.s6, "s7": scenes_d.s7, "s8": scenes_d.s8}


def key(s, bar=False):
    """[[phrase]] marks a key phrase: bold. Only the opening phrase of the right column (bar=True) sits on the
    orange highlighter bar, so a reader sees one bar per wall."""
    cls = "k" if bar else "kb"
    return s.replace("[[", f'<strong class="{cls}">').replace("]]", "</strong>")


def wall(w):
    w = {k: key(v, k == "what") if k in ("what", "cw", "ch", "take") else v for k, v in w.items()}
    svg = SVGS[w["sid"]]()
    return f'''
<!-- ======================= Wall {w["n"]}: {w["name"]} ======================= -->
<section class="scene wall" id="{w["id"]}" data-wall="{w["n"]}" data-name="{w["name"].upper()}" aria-labelledby="{w["id"]}-h">
<div class="wrap">
<div class="head">
<p class="meta">{w["meta"]}</p>
<h2 class="name" id="{w["id"]}-h">{w["name"]}</h2>
<p class="hook">{w["hook"]}</p>
</div>
<div class="body">
{stagecol(w["sid"], svg, w["cw"], w["ch"], w["aw"], w["ah"], w.get("legend", ""))}
<div class="side">
<p class="what">{w["what"]}</p>
<p class="takeaway">{w["take"]}</p>
<dl class="chips"><dt>Time</dt><dd>{w["time"]}</dd><dt>You pay for</dt><dd>{w["pay"]}</dd></dl>
<a class="modlink" href="{MOD}{w["id"]}.md" aria-label="Read the {w["name"].lower()} module on GitHub">Read the module →</a>
<a class="next" href="#{w["nxt_id"]}">{arr(w["nxt"])}</a>
</div>
</div>
</div>
</section>'''


def tok64(ch):
    return (f'<svg class="tok64" viewBox="0 0 64 64" aria-hidden="true"><circle class="obj" cx="32" cy="32" r="28"/>'
            f'<text class="ini" x="32" y="43" text-anchor="middle" style="font-size:31px">{ch}</text></svg>')


LEDGER = [
    ("work-email", "JUNE", "The sales lead leaves", "SIGN IN WITH GOOGLE"),
    ("password-manager", "AUGUST", "An old password leaks", "PASSWORD MANAGER"),
    ("hardware-keys", "OCTOBER", "A perfect fake sign-in page", "HARDWARE KEY"),
    ("admin-split", "OCTOBER", "The same fake, aimed at an admin", "SEPARATE ADMIN ACCOUNTS"),
    ("admin-audit", "JANUARY", "31 admin seats for nine people", "ADMIN AUDIT"),
    ("phone-sim", "MARCH", "A call to the phone carrier", "PHONE NUMBER LOCK"),
    ("ai-connector-scopes", "MAY", "An email written for the assistant", "AI CONNECTORS"),
]

JS = (Path(__file__).parent / "page.js").read_text()


def main():
    s0svg = scenes_a.s0()
    s1svg = scenes_a.s1()
    walls = "".join(wall(w) for w in WALLS)
    ledger = "".join(f'<li><a href="#{i}"><span class="lm">{m}</span><span class="lw">{wc}</span><span class="lh">{h}</span></a></li>' for i, m, wc, h in LEDGER)
    s0col = stagecol("s0", s0svg, "No walls inside: one breach floods the whole hull.",
                     "Walls inside: the water stays in one compartment.",
                     "A hull seen from above with no walls inside. Water from one crack spreads through the whole hull.",
                     "A hull seen from above, cut into seven compartments. Water from one crack fills one compartment and stops.")
    html = f'''<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{HEAD}
<meta name="claude:viewport-fit-sides" content="cover">
<!--FONTS-->
<style>
/* Seven Walls v4. Each scene is one screen: name, hook, animated stage, one caption, one takeaway.
   Motion rule: every element's base CSS is its final pose; animations describe only where it comes from. */
{BASE_CSS}
{PAGE_CSS.replace("STAGGER", stagger())}
/* ---------- Scene stages: base poses and sequences (Without / With) ---------- */
{chr(10).join(KF)}
{chr(10).join(CSS)}
</style>
</head>
<body>

<header class="hullbar" aria-label="Progress">
<div class="in">
<nav aria-label="The seven walls"><!--HULLNAV--></nav>
<p class="hb-label" aria-hidden="true"><span class="hb-n"></span><span class="hb-name"></span></p>
</div>
</header>

<main>

<!-- ======================= Scene 0: opening ======================= -->
<section class="scene opening" id="top" aria-labelledby="top-h">
<div class="wrap">
<header class="top">
<a class="logo" href="https://bulkheadlabs.com" aria-label="Bulkhead Labs"><!--LOGO--></a>
<nav aria-label="Elsewhere">
<a href="https://github.com/bulkhead-labs/opsec-baseline">The modules</a>
<a href="https://github.com/bulkhead-labs/opsec-baseline/blob/main/AGENTS.md">For your agent</a>
</nav>
</header>
<div class="open-body">
<p class="eyebrow">OPSEC BASELINE · ONE COMPANY, ONE YEAR</p>
<h1 class="title" id="top-h">Seven Walls</h1>
<p class="lead">A ship doesn’t sink because water gets in. It sinks when nothing stops the water.</p>
{s0col}
<p class="after">This is one small company’s year, and the seven walls that held.</p>
<a class="start" href="#wren-street">{arr("MEET WREN STREET ↓")}</a>
</div>
</div>
</section>

<!-- ======================= Scene 1: Wren Street ======================= -->
<section class="scene wren" id="wren-street" aria-labelledby="wren-h">
<div class="wrap">
<div class="head">
<p class="meta">THE COMPANY</p>
<h2 class="name" id="wren-h">Wren Street</h2>
<p class="hook">Booking software for physio clinics. Nine people, forty online tools, nobody on security.</p>
</div>
<div class="two">
<div class="words">
{s1svg}
<ul class="cast">
<li>{tok64("M")}<span class="cn">Maya</span><span class="cr">Co-founder. Runs the company.</span></li>
<li>{tok64("T")}<span class="cn">Theo</span><span class="cr">Co-founder. Runs the product.</span></li>
<li>{tok64("P")}<span class="cn">Priya</span><span class="cr">Operations. Keeps the tools running.</span></li>
</ul>
</div>
<div class="words">
<p class="trigger">Last spring, a fake invoice in Wren Street’s name nearly got paid. So they built seven walls, an afternoon or two each.</p>
<p class="small">Their AI assistant did the reading. A person did anything that could lock someone out.</p>
<a class="next" href="#work-email">{arr("WALL 1: SIGN IN WITH GOOGLE ↓")}</a>
</div>
</div>
</div>
</section>
{walls}

<!-- ======================= Scene 9: the year ======================= -->
<section class="scene year" id="the-year" aria-labelledby="year-h">
<div class="wrap">
<div class="head">
<p class="meta">MAY · ONE YEAR ON</p>
<h2 class="name" id="year-h">One year. Seven walls.</h2>
</div>
<div class="grid">
<div class="left">
<p class="line">Nothing dramatic. Each time, something got in, met a wall, and stopped there.</p>
<!--HULL:8-->
</div>
<div class="left">
<ol class="ledger">{ledger}</ol>
<div class="costs">
<h3>What it cost them</h3>
<ul>
<li>About a month of afternoons, mostly Priya’s, with the assistant reading and keeping the checklist.</li>
<li>A Google Workspace seat and a 1Password seat per person.</li>
<li>Two hardware keys per person.</li>
<li>A Workspace seat per admin account, the spare included, and two keys for the spare.</li>
</ul>
</div>
<a class="next" href="#build-your-own">{arr("NEXT: BUILD YOUR OWN ↓")}</a>
</div>
</div>
</div>
</section>

<!-- ======================= Scene 10: build your own ======================= -->
<section class="scene build" id="build-your-own" aria-labelledby="build-h">
<div class="wrap">
<div class="head">
<p class="meta">YOUR TURN</p>
<h2 class="name" id="build-h">Build your own</h2>
</div>
<div class="ways">
<div><p class="wl">With your AI assistant</p><p>Give it the prompt in the repo’s README. It reads only the walls you name and stops for a person at every step that could lock someone out.</p><a href="https://github.com/bulkhead-labs/opsec-baseline#use-it-with-your-agent">The prompt →</a></div>
<div><p class="wl">By hand</p><p>Each wall is one page: what done looks like, then the steps, in order.</p><a href="https://github.com/bulkhead-labs/opsec-baseline/tree/main/modules">The modules →</a></div>
<div class="us"><p class="wl">With us</p><p>After a call, Bulkhead Labs builds a plan for your team from these walls: your walls, in your order, and why each matters to you.</p><a href="https://bulkheadlabs.com">bulkheadlabs.com →</a></div>
</div>
<a class="back" href="#top">Back to the top ↑</a>
<footer>
<p>Wren Street and its people are invented. The attacks are real and common.</p>
<p>From <a href="https://bulkheadlabs.com">Bulkhead Labs</a>. Text under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>: copy and adapt it, with credit. The name and logo are not covered by that licence.</p>
<a class="logo" href="https://bulkheadlabs.com" aria-label="Bulkhead Labs"><!--LOGO--></a>
</footer>
</div>
</section>

</main>

<script>
{JS}
</script>
</body>
</html>
'''
    # Without always runs longer than With: With's sequence may be at most 1500ms longer than Without's.
    for sid in ["s0"] + [w["sid"] for w in WALLS]:
        wo, wi = END[sid, "without"], END[sid, "with"]
        assert wi - wo < 1500, f"{sid}: With runs {wi}ms against Without's {wo}ms"
        print(f"  {sid}: without {wo}ms, with {wi}ms")
    for w in WALLS:
        n = len(w["what"].split())
        for f in ("what", "cw", "ch", "take"):
            assert w[f].count("[[") == w[f].count("]]") >= 1, f'{w["id"]}: {f} needs a key phrase'
            assert w[f].count("[[") <= 2, f'{w["id"]}: {f} has more than two key phrases'
        assert n <= 45, f'{w["id"]}: .what has {n} words'
        assert w["what"].startswith("[[") and w["what"].count("[[") == 1, f'{w["id"]}: one bar, on the opening phrase'
    OUT.write_text(html)
    print("wrote", OUT, len(html))


main()
