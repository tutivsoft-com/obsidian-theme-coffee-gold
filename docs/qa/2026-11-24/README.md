# Coffee Gold desktop verification

Coffee Gold 3.7.2 was tested on 24 November 2026 in Obsidian 1.15.1 on Windows. The theme was installed from this repository in an isolated vault. The vault contained synthetic coffee notes, searchable text, properties and tags, linked notes, a Canvas and a Base. The screenshots show the running Obsidian desktop app.

## Link contrast fix

In 3.7.1, the unresolved wiki link `[[Seasonal Card]]` inherited Obsidian's 0.7 opacity. Its rendered text had a contrast ratio of 3.57:1 on the Light reading background. Coffee Gold 3.7.2 uses the theme's muted text color for unresolved links in Light mode at full opacity.

Reading view measured 7.59:1 after the fix. Live Preview used the same full-opacity muted color. The existing resolved and external links kept their distinct pointer hover colors in both modes. The regression test checks at least 4.5:1 against both Light backgrounds.

## Desktop coverage

All 33 desktop UI cases passed. Dark and Light each had 16 cases. Adapt to system was checked separately.

- Appearance settings applied the theme palette and displayed the available scheme and font controls.
- Reading view, Live Preview and Source mode showed the sample note with its properties, tasks, callouts, table, code, link states and selection. A task was checked and then restored.
- File navigation covered the folder tree, sort menu and file menu. Tabs opened, activated and closed. The sidebars collapsed and expanded, and the Backlinks, Outgoing links, Tags, All properties and Outline panels opened.
- Quick Switcher opened a matching file. The command palette moved keyboard selection. Search showed matching and empty states, changed case matching and opened its settings. A bookmark was saved and removed, and its Save button showed a two-pixel keyboard focus outline.
- Canvas showed selectable cards and exposed its settings and zoom controls. Graph View and Local Graph rendered, and Graph View settings opened.
- Bases showed the roster in Table and Cards views. The sort, group, filter and properties controls opened. Find accepted a query, and New created a disposable note.

Adapt to system matched the Windows Light preference. Switching to Default and back restored Coffee Gold. The five stylesheet and contrast tests passed.

## Screenshots

| Capture | Verified state |
| --- | --- |
| [01. Dark Reading](screenshots/01-dark-reading.png) | Note properties, heading, highlighted text and callout |
| [02. Dark Live Preview](screenshots/02-dark-live-preview-selection.png) | Focused editor, keyboard text selection, line numbers and task items |
| [03. Dark file menu](screenshots/03-dark-file-context-menu.png) | Selected file and open right-click menu |
| [04. Dark command palette](screenshots/04-dark-command-palette.png) | Filtered commands and keyboard-selected result |
| [05. Dark Canvas](screenshots/05-dark-canvas.png) | File card, two linked text cards, selected card and zoom toolbar |
| [06. Light Appearance](screenshots/06-light-appearance.png) | Base color scheme and installed Coffee Gold theme in settings |
| [07. Light Reading detail](screenshots/07-light-reading-detail.png) | Callout, tasks, resolved and unresolved links, external link and table |
| [08. Light Source mode](screenshots/08-light-source-markdown.png) | Markdown source, YAML properties and line numbers |
| [09. Light Search](screenshots/09-light-search-results.png) | Search results and match highlights in the sidebar |
| [10. Light Bases](screenshots/10-light-bases-cards.png) | Three results in the cards view and toolbar |

Each PNG was captured from a distinct desktop state and visually checked for private data. Platform coverage is Windows desktop.
