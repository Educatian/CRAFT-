# CRAFT-

**CRAFT** stands for **Codex Runtime & Authoring Framework for Training**.

This repository contains a working draft of a tutorial and companion assets for building interactive e-learning content with AI-assisted coding workflows.

The project focuses on a practical question:

How do we move from prompting and iterative design to real courseware behavior, including SCORM packaging, LMS testing, and web deployment?

## What Is Included

### Documentation

The `docs/` folder contains:

- the main generic tutorial in Markdown
- a Word export of the tutorial
- a PDF draft version for sharing
- a Three.js-oriented companion tutorial
- a Korean version of the earlier tutorial
- a prompt schema cheat sheet
- a SCORM QA prompt library for Codex conversations

### Example Files

The `examples/minimal-scorm-quiz/` folder contains a minimal SCORM 1.2 quiz example with:

- `index.html`
- `scormdriver.js`
- `imsmanifest.xml`

This example is intended as a readable starter reference, not a full production framework.

### Scripts

The `scripts/` folder contains a reusable Python script for rendering the Markdown tutorial into a styled Word document.

### Media

The `media/` folder contains a demonstration video related to the draft workflow.

## Repository Structure

```text
CRAFT-/
  docs/
  examples/
    minimal-scorm-quiz/
  media/
  scripts/
  README.md
  .gitignore
```

## Main Framing

One of the core ideas behind this project is that comparing AI-assisted code workflows to authoring tools such as Articulate should not stop at visual similarity.

The sharper question is whether a code-authored workflow can reproduce the **invisible runtime work** that courseware depends on:

- packaging
- launch behavior
- score and completion logic
- resume state
- maintainability over time

## Intended Audience

This repository is especially relevant for:

- instructional designers
- learning engineers
- educational technologists
- technically curious educators
- students exploring AI-assisted courseware workflows

## Status

This repository contains a **draft version** of the tutorial and supporting materials.

It should be read as:

- a workflow guide
- a prompt and packaging reference
- a starting point for classroom projects or comparative studies

It should not yet be read as final empirical proof that one workflow universally replaces another.
