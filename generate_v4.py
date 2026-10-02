import sys
import re

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#070C09">
<title>The Unveiling — NSS IIIT Naya Raipur</title>
<meta name="description" content="Inauguration ceremony of the National Service Scheme website, IIIT Naya Raipur.">
<script>document.documentElement.className += ' js';</script>

<style>
/* ---------- fonts ---------- */
@font-face{font-family:'Fraunces';font-style:normal;font-weight:100 900;font-display:block;src:url('assets/fonts/fraunces-latin-wght-normal.woff2') format('woff2');}
@font-face{font-family:'Fraunces';font-style:italic;font-weight:100 900;font-display:block;src:url('assets/fonts/fraunces-latin-wght-italic.woff2') format('woff2');}
@font-face{font-family:'Work Sans';font-style:normal;font-weight:100 900;font-display:block;src:url('assets/fonts/work-sans-latin-wght-normal.woff2') format('woff2');}

:root{
  --ink:#070C09; --ink-2:#0B120E;
  --marigold:#E8A63C; --marigold-lit:#FBDC9E; --marigold-deep:#B8801F;
  --rust:#C04A2E; --rust-lit:#E8764F; --rust-deep:#7A2A17;
  --bone:#F7F4EA; --bone-dim:rgba(247,244,234,.70); --bone-faint:rgba(247,244,234,.42);
  --hair:rgba(247,244,234,.14); --gold-hair:rgba(232,166,60,.42);
  --font-display:'Fraunces','Iowan Old Style','Palatino Linotype',Georgia,serif;
  --font-body:'Work Sans','Segoe UI',Helvetica,Arial,sans-serif;
  --leaf:#7FA56A; --moss:#4A6647; --pine:#182620; --pine-2:#20342A; --pine-3:#2A4A38;
  --ease:cubic-bezier(.22,1,.36,1);
  --edge:clamp(14px,1.8vw,26px);
  --gap:clamp(3px,.36vh,7px);
  --mouseX: 0px;
  --mouseY: 0px;
}

*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;}
body{
  background:var(--ink);color:var(--bone);
  font-family:var(--font-body);font-size:16px;line-height:1.6;
  overflow:hidden;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer;}
::selection{background:var(--marigold);color:var(--ink);}
:focus-visible{outline:2px solid var(--marigold);outline-offset:4px;border-radius:3px;}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap;}

/* ==========================================================================
   THE LIVE SCENE
   ========================================================================== */
#live{
  position:fixed;inset:0;z-index:1;
  display:grid;grid-template-rows:auto 1fr auto;
  padding:clamp(16px,3.4vh,44px) clamp(16px,3.4vw,48px);
  gap:clamp(12px,2.4vh,28px);
  background:
    radial-gradient(ellipse 70% 50% at 50% 0%, rgba(232,166,60,.16), transparent 62%),
    radial-gradient(ellipse 90% 60% at 50% 108%, rgba(127,165,106,.14), transparent 60%),
    #F7F4EA;
  color:#1C2A1E;
  opacity:0;visibility:hidden;
}
#live.on{opacity:1;visibility:visible;}

.live-halo{position:absolute;left:50%;top:50%;width:130vmax;height:130vmax;
  transform:translate(-50%,-50%) scale(.2);opacity:0;pointer-events:none;
  background:radial-gradient(circle,rgba(232,166,60,.16) 0%,rgba(232,166,60,.05) 30%,transparent 58%);
  -webkit-mask-image:radial-gradient(circle,#000 18%,transparent 62%);
  mask-image:radial-gradient(circle,#000 18%,transparent 62%);}
.live-grain{position:absolute;inset:-50%;opacity:.25;pointer-events:none;
  mix-blend-mode:overlay;
  animation:grainShift .6s steps(3) infinite;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  background-size:200px 200px;}

.live-head{position:relative;text-align:center;align-self:end;max-width:900px;justify-self:center; animation: sproutUp 1s ease-out both;}
.live-flag{
  display:inline-flex;align-items:center;gap:9px;
  font-size:clamp(.66rem,.84vw,.76rem);font-weight:700;letter-spacing:.24em;text-transform:uppercase;
  color:#1C2A1E;background:var(--marigold);
  padding:7px 16px;border-radius:99px;margin-bottom:clamp(8px,1.4vh,16px);
  box-shadow:0 14px 30px -14px rgba(184,128,31,.9), inset 0 1px 0 rgba(255,255,255,.5);
}
.live-flag i{width:7px;height:7px;border-radius:50%;background:#1C2A1E;animation:livePulse 1.9s ease-out infinite;}
@keyframes livePulse{0%{box-shadow:0 0 0 0 rgba(28,42,30,.5);}100%{box-shadow:0 0 0 9px rgba(28,42,30,0);}}
.live-head h2{
  font-family:var(--font-display);font-weight:600;color:#1C2A1E;
  font-size:clamp(2.1rem,min(5.1vw,6.2vh),3.9rem);line-height:1.04;letter-spacing:-.022em;
  position:relative;display:inline-block;
}
.live-head h2 em{font-style:italic;color:var(--moss);}
.live-head p{margin-top:9px;color:#54624F;font-size:clamp(.92rem,1.1vw,1.14rem);}
.live-head p b{color:#1C2A1E;font-weight:600;}

.shot{
  position:relative;align-self:center;justify-self:center;
  width:min(1000px,92vw);
  height:min(100%,560px);
  border-radius:10px;display:flex;flex-direction:column;
  overflow:visible;
  background:#fff;border:1px solid rgba(28,42,30,.14);
  box-shadow:0 60px 110px -50px rgba(15,23,18,.6), 0 22px 44px -30px rgba(15,23,18,.4);
  animation: sproutUp 1s ease-out 0.2s both;
}
.shot::before {
  content:''; position:absolute; inset:-10px; border:2px solid var(--leaf);
  opacity:0.2; pointer-events:none; border-radius:15px; z-index:-1;
}
.shot-bar{
  display:flex;align-items:center;gap:13px;flex-shrink:0;
  padding:11px 15px;background:#F3F0E7;border-bottom:1px solid rgba(28,42,30,.1);
  border-radius:9px 9px 0 0;
}
.shot-dots{display:flex;gap:7px;flex-shrink:0;}
.shot-dots i{width:11px;height:11px;border-radius:50%;background:#D8D2C2;}
.shot-dots i:first-child{background:var(--marigold);}
.shot-url{
  flex:1;min-width:0;background:#fff;border:1px solid rgba(28,42,30,.1);border-radius:99px;
  padding:6px 15px;font-size:.78rem;color:#54624F;
  display:flex;align-items:center;gap:8px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;
}
.shot-url svg{width:12px;height:12px;flex-shrink:0;stroke:#7FA56A;fill:none;stroke-width:2;}
.shot-body{flex:1 1 auto;min-height:0;position:relative;
  background:var(--ink-2);overflow:hidden;border-radius:0 0 9px 9px;}
.shot-body iframe{position:absolute;left:0;top:0;border:0;display:block;
  width:1440px;height:var(--fh,900px);background:var(--ink-2);
  transform-origin:0 0;transform:scale(var(--fx,1));}

.shot-mock{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;
  padding:clamp(16px,2.6vw,36px);
  background:
    radial-gradient(ellipse 80% 60% at 76% 16%, rgba(232,166,60,.42), transparent 58%),
    linear-gradient(158deg,#101A14 0%,#22392C 44%,#8A5A2B 100%);}
.shot-mock .bar{height:8px;border-radius:99px;background:rgba(247,244,234,.2);margin-bottom:10px;}
.shot-mock .bar.t1{width:62%;height:clamp(14px,2vw,22px);background:rgba(247,244,234,.9);}
.shot-mock .bar.t2{width:42%;height:clamp(14px,2vw,22px);background:rgba(247,244,234,.9);}
.shot-mock .bar.t3{width:68%;background:rgba(247,244,234,.24);}
.shot-mock .bar.t4{width:50%;background:rgba(247,244,234,.24);}
.shot-mock .cta{width:140px;height:32px;border-radius:3px;background:var(--marigold);margin-top:8px;}

.seal{
  position:absolute;z-index:3;opacity:0;
  right:clamp(-18px,-1.6vw,-8px);bottom:clamp(-22px,-2vw,-10px);
  width:clamp(84px,9vw,126px);height:clamp(84px,9vw,126px);
  filter:drop-shadow(0 22px 34px rgba(15,23,18,.5));
}
.seal svg{width:100%;height:100%;display:block;}

.live-foot{position:relative;display:flex;align-items:center;gap:clamp(12px,2vw,24px);
  flex-wrap:wrap;justify-content:center;align-self:start; animation: sproutUp 1s ease-out 0.4s both;}
.enter{
  display:inline-flex;align-items:center;gap:11px;
  background:var(--leaf);color:var(--bone);
  padding:clamp(12px,1.5vh,16px) clamp(24px,2.6vw,34px);
  border-radius: 50% 0 50% 0; font-weight:600;text-decoration:none;
  box-shadow:0 20px 40px -20px rgba(15,23,18,.75), inset 0 1px 0 rgba(255,255,255,.2);
  transition:transform .3s var(--ease), box-shadow .3s ease, filter .3s ease;
}
.enter:hover{transform:translateY(-2px);filter:brightness(1.08);
  box-shadow:0 28px 54px -20px rgba(15,23,18,.85), inset 0 1px 0 rgba(255,255,255,.2);}
.enter svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
.enter[hidden]{display:none;}
.live-note{font-size:clamp(.74rem,.9vw,.84rem);color:#6B7A66;max-width:52ch;}
.live-note:empty{display:none;}
.live-note b{color:var(--marigold-deep);font-weight:600;}

/* ==========================================================================
   THE STAGE
   ========================================================================== */
.stage{
  position:fixed;inset:0;z-index:2;background:var(--ink);overflow:hidden;
  display:grid;grid-template-rows:auto 1fr auto;
  padding:calc(var(--edge) + clamp(18px,2.5vh,28px)) var(--edge) calc(var(--edge) + clamp(13px,1.8vh,21px));
  will-change:transform;
}
.stage-core{
  grid-row:2;min-height:0;width:100%;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:var(--gap);text-align:center;
  padding:clamp(1px,.15vh,4px) 0;
  transform: translate(calc(var(--mouseX) * 0.05), calc(var(--mouseY) * 0.05));
  transition: transform 0.1s ease-out;
  z-index: 10;
}

/* ---- atmosphere ---- */
.bg{position:absolute;inset:0;overflow:hidden;pointer-events:none;}
.bg-base{position:absolute;inset:-50%;z-index:-2;
  background: radial-gradient(circle at center, var(--pine-2) 0%, var(--pine) 40%, var(--ink) 80%);
  animation: dawnShift 20s infinite alternate ease-in-out;}
@keyframes dawnShift {
  0% { background: radial-gradient(circle at center, var(--pine-2) 0%, var(--pine) 50%, var(--ink) 100%); }
  100% { background: radial-gradient(circle at center, var(--moss) 0%, var(--pine-3) 40%, var(--ink) 90%); }
}

#fireflies{position:absolute;inset:0;width:100%;height:100%;z-index:-1;}
/* hiding old dust to prevent conflict */
#dust{display:none !important;}

.vig{position:absolute;inset:0;
  background:radial-gradient(ellipse 88% 76% at 50% 46%, transparent 30%, rgba(3,6,4,.84) 100%);}
.grain{position:absolute;inset:0;opacity:.25;pointer-events:none;
  mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  background-size:200px 200px;}

.vine-svg {
  position: absolute; z-index: 5; pointer-events: none;
  stroke: var(--leaf); stroke-width: 1.5; fill: none; opacity: 0.6;
}
.vine-top-left { top: 0; left: 0; width: 300px; }
.vine-bottom-right { bottom: 0; right: 0; width: 300px; transform: rotate(180deg); }
.vine-path {
  stroke-dasharray: 1000; stroke-dashoffset: 1000;
  animation: growVine 4s forwards cubic-bezier(0.4, 0, 0.2, 1);
}
@keyframes growVine { to { stroke-dashoffset: 0; } }

.frame{position:absolute;inset:var(--edge);pointer-events:none;z-index:4;}

/* ==========================================================================
   THE COMPOSITION
   ========================================================================== */
.masthead{display:flex;flex-direction:column;align-items:center;flex-shrink:0;}
.seals{display:flex;align-items:center;justify-content:center;
  gap:clamp(14px,2vw,28px);margin-bottom:clamp(5px,.8vh,10px);}
.seals img{
  width:clamp(60px,min(7.4vw,8.7vh),102px);height:clamp(60px,min(7.4vw,8.7vh),102px);
  display:block;border-radius:50%;object-fit:contain;background:#F7F4EA;
  box-shadow:0 12px 26px -12px rgba(0,0,0,.85), 0 0 0 1px rgba(232,166,60,.42);
}
.org{font-size:clamp(.82rem,1.08vw,1rem);font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:var(--leaf);}
.org-sub{font-size:clamp(.74rem,.97vw,.9rem);font-weight:600;letter-spacing:.32em;text-transform:uppercase;
  color:var(--marigold);margin-top:4px;}

.titleblock{display:flex;flex-direction:column;align-items:center;flex-shrink:0;
  margin-top:clamp(3px,.5vh,7px);position:relative;}

.breathing-glow {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  width: 140%; height: 140%; background: radial-gradient(ellipse at center, rgba(232, 166, 60, 0.2) 0%, transparent 70%);
  z-index: -1; animation: breathGlow 4s infinite alternate ease-in-out; pointer-events: none;
}
@keyframes breathGlow {
  0% { opacity: 0.5; transform: translate(-50%, -50%) scale(0.9); }
  100% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
}

.kicker{
  display:inline-flex;align-items:center;gap:12px;
  font-size:clamp(.74rem,.97vw,.88rem);font-weight:700;letter-spacing:.34em;text-transform:uppercase;
  color:var(--leaf);margin-bottom:clamp(4px,.7vh,9px);
}
.kicker::before,.kicker::after{content:"";width:clamp(20px,3.4vw,54px);height:1px;}
.kicker::before{background:linear-gradient(to right,transparent,var(--leaf));}
.kicker::after{background:linear-gradient(to left,transparent,var(--leaf));}

h1{
  font-family:var(--font-display);font-weight:600;color:var(--bone);
  font-size:clamp(2.4rem,min(8.1vw,9.6vh),5.85rem);line-height:1.02;letter-spacing:-.03em;
  position:relative;
}
.ln3d{display:block;perspective:900px;}
h1 .ln{display:block;overflow:hidden;padding:.04em 0 .1em;}
h1 .ln3d:first-child .ln{font-style:italic;font-weight:500;
  font-size:clamp(1.6rem,min(4.6vw,5.7vh),3.25rem);letter-spacing:-.01em;padding-bottom:.03em;color:var(--marigold);}
h1 .wd{display:inline-block;white-space:nowrap;}
h1 .ch{display:inline-block;will-change:transform;}

.sparkle {
  position: absolute; width: 4px; height: 4px; background: #fff; border-radius: 50%;
  box-shadow: 0 0 10px 2px #fff, 0 0 20px 2px var(--marigold);
  top: -10px; right: -15px; animation: twinkle 3s infinite; opacity: 0; z-index:5;
}
@keyframes twinkle {
  0%, 100% { opacity: 0; transform: scale(0.5); }
  50% { opacity: 1; transform: scale(1.2); }
}

.js h1 .ch{
  background-image:linear-gradient(100deg,
    #A9741B 0%, #E8A63C 12%, #FBDC9E 21%, #FFFDF6 28%,
    #FBDC9E 35%, #E8A63C 48%, #B8801F 60%, #F3C877 74%, #FFFDF6 82%, #A9741B 100%);
  background-size:250% 100%;
  -webkit-background-clip:text;background-clip:text;
  color:transparent;-webkit-text-fill-color:transparent;
  animation:shimmer 7s linear infinite;
  animation-delay:calc(var(--i,0) * -.1s);
}
@keyframes shimmer{0%{background-position:0% 0;}100%{background-position:100% 0;}}

.lede{margin:0 auto;max-width:52ch;color:var(--bone-dim);
  font-size:clamp(1rem,min(1.3vw,2.15vh),1.28rem);text-wrap:pretty;}

/* ---- the dedication plaque ---- */
.dedicate{
  position:relative;flex-shrink:0;
  padding:clamp(6px,.9vh,11px) clamp(20px,3.6vw,48px);
  border:1px solid var(--leaf);border-radius: 50% 0 50% 0;
  background:linear-gradient(180deg,rgba(32,52,42,.4),rgba(32,52,42,0));
  width:min(660px,100%);
  box-shadow: inset 0 0 15px rgba(0,0,0,0.5);
}
.dedicate .lbl{font-size:clamp(.72rem,.92vw,.84rem);font-weight:700;letter-spacing:.32em;text-transform:uppercase;color:var(--leaf);}
.dedicate .who{
  display:inline-block;margin-top:5px;
  font-family:var(--font-display);font-style:italic;font-weight:600;
  font-size:clamp(1.36rem,min(3.1vw,3.75vh),2.2rem);letter-spacing:-.015em;color:var(--bone);
  text-shadow:0 0 34px rgba(232,166,60,.4);
}
.dedicate .who [contenteditable]{outline:none;border-bottom:1px dashed transparent;transition:border-color .25s ease;}
.dedicate .who [contenteditable]:hover,.dedicate .who [contenteditable]:focus{border-bottom-color:var(--gold-hair);}
.dedicate .role{margin-top:3px;color:var(--marigold);font-size:clamp(.86rem,1.08vw,1.04rem);
  font-weight:600;letter-spacing:.14em;text-transform:uppercase;}

/* ==========================================================================
   THE RIBBON
   ========================================================================== */
.ribbon{
  position:relative;align-self:stretch;width:auto;
  height:clamp(44px,min(6.5vw,7.1vh),68px);
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
}
.rib{position:absolute;left:0;right:0;top:50%;
  height:clamp(34px,min(4.4vw,4.8vh),52px);transform:translateY(-50%);}
.rib::after{content:"";position:absolute;inset:-30px 0;
  background:radial-gradient(ellipse 58% 100% at 50% 50%, rgba(127,165,106,.34), transparent 72%);}

.half{position:absolute;top:0;bottom:0;width:50%;overflow:hidden;
  box-shadow:0 18px 44px -20px rgba(0,0,0,.95);will-change:transform;}
.half-l{left:0;transform-origin:0% 50%;}
.half-r{right:0;transform-origin:100% 50%;}

.sever{position:absolute;left:50%;top:-18%;bottom:-18%;width:2px;margin-left:-1px;
  opacity:0;pointer-events:none;
  background:linear-gradient(180deg,transparent,rgba(255,246,225,.9) 20%,
    #FFFFFF 50%,rgba(255,246,225,.9) 80%,transparent);
  box-shadow:0 0 16px 4px rgba(255,236,190,.9);}

.cloth{position:absolute;inset:0;display:block;
  background:
    linear-gradient(180deg,
      rgba(255,246,230,0) 4%, rgba(255,246,230,.3) 27%,
      rgba(255,246,230,.09) 47%, rgba(255,246,230,0) 63%),
    repeating-linear-gradient(90deg,
      rgba(255,238,214,.05) 0 2px, rgba(0,0,0,0) 2px 15px,
      rgba(0,0,0,.055) 15px 29px, rgba(0,0,0,0) 29px 47px),
    repeating-linear-gradient(90deg,
      rgba(0,0,0,0) 0 19px, rgba(255,240,220,.04) 19px 23px,
      rgba(0,0,0,.045) 23px 37px, rgba(0,0,0,0) 37px 64px),
    linear-gradient(180deg, #8FBF76 0%, #6B9E54 12%, var(--leaf) 36%, #4A8034 66%, var(--moss) 89%, #2A5020 100%);
  background-size:100% 100%, 264px 100%, 366px 100%, 100% 100%;
  animation:clothFlow 13s linear infinite;
}
@keyframes clothFlow{to{background-position:0 0, -264px 0, -366px 0, 0 0;}}
.cloth::before,.cloth::after{content:"";position:absolute;left:0;right:0;}
.cloth::before{top:0;height:38%;
  background:linear-gradient(180deg,rgba(255,240,214,.14),rgba(255,240,214,0));}
.cloth::after{bottom:0;height:44%;
  background:linear-gradient(0deg,rgba(46,14,6,.42),rgba(46,14,6,0));}
.braid{position:absolute;left:0;right:0;height:3px;display:block;
  background:linear-gradient(90deg,
    rgba(232,166,60,.15), rgba(247,220,158,.85) 12%, rgba(232,166,60,.4) 50%,
    rgba(247,220,158,.85) 88%, rgba(232,166,60,.15));
  background-size:240px 100%;animation:braid 5.5s linear infinite;}
.braid.t{top:2px;}
.braid.b{bottom:2px;opacity:.75;animation-direction:reverse;}
@keyframes braid{to{background-position:-240px 0;}}

.gloss{position:absolute;top:0;bottom:0;width:30%;display:block;opacity:0;
  background:linear-gradient(100deg,transparent,rgba(255,246,228,.42) 44%,rgba(255,255,255,.7) 52%,transparent);
  filter:blur(4px);animation:gloss 7s ease-in-out infinite;}
.half-r .gloss{animation-delay:1.3s;}
@keyframes gloss{
  0%{opacity:0;transform:translateX(-170%);}
  14%{opacity:.85;} 44%{opacity:.85;}
  58%{opacity:0;transform:translateX(380%);}
  100%{opacity:0;transform:translateX(380%);}
}

.bow{position:relative;z-index:3;width:clamp(96px,min(12vw,13vh),160px);pointer-events:none;
  transform-origin:50% 24%;will-change:transform;}
.bow-in{display:block;animation:bowSway 8s ease-in-out infinite;transform-origin:50% 20%;}
@keyframes bowSway{0%,100%{transform:rotate(-1.1deg);}50%{transform:rotate(1.1deg);}}
.bow svg{width:100%;height:auto;display:block;overflow:visible;}

.scissors{position:absolute;left:50%;top:50%;z-index:4;
  --sw:clamp(110px,min(14vw,15vh),180px);
  width:var(--sw);height:var(--sw);margin-left:calc(var(--sw) / -2);margin-top:calc(var(--sw) / -2);
  opacity:0;pointer-events:none;will-change:transform;}
.scissors svg{width:100%;height:100%;display:block;overflow:visible;
  filter:drop-shadow(0 10px 20px rgba(0,0,0,.75));}
.trail{position:absolute;left:50%;top:50%;z-index:3;
  --tw:clamp(64px,7.6vw,100px);
  width:var(--tw);height:var(--tw);margin-left:calc(var(--tw) / -2);margin-top:calc(var(--tw) / -2);
  border-radius:50%;opacity:0;pointer-events:none;filter:blur(14px);
  background:radial-gradient(circle,rgba(255,238,200,.6),transparent 66%);}

/* ---- the button ---- */
.controls{display:flex;flex-direction:column;align-items:center;flex-shrink:0;}
.cut{
  position:relative;display:inline-flex;align-items:center;gap:14px;
  padding:clamp(15px,2.2vh,23px) clamp(46px,5.6vw,78px);
  border:0;background:none;border-radius:0;cursor:pointer;
  font-weight:600;font-size:clamp(1.1rem,min(1.45vw,2.4vh),1.36rem);letter-spacing:.02em;
  color:var(--marigold);
  transition:transform .3s var(--ease);
}
.cut:hover{transform:translateY(-3px);}
.cut:active{transform:translateY(0) scale(.985);}
.cut[disabled]{opacity:.5;pointer-events:none;}
.cut > *{position:relative;z-index:1;}

.cut-ribbon{position:absolute;inset:0;z-index:0;pointer-events:none;
  border-radius: 50% 0 50% 0;
  background:linear-gradient(180deg,var(--leaf),var(--moss));
  animation:cutGlow 4.2s ease-in-out infinite;}
@keyframes cutGlow{
  0%,100%{filter:drop-shadow(0 22px 36px rgba(127,165,106,.5));}
  50%    {filter:drop-shadow(0 32px 54px rgba(127,165,106,.8));}
}
.cut-ribbon::before{content:"";position:absolute;inset:3px;
  border-radius: 50% 0 50% 0;
  border:1px solid rgba(255,247,226,.2);}
.cut-ribbon::after{content:"";position:absolute;top:0;bottom:0;width:38%;
  background:linear-gradient(100deg,transparent,rgba(255,255,255,.2) 50%,transparent);
  animation:sheen 4.6s ease-in-out infinite;}
@keyframes sheen{0%{transform:translateX(-260%);}55%{transform:translateX(360%);}100%{transform:translateX(360%);}}

.cut-ico{display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;
  width:clamp(26px,2.6vh,30px);height:clamp(26px,2.6vh,30px);border-radius:50%;
  background:radial-gradient(circle at 38% 30%, #7E2A22, #4E1712 72%);
  box-shadow:inset 0 0 0 1.5px rgba(255,226,164,.75), 0 3px 8px -2px rgba(60,20,10,.6);}
.cut-ico svg{display:block;width:56%;height:56%;fill:none;stroke:#FFE6B4;stroke-width:1.9;
  stroke-linecap:round;stroke-linejoin:round;transition:transform .45s var(--ease);}
.cut:hover .cut-ico svg{transform:rotate(-16deg) scale(1.06);}

/* ---- HUD and foot ---- */
.hud{grid-row:1;display:flex;align-items:center;justify-content:space-between;gap:12px;z-index:6;}
.status, .status.armed{display:none !important;}

.tools{display:flex;gap:8px;margin-left:auto;}
.tool{width:38px;height:38px;border-radius:50%;border:1px solid var(--leaf);color:var(--leaf);
  display:inline-flex;align-items:center;justify-content:center;
  transition:color .25s ease,border-color .25s ease,background .25s ease;}
.tool:hover{color:var(--marigold);border-color:var(--gold-hair);background:rgba(232,166,60,.08);}
.tool svg{width:15px;height:15px;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;}
.tool.off{color:rgba(127,165,106,.5);}
.tool.off svg{opacity:.5;}

.foot{grid-row:3;display:flex;align-items:center;justify-content:space-between;gap:clamp(10px,2.6vw,36px);z-index:6;}
.foot .side{font-size:clamp(.68rem,.86vw,.8rem);font-weight:600;letter-spacing:.2em;
  text-transform:uppercase;color:var(--leaf);white-space:nowrap;}

.railwrap{position:relative;display:flex;justify-content:center;min-width:0;}
.rail-track,.rail-fill{position:absolute;left:0;top:4px;height:2px;}
.rail-track{right:0;background:var(--leaf);opacity:0.3;}
.rail-fill{width:0;background:var(--leaf);
  box-shadow:0 0 10px var(--leaf);transition:width 1s var(--ease);}
.rail{position:relative;list-style:none;display:flex;gap:clamp(10px,2.2vw,32px);flex-wrap:wrap;justify-content:center;}
.rail li{position:relative;display:flex;align-items:center;gap:8px;padding-top:13px;
  font-size:clamp(.66rem,.84vw,.78rem);font-weight:600;letter-spacing:.18em;text-transform:uppercase;
  color:var(--leaf);transition:color .6s ease;}
.rail li::before{content:"";position:absolute;top:1px;left:0;width:7px;height:7px;border-radius:50% 0 50% 0;
  background:var(--ink);border:1px solid var(--leaf);transition:all .6s ease;}
.rail li.done{color:rgba(166,220,144,.88);}
.rail li.done::before{background:#A6DC90;border-color:#A6DC90;}
.rail li.now{color:var(--marigold);}
.rail li.now::before{background:var(--marigold);border-color:var(--marigold);
  box-shadow:0 0 0 4px rgba(232,166,60,.16);}

/* ==========================================================================
   THE REVEAL EFFECTS
   ========================================================================== */
#flash{position:fixed;inset:0;z-index:7;pointer-events:none;opacity:0;
  background:radial-gradient(circle at 50% 52%, #FFFBF0 0%, rgba(232,166,60,.9) 26%, rgba(232,166,60,0) 62%);}
#shock{position:fixed;inset:0;z-index:6;pointer-events:none;opacity:0;
  background:radial-gradient(circle at 50% 52%, rgba(255,255,255,.95) 0%, rgba(255,255,255,0) 40%);}
#ring{position:fixed;z-index:7;width:20px;height:20px;border-radius:50%;opacity:0;pointer-events:none;
  border:2px solid rgba(255,244,222,.9);
  box-shadow:0 0 46px rgba(232,166,60,.9), inset 0 0 32px rgba(232,166,60,.6);}
#burst{position:fixed;z-index:7;width:24px;height:24px;border-radius:50%;opacity:0;pointer-events:none;
  background:conic-gradient(from 0deg,
    transparent 0deg,  rgba(255,246,228,.65) 1.6deg, transparent 5deg,
    transparent 46deg, rgba(255,246,228,.42) 48deg,  transparent 52deg,
    transparent 94deg, rgba(255,246,228,.58) 96deg, transparent 100deg,
    transparent 141deg,rgba(255,246,228,.38) 143deg,transparent 147deg,
    transparent 186deg,rgba(255,246,228,.52) 188deg,transparent 192deg,
    transparent 232deg,rgba(255,246,228,.4) 234deg,transparent 238deg,
    transparent 277deg,rgba(255,246,228,.58) 279deg,transparent 283deg,
    transparent 322deg,rgba(255,246,228,.42) 324deg, transparent 328deg,
    transparent 360deg);
  -webkit-mask-image:radial-gradient(circle,transparent 6%,#000 16%,transparent 58%);
  mask-image:radial-gradient(circle,transparent 6%,#000 16%,transparent 58%);}
#petals{position:fixed;inset:0;z-index:8;pointer-events:none;}

/* ---- already held ---- */
.notice{
  position:fixed;inset:0;z-index:60;display:none;
  flex-direction:column;align-items:center;justify-content:center;text-align:center;
  padding:clamp(24px,6vw,64px);gap:16px;
  background:
    radial-gradient(ellipse 70% 50% at 50% 30%, rgba(232,166,60,.14), transparent 62%),
    linear-gradient(180deg,#0C1510,#070C09);
}
.notice.on{display:flex;}
.notice h2{font-family:var(--font-display);font-weight:600;letter-spacing:-.02em;
  font-size:clamp(1.5rem,min(3.4vw,4vh),2.6rem);line-height:1.1;}
.notice p{color:var(--bone-dim);max-width:48ch;}
.notice a{display:inline-flex;align-items:center;gap:10px;margin-top:8px;
  background:linear-gradient(180deg,var(--marigold-lit),var(--marigold) 46%,var(--marigold-deep));
  color:#2A1B03;text-decoration:none;font-weight:600;padding:14px 30px;border-radius:3px;
  box-shadow:0 22px 46px -18px rgba(232,166,60,.95), inset 0 1px 0 rgba(255,255,255,.6);}

/* ==========================================================================
   THE PREVIEW FLAG
   ========================================================================== */
:root{--flag-h:0px;}
.preview-flag{
  position:fixed;left:0;right:0;top:0;z-index:70;
  display:flex;align-items:center;justify-content:center;gap:10px;
  height:var(--flag-h);padding:0 clamp(12px,3vw,26px);
  background:linear-gradient(180deg,#B8801F,#8E5F14);
  color:#FFF6E4;text-align:center;
  font-size:clamp(.66rem,.82vw,.78rem);font-weight:600;letter-spacing:.12em;text-transform:uppercase;
  box-shadow:0 10px 26px -12px rgba(0,0,0,.8);
}
.preview-flag[hidden]{display:none;}
.preview-flag b{color:#FFF;font-weight:700;}
.preview-flag.done{background:linear-gradient(180deg,#2E5B39,#1E3D26);}

body.previewing{--flag-h:clamp(34px,4.4vh,42px);}
body.previewing .stage,
body.previewing #live{top:var(--flag-h);}

/* Sound Indicator */
.sound-indicator {
    display: flex; gap: 4px; align-items: center; opacity: 1; pointer-events: none;
}
.bar {
    width: 3px; background-color: var(--marigold); border-radius: 2px;
    animation: eq 1s infinite alternate ease-in-out;
}
.bar:nth-child(1) { height: 8px; animation-delay: 0.1s; }
.bar:nth-child(2) { height: 16px; animation-delay: 0.3s; }
.bar:nth-child(3) { height: 12px; animation-delay: 0.2s; }
.bar:nth-child(4) { height: 18px; animation-delay: 0.5s; }
@keyframes eq {
    0% { transform: scaleY(0.5); }
    100% { transform: scaleY(1); }
}

/* Floating Leaves CSS */
.floating-leaf {
    position: absolute; width: 24px; height: 24px; background: var(--leaf);
    border-radius: 50% 0 50% 0; opacity: 0; pointer-events: none; z-index: 1;
    filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3));
}
@keyframes floatDown {
    0% { top: -50px; opacity: 0; }
    10% { opacity: 0.6; }
    90% { opacity: 0.6; }
    100% { top: 100vh; opacity: 0; }
}
@keyframes sway {
    0% { margin-left: 0px; transform: rotate(0deg); }
    100% { margin-left: 50px; transform: rotate(45deg); }
}

@keyframes sproutUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width:1100px){
  .shot{height:min(100%,500px);}
}
@media (max-width:820px){
  .foot{justify-content:center;}
  .foot .side{display:none;}
  .rail-track,.rail-fill{display:none;}
  .rail li{padding-top:0;}
  .rail li::before{position:static;margin-right:6px;}
  .lede{display:none;}
}
@media (max-height:720px){
  .lede{display:none;}
  .kicker{display:none;}
}
@media (max-height:600px){
  .org-sub{display:none;}
  .dedicate{padding:8px 16px;}
  h1 .ln3d:first-child .ln{font-size:1.2rem;}
}
@media (max-height:820px){
  #live{gap:clamp(8px,1.5vh,16px);
    padding:clamp(10px,2.2vh,26px) clamp(16px,3.4vw,48px);}
  .live-flag{font-size:clamp(.56rem,.7vw,.62rem);padding:5px 12px;
    margin-bottom:clamp(6px,1vh,11px);}
  .live-head h2{font-size:clamp(1.45rem,min(3.8vw,4.6vh),2.7rem);}
  .live-head p{margin-top:6px;font-size:clamp(.76rem,.94vw,.92rem);}
}

@media (prefers-reduced-motion: reduce){
  .bg-base,.grain,.bow-in,.cloth,.braid,.gloss,
  .cut-ribbon,.cut-ribbon::after,.live-flag i,.live-grain,.breathing-glow,.bar,.vine-path{animation:none;}
  .cut-ribbon{filter:drop-shadow(0 22px 36px rgba(127,165,106,.5));}
  .cut-ico svg{transition:none;}
  .gloss{opacity:.2;}
  .js h1 .ch{animation:none;color:var(--marigold);-webkit-text-fill-color:var(--marigold);background:none;}
  #fireflies{display:none;}
}
</style>
</head>
<body>

<p class="preview-flag" id="previewFlag" role="status" aria-live="polite" hidden></p>

<section id="live" aria-hidden="true">
  <div class="live-halo" id="halo" aria-hidden="true"></div>
  <div class="live-grain" aria-hidden="true"></div>

  <div class="live-head">
    <span class="live-flag" id="liveChip"><i></i> Live</span>
    <h2 id="liveHead">The NSS website<br>is now <em>live</em>.<span class="sparkle"></span></h2>
    <p id="liveCred">
      <span id="liveCredLive">Inaugurated by <b id="liveBy">the Director</b> · <span id="liveDate"></span></span>
      <span id="liveCredPreview" hidden>Not inaugurated yet · this was a local playback</span>
    </p>
  </div>

  <div class="shot" id="shot">
    <div class="shot-bar">
      <span class="shot-dots"><i></i><i></i><i></i></span>
      <span class="shot-url">
        <svg viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>
        <span id="shotUrl">nss · iiit naya raipur</span>
      </span>
    </div>
    <div class="shot-body" id="shotBody">
      <div class="shot-mock" id="shotMock" aria-hidden="true">
        <div class="bar t1"></div>
        <div class="bar t2"></div>
        <div class="bar t3"></div>
        <div class="bar t4"></div>
        <div class="cta"></div>
      </div>
    </div>

    <div class="seal" id="seal" aria-hidden="true">
      <svg viewBox="0 0 200 200">
        <defs>
          <linearGradient id="wax" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stop-color="#FBDC9E"/><stop offset=".5" stop-color="#E8A63C"/><stop offset="1" stop-color="#B8801F"/>
          </linearGradient>
          <path id="sealArc" d="M100 100 m -74 0 a 74 74 0 1 1 148 0 a 74 74 0 1 1 -148 0"/>
        </defs>
        <circle cx="100" cy="100" r="92" fill="url(#wax)"/>
        <circle cx="100" cy="100" r="92" fill="none" stroke="rgba(255,255,255,.4)" stroke-width="1.5"/>
        <circle cx="100" cy="100" r="84" fill="none" stroke="rgba(11,18,14,.34)" stroke-width="1.5"/>
        <circle cx="100" cy="100" r="52" fill="none" stroke="rgba(11,18,14,.32)" stroke-width="1.5"/>
        <text font-family="Work Sans, sans-serif" font-size="15.5" font-weight="700" letter-spacing="4.6" fill="#0B120E">
          <textPath href="#sealArc" startOffset="8%">INAUGURATED ✦ NSS IIIT NAYA RAIPUR ✦</textPath>
        </text>
        <g stroke="#0B120E" stroke-width="1.9" fill="none" stroke-linecap="round">
          <line x1="100" y1="66" x2="100" y2="80"/><line x1="100" y1="120" x2="100" y2="134"/>
          <line x1="66" y1="100" x2="80" y2="100"/><line x1="120" y1="100" x2="134" y2="100"/>
          <line x1="76" y1="76" x2="86" y2="86"/><line x1="114" y1="114" x2="124" y2="124"/>
          <line x1="76" y1="124" x2="86" y2="114"/><line x1="114" y1="86" x2="124" y2="76"/>
        </g>
        <circle cx="100" cy="100" r="7" fill="#0B120E"/>
      </svg>
    </div>
  </div>

  <div class="live-foot">
    <a class="enter" id="enter" href="index.html">
      Enter the website
      <svg viewBox="0 0 24 24"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
    </a>
    <p class="live-note" id="liveNote"></p>
  </div>
</section>

<div class="stage" id="stage">

  <div class="bg" aria-hidden="true">
    <div class="bg-base"></div>
    <div class="grain"></div>
    <canvas id="fireflies"></canvas>
    
    <svg class="vine-svg vine-top-left" viewBox="0 0 300 300">
        <path class="vine-path" d="M0,0 C100,20 150,100 150,150 C150,200 200,250 300,250 M50,15 C80,40 70,80 120,90 M100,120 C140,120 160,160 220,180" />
    </svg>
    <svg class="vine-svg vine-bottom-right" viewBox="0 0 300 300">
        <path class="vine-path" d="M0,0 C100,20 150,100 150,150 C150,200 200,250 300,250 M50,15 C80,40 70,80 120,90 M100,120 C140,120 160,160 220,180" />
    </svg>

    <canvas id="dust"></canvas>
  </div>

  <div class="frame" aria-hidden="true"></div>

  <div class="hud">
    <div class="status" id="status" hidden style="display:none !important;">
      <i></i><span id="statusText"></span>
    </div>
    <div class="tools">
      <div class="sound-indicator" title="Ambient Atmosphere Active" style="margin-right: 12px; opacity:0.5;">
        <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
      </div>
      <button class="tool" id="soundBtn" type="button" aria-pressed="true" title="Sound on / off">
        <svg id="soundIcon" viewBox="0 0 24 24"><path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M17 8.5a5 5 0 0 1 0 7"/></svg>
      </button>
      <button class="tool" id="fsBtn" type="button" title="Full screen (F)">
        <svg viewBox="0 0 24 24"><path d="M4 9V4h5"/><path d="M20 9V4h-5"/><path d="M4 15v5h5"/><path d="M20 15v5h-5"/></svg>
      </button>
    </div>
  </div>

  <div class="stage-core">
    <header class="masthead">
      <div class="seals">
        <img src="assets/images/iiit.png" width="302" height="302" alt="Dr. SPM IIIT Naya Raipur">
        <img src="assets/images/nss_logo.png" width="738" height="738" alt="National Service Scheme">
      </div>
      <p class="org">Dr. SPM IIIT Naya Raipur</p>
      <p class="org-sub">National Service Scheme</p>
    </header>

    <div class="titleblock">
      <div class="breathing-glow"></div>
      <p class="kicker">Website Inauguration</p>
      <h1 id="title">
        <span class="ln3d"><span class="ln">The</span></span>
        <span class="ln3d"><span class="ln">Unveiling<span class="sparkle"></span></span></span>
      </h1>
      <p class="lede" style="margin-top:clamp(6px,1vh,11px)">The official NSS IIIT-NR website goes live in front of you — built by students, for the work they do.</p>
    </div>

    <div class="dedicate">
      <p class="lbl">To be inaugurated by</p>
      <p class="who"><span id="dirName" contenteditable="true" spellcheck="false" role="textbox" aria-label="Name of the inaugurating guest">Prof. (Dr.) Om Prakash Vyas</span></p>
      <p class="role">Director, IIIT Naya Raipur</p>
    </div>

    <div class="ribbon" id="ribbon">
      <div class="rib">
        <span class="half half-l"><i class="cloth"></i><i class="braid t"></i><i class="braid b"></i><i class="gloss"></i></span>
        <span class="half half-r"><i class="cloth"></i><i class="braid t"></i><i class="braid b"></i><i class="gloss"></i></span>
        <i class="sever" id="sever" aria-hidden="true"></i>
      </div>

      <div class="bow" id="bow">
        <span class="bow-in" aria-hidden="true">
          <svg viewBox="0 0 240 200">
            <defs>
              <linearGradient id="ribG" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0" stop-color="#F08A62"/><stop offset=".42" stop-color="#C04A2E"/><stop offset="1" stop-color="#7A2A17"/>
              </linearGradient>
              <linearGradient id="ribG2" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0" stop-color="#D9563A"/><stop offset="1" stop-color="#8E3220"/>
              </linearGradient>
              <radialGradient id="knotG" cx="0.34" cy="0.28" r="0.9">
                <stop offset="0" stop-color="#F5926B"/><stop offset=".5" stop-color="#C04A2E"/><stop offset="1" stop-color="#6E2414"/>
              </radialGradient>
            </defs>

            <path d="M104 100 L76 180 L96 167 L110 190 L130 102 Z" fill="url(#ribG2)" stroke="rgba(232,166,60,.45)" stroke-width="1"/>
            <path d="M136 100 L172 178 L152 167 L140 192 L118 102 Z" fill="url(#ribG2)" stroke="rgba(232,166,60,.45)" stroke-width="1"/>
            <path d="M108 104 L88 170" stroke="rgba(255,240,214,.26)" stroke-width="2.6" fill="none" stroke-linecap="round"/>
            <path d="M132 104 L160 170" stroke="rgba(255,240,214,.2)" stroke-width="2.6" fill="none" stroke-linecap="round"/>

            <path d="M120 96 C 70 26, 8 34, 16 88 C 22 132, 84 134, 120 96 Z" fill="url(#ribG)" stroke="rgba(232,166,60,.45)" stroke-width="1"/>
            <path d="M120 96 C 170 26, 232 34, 224 88 C 218 132, 156 134, 120 96 Z" fill="url(#ribG)" stroke="rgba(232,166,60,.45)" stroke-width="1"/>
            <path d="M116 94 C 80 56, 40 56, 34 86 C 30 112, 72 118, 116 94 Z" fill="rgba(52,16,8,.34)"/>
            <path d="M124 94 C 160 56, 200 56, 206 86 C 210 112, 168 118, 124 94 Z" fill="rgba(52,16,8,.34)"/>
            <path d="M118 92 C 74 30, 16 38, 20 84" fill="none" stroke="rgba(255,242,220,.46)" stroke-width="2.8" stroke-linecap="round"/>
            <path d="M122 92 C 166 30, 224 38, 220 84" fill="none" stroke="rgba(255,242,220,.36)" stroke-width="2.8" stroke-linecap="round"/>

            <ellipse cx="120" cy="98" rx="21" ry="23" fill="url(#knotG)" stroke="rgba(232,166,60,.55)" stroke-width="1.3"/>
            <ellipse cx="120" cy="98" rx="21" ry="23" fill="none" stroke="rgba(255,242,220,.18)" stroke-width="5"/>
            <ellipse cx="113" cy="89" rx="6" ry="7" fill="rgba(255,242,220,.26)"/>
            <circle cx="120" cy="98" r="6.5" fill="#E8A63C" stroke="#8B5F15" stroke-width="1.2"/>
            <circle cx="118" cy="96" r="2" fill="rgba(255,255,255,.8)"/>
          </svg>
        </span>
      </div>

      <div class="trail" id="trail" aria-hidden="true"></div>

      <div class="scissors" id="scissors" aria-hidden="true">
        <svg viewBox="0 0 240 150">
          <defs>
            <linearGradient id="scSteelTop" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#8C8676"/><stop offset=".3" stop-color="#CFC9B8"/>
              <stop offset=".64" stop-color="#F4F1E6"/><stop offset=".88" stop-color="#FFFFFF"/>
              <stop offset="1" stop-color="#D8D2C1"/>
            </linearGradient>
            <linearGradient id="scSteelBot" x1="0" y1="1" x2="0" y2="0">
              <stop offset="0" stop-color="#8C8676"/><stop offset=".3" stop-color="#CFC9B8"/>
              <stop offset=".64" stop-color="#F4F1E6"/><stop offset=".88" stop-color="#FFFFFF"/>
              <stop offset="1" stop-color="#D8D2C1"/>
            </linearGradient>
            <linearGradient id="scGripTop" x1="0" y1="1" x2="0" y2="0">
              <stop offset="0" stop-color="#948E7D"/><stop offset="1" stop-color="#EDE9DC"/>
            </linearGradient>
            <linearGradient id="scGripBot" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#948E7D"/><stop offset="1" stop-color="#EDE9DC"/>
            </linearGradient>
            <radialGradient id="scScrew" cx=".36" cy=".3" r=".85">
              <stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#DACFA6"/>
              <stop offset="1" stop-color="#87702A"/>
            </radialGradient>
          </defs>

          <g id="bladeTop">
            <path d="M117 61 Q 58 24, 7 29 L 118 79 Z" fill="url(#scSteelTop)"/>
            <path d="M113 68 Q 60 33, 22 34 L 117 76 Z" fill="rgba(255,255,255,.5)"/>
            <path d="M7 29 L118 79" stroke="#FFFFFF" stroke-width="1.2" fill="none" opacity=".85"/>
            <path d="M117 61 Q 58 24, 7 29" stroke="rgba(58,54,42,.5)" stroke-width="1.4" fill="none"/>
            <path d="M120 57 C 152 46, 174 39, 188 33 L 194 47 C 178 54, 154 63, 122 76 Z"
                  fill="url(#scGripTop)" stroke="rgba(58,54,42,.45)" stroke-width="1.2" stroke-linejoin="round"/>
            <path fill-rule="evenodd" fill="url(#scGripTop)" stroke="rgba(58,54,42,.45)" stroke-width="1.2"
              d="M204 13 A 17 17 0 1 0 204 47 A 17 17 0 1 0 204 13 Z
                 M204 22 A 8 8 0 1 0 204 38 A 8 8 0 1 0 204 22 Z"/>
            <path d="M193 21 A 14 14 0 0 1 200 16" stroke="rgba(255,255,255,.8)" stroke-width="2.4"
                  fill="none" stroke-linecap="round"/>
          </g>

          <g id="bladeBot">
            <path d="M117 89 Q 58 126, 7 121 L 118 71 Z" fill="url(#scSteelBot)"/>
            <path d="M113 82 Q 60 117, 22 116 L 117 74 Z" fill="rgba(255,255,255,.42)"/>
            <path d="M7 121 L118 71" stroke="#FFFFFF" stroke-width="1.2" fill="none" opacity=".8"/>
            <path d="M117 89 Q 58 126, 7 121" stroke="rgba(58,54,42,.5)" stroke-width="1.4" fill="none"/>
            <path d="M120 93 C 152 104, 174 111, 188 117 L 194 103 C 178 96, 154 87, 122 74 Z"
                  fill="url(#scGripBot)" stroke="rgba(58,54,42,.45)" stroke-width="1.2" stroke-linejoin="round"/>
            <path fill-rule="evenodd" fill="url(#scGripBot)" stroke="rgba(58,54,42,.45)" stroke-width="1.2"
              d="M204 103 A 17 17 0 1 0 204 137 A 17 17 0 1 0 204 103 Z
                 M204 112 A 8 8 0 1 0 204 128 A 8 8 0 1 0 204 112 Z"/>
            <path d="M193 129 A 14 14 0 0 0 200 134" stroke="rgba(255,255,255,.6)" stroke-width="2.4"
                  fill="none" stroke-linecap="round"/>
          </g>
          <circle cx="120" cy="75" r="8.5" fill="url(#scScrew)" stroke="rgba(58,48,20,.6)" stroke-width="1"/>
          <path d="M114.5 75 L125.5 75" stroke="rgba(70,58,22,.7)" stroke-width="1.6" stroke-linecap="round"/>
          <circle cx="117.5" cy="72.4" r="1.8" fill="rgba(255,255,255,.9)"/>
        </svg>
      </div>
    </div>

    <div class="controls" id="controls">
      <button class="cut" id="cutBtn" type="button">
        <i class="cut-ribbon" aria-hidden="true"></i>
        <span class="cut-ico" aria-hidden="true">
          <svg viewBox="0 0 24 24"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4L8.12 15.88"/><path d="M14.47 14.48L20 20"/><path d="M8.12 8.12L12 12"/></svg>
        </span>
        <span>Cut the ribbon</span>
      </button>
    </div>
  </div>

  <div class="foot">
    <p class="side" id="footDate"></p>
    <div class="railwrap">
      <i class="rail-track" aria-hidden="true"></i>
      <i class="rail-fill" id="railFill" aria-hidden="true"></i>
      <ul class="rail" id="rail">
        <li class="done"><i></i><span>Lighting of the lamp</span></li>
        <li class="done"><i></i><span>Welcome address</span></li>
        <li class="now" id="railCut"><i></i><span>Ribbon cutting</span></li>
        <li id="railLive"><i></i><span>Website goes live</span></li>
      </ul>
    </div>
    <p class="side">IIIT Naya Raipur</p>
  </div>
</div>

<div id="shock"></div>
<div id="flash"></div>
<div id="burst"></div>
<div id="ring"></div>
<canvas id="petals"></canvas>

<p class="sr" id="announce" role="status" aria-live="polite"></p>

<div class="notice" id="notice">
  <h2 id="noticeTitle">This ceremony has already been held.</h2>
  <p id="noticeText">The website itself is live below.</p>
  <a href="index.html">Go to the website
    <svg viewBox="0 0 24 24" width="17" height="17" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
  </a>
</div>

<script>
    document.addEventListener('mousemove', (e) => {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;
        document.documentElement.style.setProperty('--mouseX', `${x}px`);
        document.documentElement.style.setProperty('--mouseY', `${y}px`);
    });

    const canvas = document.getElementById('fireflies');
    const ctx = canvas.getContext('2d');
    let fireflies = [];
    let mx = window.innerWidth / 2;
    let my = window.innerHeight / 2;

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    document.addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; });

    class Firefly {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.vx = (Math.random() - 0.5) * 1;
            this.vy = (Math.random() - 0.5) * 1;
            this.size = Math.random() * 2 + 1;
            this.life = Math.random();
            this.lifeSpeed = Math.random() * 0.02 + 0.01;
            this.color = `rgba(232, 166, 60, `;
        }
        update() {
            const dx = mx - this.x;
            const dy = my - this.y;
            const dist = Math.sqrt(dx*dx + dy*dy);
            if (dist < 300) {
                this.vx += (dx / dist) * 0.02;
                this.vy += (dy / dist) * 0.02;
            }
            this.vx *= 0.98;
            this.vy *= 0.98;
            this.vx += (Math.random() - 0.5) * 0.1;
            this.vy += (Math.random() - 0.5) * 0.1;
            this.x += this.vx;
            this.y += this.vy;
            if (this.x < 0) this.x = canvas.width;
            if (this.x > canvas.width) this.x = 0;
            if (this.y < 0) this.y = canvas.height;
            if (this.y > canvas.height) this.y = 0;
            this.life += this.lifeSpeed;
        }
        draw() {
            const alpha = Math.abs(Math.sin(this.life)) * 0.8;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color + alpha + ')';
            ctx.shadowBlur = 10;
            ctx.shadowColor = 'rgba(232, 166, 60, 0.8)';
            ctx.fill();
        }
    }
    for (let i = 0; i < 50; i++) fireflies.push(new Firefly());

    function animateFireflies() {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        fireflies.forEach(f => { f.update(); f.draw(); });
        requestAnimationFrame(animateFireflies);
    }
    animateFireflies();

    function createLeaf() {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        const leaf = document.createElement('div');
        leaf.classList.add('floating-leaf');
        leaf.style.left = Math.random() * 100 + 'vw';
        leaf.style.top = '-50px';
        const duration = Math.random() * 10 + 10;
        const delay = Math.random() * 5;
        const rotation = Math.random() * 360;
        leaf.style.animation = `floatDown ${duration}s ${delay}s linear forwards, sway ${duration/2}s ${delay}s ease-in-out infinite alternate`;
        leaf.style.transform = `rotate(${rotation}deg)`;
        const colors = ['var(--leaf)', 'var(--moss)', 'var(--pine-3)'];
        leaf.style.background = colors[Math.floor(Math.random() * colors.length)];
        document.body.appendChild(leaf);
        setTimeout(() => { leaf.remove(); }, (duration + delay) * 1000);
    }
    setInterval(createLeaf, 3000);
    createLeaf();
</script>

<script src="vendor/gsap.min.js"></script>
'''

with open(r"c:\Users\samai\Desktop\nss_main\inauguration.html", "r", encoding="utf-8") as f:
    orig = f.read()

# Extract the script from original file exactly
script_match = re.search(r'<script>(.*?)</script>\s*</body>', orig, re.DOTALL)
if script_match:
    exact_script = f"<script>{script_match.group(1)}</script>"
else:
    raise ValueError("Could not find the original script")

with open(r"c:\Users\samai\Desktop\nss_main\inauguration-v4.html", "w", encoding="utf-8") as out:
    out.write(html_content + exact_script + "\n</body>\n</html>\n")

print("File generated successfully")
