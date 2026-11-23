import json
import re
import unittest
from pathlib import Path

import cssselect2
import tinycss2


ROOT = Path(__file__).resolve().parents[1]
MODES = ("body.theme-light", "body.theme-dark")


def read_rules(stylesheet):
    rules = {}
    parsed = tinycss2.parse_stylesheet(stylesheet, skip_comments=True, skip_whitespace=True)
    for rule in parsed:
        if rule.type != "qualified-rule":
            raise ValueError(f"Unexpected CSS rule at line {rule.source_line}: {rule.type}")
        selectors = tinycss2.serialize(rule.prelude).strip()
        cssselect2.compile_selector_list(selectors)
        declarations = {}
        items = tinycss2.parse_declaration_list(rule.content, skip_comments=True, skip_whitespace=True)
        for item in items:
            if item.type != "declaration":
                raise ValueError(f"Invalid declaration at line {item.source_line}")
            declarations[item.name] = tinycss2.serialize(item.value).strip()
        for selector in selectors.split(","):
            rules.setdefault(selector.strip(), {}).update(declarations)
    return rules


def resolve_color(value, palette):
    if value.startswith("var("):
        return resolve_color(palette[value[4:-1]], palette)
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise ValueError(f"Expected a six-digit hex color, got {value}")
    return value


def luminance(color):
    channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [
        channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
        for channel in channels
    ]
    return sum(channel * weight for channel, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


class ThemeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stylesheet = (ROOT / "theme.css").read_text(encoding="utf-8")
        cls.rules = read_rules(cls.stylesheet)

    def assert_contrast(self, first, second, minimum):
        dark, light = sorted((luminance(first), luminance(second)))
        ratio = (light + 0.05) / (dark + 0.05)
        self.assertGreaterEqual(ratio, minimum, f"{first} on {second}: {ratio:.2f}:1")

    def test_links_have_distinct_readable_hover_colors_in_both_modes(self):
        for mode in MODES:
            palette = self.rules[mode]
            for name in ("--link-color", "--link-external-color"):
                with self.subTest(mode=mode, link=name):
                    default = resolve_color(palette[name], palette)
                    hover_name = f"{name}-hover"
                    self.assertIn(hover_name, palette)
                    hover = resolve_color(palette[hover_name], palette)
                    self.assertNotEqual(default, hover)
                    for surface in ("--background-primary", "--background-secondary"):
                        self.assert_contrast(default, palette[surface], 4.5)
                        self.assert_contrast(hover, palette[surface], 4.5)

    def test_accent_button_keyboard_focus_contrasts_with_its_fill(self):
        for mode in MODES:
            palette = self.rules[mode]
            for container in (".workspace-leaf-content", ".modal", ".menu"):
                with self.subTest(mode=mode, container=container):
                    base = self.rules[f"{container} :focus-visible"]
                    button = self.rules.get(f"{container} button.mod-cta:focus-visible", {})
                    self.assertEqual(base["outline-offset"], "-2px")
                    default_color = base["outline"].split()[-1]
                    default_ring = resolve_color(default_color, palette)
                    self.assert_contrast(default_ring, palette["--background-primary"], 3)
                    ring = resolve_color(button.get("outline-color", default_color), palette)
                    self.assert_contrast(ring, palette["--interactive-accent"], 3)
                    self.assert_contrast(ring, palette["--interactive-accent-hover"], 3)

    def test_mobile_editor_retains_padding_inside_the_focus_outline(self):
        selector = ".is-mobile .markdown-source-view.mod-cm6 .cm-contentContainer > .cm-content"
        self.assertEqual(self.rules[selector]["padding-inline"], "8px")

    def test_source_version_and_preview_paths(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        for field in ("name", "author", "minAppVersion", "version"):
            self.assertTrue(manifest[field])
        version = manifest["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertTrue(self.stylesheet.startswith(f"/* {manifest['name']} {version}."))
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"Source version {version}.", readme)
        for markdown in (readme, (ROOT / "PLAN.md").read_text(encoding="utf-8")):
            for path in re.findall(r"!?\[[^]]+\]\(([^():]+)\)", markdown):
                self.assertTrue((ROOT / path).is_file(), path)


if __name__ == "__main__":
    unittest.main()
