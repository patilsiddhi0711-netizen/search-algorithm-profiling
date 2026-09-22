## 🤝 Contribution & Collaboration Breakdown

This project was developed through a collaborative workflow between human implementation/execution and AI-assisted documentation, debugging, and repository structure optimization.

### 👤 Developer Contribution (Siddhi Patil)
* **Code Implementation & Execution:** Written pure Python implementations for Linear Search ($O(n)$) and Binary Search ($O(\log n)$) on datasets of $N = 1,000,000$ elements.
* **Profiling & Environment Execution:** Installed and configured `py-spy` locally, executed PowerShell terminal profiling commands, and generated interactive flamegraph SVG artifacts.
* **Version Control & GitHub Management:** Initialized local Git repository, configured `.gitignore` to strip CPython artifacts (`__pycache__`), committed codebase, and managed branch pushes to GitHub.
* **Empirical Data Verification:** Measured and verified real-time execution bounds ($\approx 157.85\text{ ms}$ for Linear Search; $\approx 4.41\text{ s}$ batch runtime for Binary Search) to satisfy profiling metrics (>0.1 ms execution threshold).

### 🤖 AI Contribution (Gemini)
* **Asymptotic & Empirical Analysis:** Drafted formal algorithm complexity breakdowns, theoretical time/space bounds, and comparative performance summaries.
* **Documentation Authoring:** Structured and formatted the comprehensive `README.md`, including table metrics, LaTeX mathematical notation, and step-by-step replication guides.
* **Troubleshooting & Git Workflow Guidance:** Provided real-time terminal error resolution (PowerShell pathing, Git line-ending warnings, and file placement inside root directory vs. subfolders).
* **Profiling Batch Strategy:** Advised on batch iteration parameters (500,000 loops) to ensure `py-spy` captured sufficient stack samples for fast logarithmic functions.

---

## 📝 Chronological Milestone Log

| Phase / Milestone | Date | Key Tasks | Primary Contributor | Artifact / Commit | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **01. Repo & Env Setup** | 2026-09-22 | Workspace init, `.gitignore` configuration | Siddhi Patil | `.gitignore` | Completed |
| **02. Core Algorithms** | 2026-09-22 | Implementation of $O(n)$ and $O(\log n)$ searches | Siddhi Patil | `linear_search.py`<br>`binary_search.py` | Completed |
| **03. Profiling Automation** | 2026-09-22 | Driver scripts with batching logic | Siddhi Patil & Gemini | `generate_linear_svg.py`<br>`generate_binary_svg.py` | Completed |
| **04. Flamegraph Generation** | 2026-09-22 | Terminal execution & stack sampling (100 Hz) | Siddhi Patil | `images/*_flamegraph.svg` | Completed |
| **05. README & Submission** | 2026-09-22 | Analytical documentation & GitHub sync | Siddhi Patil & Gemini | `README.md` | Completed |