#!/usr/bin/env python3
"""
atakrr_status.py — Pre-alpha project statement + scaffolder

Usage:
  python atakrr_status.py --print
  python atakrr_status.py --write  # writes README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md
"""

from datetime import date
import argparse
from textwrap import dedent

PROJECT = "ATAKRR (Android Team Awareness Kit — Radio Reconnaissance)"
VERSION = "Pre-Alpha (Proof-of-Concept)"
TODAY = date.today().isoformat()

ASCII = r"""
  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$   /$$ /$$$$$$$  /$$$$$$$       
 /$$__  $$|__  $$__//$$__  $$| $$  /$$/| $$__  $$| $$__  $$      
| $$  \ $$   | $$  | $$  \ $$| $$ /$$/ | $$  \ $$| $$  \ $$      
| $$$$$$$$   | $$  | $$$$$$$$| $$$$$/  | $$$$$$$/| $$$$$$$/      
| $$__  $$   | $$  | $$__  $$| $$  $$  | $$__  $$| $$__  $$      
| $$  | $$   | $$  | $$  | $$| $$\  $$ | $$  \ $$| $$  \ $$      
| $$  | $$   | $$  | $$  | $$| $$ \  $$| $$  | $$| $$  | $$      
|__/  |__/   |__/  |__/  |__/|__/  \__/|__/  |__/|__/  |__/
"""

def statement():
    return dedent(f"""
    {ASCII}
    Project: {PROJECT}
    Status:  {VERSION}
    Date:    {TODAY}

    # What this is
    ATAKRR is a modular RF situational-awareness stack for ATAK:
      • PEWPEW — low-profile capture nodes (fixed/drone-deployable) for multi-band IQ & metadata
      • BAMMO — beacon-activated, encrypted, low-probability-of-intercept data retrieval
      • FoG Nodes — backpack/vehicular edge compute for triage, geolocation, & cueing
      • AMC/ML — automatic modulation/protocol/emitters (RF fingerprinting) classification
      • ATAK Plugin — UI overlays, tasking, retrieval control, and live alerting
      • Infra — storage, labeling, evaluation pipelines, and deployment tooling

    # Why you're seeing this now (and why there's “no code” yet)
    This repo is intentionally in **pre-alpha** while we validate hardware, data pipelines,
    and funding. Portions of the work exist as private prototypes (hardware test rigs,
    acquisition scripts, labeling pipelines, and ATAK UI spikes). Open-sourcing RF tools
    responsibly requires:
      1) scrubbing sensitive captures & locations,
      2) publishing reproducible datasets & tests,
      3) splitting research code from field tools, and
      4) hardening for on-device reliability.

    We’re staging that in public, incrementally. If you need a date-stamped statement:
    “As of {TODAY}, ATAKRR is a pre-alpha proof-of-concept recruiting collaborators.
     Source drops will begin as milestones (M1→M3) are met.”

    # Roadmap (subject to revision)
    M0 — Project skeleton & public plan (this) ✓
    M1 — Data & DevKit drop:
          • SDR capture scripts (HackRF/BladeRF/SDR-Play) + sample IQ datasets
          • Label schema, eval harness, and baseline AMC models
    M2 — BAMMO beacon prototype:
          • Retrieval handshake & encrypted transfer over controlled beacon SSID
          • Air-gapped buffering + audit logs
    M3 — ATAK plugin alpha:
          • Map overlays, capture/retrieval controls, alert toasts
          • Sim feed playback for demoing without hardware
    M4 — Geolocation & multipath helpers:
          • TDOA/FDOA building blocks; heatmap overlay
    M5 — Fieldable FoG bundle:
          • Edge triage on SBC (Jetson/Orange Pi), health telemetry
    M6 — Hardening & OSS split:
          • Public SDKs, plugin template, docs, and stable APIs

    # What help we’re recruiting (paid if/when funding lands)
      • Android/ATAK devs — plugin UX, data layers, offline-first sync
      • SDR wranglers — capture pipelines, RF front-ends, calibration
      • ML/AMC folks — robust modulation/protocol/RF-FP models, on-device optimizations
      • Backend/data — dataset versioning, eval dashboards, auth, object storage
      • Field eng — packaging, power, thermal, antennas, deployment SOPs

    Compensation & IP
      • Roles convert to **paid** under grant/contract awards; we budget for market-rate
        stipends or subcontracts.
      • We use lightweight contributor agreements (CLA/DCO). Public modules ship under
        permissive licenses (MIT/BSD/Apache) unless a dependency forces otherwise.
      • We attribute contributors in docs and grant reports.

    # Code you will see first
      • /src/atakrr.py           — yay, now there's code! 2025-10-10
      • /sdk/atakrr-core         — typed data models, message bus, test fixtures
      • /plugins/atakrr          — ATAK plugin (alpha)
      • /rf/capture              — CLI capture tools + reproducible IQ datasets
      • /ml/amc                  — baselines + eval harness, export to ONNX/TFLite
      • /infra/pipelines         — labeling/packaging/eval CI

    # Security & ethics
      • No undisclosed collection. Demo datasets are synthetically generated or consented.
      • Red-team ourselves. Document limitations, failure modes, and safe-use guidelines.

    # Get involved
      1) Open an issue titled “Interested: <role>”
      2) Share a small artifact (repo, snippet, or write-up)
      3) We’ll schedule a short sync and align a starter task

    # Contact
      • Primary maintainer: Fitz (Jack Driscoll) — via GitHub issues or project email (listed in README)
      • Project tag: #ATAKRR
      • ELECTRONIC MAIL: ATAKRR@ETHERTECH.ORG

    # FAQ (short)
      • “Why not just push rough code?”  Because brittle RF tools create unsafe expectations in the field.
      • “Will this be open source?”       Yes—public by default, with clear redlines for sensitive bits.
      • “Is there a way to support?”      Yes—issues, PRs, introductions, and (soon) sponsor links.

    — End of statement —
    """)

def readme():
    return dedent(f"""\
    # {PROJECT}

    **Status:** {VERSION} — public planning & collaborator intake.  
    **Date:** {TODAY}

    {statement().split("# What this is")[0].strip()}

    ## What this is
    {dedent("""ATAKRR is a modular RF situational-awareness stack for ATAK. It targets low-signature collection (PEWPEW),
    safe retrieval (BAMMO), on-edge triage (FoG), practical AMC/ML, and an ATAK plugin for operators.""")}

    ## Current reality (pre-alpha)
    See the “Why you’re seeing this now” section in the project statement above.

    ## Roadmap
    {dedent("""M0✓, M1–M6 as detailed in the statement. We will cut public releases at each milestone with tagged artifacts and changelogs.""")}

    ## Contributing
    We welcome issues and small PRs that improve docs, reproducibility, or add tests. For code contributions,
    please read `CONTRIBUTING.md`.

    ## Funding & Compensation
    Collaborators convert to **paid** roles upon grant/contract award. We keep an interest list and match skills to funded work packages.

    ## Security, Safety, and Ethics
    We ship demo data that is either synthetic or consented. We do not publish sensitive collections or target identification recipes.

    ## License
    To be finalized per-module (MIT/BSD/Apache-2.0 favored). See headers as code lands.

    ## Contact
    Open an issue or reach the maintainer via the address in repository settings.

    ---
    _This README was scaffolded by `atakrr_status.py` on {TODAY}._
    """)

def contributing():
    return dedent(f"""\
    {ASCII}
    # Contributing to {PROJECT}

    Thanks for your interest! This project is **pre-alpha** and evolving quickly. The safest way to help right now:

    1. File an issue describing your background and what you’d like to tackle.
    2. Start small: docs, test fixtures, eval harness improvements.
    3. Respect the security/ethics notes in README.
    4. Want there to be more here than just this sorry excuse for code?  Then contribute!  Even having competent developers sign onto the project as being willing to work (yes, for money!) makes a huge difference in our ability - *my* ability - to do dozens of hours of completely unpaid work getting grants to fund this!

    ## Development Principles
    - Reproducible: every figure and metric must be one command away.
    - Portable: Linux-first; no vendor lock-in without a fallback path.
    - Field-aware: prefer reliability over cleverness; document failure modes.

    ## Code Style
    - Python: Ruff/Black/mypy; type-annotate public functions.
    - Android: Kotlin + Jetpack; strict lint.
    - C/C++: clang-format; -Wall -Wextra; sanitized CI builds.

    ## Commit & DCO
    Use conventional commits. Sign off (`-s`) to agree with the Developer Certificate of Origin.

    ## Security
    - Never push real locations or sensitive captures.
    - Redact MACs/IMEIs/SSIDs or synthesize them.

    ## Contributor Path
    We keep an interest list matched to funded tasks. When funds land, we convert active contributors to paid roles.
    
    ## CONTACT
    atakrr@ethertech.org / ProfPotatoes (discord) / @itfitz (telegram) / phone (contact me)
    """)

def code_of_conduct():
    return dedent("""\
    # Code of Conduct

    We are committed to a respectful, inclusive project.
    - Be kind. No harassment, hate speech, or discrimination.
    - Assume good intent; prefer curiosity over conflict.
    - Moderators may warn, restrict, or remove violators.

    Report issues to the maintainer email listed in the repository.
    """)

def write_files():
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme())
    with open("CONTRIBUTING.md", "w", encoding="utf-8") as f:
        f.write(contributing())
    with open("CODE_OF_CONDUCT.md", "w", encoding="utf-8") as f:
        f.write(code_of_conduct())
    print("Wrote README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--print",
        nargs="?",
        const="statement",
        choices=["statement", "readme", "contributing", "code", "all"],
        help="print a section (default: statement)",
    )
    ap.add_argument("--write", action="store_true", help="write repo scaffolding files")
    args = ap.parse_args()

    # Only run if --print or --write was specified
    if not args.print and not args.write:
        ap.print_help()
        return

    # Handle printing
    if args.print:
        if args.print == "statement":
            print(statement())
        elif args.print == "readme":
            print(readme())
        elif args.print == "contributing":
            print(contributing())
        elif args.print == "code":
            print(code_of_conduct())
        elif args.print == "all":
            print(statement())
            print(readme())
            print(contributing())
            print(code_of_conduct())
        return

    # Handle writing files
    if args.write:
        write_files()
        return


if __name__ == "__main__":
    main()
