"""Usage: python scripts/generate-assets.py assets

Generate the animated SVG assets for the GitHub profile README.

Every SVG is self-contained: inline CSS, no external fonts or scripts,
so GitHub renders it through <img> exactly as designed.
All motion respects prefers-reduced-motion (elements end in their final, visible state).
"""
import os
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"
os.makedirs(OUT, exist_ok=True)

# ---------- Brand palette (dark cards on any GitHub theme) ----------
BG = "#0D1117"
PANEL = "#161B22"
BORDER = "#30363D"
TEXT = "#E6EDF3"
MUTED = "#8B949E"
VIOLET = "#8B5CF6"
VIOLET_L = "#A78BFA"
VIOLET_XL = "#C4B5FD"
CYAN = "#22D3EE"
CYAN_L = "#67E8F9"
AMBER = "#FBBF24"
RED = "#F87171"
GREEN = "#3FB950"

MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', 'DejaVu Sans Mono', monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

REDUCED = """
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; }
}"""


def write(name, svg):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", path, len(svg), "bytes")


def frame_defs(gid):
    """Gradient border + soft glow shared by the card-style SVGs."""
    return f"""
  <linearGradient id="{gid}-border" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{VIOLET}"/>
    <stop offset="0.5" stop-color="{BORDER}"/>
    <stop offset="1" stop-color="{CYAN}"/>
  </linearGradient>
  <radialGradient id="{gid}-glow" cx="0.85" cy="0" r="0.7">
    <stop offset="0" stop-color="{VIOLET}" stop-opacity="0.18"/>
    <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="{gid}-glow2" cx="0.05" cy="1" r="0.6">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0.10"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </radialGradient>"""


# =====================================================================
# 1) Terminal: `curl /api/v1/me` with a typed command and a JSON reply
# =====================================================================
def terminal():
    W, H = 860, 452
    cmd = "curl -s localhost:3000/api/v1/me | jq"
    # Only facts Mohammed stated. Edit here, then re-run the script.
    body = [
        ("{", None),
        ('  "name": "Mohammed Ferwana",', None),
        ('  "role": "Backend Engineer",', None),
        ('  "location": "Gaza, Palestine",', None),
        ('  "education": "Computer Systems Engineering @ Al-Azhar University",', None),
        ('  "graduating": 2027,', None),
        ('  "cgpa": 93.3,', None),
        ('  "stack": ["Node.js", "Express", "MongoDB", "PostgreSQL"],', None),
        ('  "building": "Sawn, a multi-tenant claims SaaS for insurers",', None),
        ('  "focus": ["REST APIs", "RBAC", "state machines", "testing"]', None),
        ("}", None),
    ]

    def colorize(line):
        """Tiny JSON highlighter: keys violet, strings cyan, numbers amber."""
        out, i = [], 0
        n = len(line)
        while i < n:
            c = line[i]
            if c == '"':
                j = line.index('"', i + 1)
                tok = line[i:j + 1]
                is_key = line[j + 1:j + 2] == ":"
                color = VIOLET_XL if is_key else CYAN_L
                out.append(f'<tspan fill="{color}">{escape(tok)}</tspan>')
                i = j + 1
            elif c.isdigit():
                j = i
                while j < n and (line[j].isdigit() or line[j] == "."):
                    j += 1
                out.append(f'<tspan fill="{AMBER}">{line[i:j]}</tspan>')
                i = j
            else:
                j = i
                while j < n and line[j] != '"' and not line[j].isdigit():
                    j += 1
                out.append(f'<tspan fill="{MUTED}">{escape(line[i:j])}</tspan>')
                i = j
        return "".join(out)

    type_start, per_char = 0.6, 0.045
    type_end = type_start + per_char * len(cmd)
    resp_start = type_end + 0.45
    per_line = 0.14

    chars = "".join(
        f'<tspan class="ch" style="animation-delay:{type_start + k * per_char:.3f}s">{escape(ch)}</tspan>'
        for k, ch in enumerate(cmd)
    )

    x0, y_cmd, lh = 28, 84, 25
    lines = []
    for k, (ln, _) in enumerate(body):
        y = y_cmd + 36 + k * lh
        d = resp_start + k * per_line
        lines.append(
            f'<text class="ln" x="{x0}" y="{y}" style="animation-delay:{d:.2f}s">{colorize(ln)}</text>'
        )
    final_y = y_cmd + 36 + len(body) * lh + 14
    cursor_delay = resp_start + len(body) * per_line + 0.2

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">GET /api/v1/me</title>
<desc id="d">A terminal that calls an API endpoint and prints a JSON profile of Mohammed Ferwana, a backend engineer from Gaza.</desc>
<defs>{frame_defs("term")}
</defs>
<style>
  .ch {{ opacity: 0; animation: show 0.01s linear both; }}
  .ln {{ opacity: 0; animation: rise 0.35s ease-out both; }}
  .cursor {{ opacity: 0; animation: show 0.01s linear {cursor_delay:.2f}s both, blink 1.1s steps(1) {cursor_delay:.2f}s infinite; }}
  .prompt {{ opacity: 0; animation: show 0.01s linear {cursor_delay:.2f}s both; }}
  .status {{ opacity: 0; animation: rise 0.4s ease-out {resp_start - 0.15:.2f}s both; }}
  @keyframes show {{ to {{ opacity: 1; }} }}
  @keyframes rise {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}
  @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
  text {{ font-family: {MONO}; font-size: 15px; white-space: pre; }}
  {REDUCED}
  @media (prefers-reduced-motion: reduce) {{ .ch, .ln, .cursor, .status, .prompt {{ opacity: 1; }} }}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{BG}" stroke="url(#term-border)" stroke-width="1.5"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#term-glow)"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#term-glow2)"/>
<path d="M15 1.75 H{W - 15} A13.25 13.25 0 0 1 {W - 1.75} 15 V40 H1.75 V15 A13.25 13.25 0 0 1 15 1.75 Z" fill="{PANEL}"/>
<line x1="1.75" y1="40" x2="{W - 1.75}" y2="40" stroke="{BORDER}"/>
<circle cx="24" cy="21" r="6" fill="#FF5F56"/>
<circle cx="44" cy="21" r="6" fill="#FFBD2E"/>
<circle cx="64" cy="21" r="6" fill="#27C93F"/>
<text x="{W / 2}" y="26" text-anchor="middle" fill="{MUTED}" style="font-size:13px">ferwana@gaza: ~/api</text>
<text x="{W - 24}" y="26" text-anchor="end" class="status" style="font-size:12px"><tspan fill="{GREEN}">●</tspan><tspan fill="{MUTED}"> 200 OK · application/json</tspan></text>
<text x="{x0}" y="{y_cmd}" xml:space="preserve"><tspan fill="{GREEN}">$ </tspan><tspan fill="{TEXT}">{chars}</tspan></text>
{chr(10).join(lines)}
<text class="prompt" x="{x0}" y="{final_y}"><tspan fill="{GREEN}">$</tspan></text>
<rect class="cursor" x="{x0 + 16}" y="{final_y - 14}" width="9" height="18" rx="1" fill="{VIOLET_L}"/>
</svg>
"""
    write("terminal.svg", svg)


# =====================================================================
# 2) Request pipeline: how a request moves through Mohammed's API layers
# =====================================================================
def pipeline():
    nodes = [
        ("Client", "HTTPS · JSON"),
        ("Router", "rate limit"),
        ("Validate", "Joi schema"),
        ("Auth", "JWT · RBAC"),
        ("Controller", "asyncWrapper"),
        ("Service", "business rules"),
        ("Repository", "tenant-scoped"),
        ("MongoDB", "Atlas"),
    ]
    W, H = 892, 268
    bw, bh, gap, x0, y0 = 92, 62, 15, 32, 64
    step = bw + gap
    cx = [x0 + i * step + bw / 2 for i in range(len(nodes))]
    cycle = 7.0
    req_t, resp_from, resp_t = 3.2, 3.6, 6.4
    dist = cx[-1] - cx[0]
    lane_req, lane_resp = 168, 200

    def pct(t):
        return f"{t / cycle * 100:.2f}%"

    boxes = []
    for i, (name, sub) in enumerate(nodes):
        x = x0 + i * step
        delay = req_t * i / (len(nodes) - 1)
        boxes.append(
            f'<g><rect class="node" x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="10" style="animation-delay:{delay:.2f}s"/>'
            f'<text x="{x + bw / 2}" y="{y0 + 27}" text-anchor="middle" class="nm">{name}</text>'
            f'<text x="{x + bw / 2}" y="{y0 + 46}" text-anchor="middle" class="sb">{escape(sub)}</text></g>'
        )
    arrows = []
    for i in range(len(nodes) - 1):
        xa = x0 + i * step + bw + 1
        xb = xa + gap - 2
        y = y0 + bh / 2
        arrows.append(f'<line class="flow" x1="{xa}" y1="{y}" x2="{xb}" y2="{y}"/>')
    ticks = "".join(
        f'<line x1="{c}" y1="{lane_req - 5}" x2="{c}" y2="{lane_resp + 5}" stroke="{BORDER}" stroke-dasharray="2 3"/>' for c in cx
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Request lifecycle</title>
<desc id="d">A request travels from the client through router, validation, auth, controller, service and repository layers to MongoDB, and a JSON response travels back.</desc>
<defs>{frame_defs("pipe")}
  <filter id="pipe-blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<style>
  text {{ font-family: {SANS}; }}
  .ttl {{ font-size: 13px; fill: {MUTED}; letter-spacing: 0.08em; }}
  .nm {{ font-size: 14px; font-weight: 600; fill: {TEXT}; }}
  .sb {{ font-family: {MONO}; font-size: 10.5px; fill: {MUTED}; }}
  .lane {{ font-family: {MONO}; font-size: 11px; }}
  .node {{ fill: {PANEL}; stroke: {BORDER}; stroke-width: 1.2; animation: pulse {cycle}s ease-out infinite both; }}
  .flow {{ stroke: {VIOLET}; stroke-width: 2; stroke-dasharray: 3 3; animation: dash 0.8s linear infinite; }}
  .req {{ animation: req {cycle}s cubic-bezier(.45,.05,.55,.95) infinite both; }}
  .resp {{ animation: resp {cycle}s cubic-bezier(.45,.05,.55,.95) infinite both; }}
  .ok {{ animation: ok {cycle}s ease-out infinite both; }}
  @keyframes dash {{ to {{ stroke-dashoffset: -6; }} }}
  @keyframes pulse {{
    0% {{ stroke: {BORDER}; fill: {PANEL}; }}
    3% {{ stroke: {VIOLET_L}; fill: #221A3A; }}
    14% {{ stroke: {BORDER}; fill: {PANEL}; }}
    100% {{ stroke: {BORDER}; fill: {PANEL}; }}
  }}
  @keyframes req {{
    0% {{ transform: translateX(0); opacity: 0; }}
    2% {{ opacity: 1; }}
    {pct(req_t)} {{ transform: translateX({dist}px); opacity: 1; }}
    {pct(req_t + 0.2)} {{ transform: translateX({dist}px); opacity: 0; }}
    100% {{ transform: translateX({dist}px); opacity: 0; }}
  }}
  @keyframes resp {{
    0%, {pct(resp_from)} {{ transform: translateX(0); opacity: 0; }}
    {pct(resp_from + 0.1)} {{ opacity: 1; }}
    {pct(resp_t)} {{ transform: translateX(-{dist}px); opacity: 1; }}
    {pct(resp_t + 0.2)}, 100% {{ transform: translateX(-{dist}px); opacity: 0; }}
  }}
  @keyframes ok {{
    0%, {pct(resp_t - 0.1)} {{ opacity: 0; }}
    {pct(resp_t + 0.15)}, 96% {{ opacity: 1; }}
    100% {{ opacity: 0; }}
  }}
  {REDUCED}
  @media (prefers-reduced-motion: reduce) {{ .req, .resp {{ opacity: 0; }} .ok {{ opacity: 1; }} }}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{BG}" stroke="url(#pipe-border)" stroke-width="1.5"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#pipe-glow)"/>
<text x="26" y="38" class="ttl">ONE PATH FOR EVERY REQUEST</text>
<text x="{W - 26}" y="38" text-anchor="end" class="ttl" style="letter-spacing:0">modular layered architecture</text>
{"".join(arrows)}
{"".join(boxes)}
{ticks}
<line x1="{cx[0]}" y1="{lane_req}" x2="{cx[-1]}" y2="{lane_req}" stroke="{VIOLET}" stroke-opacity="0.25" stroke-width="2"/>
<line x1="{cx[0]}" y1="{lane_resp}" x2="{cx[-1]}" y2="{lane_resp}" stroke="{CYAN}" stroke-opacity="0.22" stroke-width="2"/>
<text x="{cx[0] - 6}" y="{lane_req + 4}" text-anchor="end" class="lane" fill="{VIOLET_L}">req</text>
<text x="{cx[0] - 6}" y="{lane_resp + 4}" text-anchor="end" class="lane" fill="{CYAN_L}">res</text>
<g class="req">
  <circle cx="{cx[0]}" cy="{lane_req}" r="9" fill="{VIOLET}" filter="url(#pipe-blur)"/>
  <circle cx="{cx[0]}" cy="{lane_req}" r="5" fill="{VIOLET_XL}"/>
</g>
<g class="resp">
  <circle cx="{cx[-1]}" cy="{lane_resp}" r="9" fill="{CYAN}" filter="url(#pipe-blur)"/>
  <circle cx="{cx[-1]}" cy="{lane_resp}" r="5" fill="{CYAN_L}"/>
</g>
<text x="26" y="{H - 24}" class="lane ok"><tspan fill="{GREEN}">200 OK</tspan><tspan fill="{MUTED}">  {{ </tspan><tspan fill="{VIOLET_XL}">success</tspan><tspan fill="{MUTED}">, </tspan><tspan fill="{VIOLET_XL}">data</tspan><tspan fill="{MUTED}">, </tspan><tspan fill="{VIOLET_XL}">error</tspan><tspan fill="{MUTED}">, </tspan><tspan fill="{VIOLET_XL}">meta</tspan><tspan fill="{MUTED}"> }}</tspan></text>
<text x="{W - 26}" y="{H - 24}" text-anchor="end" class="lane" fill="{MUTED}">organizationId comes from the JWT, never from the client</text>
</svg>
"""
    write("request-pipeline.svg", svg)


# =====================================================================
# 3) Sawn claim lifecycle: the finite state machine, happy path animated
# =====================================================================
def fsm():
    W, H = 900, 398
    bw, bh = 134, 44
    colx = [22 + i * (bw + 47) for i in range(5)]
    rowy = [86, 196, 306]

    def box(c, r):
        return colx[c], rowy[r]

    states = {
        "NEW": (0, 0, "normal"),
        "PENDING_ACCEPTANCE": (1, 0, "normal"),
        "ASSIGNED": (2, 0, "normal"),
        "IN_PROGRESS": (3, 0, "normal"),
        "SUBMITTED": (4, 0, "normal"),
        "CORRECTION_REQUIRED": (3, 1, "loop"),
        "UNDER_REVIEW": (4, 1, "normal"),
        "CLOSED": (2, 2, "terminal"),
        "APPROVED": (3, 2, "normal"),
        "REJECTED": (4, 2, "reject"),
    }
    happy = ["NEW", "PENDING_ACCEPTANCE", "ASSIGNED", "IN_PROGRESS", "SUBMITTED",
             "UNDER_REVIEW", "APPROVED", "CLOSED"]
    cycle = 9.6
    step_t = 1.0

    def center(s):
        c, r, _ = states[s]
        x, y = box(c, r)
        return x + bw / 2, y + bh / 2

    parts = []
    for s, (c, r, kind) in states.items():
        x, y = box(c, r)
        delay = happy.index(s) * step_t if s in happy else None
        cls = "st hp" if delay is not None else "st"
        stroke = {"normal": BORDER, "loop": AMBER, "terminal": BORDER, "reject": RED}[kind]
        style = f' style="animation-delay:{delay:.1f}s"' if delay is not None else ""
        dash = ' stroke-dasharray="4 3"' if kind == "loop" else ""
        parts.append(
            f'<rect class="{cls}" x="{x}" y="{y}" width="{bw}" height="{bh}" rx="9" stroke="{stroke}"{dash}{style}/>'
        )
        if kind in ("terminal", "reject"):
            parts.append(
                f'<rect x="{x + 4}" y="{y + 4}" width="{bw - 8}" height="{bh - 8}" rx="6" fill="none" stroke="{stroke}" stroke-opacity="0.6"/>'
            )
        label_color = {"loop": AMBER, "reject": RED}.get(kind, TEXT)
        size = "10.5" if len(s) > 15 else "12"
        parts.append(
            f'<text x="{x + bw / 2}" y="{y + bh / 2 + 4}" text-anchor="middle" class="sn" fill="{label_color}" style="font-size:{size}px">{s}</text>'
        )

    def arrow(x1, y1, x2, y2, color, label=None, lx=None, ly=None, dashed=False, cls="ed"):
        d = ' stroke-dasharray="4 3"' if dashed else ""
        out = f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.6"{d} marker-end="url(#ah-{color[1:]})"/>'
        if label:
            out += f'<text x="{lx}" y="{ly}" text-anchor="middle" class="el">{label}</text>'
        return out

    edges = []
    # Row A, left to right
    labels_a = ["assign", "accept", "start", "submit"]
    for i in range(4):
        x1 = colx[i] + bw + 2
        x2 = colx[i + 1] - 4
        y = rowy[0] + bh / 2
        edges.append(arrow(x1, y, x2, y, VIOLET, labels_a[i], (x1 + x2) / 2, y - 9))
    # SUBMITTED -> UNDER_REVIEW
    x = colx[4] + bw / 2
    edges.append(arrow(x, rowy[0] + bh + 2, x, rowy[1] - 4, VIOLET, "review", x + 28, (rowy[0] + bh + rowy[1]) / 2 + 4))
    # UNDER_REVIEW -> CORRECTION_REQUIRED
    y = rowy[1] + bh / 2
    edges.append(arrow(colx[4] - 2, y, colx[3] + bw + 4, y, AMBER, "fix", (colx[4] + colx[3] + bw) / 2, y - 9, dashed=True))
    # CORRECTION_REQUIRED -> IN_PROGRESS
    x = colx[3] + bw / 2
    edges.append(arrow(x, rowy[1] - 2, x, rowy[0] + bh + 4, AMBER, "resume", x - 30, (rowy[0] + bh + rowy[1]) / 2 + 4, dashed=True))
    # UNDER_REVIEW -> REJECTED
    x = colx[4] + bw / 2
    edges.append(arrow(x, rowy[1] + bh + 2, x, rowy[2] - 4, RED, "reject", x + 26, (rowy[1] + bh + rowy[2]) / 2 + 4))
    # UNDER_REVIEW -> APPROVED (diagonal)
    edges.append(arrow(colx[4] + 18, rowy[1] + bh + 2, colx[3] + bw - 14, rowy[2] - 4, VIOLET, "approve",
                       colx[3] + bw + 2, (rowy[1] + bh + rowy[2]) / 2 + 16))
    # APPROVED -> CLOSED
    y = rowy[2] + bh / 2
    edges.append(arrow(colx[3] - 2, y, colx[2] + bw + 4, y, VIOLET, "close", (colx[3] + colx[2] + bw) / 2, y - 9))

    # Travelling token along the happy path
    pts = [center(s) for s in happy]
    path_d = "M" + " L".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    n_seg = len(pts) - 1
    # keyPoints are fractions of path LENGTH, so weight each segment by its real length
    seg = [((pts[i + 1][0] - pts[i][0]) ** 2 + (pts[i + 1][1] - pts[i][1]) ** 2) ** 0.5 for i in range(n_seg)]
    acc, cum = 0.0, [0.0]
    for s_len in seg:
        acc += s_len
        cum.append(acc)
    key_points = ";".join(f"{c / acc:.4f}" for c in cum)

    markers = "".join(
        f'<marker id="ah-{c[1:]}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
        for c in (VIOLET, AMBER, RED)
    )

    legend_y = H - 22
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Sawn claim lifecycle</title>
<desc id="d">Finite state machine of an insurance claim in Sawn: NEW, PENDING_ACCEPTANCE, ASSIGNED, IN_PROGRESS, SUBMITTED, UNDER_REVIEW, then APPROVED and CLOSED, or REJECTED, or CORRECTION_REQUIRED which loops back to IN_PROGRESS.</desc>
<defs>{frame_defs("fsm")}{markers}
  <filter id="fsm-blur" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="4"/></filter>
</defs>
<style>
  text {{ font-family: {SANS}; }}
  .ttl {{ font-size: 13px; fill: {MUTED}; letter-spacing: 0.08em; }}
  .sn {{ font-family: {MONO}; font-weight: 600; }}
  .el {{ font-family: {MONO}; font-size: 10px; fill: {MUTED}; }}
  .st {{ fill: {PANEL}; stroke-width: 1.3; }}
  .hp {{ animation: lit {cycle}s ease-out infinite both; }}
  @keyframes lit {{
    0% {{ fill: {PANEL}; }}
    2% {{ fill: #2A1F4A; stroke: {VIOLET_L}; }}
    11% {{ fill: #1E1833; stroke: {VIOLET}; }}
    20%, 100% {{ fill: {PANEL}; stroke: {BORDER}; }}
  }}
  {REDUCED}
</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{BG}" stroke="url(#fsm-border)" stroke-width="1.5"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#fsm-glow)"/>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#fsm-glow2)"/>
<text x="22" y="38" class="ttl">SAWN · CLAIM LIFECYCLE</text>
<text x="{W - 22}" y="38" text-anchor="end" class="ttl" style="letter-spacing:0">10 states · role-guarded transitions</text>
{"".join(edges)}
{"".join(parts)}
<g>
  <circle r="8" fill="{VIOLET}" filter="url(#fsm-blur)" opacity="0.75">
    <animateMotion dur="{cycle}s" repeatCount="indefinite" calcMode="linear" keyPoints="{key_points};1" keyTimes="{";".join(f"{(i * step_t) / cycle:.4f}" for i in range(n_seg + 1))};1" path="{path_d}"/>
  </circle>
  <circle r="3.5" fill="{VIOLET_XL}">
    <animateMotion dur="{cycle}s" repeatCount="indefinite" calcMode="linear" keyPoints="{key_points};1" keyTimes="{";".join(f"{(i * step_t) / cycle:.4f}" for i in range(n_seg + 1))};1" path="{path_d}"/>
  </circle>
</g>
<text x="22" y="{legend_y}" class="el" style="font-size:11px"><tspan fill="{VIOLET_L}">■</tspan> happy path   <tspan fill="{AMBER}">■</tspan> correction loop   <tspan fill="{RED}">■</tspan> rejected   <tspan fill="{MUTED}">▣ terminal state</tspan></text>
<text x="{W - 22}" y="{legend_y}" text-anchor="end" class="el" style="font-size:11px">atomic findOneAndUpdate on organizationId + expected status</text>
</svg>
"""
    write("claim-lifecycle.svg", svg)


# =====================================================================
# 4) Divider: gradient line with a light sweep
# =====================================================================
def divider():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="8" viewBox="0 0 1000 8" preserveAspectRatio="none" role="img" aria-label="divider">
<defs>
  <linearGradient id="base" x1="0" x2="1">
    <stop offset="0" stop-color="{VIOLET}" stop-opacity="0"/>
    <stop offset="0.25" stop-color="{VIOLET}"/>
    <stop offset="0.75" stop-color="{CYAN}"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="shine" x1="0" x2="1">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
    <stop offset="0.5" stop-color="#FFFFFF" stop-opacity="0.9"/>
    <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
  </linearGradient>
  <clipPath id="c"><rect x="0" y="3" width="1000" height="2"/></clipPath>
</defs>
<style>
  .sweep {{ animation: sweep 4.5s ease-in-out infinite; }}
  @keyframes sweep {{ from {{ transform: translateX(-220px); }} to {{ transform: translateX(1000px); }} }}
  {REDUCED}
  @media (prefers-reduced-motion: reduce) {{ .sweep {{ opacity: 0; }} }}
</style>
<rect x="0" y="3" width="1000" height="2" fill="url(#base)"/>
<g clip-path="url(#c)"><rect class="sweep" x="0" y="3" width="220" height="2" fill="url(#shine)"/></g>
</svg>
"""
    write("divider.svg", svg)


# =====================================================================
# 5) Header banner: aurora gradient, drifting waves, role and stack
# =====================================================================


def wave_path(y, amp, seed=0):
    """A seamless wave across 2000px (two periods of 1000px) so a -1000px loop has no jump."""
    pts = []
    for i in range(0, 9):
        x = i * 250
        dy = amp if (i + seed) % 2 else -amp
        pts.append((x, y + dy))
    d = f"M0 {pts[0][1]}"
    for i in range(1, len(pts)):
        x0, y0 = pts[i - 1]
        x1, y1 = pts[i]
        d += f" C {x0 + 125} {y0}, {x1 - 125} {y1}, {x1} {y1}"
    return d + " L 2000 400 L 0 400 Z"


def header():
    W, H = 1000, 250
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Backend Engineer</title>
<desc id="d">Banner: Backend Engineer working with Node.js, Express, MongoDB and PostgreSQL, based in Gaza, Palestine.</desc>
<defs>
  <linearGradient id="hd-bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#1E1B4B"/>
    <stop offset="0.5" stop-color="#5B21B6"/>
    <stop offset="1" stop-color="#0E7490"/>
  </linearGradient>
  <radialGradient id="hd-a1" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{VIOLET_L}" stop-opacity="0.55"/>
    <stop offset="1" stop-color="{VIOLET_L}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="hd-a2" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0.45"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="hd-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#FFFFFF" fill-opacity="0.10"/>
  </pattern>
  <clipPath id="hd-clip"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<style>
  text {{ font-family: {SANS}; }}
  .mono {{ font-family: {MONO}; }}
  .a1 {{ animation: drift1 14s ease-in-out infinite alternate; }}
  .a2 {{ animation: drift2 18s ease-in-out infinite alternate; }}
  .w1 {{ animation: wave 16s linear infinite; }}
  .w2 {{ animation: wave 24s linear infinite reverse; }}
  .up {{ opacity: 0; animation: up 0.8s ease-out both; }}
  .ping {{ animation: ping 1.8s ease-out infinite; transform-origin: 862px 41px; }}
  @keyframes drift1 {{ from {{ transform: translate(0, 0); }} to {{ transform: translate(180px, 30px); }} }}
  @keyframes drift2 {{ from {{ transform: translate(0, 0); }} to {{ transform: translate(-200px, -20px); }} }}
  @keyframes wave {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-1000px); }} }}
  @keyframes up {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
  @keyframes ping {{ 0% {{ transform: scale(1); opacity: 0.8; }} 100% {{ transform: scale(2.6); opacity: 0; }} }}
  {REDUCED}
  @media (prefers-reduced-motion: reduce) {{ .up {{ opacity: 1; }} .ping {{ opacity: 0; }} }}
</style>
<g clip-path="url(#hd-clip)">
  <rect width="{W}" height="{H}" fill="url(#hd-bg)"/>
  <rect width="{W}" height="{H}" fill="url(#hd-dots)"/>
  <circle class="a1" cx="160" cy="40" r="260" fill="url(#hd-a1)"/>
  <circle class="a2" cx="860" cy="220" r="280" fill="url(#hd-a2)"/>
  <path class="w1" d="{wave_path(205, 14)}" fill="#FFFFFF" fill-opacity="0.07"/>
  <path class="w2" d="{wave_path(222, 10, 1)}" fill="#FFFFFF" fill-opacity="0.06"/>
</g>
<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="17.25" fill="none" stroke="#FFFFFF" stroke-opacity="0.12" stroke-width="1.5"/>
<g>
  <rect x="842" y="27" width="128" height="28" rx="14" fill="#0D1117" fill-opacity="0.45" stroke="#FFFFFF" stroke-opacity="0.15"/>
  <circle class="ping" cx="862" cy="41" r="4.5" fill="{GREEN}"/>
  <circle cx="862" cy="41" r="4.5" fill="{GREEN}"/>
  <text x="874" y="45.5" class="mono" font-size="12.5" fill="#E6EDF3">api: online</text>
</g>
<text class="up mono" x="56" y="78" font-size="15" fill="{CYAN_L}" style="animation-delay:0.1s">$ whoami</text>
<text class="up" x="54" y="140" font-size="60" font-weight="800" fill="#FFFFFF" letter-spacing="-1" style="animation-delay:0.25s">Backend Engineer</text>
<text class="up mono" x="57" y="182" font-size="19" fill="#E9D5FF" style="animation-delay:0.45s">Node.js · Express · MongoDB · PostgreSQL</text>
<text class="up mono" x="57" y="214" font-size="14" fill="#FFFFFF" fill-opacity="0.75" style="animation-delay:0.6s">Gaza, Palestine</text>
</svg>
"""
    write("header.svg", svg)


def footer():
    W, H = 1000, 110
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" preserveAspectRatio="none" role="img" aria-label="decorative footer wave">
<defs>
  <linearGradient id="ft-bg" x1="0" x2="1">
    <stop offset="0" stop-color="#0E7490"/>
    <stop offset="0.5" stop-color="#5B21B6"/>
    <stop offset="1" stop-color="#1E1B4B"/>
  </linearGradient>
  <clipPath id="ft-clip"><rect width="{W}" height="{H}"/></clipPath>
</defs>
<style>
  .w1 {{ animation: wave 18s linear infinite; }}
  .w2 {{ animation: wave 26s linear infinite reverse; }}
  @keyframes wave {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-1000px); }} }}
  {REDUCED}
</style>
<g clip-path="url(#ft-clip)">
  <path class="w2" d="{wave_path(40, 12, 1)}" fill="url(#ft-bg)" fill-opacity="0.35"/>
  <path class="w1" d="{wave_path(55, 14)}" fill="url(#ft-bg)"/>
</g>
</svg>
"""
    write("footer.svg", svg)


# =====================================================================
# 6) Typing line: SMIL discrete steps, exact per character via textLength
# =====================================================================
def typing():
    lines = [
        "I design secure, multi-tenant REST APIs",
        "Sole backend engineer on Sawn, a claims SaaS",
        "Clean layers · RBAC · state machines · tests",
    ]
    W, H, fs = 760, 48, 21
    cw = 12.6  # forced advance per character (textLength), so steps land on glyph edges
    type_dt, erase_dt, hold, gap = 0.065, 0.025, 1.8, 0.35
    slots, t = [], 0.0
    for ln in lines:
        n = len(ln)
        dur = n * type_dt + hold + n * erase_dt + gap
        slots.append((t, n))
        t += dur
    C = t
    color = VIOLET

    def kt(x):
        return f"{min(x / C, 1):.5f}"

    groups = []
    for i, ((s, n), ln) in enumerate(zip(slots, lines)):
        w = n * cw
        left = W / 2 - w / 2
        times, vals = [0.0], [0.0]
        for k in range(1, n + 1):
            times.append(s + k * type_dt)
            vals.append(k * cw)
        te = s + n * type_dt + hold
        for k in range(1, n + 1):
            times.append(te + k * erase_dt)
            vals.append((n - k) * cw)
        if times[1] <= 0:  # first line starts at t=0: drop the duplicate 0 key
            times[1] = 0.0001
        key_times = ";".join(kt(x) for x in times)
        widths = ";".join(f"{v:.1f}" for v in vals)
        cursor_x = ";".join(f"{left + v:.1f}" for v in vals)
        # cursor only visible during this line's slot
        vis_t = ";".join(kt(x) for x in (0, max(s, 0.0001) if i else 0, te + n * erase_dt))
        vis_v = "0;1;0" if i else "1;1;0"
        if i == 0:
            vis_t = f"0;{kt(te + n * erase_dt)}"
            vis_v = "1;0"
        groups.append(f"""
  <clipPath id="ty-c{i}"><rect x="{left:.1f}" y="0" width="0" height="{H}">
    <animate attributeName="width" dur="{C:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{key_times}" values="{widths}"/>
  </rect></clipPath>
  <text x="{W / 2}" y="{H / 2 + 7}" text-anchor="middle" textLength="{w:.1f}" lengthAdjust="spacingAndGlyphs" clip-path="url(#ty-c{i})">{escape(ln)}</text>
  <rect class="cur" x="{left:.1f}" y="{H / 2 - 12}" width="2.5" height="24" fill="{color}" opacity="0">
    <animate attributeName="x" dur="{C:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{key_times}" values="{cursor_x}"/>
    <animate attributeName="opacity" dur="{C:.2f}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{vis_t}" values="{vis_v}"/>
  </rect>""")

    first = lines[0]
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
<title id="t">{escape(" / ".join(lines))}</title>
<style>
  text {{ font-family: {MONO}; font-size: {fs}px; font-weight: 600; fill: {color}; }}
  .static {{ display: none; }}
  @media (prefers-reduced-motion: reduce) {{ .anim {{ display: none; }} .static {{ display: inline; }} }}
</style>
<g class="anim">{"".join(groups)}
</g>
<g class="static"><text x="{W / 2}" y="{H / 2 + 7}" text-anchor="middle">{escape(first)}</text></g>
</svg>
"""
    write("typing.svg", svg)


terminal()
pipeline()
fsm()
divider()
header()
footer()
typing()
