(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");
  var RM = window.matchMedia("(prefers-reduced-motion: reduce)");
  var reduced = function () { return RM.matches; };
  var HOLD = 1000;  // ms the Without frame holds before autoplay moves to With

  // ---------- Stages: Without / With, Replay, autoplay ----------
  var COUNTS = { s6: { without: 31, "with": 18 } };

  function Stage(fig) {
    this.fig = fig;
    this.col = fig.parentNode;
    this.svg = fig.querySelector("svg");
    this.btns = this.col.querySelectorAll(".seg button");
    this.caps = { without: this.col.querySelector(".cap-without"), "with": this.col.querySelector(".cap-with") };
    this.auto = false;
    this.timer = 0;
    this.count = fig.querySelector(".cnum");
    this.n = 0;
    this.caps.without.hidden = this.state() !== "without";
    this.caps["with"].hidden = this.state() !== "with";
    var self = this;
    for (var i = 0; i < this.btns.length; i++) {
      this.btns[i].addEventListener("click", function () { self.cancel(); self.show(this.getAttribute("data-set"), true); });
    }
    this.col.querySelector(".replay").addEventListener("click", function () { self.cancel(); self.show(self.state(), true); });
    fig.addEventListener("animationend", function (e) {
      var p = fig.getAttribute("data-play");
      if (p && e.target.classList && e.target.classList.contains("last-" + p)) self.done(p);
    });
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
  Stage.prototype.cancel = function () { this.touched = true; this.auto = false; clearTimeout(this.timer); };
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
      fig.setAttribute("data-play", state);
      fig.classList.add("is-playing");
    }
  };
  Stage.prototype.done = function (state) {
    var self = this;
    this.fig.removeAttribute("data-play");
    this.fig.classList.remove("is-playing");
    if (this.count) this.count.textContent = String(COUNTS[this.fig.id][state]);
    if (this.auto && state === "without") {
      this.timer = setTimeout(function () {
        if (!self.auto) return;
        self.auto = false;
        self.show("with", true);
      }, HOLD);
    } else {
      this.auto = false;
    }
  };
  Stage.prototype.autoplay = function () {
    if (reduced() || this.touched) return;
    this.auto = true;
    this.show("without", true);
  };

  var stages = {};
  var figs = document.querySelectorAll(".stage");
  for (var i = 0; i < figs.length; i++) stages[figs[i].id] = new Stage(figs[i]);

  // The opening hull plays on load, once the fonts are in or after 300ms.
  var opened = false;
  function openHull() { if (!opened) { opened = true; stages.s0.autoplay(); } }
  setTimeout(openHull, 300);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(openHull);

  // Every other stage plays once, the first time it is 60% in view.
  var once = function (el, fn) {
    if (!("IntersectionObserver" in window)) return;
    var io = new IntersectionObserver(function (es) {
      for (var k = 0; k < es.length; k++) {
        if (es[k].isIntersecting) { io.disconnect(); fn(); }
      }
    }, { threshold: 0.6 });
    io.observe(el);
  };
  Object.keys(stages).forEach(function (id) {
    if (id !== "s0") once(stages[id].svg, function () { stages[id].autoplay(); });
  });
  var playOnce = function (el, target) {
    once(el, function () { if (!reduced()) (target || el).classList.add("is-playing"); });
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

  // ---------- Pause everything while the tab is hidden ----------
  document.addEventListener("visibilitychange", function () { root.classList.toggle("paused", document.hidden); });
})();
