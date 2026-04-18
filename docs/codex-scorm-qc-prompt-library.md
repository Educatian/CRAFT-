# Codex SCORM QA Prompt Library

## Prompt Set for Building, Inspecting, and Verifying SCORM Packages

This file is a compact operational library for working with Codex when you need SCORM packaging help, Moodle-readiness checks, or runtime-state review.

It complements the longer tutorial and is meant to be copied into live Codex conversations.

---

## 1. First Build Prompt

```text
Create the first working version of this e-learning object.

Learning goal:
[goal]

Audience:
[audience]

Content type:
[type]

Core interactions:
- [interaction 1]
- [interaction 2]

Feedback or assessment behavior:
- [feedback rule]

Content or data source:
- [source]

Tracking and persistence requirements:
- [what should be tracked or restored]

Deployment target:
[web / SCORM / both]

Technical constraints:
- [constraints]

For the first version:
- prioritize a working instructional structure over polish
- use placeholder content if needed
- keep the code easy to revise
```

---

## 2. SCORM Zip Structure Audit Prompt

```text
Inspect this SCORM zip package and verify whether it is correctly structured for SCORM 1.2 and Moodle 4.3+ upload.

Please check:
- whether imsmanifest.xml exists at the package root
- whether the manifest declares SCORM 1.2 correctly
- whether the launch file referenced in the manifest actually exists
- whether required files are present inside the zip
- whether the package appears to be a single-SCO or multi-SCO structure
- whether the internal file paths match the manifest references
- whether there are obvious packaging mistakes that would break LMS import or launch

Do not rewrite the package yet.
First report:
1. findings
2. risks
3. exact files or manifest lines that look wrong
4. whether the package is likely Moodle-ready as-is
```

---

## 3. Manifest Review Prompt

```text
Review the imsmanifest.xml in this package.

I want you to verify:
- SCORM version assumptions
- schema and schemaversion entries
- organization and item structure
- resource declarations
- launch href correctness
- whether the manifest matches the actual files in the package

Please explain your findings in plain language, not only XML terms.
```

---

## 4. Resume and Runtime-State Audit Prompt

```text
Review this SCORM activity for resume and runtime-state readiness.

Please check:
- what learner state is currently saved
- whether suspend_data is actually used
- whether lesson_location is used meaningfully
- whether score and lesson_status are updated coherently
- whether exit is set in a sensible way
- whether the object is likely to restore the learner to the correct place on re-entry

Report:
1. what is currently tracked
2. what is missing
3. what is fragile
4. what should be fixed before LMS testing
```

---

## 5. Moodle Readiness Prompt

```text
I want a Moodle-readiness review for this SCORM package.

Assume Moodle 4.3+ as the target.

Please evaluate:
- import readiness
- launch readiness
- visibility of learner instructions inside the LMS frame
- likelihood of resume working
- score/completion readiness
- whether any setting assumptions should be called out for the Moodle activity configuration

Do not only say "it looks fine."
Give a practical launch-risk assessment.
```

---

## 6. Fix-After-Review Prompt

```text
Based on the issues you found in the SCORM review, please fix the package.

Important:
- preserve the current learner-facing interaction
- only change packaging, manifest, runtime-state handling, or missing-file issues
- keep the package as SCORM 1.2 unless you explain why a change is necessary

After fixing it, summarize:
1. what you changed
2. why those changes matter
3. what I should test first in Moodle
```

---

## 7. Web Fork Prompt

```text
Create a separate browser-deployable web version from this SCORM package.

Important:
- do not overwrite the SCORM version
- preserve the learner-facing interaction
- replace SCORM persistence with localStorage or another browser-side mechanism
- keep the code easy to compare against the SCORM version

Afterward, explain what changed at the runtime layer and what did not change at the interaction layer.
```

---

## 8. Maintainability Review Prompt

```text
Review this learning object from a maintainability perspective.

Please assess:
- file organization
- readability of the interaction logic
- ease of changing content later
- ease of changing scoring or branching later
- whether the structure is friendly to Git-based version control
- what would become painful if this object grows

Then suggest:
1. the biggest maintainability risk
2. the most useful refactor
3. how this workflow compares to a proprietary authoring-file workflow
```

---

## 9. Strong Conversation Pattern

Use this pattern when you want Codex to behave less like a generator and more like a reviewer.

```text
The activity works, but I need a stricter SCORM QA pass now.

Please inspect the package for:
- manifest correctness
- root-level zip structure
- launch-file consistency
- resume-state handling

Do not edit yet.
First report findings, risks, and what you would fix before Moodle upload.
```

This usually produces better results than asking only:

```text
Can you check if this is okay?
```
