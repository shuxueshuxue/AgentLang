# analyze_project.al - AgentLang script for project analysis

# Load project files
readme = load_file("README.md")
core_concepts = load_file("agentlang-core-concepts.md")
transpiler = load_file("transpiler_minimal.py")

# Extract high-level information
project_vision = readme.vision
key_features = readme.features
innovation = core_concepts.key_innovations

# Analyze code complexity
code_complexity = transpiler.complexity
design_patterns = transpiler.patterns

# Generate insights
print("=== Project Analysis ===")
print(f"Vision: {project_vision}")
print(f"\nKey Features: {key_features}")
print(f"\nMain Innovations: {innovation}")
print(f"\nCode Complexity: {code_complexity}")

# Conditional analysis
if core_concepts.revolutionary_level == "high":
    implications = core_concepts.implications
    print(f"\nRevolutionary Implications: {implications}")

# Generate summary report
report = f"""
Project: {readme.title}
Status: {readme.status}
Complexity: {code_complexity}
Innovation Level: {core_concepts.innovation_level}
"""

print("\n=== Summary Report ===")
print(report)