from polycli.polyagent import PolyAgent

def __extract(source, attribute):
    prompt = f"Extract {attribute} from the following material:\n\n{source}"
    return PolyAgent().run(prompt, cli="no-tools").content

def load_file(path: str, specs=""):
    if path.endswith(".md") or path.endswith(".txt"):
        with open(path, 'r', encoding="utf-8") as f:
            return f.read()
    else:
        prompt = f"Extract all information from the following material path:\n\n{path}"
        if specs:
            prompt += f"\n\nRequirements: {specs}"
        return PolyAgent().run(prompt, cli="claude-code").content

