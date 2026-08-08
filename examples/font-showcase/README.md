# Font Showcase Example

A typographic sampler demonstrating the `font` universal property added in JUN v1.1.

## Features Demonstrated

- The `font` property on text components
- Named platform fonts: Helvetica, Courier, Georgia, Helvetica Neue
- `font` combined with `fontSize` and `fontWeight`
- Several typefaces within one document
- Hex colors and a tinted container background

## Font availability

`font` names are resolved at render time against whatever the platform has. Availability
differs between platforms and between devices, so implementations fall back to the system
font when a name cannot be resolved rather than failing.

The names in this example are chosen because they resolve on Apple platforms out of the box.
A document that must render identically everywhere should not depend on a specific typeface
being present.

Application-bundled fonts are referenced by the same property, but the host application is
responsible for registering them — on iOS, via `UIAppFonts` in `Info.plist`.

## Files

- `screen.json` — the JUN document
