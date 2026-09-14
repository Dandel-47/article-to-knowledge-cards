---
name: "make-knowledge-cards"
description: "Converts articles or Markdown/TXT files into 5-8 knowledge cards with title, core knowledge, explanation, and self-test. Invoke when user wants study cards from an article."
---

# Make Knowledge Cards

Turn an article into a concise set of knowledge cards for review and self-testing.

## Supported Inputs

- **Pasted text**: The user pastes article content directly in the chat.
- **Local Markdown files (`.md`)**: The user provides a file path.
- **Local text files (`.txt`)**: The user provides a file path.

## Not Supported

- Web scraping (do not fetch URLs).
- PDF files.
- Anki export.
- Graphical interfaces.

## How to Process Input

1. **Read the content.** If the user provides a file path, read the file with the Read tool. If the user pastes text, use that text directly.
2. **Understand the article.** Identify the topic, the main arguments, and the key facts or concepts the author presents.
3. **Select knowledge points.** Choose 5 to 8 points that are genuinely important to understanding the article. See the selection rules below.
4. **Generate cards.** Write one card per knowledge point using the card format below.
5. **Output the cards.** Present all cards in a single response using Markdown.

## Output Language

Always output cards in the same language as the source article. If the article is in Chinese, the cards should be in Chinese. If the article is in English, the cards should be in English. Do not translate unless the user explicitly asks.

## Knowledge Point Selection Rules

- **Importance first.** Pick the points that matter most for understanding the article's core message. Skip filler, transitions, and minor details.
- **One point per card.** If a point has two distinct ideas, split it into two cards. If two points overlap heavily, merge them into one.
- **No duplication.** After drafting all cards, review them. If two cards repeat the same idea from different angles, keep only the clearer one.
- **No fabrication.** Every piece of information on a card must come from the source text. Do not add background knowledge, external examples, or inferred conclusions that the article does not state or directly support.
- **No padding.** If the article only supports 3 or 4 meaningful cards, output 3 or 4 cards. Do not inflate the count by splitting trivial points or restating the same idea with different wording.
- **Target range.** Aim for 5 to 8 cards. Fewer is acceptable when the source material is thin. More than 8 means you are probably including low-value points.

## Card Format

Each card uses this structure:

```
---

## Card N: <Title>

**Core Knowledge:**
<One or two sentences stating the key fact, concept, or argument.>

**Explanation:**
<Two to four sentences explaining the idea in plain language. Expand on why it matters or how it fits into the article's argument.>

**Example / Self-test:**
<Choose EXACTLY ONE of the following — do not include both:>
- If the article includes a concrete example, restate it briefly here.
- If the article has no example, write a self-test question whose answer is the core knowledge above. The question should test understanding (why/how), not just recall (what). Format it as "Q: <question>"
```

### Field Guidelines

| Field | Length | Rules |
|---|---|---|
| Title | 3-15 words | Concise, descriptive, reflects the single knowledge point. |
| Core Knowledge | 1-2 sentences | The essential fact or claim. Must be traceable to the source text. |
| Explanation | 2-4 sentences | Clarify the core knowledge. Use the article's own logic, not external knowledge. |
| Example / Self-test | 1-3 sentences | Prefer the article's example. If none exists, write a self-test question. |

## Output Template

After generating all cards, present them in this format:

```
# Knowledge Cards: <Article Title or Topic>

> Source: <filename, "pasted text", or short description>
> Cards: <actual number> / 5-8 target

---

## Card 1: <Title>

**Core Knowledge:**
...

**Explanation:**
...

**Example / Self-test:**
...

---

## Card 2: <Title>

...

---

(continue for all cards)
```

## Edge Cases

- **Very short article** (under 200 words): Generate as many cards as the content supports (may be fewer than 5). Add a note: "Source article is brief; generated N cards based on available content."
- **Very long article** (over 3000 words): Focus on the article's thesis and main supporting points. Do not try to cover every section.
- **Article with no clear structure** (stream-of-consciousness, informal): Identify the key messages the author is conveying, even if they are not explicitly headed.
- **Article is mostly code or data**: Extract the conceptual knowledge around the code, not the code syntax itself.
- **Article in any language**: Process in the article's original language. Output cards in the same language as the article (see Output Language above).

## Quality Checklist

Before outputting, verify each card:

- [ ] The title is concise and specific (3-15 words).
- [ ] The core knowledge is traceable to the source text.
- [ ] The explanation adds clarity without introducing outside information.
- [ ] The "Example / Self-test" field contains exactly one item: either the article's example or a self-test question (not both).
- [ ] The self-test question tests understanding (why/how), not just recall (what).
- [ ] No two cards cover the same idea.
- [ ] The total card count is between 3 and 8 (5-8 is the target; fewer only when the source is thin).
- [ ] All cards are in the same language as the source article.
