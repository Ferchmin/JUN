# Counter Example

An interactive counter demonstrating the JUN v1.2 action format.

## Features Demonstrated

- Structured actions with parameters (`adjustCount` with `by: 1` / `by: -1`)
- String-shorthand actions (`"action": "resetCount"`)
- Buttons with distinct visual treatments
- Fixed-width buttons in an HStack
- A monospaced `font` for the numeral so its width does not jump between values

## What this example does *not* do

JUN has no state and no data binding, so the displayed count is a literal `"0"`. The document
describes a screen; it does not describe how the screen changes.

That is the point of the action model. The buttons name an intent — `adjustCount` with a
parameter — and the host application decides what that means. A host would typically keep the
count itself and re-render, either by substituting a new document or by rendering a JUN
subtree inside its own stateful view.

Nothing happens if the host supplies no action handler. A JUN document can only *name* an
intent; it cannot cause one.

## Host handling

```swift
ComponentRenderer(component: document.root)
    .junActionHandler { action in
        switch action.name {
        case "adjustCount":
            count += action.params["by"]?.intValue ?? 0
        case "resetCount":
            count = 0
        default:
            break
        }
    }
```

## Files

- `screen.json` — the JUN document
