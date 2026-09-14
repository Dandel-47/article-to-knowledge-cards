# make-knowledge-cards

A skill that converts articles into concise knowledge cards for study and self-testing. Paste an article or provide a local Markdown/TXT file, and get 5-8 cards — each covering one key idea with a title, core knowledge, explanation, and an example or self-test question.

## Features

- Extracts genuinely important knowledge points from articles
- One knowledge point per card — no duplication, no padding
- Each card includes a self-test question or the article's own example
- Outputs in the same language as the source article
- Does not fabricate information — everything is traceable to the source

## Limitations

- No web scraping (cannot fetch URLs)
- No PDF support
- No Anki export
- No graphical interface

## Installation

This is a TRAE Skill — a rule module that tells TRAE's AI how to convert articles into knowledge cards. It runs inside TRAE, not as a standalone app.

### Step 1: Download the project

**Option A: Clone via Git**

```bash
git clone https://github.com/Dandel-47/article-to-knowledge-cards.git
```

**Option B: Download ZIP**

Go to https://github.com/Dandel-47/article-to-knowledge-cards, click the green "Code" button, then "Download ZIP". Extract it.

### Step 2: Copy the skill to TRAE's skills directory

Find your TRAE skills directory:

| OS | Path |
|---|---|
| Windows | `C:\Users\<your-username>\.trae-cn\skills\` |
| macOS | `~/.trae-cn/skills/` |
| Linux | `~/.trae-cn/skills/` |

If the `skills` folder does not exist, create it manually.

Then copy the `make-knowledge-cards` folder into it:

```
# Example (Windows PowerShell)
Copy-Item -Path ".\skills\make-knowledge-cards" -Destination "C:\Users\<your-username>\.trae-cn\skills\" -Recurse

# Example (macOS / Linux)
cp -r ./skills/make-knowledge-cards ~/.trae-cn/skills/
```

The final structure should look like:

```
~/.trae-cn/skills/
└── make-knowledge-cards/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

### Step 3: Verify installation

Open TRAE, start a new conversation, and try:

> Use make-knowledge-cards to turn the following article into knowledge cards: [paste your article here]

If TRAE recognizes the skill, it will generate 5-8 knowledge cards following the format defined in SKILL.md.

### Optional: Keep the validation script

The `quick_validate.py` script checks the skill structure. You can keep it anywhere on your computer:

```bash
python quick_validate.py
```

## Usage

### Input Methods

1. **Paste text** — paste the article content directly.
2. **Local file** — provide a `.md` or `.txt` file path.

### Example Input (pasted text)

```
Recursion is a programming technique where a function calls itself to solve a problem
by breaking it down into smaller, similar sub-problems. Every recursive function must
have a base case that stops the recursion, and a recursive case that calls itself with
modified input moving closer to the base case...
```

### Example Output

```
# Knowledge Cards: Understanding Recursion

> Source: pasted text
> Cards: 2 / 5-8 target

---

## Card 1: What Is Recursion

**Core Knowledge:**
Recursion is a programming technique where a function calls itself to solve a problem
by breaking it down into smaller, similar sub-problems.

**Explanation:**
Instead of solving a large problem directly, recursion divides it into smaller versions
of the same problem. Each recursive call works on a simpler input, building up the final
solution from the results of these smaller calls.

**Example / Self-test:**
Q: What makes recursion different from simply calling another function?

---

## Card 2: Base Case and Recursive Case

**Core Knowledge:**
Every recursive function needs a base case (which stops the recursion) and a recursive
case (which calls itself with modified input moving toward the base case).

**Explanation:**
The base case is the termination condition — without it, the function recurses forever
and causes a stack overflow. The recursive case must alter the input so that each call
gets closer to the base case.

**Example / Self-test:**
Q: What happens if a recursive function has no base case?
```

## Validation

Run the validation script to check the skill structure:

```bash
python quick_validate.py
```

Expected output:

```
[OK]   Skill directory: .../skills/make-knowledge-cards
[OK]   SKILL.md: frontmatter valid, required sections present
[OK]   agents/openai.yaml: interface block valid, required fields present
[OK]   No unnecessary files in skill directory
Result: PASSED
```

## Project Structure

```
make-knowledge-cards/
├── skills/
│   └── make-knowledge-cards/
│       ├── SKILL.md              # Skill instructions
│       └── agents/
│           └── openai.yaml       # Agent interface definition
├── tests/                        # Test articles and sample outputs
│   ├── test_technical.md
│   ├── test_narrative.txt
│   ├── test_short.md
│   ├── output_technical.md
│   ├── output_narrative.md
│   └── output_short.md
├── quick_validate.py             # Validation script
└── README.md
```
