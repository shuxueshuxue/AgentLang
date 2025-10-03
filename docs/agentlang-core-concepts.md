# AgentLang: Core Concepts and Innovations

## 1. Fundamental Insight: Text as Semantic Object

**The Gem:** Any text automatically has structure when accessed - the LLM extracts it on demand.

```python
# Novel is just a string, but has implicit structure
novel = "Pride and Prejudice by Jane Austen..."
characters = novel.characters  # LLM extracts character list
theme = novel.theme           # LLM extracts theme
plot_twist = novel.plot.twist # Nested extraction
```

**Why It Matters:** Unifies data and schema - no parsing, no predefinition, just natural access to information as if it was always structured.

## 2. Two-Layer Architecture: Surface Language vs Internal Language

**Surface Language (AgentLang - what humans write):**
- Pure semantic intention
- No type system needed
- Everything is text
- Rigorous control flow

**Internal Language (The actual execution target - C/Python/JS/etc):**
- Could be ANY language: Python, JavaScript, C, Rust, WASM
- Choice affects system characteristics:
  - **Python IR**: Easy regex, slow loops, good for prototyping
  - **JavaScript IR**: Fast JIT, async native, good for web
  - **C IR**: Maximum speed, memory control, good for production
  - **WASM IR**: Portable, sandboxed, good for distribution

```python
# Surface Language (always the same):
email.sender

# Internal Language Generation (varies by target):

# Python IR (Generation 10):
def extract_sender_v10(text):
    if len(text) > 5000: return llm_fallback(text)
    match = re.search(r'From: (.*?)\n', text)
    return match.group(1) if match else llm_fallback(text)

# C IR (Generation 50):
char* extract_sender_v50(const char* text) {
    if (strlen(text) > 5000) return llm_fallback(text);
    char* from = strstr(text, "From: ");
    if (!from) return llm_fallback(text);
    // ... fast native extraction
}

# JavaScript IR (Generation 50):
function extract_sender_v50(text) {
    if (text.length > 5000) return llm_fallback(text);
    const match = text.match(/From: (.*?)\n/);
    return match?.[1] ?? llm_fallback(text);
}
```

**Key Insight:** The same Surface Language program can evolve into different Internal Languages based on deployment needs. A development environment might use Python IR for flexibility, while production uses C IR for speed.

## 3. Conservative Evolution with Sanity Epsilon

**The Gem:** Even "perfect" patterns keep learning through probabilistic sampling.

```python
Pattern(guards=[A, B, C], sanity_epsilon=0.01)
if ALL guards pass AND random() > sanity_epsilon:
    use_native()
else:
    use_llm()  # Maintains learning
```

**Why It Matters:** Prevents overfitting while achieving near-native performance. The 0.01% sampling catches edge cases and prevents staleness.

## 4. LLM Anchors with Runtime Context Resolution

**The Gem:** Same code location, different behavior based on runtime data.

```python
def process(doc):
    return doc.total  # <- Single LLM anchor

# Runtime determines context from actual data:
# Invoice? -> sum_amounts_policy
# Game scores? -> max_score_policy
# Survey? -> count_responses_policy
```

**Key Innovation:** LLM anchors are static in code but dynamic in behavior. Context computed at runtime determines which policy script to use.

## 5. Ownership System for Neural Outputs

**The Gem:** Every LLM-generated value knows where it came from and how to regenerate itself.

```python
agent analyze(owned document):
    owned summary = document.summary  # Tracked extraction

    # Can trace lineage
    assert summary.owner == analyze
    assert summary.source == document
    assert summary.extraction == "summary"

    # Can refresh
    if stale(summary):
        summary = refresh(summary)  # Re-runs original
```

**Why It Matters:** Solves provenance, debugging, and cache invalidation for AI-generated content.

## 6. Cross-Program Learning (DNA Database)

**The Gem:** Patterns learned by one program immediately benefit all programs.

```python
# Program A learns email.sender pattern
# Program B immediately uses it without training

Global DNA Database:
  "email.sender" -> regex_v47
  "invoice.total" -> sum_algorithm_v23
  "code.complexity" -> cyclomatic_v3
```

## 7. Minimal Language Primitives

**The Gem:** Only 5 core primitives create the entire language.

```python
agent    # LLM-backed function
run      # Execute LLM call
par      # Parallel execution
assert   # Validation with retry
>        # Pipeline operator
```

Everything else emerges from these primitives - no magic keywords, just composable operations.

## 8. Lazy Structural Inference with Schema from Usage

**The Original Vision:** The structure you access defines the schema.

```python
result = agent.run("Extract user details")
name = result.name      # These accesses define
age = result.age        # the expected schema
# Compiler infers: {name: str, age: int}
```

**The Challenge:** Breaks with complex control flow.
**The Solution:** Runtime context makes it work - schema inferred at each anchor point.

## 9. Self-Optimizing Runtime

**The Gem:** Programs literally get faster each time they run.

```python
# Day 1: analyze(text) takes 5 seconds (pure LLM)
# Day 30: takes 0.5 seconds (hybrid)
# Day 100: takes 0.01 seconds (native with LLM creativity layer)
# WITHOUT changing source code
```

## 10. Policy Scripts as Evolved Behaviors

**The Gem:** LLM behaviors crystallize into compiled functions.

```python
# Evolution creates policy scripts
policy_script: extract_email_sender_v47 {
    guards: [has_email_headers, length < 5000]
    implementation: compiled_wasm
    confidence: 0.99
    sanity_epsilon: 0.01
}
```

---

## The Core Philosophy

**AgentLang is a rigorous programming language where:**
1. Text and structure are unified
2. Programs evolve from neural to symbolic
3. Every value has traceable ownership
4. Patterns are shared across all programs
5. The runtime gets smarter with use

**It's NOT:**
- Prompt engineering
- An LLM wrapper
- A framework or library
- Non-deterministic

**It IS:**
- A real language with deterministic semantics
- Where strings have semantic properties
- That compiles itself through use
- With built-in provenance for AI content

## The Breakthrough

The key insight: **In a world where LLMs exist, the boundary between data and program, between text and structure, between neural and symbolic - all these boundaries become fluid.**

AgentLang is the first language designed for this reality.