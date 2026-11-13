(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");
  var RM = window.matchMedia("(prefers-reduced-motion: reduce)");
  var reduced = function () { return RM.matches; };
  var HOVER = window.matchMedia("(hover: hover)");
  var HOLD = { without: 5000, "with": 3500 };  // ms each state's final frame holds while the stage cycles
  var RESUME = 1500;                             // the least a hold runs after a pause ends
  var CYCLES = 3;                                // Without, With, three times; then rest on With
  var other = function (s) { return s === "with" ? "without" : "with"; };

  // ---------- Seen: an element at least half in view (or filling half the screen, if it is taller) ----------
  var TH = [];
  for (var t = 0; t <= 20; t++) TH.push(t / 20);
  function seen(el, fn, every) {
    if (!("IntersectionObserver" in window)) return;
    var io = new IntersectionObserver(function (es) {
      var e = es[es.length - 1];
      var on = e.isIntersecting && (e.intersectionRatio >= 0.5 || e.intersectionRect.height >= window.innerHeight / 2);
      if (every) fn(on);
      else if (on) { io.disconnect(); fn(); }
    }, { threshold: TH });
    io.observe(el);
  }

  // ---------- The Next highlight: once the scene has been seen, the way on is lit ----------
  function ready(sec) {
    var link = sec && sec.querySelector(".next, .start");
    if (link) link.classList.add("is-ready");
  }

  // ---------- Stages: Without / With, the cycle, Pause and Replay ----------
  var COUNTS = { s6: { without: 31, "with": 18 } };

  function Stage(fig) {
    var self = this;
    this.fig = fig;
    this.col = fig.parentNode;
    this.sec = fig.closest("section");
    this.svg = fig.querySelector("svg");
    this.btns = this.col.querySelectorAll(".seg button");
    this.ctl = this.col.querySelector(".replay");
    this.cap = this.col.querySelector(".caption");
    this.caps = { without: this.col.querySelector(".cap-without"), "with": this.col.querySelector(".cap-with") };
    this.cycling = false;   // the cycle is running
    this.stopped = false;   // the reader took control, or the cycle finished: it never starts again
    this.cycles = 0;        // With holds completed
    this.phase = "";        // "play" while a sequence runs, "hold" while its final frame holds
    this.remaining = 0;     // ms left in the current hold
    this.timer = 0;
    this.why = { hover: false, focus: false, offscreen: false, hidden: document.hidden };  // pause reasons
    this.shown = {};        // states the reader showed with the buttons
    this.count = fig.querySelector(".cnum");
    this.n = 0;
    this.caps.without.hidden = this.state() !== "without";
    this.caps["with"].hidden = this.state() !== "with";
    for (var i = 0; i < this.btns.length; i++) {
      this.btns[i].addEventListener("click", function () {
        var s = this.getAttribute("data-set");
        self.stop();
        self.shown[s] = true;
        self.show(s, true);
      });
    }
    this.ctl.addEventListener("click", function () {
      var cycling = self.cycling;
      self.stop();
      if (!cycling) self.show(self.state(), true);  // Replay; a Pause lets the current state finish and hold
    });
    fig.addEventListener("animationend", function (e) {
      var p = fig.getAttribute("data-play");
      if (p && e.target.classList && e.target.classList.contains("last-" + p)) self.done(p);
    });
    if (HOVER.matches) {
      this.col.addEventListener("mouseenter", function () { self.pause("hover", true); });
      this.col.addEventListener("mouseleave", function () { self.pause("hover", false); });
    }
    this.col.addEventListener("focusin", function () { self.pause("focus", true); });
    this.col.addEventListener("focusout", function (e) { if (!self.col.contains(e.relatedTarget)) self.pause("focus", false); });
    if (this.count) {
      fig.addEventListener("animationstart", function (e) {
        if (!fig.getAttribute("data-play")) return;
        if (e.animationName === "pop" && e.target.classList.contains("dot")) self.n++;
        else if (e.animationName === "shrink") self.n--;
        else return;
        self.count.textContent = String(self.n);
      });
    }
  }
  Stage.prototype.state = function () { return this.fig.getAttribute("data-state"); };
  // The third button's face, and whether the caption is read out: not while it changes every few seconds.
  Stage.prototype.face = function () {
    this.ctl.classList.toggle("is-pause", this.cycling);
    this.ctl.setAttribute("aria-label", this.cycling ? "Pause" : "Replay");
    this.cap.setAttribute("aria-live", this.cycling ? "off" : "polite");
  };
  Stage.prototype.start = function () {
    if (reduced() || this.stopped || this.cycling) return;
    this.cycling = true;
    this.face();
    this.show("without", true);
  };
  Stage.prototype.stop = function () {
    this.cycling = false;
    this.stopped = true;
    if (this.phase === "hold") this.phase = "";
    clearTimeout(this.timer);
    this.timer = 0;
    this.face();
  };
  Stage.prototype.show = function (state, animate) {
    var fig = this.fig;
    fig.removeAttribute("data-play");
    fig.classList.remove("is-playing");
    void fig.offsetWidth;  // restart every sequence from frame 0
    fig.setAttribute("data-state", state);
    for (var i = 0; i < this.btns.length; i++) {
      this.btns[i].setAttribute("aria-pressed", String(this.btns[i].getAttribute("data-set") === state));
    }
    this.caps.without.hidden = state !== "without";
    this.caps["with"].hidden = state !== "with";
    this.svg.setAttribute("aria-labelledby", fig.id + "-alt-" + state);
    var play = animate && !reduced();
    if (this.count) {
      this.n = 0;
      this.count.textContent = String(play ? 0 : COUNTS[fig.id][state]);
    }
    if (play) {
      this.phase = "play";
      fig.setAttribute("data-play", state);
      fig.classList.add("is-playing");
    } else {
      this.played(state);
    }
  };
  // A sequence reached its last frame.
  Stage.prototype.done = function (state) {
    this.fig.removeAttribute("data-play");
    this.fig.classList.remove("is-playing");
    if (this.count) this.count.textContent = String(COUNTS[this.fig.id][state]);
    this.played(state);
  };
  Stage.prototype.played = function (state) {
    if (this.cycling) {
      this.phase = "hold";
      this.remaining = HOLD[state];
      this.run();
      return;
    }
    this.phase = "";
    if (this.shown[state] && this.shown.without && this.shown["with"]) ready(this.sec);
  };
  // The hold's timer runs only while nothing pauses it.
  Stage.prototype.run = function () {
    var w = this.why, self = this;
    if (!this.cycling || this.phase !== "hold" || this.timer || w.hover || w.focus || w.offscreen || w.hidden) return;
    this.t0 = Date.now();
    this.timer = setTimeout(function () { self.timer = 0; self.next(); }, this.remaining);
  };
  Stage.prototype.pause = function (why, on) {
    if (this.why[why] === on) return;
    this.why[why] = on;
    if (on) {
      if (this.timer) { clearTimeout(this.timer); this.timer = 0; this.remaining -= Date.now() - this.t0; }
      return;
    }
    // Back from a pointer or focus: what was left, but at least 1.5s. Back in view: 1.5s.
    if (this.phase === "hold") this.remaining = (why === "hover" || why === "focus") ? Math.max(this.remaining, RESUME) : RESUME;
    this.run();
  };
  Stage.prototype.next = function () {
    var s = this.state();
    if (s === "with") {
      this.cycles++;
      if (this.cycles === 1) ready(this.sec);
      if (this.cycles >= CYCLES) {  // rest on With
        this.cycling = false;
        this.stopped = true;
        this.phase = "";
        this.face();
        return;
      }
    }
    this.show(other(s), true);
  };

  var stages = {};
  var figs = document.querySelectorAll(".stage");
  for (var i = 0; i < figs.length; i++) stages[figs[i].id] = new Stage(figs[i]);

  // The opening hull cycles from load, once the fonts are in or after 300ms. Every other stage starts the first
  // time it is half in view. Out of view, a stage's hold waits.
  var opened = false;
  function openHull() { if (!opened) { opened = true; stages.s0.start(); } }
  setTimeout(openHull, 300);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(openHull);
  Object.keys(stages).forEach(function (id) {
    var st = stages[id], first = true;
    seen(st.svg, function (on) {
      st.pause("offscreen", !on);
      if (!on || !first) return;
      first = false;
      if (id !== "s0") st.start();
      if (!reduced()) setTimeout(function () { ready(st.sec); }, 20000);
    }, true);
  });
  // Scenes without a stage light their Next 6s after they are seen; under reduced motion, every scene does at 8s.
  var scenes = document.querySelectorAll("section.scene");
  Array.prototype.forEach.call(scenes, function (sec) {
    if (!sec.querySelector(".next, .start")) return;
    var wait = reduced() ? 8000 : sec.querySelector(".stage") ? 0 : 6000;
    if (wait) seen(sec, function () { setTimeout(function () { ready(sec); }, wait); });
  });

  var playOnce = function (el, target) {
    seen(el, function () { if (!reduced()) (target || el).classList.add("is-playing"); });
  };
  var dia = document.querySelector(".ws-dia");
  if (dia) playOnce(dia);
  var year = document.getElementById("the-year");
  if (year) playOnce(year.querySelector(".hull"), year);

  // ---------- The hull bar: progress and table of contents ----------
  var bar = document.querySelector(".hullbar");
  var links = bar.querySelectorAll(".hullnav a");
  var num = bar.querySelector(".hb-n");
  var nameEl = bar.querySelector(".hb-name");
  function setCurrent(sec) {
    var wall = parseInt(sec.getAttribute("data-wall") || "0", 10);
    if (sec.id === "the-year" || sec.id === "build-your-own") wall = 8;
    bar.classList.toggle("is-hidden", sec.id === "top");
    bar.classList.toggle("is-wren", sec.id === "wren-street");
    for (var k = 0; k < links.length; k++) {
      var w = k + 1;
      var shape = links[k].querySelector(".c, .bow");
      shape.classList.toggle("done", wall === 8 || w < wall);
      shape.classList.toggle("lit", w === wall && w <= 7);
      if (w === wall && w <= 7) links[k].setAttribute("aria-current", "step");
      else links[k].removeAttribute("aria-current");
    }
    if (sec.id === "wren-street") { num.textContent = ""; nameEl.textContent = "WREN STREET"; }
    else if (wall === 8) { num.textContent = "7 / 7"; nameEl.textContent = " · THE YEAR"; }
    else if (wall > 0) { num.textContent = wall + " / 7"; nameEl.textContent = " · " + sec.getAttribute("data-name"); }
  }
  bar.classList.add("is-hidden");
  if ("IntersectionObserver" in window) {
    var sio = new IntersectionObserver(function (es) {
      for (var k = 0; k < es.length; k++) if (es[k].isIntersecting) setCurrent(es[k].target);
    }, { rootMargin: "-50% 0px -50% 0px" });
    var secs = document.querySelectorAll("section.scene");
    for (var k = 0; k < secs.length; k++) sio.observe(secs[k]);
  }

  // ---------- A deep link lands on its scene ----------
  // Fonts arriving after the browser's own jump move the target, and snapping then settles past it.
  if (location.hash.length > 1) {
    var target = document.getElementById(location.hash.slice(1));
    var land = function () {
      if (!target) return;
      root.style.scrollBehavior = "auto";
      target.scrollIntoView();
      root.style.scrollBehavior = "";
    };
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(land); else window.addEventListener("load", land);
  }

  // ---------- Pause everything while the tab is hidden: the animations, and every hold's timer ----------
  document.addEventListener("visibilitychange", function () {
    root.classList.toggle("paused", document.hidden);
    Object.keys(stages).forEach(function (id) { stages[id].pause("hidden", document.hidden); });
  });
})();
