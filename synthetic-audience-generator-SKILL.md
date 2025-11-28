---
name: synthetic-audience-generator
description: Generate realistic synthetic survey responses and audience data for testing surveys, validating question design, and simulating user research. Use when users need to test surveys before launch, generate sample data for analysis practice, stress-test question wording, identify survey design flaws, or create realistic respondent datasets. Triggers include phrases like "test my survey", "generate fake responses", "synthetic data", "simulate respondents", "practice data for analysis", or "validate my questionnaire".
---

# Synthetic Audience Generator

Generate realistic synthetic survey responses by first understanding context, then creating diverse personas, and finally producing clean output data.

## Workflow

### Phase 1: Gather Context (Required)

Before generating any data, collect the following information. Ask questions — do not assume.

**Required information:**

1. **Survey questions** — exact wording and answer options
2. **Target audience** — who is this survey for?
3. **Distribution context** — how/where will respondents encounter this survey?
4. **Sample size** — how many responses needed?

**Optional but valuable:**

5. **Hypotheses** — what does the user expect to find?
6. **Known segments** — any audience subgroups the user already identified?
7. **Drop-off context** — at what point do respondents see this survey?

Ask 2-3 questions at a time. Do not proceed until context is clear.

### Phase 2: Design Personas

Create 5-8 realistic persona types that would realistically encounter this survey. Each persona must include:

| Attribute | Description |
|---|---|
| Name pattern | Realistic first name + last initial |
| Role/context | Job title, situation, or demographic |
| Mental state | What they're thinking when they see the survey |
| Behavior pattern | How they typically respond (thorough, rushed, skeptical, etc.) |
| Likely answers | How this persona would answer each question |
| Why they're here | What brought them to this point |

**Required persona types to consider:**

- **Ideal respondent** — engaged, thoughtful, fits target audience perfectly
- **Skeptic** — distrustful, needs proof, questions everything
- **Rushed/lazy responder** — minimal effort, picks first options, skips optional fields
- **Wrong target** — ended up here but isn't the intended audience
- **Edge case** — legitimate user with unusual needs or use case
- **Comparison shopper** — evaluating options, not committed
- **Return/churned user** — has prior experience with product/service

Present personas to user for approval before generating data. Ask:
- "Do these personas match your expected audience?"
- "Any segments missing?"
- "Should I adjust the distribution?"

### Phase 3: Generate Responses

**Distribution guidelines:**

- Lazy/rushed responders: 15-25% (realistic survey noise)
- Wrong target: 5-15% (depends on distribution method)
- Ideal respondents: 20-35%
- Remaining personas: distribute based on context

**Realism rules:**

1. **Lazy responders** select first option for single-select questions
2. **Skeptics** leave skeptical comments or skip optional fields
3. **Wrong targets** select "Other" or leave confused comments
4. **Open-text responses** should vary in length, detail, punctuation, and grammar
5. **Some responses have typos** — realistic humans make mistakes
6. **Optional fields have 30-50% completion rate** unless highly motivated audience
7. **Time-of-day patterns** — if timestamp included, cluster around realistic times

**Comment realism checklist:**

- Vary sentence length (3-25 words)
- Include incomplete sentences
- Mix formal/informal tone
- Add occasional typos or missing punctuation
- Some comments are questions, not statements
- Some are single words or phrases

### Phase 4: Output Format

**Default CSV columns:**

```
response_id, respondent_name, [survey_question_columns], timestamp (optional)
```

**Critical: Do NOT include persona_type in final output.** The user should analyze data without knowing ground truth. Store persona mapping separately only if user explicitly requests it for later validation.

**If user requests persona labels:**
Create two files:
1. `survey_responses.csv` — clean data without labels
2. `persona_key.csv` — mapping of response_id to persona_type (for validation)

### Phase 5: Validation Summary

After generating data, provide:

1. **Distribution summary** — count by each answer option
2. **Potential issues revealed** — what survey design problems the simulation exposed
3. **Signal vs. noise estimate** — what % of data is likely actionable vs. polluted

## Anti-Patterns to Avoid

| Don't | Do instead |
|---|---|
| Generate data before understanding context | Ask clarifying questions first |
| Use identical comment styles | Vary length, tone, grammar, punctuation |
| Make all responses complete | Include realistic skip patterns |
| Assume audience segments | Ask user about expected respondents |
| Include persona labels in main output | Keep output clean, provide key separately |
| Generate perfectly distributed data | Add realistic noise and clustering |

## Example Clarifying Questions

**For survey context:**
- "What's the exact wording of each question and the answer options?"
- "Who is the target audience for this survey?"
- "At what point do respondents see this — checkout, post-purchase, cold outreach?"

**For personas:**
- "Do you have hypotheses about why different people might respond?"
- "Are there any segments you already know exist in your audience?"
- "What percentage of respondents do you expect to be wrong-fit or accidental?"

**For output:**
- "How many responses do you need?"
- "Do you want timestamps included?"
- "Should I provide a separate key mapping responses to persona types for validation?"
