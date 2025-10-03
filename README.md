# AgentLang

A programming language where text has semantic properties. Any text becomes a semantic object with properties accessible via LLM extraction.

## Key Innovation

```python
# In AgentLang, any text automatically has structure
passage = load_file("document.txt")
title = passage.title        # LLM extracts title
summary = passage.summary    # LLM extracts summary
sentiment = passage.sentiment # LLM analyzes sentiment
```

## Installation

```bash
# Install PolyCLI (prerequisite)
# See: https://github.com/shuxueshuxue/PolyCLI

# Install AgentLang (development mode)
pip install -e .
```

## Usage

```bash
# Run an AgentLang script
python al.py examples/hello_world.al

# Or use the module directly
python -m agentlang.cli examples/analyze_project.al

# Show transpiled Python code
python al.py --transpile examples/hello_world.al
```

## How It Works

1. **Transpilation**: AgentLang code is transpiled to Python
2. **Semantic Access**: Property access on text triggers LLM extraction
3. **Runtime Integration**: Uses PolyCLI for LLM interactions

## Example

```python
# example.al
doc = load_file("README.md")
goal = doc.main_goal
features = doc.key_features

print(f"Goal: {goal}")
print(f"Features: {features}")
```

Transpiles to:

```python
doc = load_file("README.md")
goal = __extract(doc, 'main_goal')
features = __extract(doc, 'key_features')

print(f"Goal: {goal}")
print(f"Features: {features}")
```

## Project Structure

```
AgentLang/
├── agentlang/          # Core package
│   ├── transpiler.py   # AST transformation
│   ├── runtime.py      # LLM extraction functions
│   └── cli.py          # Command-line interface
├── examples/           # Example scripts (.al files)
├── docs/               # Documentation
└── models.json         # PolyCLI model configuration
```

## Core Concepts

- **Text as Semantic Object**: Any text has implicit structure accessible via properties
- **Compile-time Magic**: Property access is transpiled to LLM extraction calls
- **Progressive Optimization**: System learns patterns over time (future feature)

See [docs/agentlang-core-concepts.md](docs/agentlang-core-concepts.md) for detailed philosophy.

## Dependencies

- Python 3.8+
- PolyCLI framework
- Claude API access (via PolyCLI)

## References

- Neural Symbolic PL: https://arxiv.org/pdf/2304.04812
- Related work: https://arxiv.org/abs/2505.13453
- PolyCLI: https://github.com/shuxueshuxue/PolyCLI