# Detailed Codex Collaboration Tutorial

## Building a Three.js PISA Globe as Both a SCORM Package and a Web App

This document is a detailed English tutorial for working with Codex to build an interactive learning visualization from concept to delivery.

It is based on a real workflow that produced:

- a Three.js PISA globe visualization
- a SCORM-ready package for Moodle
- click tracking and state persistence
- a lighter, web-deployment version as a single HTML file
- multiple rounds of layout, tone, data, and interaction refinement

The goal of this tutorial is not only to explain what to ask Codex to do, but also how to collaborate effectively so the process stays structured, iterative, and easy to debug.

---

## 1. What This Tutorial Covers

This guide shows you how to:

- define the project clearly before asking for code
- write better prompts for Codex
- break work into manageable stages
- review interactive output in the browser
- give useful visual and technical feedback
- convert a visualization into a SCORM package
- test the package in Moodle
- fork the SCORM version into a separate web version
- keep versions organized instead of overwriting everything
- build a repeatable workflow you can reuse for future projects

This tutorial is especially useful if you are building:

- interactive educational visualizations
- learning-engineering prototypes
- SCORM-based demos or experiments
- single-file HTML learning apps
- data-rich visual stories with Three.js

---

## 2. The Core Collaboration Principle

The most important rule is simple:

Do not try to write one perfect mega-prompt.

Instead, work in stages:

1. Define the idea
2. Build a working draft
3. Review it in the browser
4. Give specific feedback
5. Refine layout and interaction
6. Add packaging and tracking
7. Test in the target environment
8. Split deliverables for different deployment needs

In practice, Codex works best when you use it like a technical collaborator, not like a one-shot image generator.

That means:

- ask for one meaningful step at a time
- verify results before moving on
- describe concrete issues, not vague impressions
- preserve stable versions instead of rewriting the same file forever

---

## 3. Project Outcome We Are Using as the Example

This tutorial uses the PISA globe project as the reference case.

The project goal was:

- build an interactive 3D globe visualization in Three.js
- show top-performing PISA systems by country
- visualize country locations, comparative scores, and similarity links
- support multiple PISA cycles over time
- create a SCORM-compatible version for LMS testing
- preserve click tracking and state
- also create a non-SCORM single-HTML web version

Current workspace artifacts from this project include:

- Moodle install directory:
  `C:\Users\jewoo\Documents\Playground\moodle-install`
- SCORM package folder:
  `C:\Users\jewoo\Documents\Playground\moodle-install\packages\pisa-globe-scorm`
- SCORM zip:
  `C:\Users\jewoo\Documents\Playground\moodle-install\packages\pisa-globe-scorm.zip`
- Web app folder:
  `C:\Users\jewoo\Documents\Playground\moodle-install\packages\pisa-globe-web`
- Single HTML web file:
  `C:\Users\jewoo\Documents\Playground\moodle-install\packages\pisa-globe-web.html`

You can adapt the same workflow to other topics such as:

- world logistics networks
- global AI company ecosystems
- K-pop diffusion maps
- educational achievement comparisons
- climate, trade, migration, or policy visualizations

---

## 4. Before You Start: Decide What Kind of Deliverable You Need

Before you ask Codex to build anything, decide what kind of final artifact you want.

### Option A: Pure Web App

Choose this if you want:

- a link you can share
- a single HTML prototype
- hosting on GitHub Pages, Netlify, or Vercel
- browser-based presentation or demo use

### Option B: SCORM Package

Choose this if you want:

- upload into Moodle or another LMS
- package-level LMS testing
- completion and score tracking
- state persistence inside SCORM runtime constraints

### Option C: Both

This is often the best choice.

Why?

- the SCORM version is for LMS integration and testing
- the web version is for easier sharing, showcasing, and iteration
- maintaining both helps you separate runtime packaging problems from visualization problems

For the PISA globe project, the correct answer was "both."

---

## 5. How to Structure Your First Prompt

Your first prompt should establish five things:

1. Topic
2. Data structure
3. Interaction goals
4. Visual direction
5. Technical constraints

Do not start with micro-details unless those details are essential.

### Good First Prompt Pattern

```text
Create an interactive 3D globe visualization in Three.js.

Topic:
OECD PISA top-performing countries and their learning performance profiles.

Goals:
- Plot the top countries on a globe
- Show reading, mathematics, science, and composite performance
- Visualize similarity links between countries rather than real trade or policy flows
- Make it feel presentation-ready and visually polished

Data:
- Use mock data if necessary
- Include country, ISO code, capital city, latitude, longitude, year, reading, mathematics, science, composite score, OECD gap, and region

Interactions:
- Rotate by drag
- Zoom by mouse wheel
- Hover for tooltip
- Click for detail modal
- Include a left list panel, right control panel, and bottom timeline

Technical constraints:
- Three.js r128
- No OrbitControls
- Manual pointer-based rotation
- Single HTML file
- Only use CDN libraries from cdnjs, jsdelivr, or unpkg

For the first version, prioritize a working structure over polish.
```

### Why This Works

This prompt gives Codex enough structure to produce something meaningful without forcing every implementation detail too early.

It also leaves room for iteration, which is where most quality improvements actually happen.

---

## 6. What Not to Do in the First Prompt

Avoid these common mistakes.

### Mistake 1: Asking for Everything at Once

Bad example:

```text
Make a perfect educational globe with SCORM, xAPI, moodboard-level design, multiple years, perfect labels, amazing animation, Google Classroom compatibility, and deployment-ready hosting.
```

Why it fails:

- too many layers at once
- no priority order
- harder to debug when something breaks
- you cannot tell whether the problem is visual, technical, or packaging-related

### Mistake 2: Being Too Vague

Bad example:

```text
Make a nice globe. Something feels academic but also cool.
```

Why it fails:

- Codex has no clear success criteria
- "nice" is not technically actionable
- you will likely get something generic

### Mistake 3: Mixing Review and Implementation

Bad example:

```text
Can you think through the concept, compare frameworks, write the app, test it, and explain research implications in one response?
```

Why it fails:

- multiple incompatible tasks in one turn
- unclear whether you want analysis or implementation first

---

## 7. The Recommended Collaboration Sequence

Here is the best overall process for a project like this.

### Phase 1: Build the First Working Visualization

Ask Codex to create:

- the first HTML prototype
- mock data
- basic interactions
- a visible layout structure

At this phase, you should not worry about:

- exact glow intensity
- final typography
- perfect country placement
- SCORM packaging
- deployment strategy

Your only goal is to get something working in the browser.

### Phase 2: Review the Visualization Visually

Open the output in the browser and inspect:

- whether the globe is centered properly
- whether panels block too much of the stage
- whether the title is too large
- whether the interaction model feels usable
- whether the brightness and contrast feel right
- whether nodes and lines are legible

### Phase 3: Give Specific Feedback

This is where collaboration quality really matters.

Good feedback examples:

```text
The title is too large and covers too much of the globe.
The left and right panels are eating too much horizontal space.
The connection lines still feel too glowy.
The Earth texture is too dark.
Country locations look off relative to the texture orientation.
```

Bad feedback examples:

```text
Something is weird.
I do not love it.
Still not right.
```

Codex responds much better to specific layout and rendering issues than to general taste reactions.

### Phase 4: Refine Visual and Interaction Layers

Typical refinement requests include:

- English UI instead of Korean
- brighter Earth texture
- reduced halo intensity
- thinner links
- corrected latitude/longitude mapping
- less intrusive overlay layout
- collapsible title block

### Phase 5: Expand Data and Time Support

Once the structure is stable, ask for:

- multiple years
- historical snapshots
- a cleaner timeline model
- derived metrics such as region, composite score, strongest domain, weakest domain

### Phase 6: Convert to SCORM

Only after the visualization works well as a standalone interactive should you ask Codex to create the SCORM version.

At this stage, request:

- `imsmanifest.xml`
- `index.html`
- `scormdriver.js`
- click tracking
- state persistence
- score handling if needed

### Phase 7: Test in Moodle

Upload the SCORM zip into Moodle and inspect:

- package import success
- launch behavior
- content rendering
- interaction persistence
- resume behavior
- whether SCORM status and score update properly

### Phase 8: Fork a Separate Web Version

Once the SCORM version is stable, ask Codex to create a separate web version rather than stripping SCORM out of the same file in place.

This is critical.

Do not overwrite the SCORM version if you still want LMS testing.

Instead:

- keep the SCORM package intact
- duplicate the visualization into a web version
- replace SCORM persistence with `localStorage` or another browser-side mechanism

---

## 8. The Exact Kinds of Prompts You Will Use

Below are the main prompt types that cover most of the workflow.

## 8.1 Base Visualization Prompt

Use this to generate the initial prototype.

```text
Create an interactive 3D globe visualization in Three.js.

Topic:
Top-performing OECD PISA countries.

Goals:
- Plot countries on a globe
- Show reading, mathematics, science, and composite performance
- Use similarity links between countries rather than real-world trade or policy relationships
- Make the experience suitable for a presentation-quality educational visualization

Data:
- Include mock top-country data if needed
- Use country, ISO code, capital city, latitude, longitude, year, reading, mathematics, science, composite score, OECD gap, and region

Interface:
- Left panel with country list
- Right panel with controls
- Bottom timeline
- Hover tooltip
- Click modal

Technical constraints:
- Three.js r128
- Manual pointer-driven rotation
- No OrbitControls
- Single HTML file
- Only CDN libraries from cdnjs, jsdelivr, or unpkg

For the first version, focus on functionality and structure first.
```

## 8.2 SCORM Packaging Prompt

Use this only after the visualization works.

```text
Convert this visualization into a SCORM 1.2 package.

Requirements:
- single SCO
- include imsmanifest.xml at the package root
- keep the visualization launch file as index.html
- add a lightweight scormdriver.js wrapper

Track at least:
- total click count
- country click count
- control panel changes
- timeline changes
- selected country
- current year

Persistence requirements:
- store interaction state in suspend_data
- restore state on re-entry
- keep the package Moodle-compatible

Output:
- imsmanifest.xml
- index.html
- scormdriver.js
- final zip package
```

## 8.3 UI Language Change Prompt

```text
Change the interface language from Korean to English.
Update titles, labels, button text, panel copy, and modal labels.
Keep the data model unchanged.
Do not alter the interaction structure unless necessary.
```

## 8.4 Tone and Glow Reduction Prompt

```text
The visualization still feels too dark and too glowy.

Please:
- switch to a brighter Earth texture
- reduce atmosphere intensity
- reduce node halo intensity
- reduce pulse brightness
- make connection lines more restrained and less luminous

The result should feel cleaner and more editorial, not ambient or cinematic.
```

## 8.5 Layout Repair Prompt

```text
The layout does not feel balanced.

Please redesign the HUD layout so the globe remains the visual center.
I want:
- a left rail for the country list
- a center stage for the globe
- a right rail for controls
- a bottom dock for the timeline

Avoid overlapping panels floating across the center.
Preserve the existing functionality.
```

## 8.6 Country Location Correction Prompt

```text
Country locations look wrong relative to the Earth texture.

Please review the latitude/longitude to sphere conversion and correct the mapping so markers align properly with the texture orientation.
Keep the same data values, but fix the projection math and any texture offset assumptions.
```

## 8.7 Multi-Year Data Expansion Prompt

```text
Expand the dataset to support multiple PISA cycles.

Please include:
- 2009
- 2012
- 2015
- 2018
- 2022

If complete historical data is not available, use deterministic mock historical series derived from the current dataset structure.
Update the timeline and modal so year-based changes are visible.
```

## 8.8 Collapsible Title Prompt

```text
The title block is too large and takes over the composition.

Make the title area collapsible.
It should:
- start collapsed by default
- use a smaller compact state
- allow expansion on demand
- preserve the state when the user returns
```

## 8.9 Web Version Fork Prompt

```text
Create a separate web deployment version.

Important:
- do not delete or overwrite the SCORM version
- create a separate single-HTML web version
- replace SCORM persistence with localStorage
- preserve click tracking, selected country, selected year, and UI state
- keep the visual design consistent with the SCORM version
```

---

## 9. How to Review the Output Properly

When Codex finishes a stage, do not immediately ask for another feature.

First review what already exists.

### Review Checklist for Visual Output

Ask yourself:

- Is the globe still the main focal point?
- Do the side panels support the visualization or overpower it?
- Is the title too dominant?
- Are the labels readable?
- Are the lines too thick?
- Is the glow distracting?
- Is the Earth texture helping or hurting the clarity?
- Is the timeline understandable?
- Does the modal feel useful or overloaded?

### Review Checklist for Interaction

- Can I rotate easily?
- Can I zoom without losing orientation?
- Does hover feel responsive?
- Does click selection feel clear?
- Do filters make sense?
- Does the timeline update the view clearly?
- Is the control panel understandable?

### Review Checklist for Educational Clarity

- Is the data meaning obvious?
- Is it clear that links show similarity, not real flows?
- Can a viewer understand the narrative without reading code?
- Does the interface reflect the educational purpose rather than just technical spectacle?

---

## 10. How to Give Better Feedback to Codex

The difference between slow iteration and fast iteration is usually feedback quality.

### Best Practice: Separate Feedback into Categories

Use grouped feedback such as:

#### Layout

- The title is too big.
- The side panels are too wide.
- The timeline should feel docked instead of floating.

#### Tone

- The scene is too dark.
- The glow reads as too ambient.
- The links should feel calmer and less luminous.

#### Data

- Add more historical years.
- Show a trend strip in the modal.
- Include more metadata for each country.

#### Runtime

- Preserve title collapse state.
- Track more interactions in SCORM.
- Keep the web version separate from the SCORM version.

This structure makes your request easier to execute accurately.

### Best Practice: Explain the Why

Instead of only saying what is wrong, explain why.

Example:

```text
The title is too large because it competes with the globe instead of framing it.
The lines are too bright because they pull attention away from the country markers.
The side panels are too intrusive because they reduce the stage width too much.
```

That gives Codex a design rationale, not just an instruction.

---

## 11. When to Ask for SCORM and When Not To

SCORM should not be your first step.

Ask for SCORM only after:

- the core visualization works
- the layout is reasonably stable
- the data model is settled enough
- the interactions behave as expected

Why?

- SCORM adds packaging complexity
- SCORM introduces state management constraints
- SCORM makes iteration slower if you are still changing the core structure

So the recommended order is:

1. Build the interactive
2. Refine the interactive
3. Package the interactive for SCORM
4. Test it in Moodle
5. Then make a separate web version if needed

---

## 12. How SCORM Fits Into This Workflow

For a project like this, SCORM is not the visualization engine.

SCORM is the wrapper.

That means:

- Three.js still handles the visualization
- HTML/CSS/JS still handle the interface
- SCORM mainly handles packaging, launch, persistence, and tracking

So when you ask Codex to make something "SCORM-ready," you are usually asking for:

- the manifest
- the package structure
- runtime tracking hooks
- persistence logic
- LMS-safe packaging

This is a very different task from building the visualization itself.

Treat it that way.

---

## 13. Testing the SCORM Version in Moodle

Once the SCORM package exists, test it in Moodle carefully.

### Suggested Moodle Workflow

1. Create or open a test course
2. Add a new SCORM package activity
3. Upload the generated zip
4. Save and launch it
5. Interact with the visualization
6. Exit
7. Re-enter
8. Check whether the state is restored

### What to Observe

- Does the package import cleanly?
- Does it launch in the current window?
- Does the visualization render correctly?
- Are interactions still smooth inside Moodle?
- Does click tracking persist?
- Does selected country restore?
- Does the timeline restore?
- Does title collapse state restore?

### If Something Breaks

Ask Codex using a runtime-oriented prompt such as:

```text
The SCORM package uploads, but state restoration is not behaving correctly in Moodle.
Please review the suspend_data save and restore flow.
I need selected country, year, and UI state to persist reliably on re-entry.
Keep the rest of the visualization unchanged.
```

---

## 14. Why You Should Keep the SCORM and Web Versions Separate

This is one of the most important practical lessons.

Do not keep forcing one single file to serve every deployment context forever.

Why separate them?

### The SCORM Version Needs

- manifest packaging
- SCORM runtime hooks
- LMS persistence logic
- LMS-specific testing

### The Web Version Needs

- simpler deployment
- no LMS dependency
- browser-side persistence such as localStorage
- easier sharing via URL

If you keep rewriting one file back and forth, you create confusion.

Instead:

- freeze the SCORM branch when it works
- fork a web version
- keep them visually aligned but technically separate

That is exactly what was done in this project.

---

## 15. Recommended File Organization

Use a structure like this:

```text
moodle-install/
  codex-collaboration-tutorial-ko.md
  codex-collaboration-tutorial-en-detailed.md
  docker-compose.yml
  packages/
    pisa-globe-scorm/
      imsmanifest.xml
      index.html
      scormdriver.js
    pisa-globe-scorm.zip
    pisa-globe-web/
      index.html
    pisa-globe-web.html
```

Why this helps:

- tutorials stay near the project
- the SCORM source stays separate from the zipped package
- the web version has its own folder
- the single HTML version is easy to share quickly

---

## 16. How to Ask for Revisions Without Causing Chaos

When revising, tell Codex what to preserve.

This is one of the most useful prompt habits.

Example:

```text
Redesign the layout, but preserve:
- the data model
- the existing interactions
- the tooltip and modal behavior
- the current timeline logic

Only change the panel structure and spacing.
```

This prevents accidental regression.

Similarly:

```text
Reduce the visual glow, but do not change:
- the country coordinates
- the historical data model
- the click tracking logic
```

This tells Codex what is in scope and what is not.

---

## 17. How to Use the Browser During Collaboration

The browser is not optional for a project like this.

You need to look at the actual result.

The workflow should look like this:

1. Ask Codex to make a change
2. Open the result in the browser
3. Identify specific issues
4. Report those issues back
5. Repeat

This is especially important for:

- Three.js layout
- overlay spacing
- text scale
- tooltip behavior
- brightness and tone
- alignment between data points and texture

For interactive visual work, browser review is part of the build process, not an afterthought.

---

## 18. A Full Example End-to-End Prompt Sequence

Below is a realistic sequence you can follow from scratch.

### Step 1: Initial Build

```text
Create an interactive Three.js globe visualization for OECD PISA top-performing countries.
Use mock data for now.
I want country points, similarity links, a left country panel, a right control panel, and a bottom timeline.
Use a single HTML file and Three.js r128 with manual drag rotation.
Make the first version functional before trying to polish it.
```

### Step 2: First Visual Feedback

```text
The first version works, but I want a more refined data-journalism feel.
Please improve the composition, typography, and panel styling without changing the data logic.
```

### Step 3: Technical and Design Corrections

```text
The globe is too dark, the glow is too strong, and the country coordinates look off.
Please switch to a brighter Earth texture, tone down glow everywhere, and correct the lat/lng projection mapping.
Keep the same interaction structure.
```

### Step 4: Layout Rebuild

```text
The floating overlays do not feel balanced.
Please rebuild the layout using a left rail, center stage, right rail, and bottom timeline dock.
The globe should remain the dominant visual center.
```

### Step 5: Historical Expansion

```text
Add support for 2009, 2012, 2015, 2018, and 2022.
If needed, create deterministic mock historical series derived from the current dataset.
Update the modal and timeline accordingly.
```

### Step 6: Title Refinement

```text
The title block is too large.
Make it collapsible and start in the collapsed state by default.
Persist that state.
```

### Step 7: SCORM Conversion

```text
Now convert this into a SCORM 1.2 package.
Keep it as a single SCO.
Track click count, country selections, control changes, and timeline changes.
Persist state through suspend_data and make it Moodle-compatible.
```

### Step 8: Web Fork

```text
Create a separate web deployment version.
Do not overwrite the SCORM version.
Use localStorage instead of SCORM, but preserve the same interaction state and tracking behavior.
```

---

## 19. Troubleshooting Guide

Here are the most common issues and how to ask Codex to fix them.

### Problem: The markers are in the wrong place

Use:

```text
Please review the sphere projection math and texture alignment.
Country markers do not line up correctly with the Earth texture.
Fix the lat/lng to 3D conversion without changing the dataset itself.
```

### Problem: The scene feels too dark

Use:

```text
The scene feels too dark and muted.
Please brighten the Earth texture, lift the ambient feel, and reduce atmospheric heaviness.
I want clarity over drama.
```

### Problem: The links dominate too much

Use:

```text
The connection lines are too visually loud.
Make them thinner, dimmer, and less glowy.
They should support the country pattern, not overpower it.
```

### Problem: The layout covers the globe

Use:

```text
The overlays are taking too much space away from the globe.
Please rebalance the layout so the globe is clearly the focal center and the panels feel secondary.
```

### Problem: The SCORM version does not restore state

Use:

```text
The package loads, but state restoration is inconsistent on re-entry in Moodle.
Please review the suspend_data save and restore flow and make sure year, selected country, and UI state are preserved.
```

### Problem: I need a web version without losing the SCORM version

Use:

```text
Please fork the current SCORM visualization into a separate web version.
Do not overwrite the SCORM package.
Replace SCORM runtime persistence with localStorage while preserving the same user-facing behavior.
```

---

## 20. Quality Checklist Before You Consider It Done

Use this checklist before declaring the project finished.

### Visual Quality

- The globe feels like the main stage
- The title does not dominate the composition
- The side panels feel controlled and useful
- The Earth texture is readable
- The glow is restrained
- The links are legible but not distracting
- The typography is consistent

### Data Quality

- Country coordinates are correct
- The year model works
- Composite score is computed consistently
- Strongest and weakest domains make sense
- Similarity links are clearly explained as similarity, not causality

### Interaction Quality

- Drag rotation works smoothly
- Zoom works predictably
- Tooltip appears correctly
- Modal opens and closes correctly
- Country list filtering works
- Timeline switching works
- Title collapse works

### SCORM Quality

- Zip imports into Moodle
- The package launches correctly
- Interaction state persists
- Re-entry restores state
- Tracking values update as expected

### Web Version Quality

- The file works outside Moodle
- localStorage persists the expected state
- The web version does not depend on SCORM runtime
- The visual behavior matches the SCORM version closely

---

## 21. Suggested Collaboration Rules for Future Projects

If you want a reusable workflow, keep these rules.

### Rule 1

Always define the deployment target early.

### Rule 2

Build the visualization first, then package it.

### Rule 3

Use browser review after each major iteration.

### Rule 4

Give concrete, grouped feedback.

### Rule 5

Preserve stable versions instead of constantly overwriting the same artifact.

### Rule 6

Separate visual issues from packaging issues.

### Rule 7

When asking for revisions, say what should change and what should remain untouched.

---

## 22. A Reusable Master Prompt Template

You can reuse the following template for future projects.

```text
Create an interactive [visualization/app type] in [framework/library].

Topic:
[Describe the subject clearly]

Goals:
- [Goal 1]
- [Goal 2]
- [Goal 3]

Data requirements:
- [field 1]
- [field 2]
- [field 3]

Interactions:
- [interaction 1]
- [interaction 2]
- [interaction 3]

Visual direction:
- [tone]
- [layout preferences]
- [clarity vs spectacle preference]

Technical constraints:
- [library version]
- [single HTML or multi-file]
- [deployment target]
- [restricted CDNs or runtime constraints]

For the first version:
- prioritize a working structure
- use mock data if needed
- keep the code easy to modify
```

Then follow up with more focused prompts for:

- design refinement
- data expansion
- packaging
- version splitting
- deployment

---

## 23. Final Advice

The best way to collaborate with Codex on a project like this is to think like a director with a build loop.

You are not only asking for code.

You are doing:

- problem framing
- scope control
- visual review
- packaging decisions
- iterative refinement

The workflow becomes much easier once you stop expecting the first prompt to solve everything.

Instead, use Codex to:

- build the first stable version fast
- respond to concrete design and runtime feedback
- separate versions cleanly
- preserve momentum across iterations

That is the real collaboration model.

---

## 24. Recommended Next Documents You May Want to Create

After this tutorial, useful follow-up documents might include:

- a SCORM-only packaging checklist
- a Moodle testing checklist
- a web deployment guide for GitHub Pages or Netlify
- a prompt library for educational visualization projects
- a research-method memo on using sandboxed LMS testing for learning-engineering experiments

If you build more projects like this, those documents become very valuable.

---

## 25. Short Version of the Workflow

If you need the whole process in one compact block:

1. Define topic, data, interaction, and deployment target.
2. Ask Codex for a working first version.
3. Open it in the browser and inspect it visually.
4. Give specific feedback about layout, tone, data, and interaction.
5. Stabilize the visualization first.
6. Convert it into SCORM only after the interactive works.
7. Test it in Moodle.
8. Fork a separate web version instead of overwriting the SCORM build.
9. Keep iterating with concrete, structured prompts.

That is the full method.
