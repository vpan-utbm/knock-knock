"""Writes docs/sinai.svg (dawn over the mountain) and docs/tablet-crown.svg, tablet-body.svg, tablet-base.svg (a carved
stone tablet in three pieces). Fixed seeds. Usage: python -I tools/make_art.py <repository folder>"""
import random
import sys

root = sys.argv[1]
W, H = 1600, 760
OY = 200  # sky above the summit, for the rays to fade into


def ridge(points, rough, depth, rnd):
    """Midpoint displacement between fixed control points: a craggy but deterministic ridgeline."""
    out = [points[0]]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        seg = [(x0, y0), (x1, y1)]
        amp = rough
        for _ in range(depth):
            nxt = [seg[0]]
            for (ax, ay), (bx, by) in zip(seg, seg[1:]):
                nxt += [((ax + bx) / 2, (ay + by) / 2 + rnd.uniform(-amp, amp)), (bx, by)]
            seg, amp = nxt, amp * 0.55
        out += seg[1:]
    return [(x, y + OY) for x, y in out]


def path(pts):
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + f" L{W} {H} L0 {H} Z"


rnd = random.Random(1813)
far = ridge([(0, 250), (220, 205), (420, 236), (600, 190), (1000, 196), (1180, 228), (1390, 198), (1600, 240)], 16, 5, rnd)
massif = ridge([(250, 340), (430, 262), (560, 226), (690, 172), (800, 124), (905, 170), (1030, 216), (1170, 258), (1350, 340)], 20, 5, rnd)
mid_l = ridge([(0, 300), (140, 272), (330, 300), (520, 286), (700, 330), (820, 360)], 14, 5, rnd)
mid_r = ridge([(780, 362), (930, 322), (1100, 288), (1280, 302), (1460, 268), (1600, 286)], 14, 5, rnd)
near = ridge([(0, 380), (200, 352), (420, 384), (640, 372), (800, 400), (980, 374), (1200, 388), (1400, 356), (1600, 378)], 10, 5, rnd)
summit = min(massif, key=lambda p: p[1])
sx, sy = summit

rays = []
rr = random.Random(7)
for i in range(26):
    a = -172 + i * (164 / 25) + rr.uniform(-2, 2)
    w = rr.uniform(1.2, 3.2)
    rays.append(f'<path d="M0 0 L1400 {-w * 12:.0f} L1400 {w * 12:.0f} Z" transform="rotate({a:.1f})" '
                f'opacity="{rr.uniform(0.5, 1):.2f}"/>')

sinai = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="rayfade" cx="0" cy="0" r="900" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#fffcf4" stop-opacity="1"/>
      <stop offset="0.4" stop-color="#fff6e4" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#fff3dc" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="dawn" cx="{sx}" cy="{sy + 10}" r="520" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#fffdf6"/>
      <stop offset="0.18" stop-color="#fff4dc" stop-opacity="0.95"/>
      <stop offset="0.55" stop-color="#fbe2b8" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#fbe2b8" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="fadeup" x1="0" y1="0" x2="0" y2="{sy}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.75" stop-color="#fff" stop-opacity="1"/>
    </linearGradient>
    <mask id="skyfade" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">
      <rect width="{W}" height="{H}" fill="url(#fadeup)"/>
    </mask>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6"/></filter>
    <filter id="grain" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.9 0.35" numOctaves="3" seed="11" result="n"/>
      <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.42  0 0 0 0 0.28  0 0 0 0 0.16  0.7 0 0 0 -0.32" result="g"/>
      <feComposite in="g" in2="SourceGraphic" operator="in" result="gi"/>
      <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="gi"/></feMerge>
    </filter>
    <linearGradient id="gfar" x1="0" y1="390" x2="0" y2="530" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#e9d2c2"/><stop offset="1" stop-color="#f4e5d2"/>
    </linearGradient>
    <linearGradient id="gmassif" x1="0" y1="290" x2="0" y2="560" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#d6a786"/><stop offset="0.55" stop-color="#e2bf9d"/><stop offset="1" stop-color="#efd9bc"/>
    </linearGradient>
    <linearGradient id="gmid" x1="0" y1="460" x2="0" y2="600" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#cf9e78"/><stop offset="1" stop-color="#e8cba7"/>
    </linearGradient>
    <linearGradient id="gnear" x1="0" y1="550" x2="0" y2="{H}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#d8ab82"/><stop offset="0.3" stop-color="#e6c6a0"/><stop offset="0.62" stop-color="#efdcbc"/><stop offset="1" stop-color="#efdcbc"/>
    </linearGradient>
    <linearGradient id="rim" x1="{sx - 330}" y1="0" x2="{sx + 330}" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#fff6e0" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#fffaf0" stop-opacity="1"/>
      <stop offset="1" stop-color="#fff6e0" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <g mask="url(#skyfade)">
    <g transform="translate({sx:.1f} {sy:.1f})" filter="url(#soft)">
      <g fill="url(#rayfade)">{''.join(rays)}</g>
    </g>
  </g>
  <circle cx="{sx:.1f}" cy="{sy:.1f}" r="520" fill="url(#dawn)"/>
  <path d="{path(far)}" fill="url(#gfar)"/>
  <path d="{path(massif)}" fill="url(#gmassif)" filter="url(#grain)"/>
  <path d="{'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in massif)}" fill="none" stroke="url(#rim)" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="{path(mid_l)}" fill="url(#gmid)" filter="url(#grain)"/>
  <path d="{path(mid_r)}" fill="url(#gmid)" filter="url(#grain)"/>
  <path d="{path(near)}" fill="url(#gnear)"/>
</svg>
"""

# The tablet, cut from one master drawing (600 x 940) into three pieces that CSS lays out at the tablet's width:
# the crown (y 0-260) and base (y 860-940) keep their shape, the body (y 260-860) repeats down the tablet. Each piece
# is rasterised once at a fixed size, so the cost never grows with the tablet's height. The stone's noise is tiled
# with the body's period (600) at the same phase in every piece, and each filter reaches past its piece's edges,
# so the pieces and the repeats join without a seam. One filter carves it all: chipped outline, bevelled rim lit
# from the top left, sunken writing field, grain, and the slab's thickness on the right and bottom.
TW, TOP, P, BOT = 600, 260, 600, 80  # the body is as tall as the tablet is wide: whole pixels at whole widths
TH = TOP + P + BOT
SHAPE = f"M11 {TOP - 30} A289 {TOP - 41} 0 0 1 589 {TOP - 30} L589 {TH - 14} L11 {TH - 14} Z"
# the writing field, 17 units inside the face: drawn white over the red face, so the filter reads both masks
# from the colour channels instead of eroding the outline (much cheaper)
FIELD = f"M28 {TOP - 30} A272 {TOP - 58} 0 0 1 572 {TOP - 30} L572 {TH - 31} L28 {TH - 31} Z"


def piece(vy0, vy1, fy0, fy1, ty):
    """The master drawing seen through y vy0-vy1; the filter works on y fy0-fy1; noise tiles start at y ty."""
    noise = f'stitchTiles="stitch" x="0" y="{ty}" width="{TW}" height="{P}"'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{TW}" height="{vy1 - vy0}" viewBox="0 {vy0} {TW} {vy1 - vy0}">
  <defs>
    <filter id="carve" filterUnits="userSpaceOnUse" x="0" y="{fy0}" width="{TW}" height="{fy1 - fy0}" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="3" seed="4" {noise} result="chipsT"/>
      <feTile in="chipsT" result="chips"/>
      <feColorMatrix in="SourceGraphic" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1 0 0 0 0" result="faceA"/>
      <feColorMatrix in="SourceGraphic" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 1 0 0 0" result="field"/>
      <feDisplacementMap in="faceA" in2="chips" scale="6" xChannelSelector="R" yChannelSelector="G" result="face"/>
      <feGaussianBlur in="face" stdDeviation="3.5" result="faceH"/>
      <feGaussianBlur in="field" stdDeviation="1.6" result="fieldH"/>
      <feComposite in="faceH" in2="fieldH" operator="arithmetic" k2="1" k3="-0.2" result="carved"/>
      <feTurbulence type="fractalNoise" baseFrequency="0.028" numOctaves="4" seed="3" {noise} result="reliefT"/>
      <feTile in="reliefT" result="relief"/>
      <feComposite in="carved" in2="relief" operator="arithmetic" k2="1" k3="0.3" k4="-0.15" result="height"/>
      <feDiffuseLighting in="height" surfaceScale="6" diffuseConstant="1" lighting-color="#ffffff" result="light">
        <feDistantLight azimuth="235" elevation="50"/>
      </feDiffuseLighting>
      <feComponentTransfer in="light" result="light2">
        <feFuncR type="linear" slope="0.75" intercept="0.33"/><feFuncG type="linear" slope="0.75" intercept="0.33"/><feFuncB type="linear" slope="0.75" intercept="0.33"/>
      </feComponentTransfer>
      <feFlood flood-color="#f6eee0" result="stone"/>
      <feBlend in="light2" in2="stone" mode="multiply" result="lit"/>
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="5" {noise} result="fineT"/>
      <feTile in="fineT" result="fine"/>
      <feColorMatrix in="fine" type="matrix" values="0.18 0 0 0 0.9  0.18 0 0 0 0.89  0.18 0 0 0 0.88  0 0 0 0 1" result="grain"/>
      <feBlend in="lit" in2="grain" mode="multiply" result="lit3"/>
      <feComposite in="lit3" in2="face" operator="in" result="slab"/>
      <feOffset in="face" dx="5" dy="7" result="sideA"/>
      <feFlood flood-color="#b3a488" result="sideC"/>
      <feBlend in="sideC" in2="grain" mode="multiply" result="sideG"/>
      <feComposite in="sideG" in2="sideA" operator="in" result="side"/>
      <feMerge><feMergeNode in="side"/><feMergeNode in="slab"/></feMerge>
    </filter>
  </defs>
  <g filter="url(#carve)"><path d="{SHAPE}" fill="#f00"/><path d="{FIELD}" fill="#fff"/></g>
</svg>
"""


pieces = {
    # crown and base run 16 units under the body, whose ends CSS fades out: the joins cross-fade on stone
    "tablet-crown.svg": piece(0, TOP + 16, TOP - P, TOP + 56, TOP - P),
    "tablet-body.svg": piece(TOP, TH - BOT, TOP - 40, TH - BOT + 40, TOP),
    "tablet-base.svg": piece(TH - BOT - 16, TH, TOP, TH, TOP),
}

for name, data in {"sinai.svg": sinai, **pieces}.items():
    with open(f"{root}/docs/{name}", "w", encoding="utf-8", newline="\n") as f:
        f.write(data)
print("summit", summit)
