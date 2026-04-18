# Codex Prompt Schema Cheat Sheet

## One-Page Reference for Interactive E-Learning Content

Use this card when you want to write a strong build prompt for Codex without reopening the full tutorial.

The rule is simple:

Use the same headings in your planning notes and in your actual prompt.

If your concept framing says `Learning goal`, `Audience`, and `Core interactions`, your prompt should use those same labels.

---

## The Non-Negotiable Components

Always include:

1. `Learning goal:`
2. `Audience:`
3. `Content type:`
4. `Core interactions:`
5. `Feedback or assessment behavior:`
6. `Content or data source:`
7. `Tracking and persistence requirements:`
8. `Deployment target:`
9. `Technical constraints:`
10. `For the first version:`

If one of these is omitted, Codex will make assumptions. That is often where instructional mismatch begins.

---

## Reusable Master Prompt

```text
Create an interactive e-learning object.

Learning goal:
[what the learner should understand, practice, or decide]

Audience:
[who the learner is]

Content type:
[explainer / quiz / branching scenario / simulation / mini-game / data visualization]

Core interactions:
- [interaction 1]
- [interaction 2]
- [interaction 3]

Feedback or assessment behavior:
- [feedback rule 1]
- [feedback rule 2]

Content or data source:
- [existing authored content / mock content / dataset / scenario script / generated placeholder]

Tracking and persistence requirements:
- [what should be tracked]
- [what should be restorable]

Deployment target:
[SCORM / web / both]

Technical constraints:
- [single HTML or multi-file]
- [library restrictions with versions]
- [runtime restrictions]
- [design or device constraints]

For the first version:
- prioritize working structure over polish
- use mock content or mock data if necessary
- keep the code easy to revise
```

---

## Quick Reminders

### For SCORM

- Default to `SCORM 1.2` unless you intentionally need SCORM 2004
- Put `imsmanifest.xml` at the package root
- State what should resume on re-entry
- If you mention `scormdriver.js`, provide the actual file or inline code

### For Web Delivery

- Keep the SCORM version separate from the web version
- Use `localStorage` or another explicit persistence method if needed
- Platforms like Google Classroom usually work better as hosted web-link destinations than as SCORM targets

### For Libraries

- Always pin versions on purpose
- Example: `Three.js r128`
- Do not say only "use D3" or "use Three.js"

### For LMS Testing

- Treat local Moodle as a practical first sandbox
- Do not assume Moodle behavior automatically equals Canvas or Blackboard behavior
- Validate more broadly if cross-platform compatibility matters

---

## Strong Revision Prompt Pattern

```text
Please revise the activity.

Change:
- [what should change]

Preserve:
- [what should remain stable]

Reason:
- [why this revision matters instructionally or technically]
```

This is one of the safest ways to reduce regression during iteration.
