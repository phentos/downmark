# Downmark
## Thoughts
I'd like to make my own notetaking tool.

I want:
- to use `Tkinter`
- Markdown
- Wikilinking
- Zettlekasten-ish
- storage to be git-oriented

## How
### Tkinter
Use `ttk.Notebook`.

### Markdown
Render-edit, like jupyter cells.

### Wikilinking
When parsing markdown:
- `[foo]` renders as a link to a new tab

### Navigation
- Entry points[^2] are top-level and/or recent frames
- Once in, there's upstream+downstream[^1]
    - upstream: frames that link to the current frame
    - downstream: frames this frame links to

### Persistence
Plain-text storage as markdown, in a way that's web-navigable maybe? e.g. `[foo]` that's a link to a frame in Downmark would be saved as `[foo]('bar/foo.md')`, a github-compatible link structure.

## Nifties
i.e. features i think would be cool
[^1] show a "peak" of a tab when hovered
[^2] search, favorites, tags organization