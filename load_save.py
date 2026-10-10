import json
from pathlib import Path

def load_progress():
    path = Path("data/progress.json")

    if not path.exists():
        return {"unlocked_level": 1, "completed_levels": []}

    content = path.read_text(encoding="utf-8")

    return json.loads(content)


def save_progress(app):
    progress = {"unlocked_level": app.unlocked_level, "completed_levels": app.completed_levels}
    content = json.dumps(progress, indent=4)

    Path("data/progress.json").write_text(content, encoding="utf-8")

def load_config():
    content = Path("config.json").read_text(encoding="utf-8")

    return json.loads(content)

def save_config(config):
    content = json.dumps(config, indent=4)

    Path("config.json").write_text(content, encoding="utf-8")

def load_default_config():
    content = Path("default_config.json").read_text(encoding="utf-8")

    return json.loads(content)

def reset_settings(app):
    app.config = load_default_config()
    save_config(app.config)

def load_levels():
    content = Path("data/levels.json").read_text(encoding="utf-8")

    return json.loads(content)

def load_coins():
    content = Path("data/coins.json").read_text(encoding="utf-8")
    return json.loads(content)


def save_coins(coins):
    data = {"coins": coins}
    content = json.dumps(data, indent=4)

    Path("data/coins.json").write_text(content,encoding="utf-8")

def load_upgrades():
    content = Path("data/upgrades.json").read_text(
        encoding="utf-8"
    )

    return json.loads(content)


def save_upgrades(upgrades):
    content = json.dumps(
        upgrades,
        indent=4
    )

    Path("data/upgrades.json").write_text(
        content,
        encoding="utf-8"
    )