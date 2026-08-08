# Remote Images Example

An image gallery demonstrating remote image loading via `imageURL`.

## Features Demonstrated

- `imageURL` with remote HTTPS sources
- `resizable` combined with `contentMode` (`fit` and `fill`)
- Fixed sizes, `maxWidth`, and aspect-ratio-driven sizing
- `cornerRadius` with `clipped` for rounded and circular images
- A vertical `scrollView` containing a mixed gallery

## Loading behaviour

`imageURL` is fetched at render time, so implementations show a loading state while the
request is in flight and a placeholder if it fails. This example uses `picsum.photos`, which
means it needs network access and will render placeholders offline — that is the intended
demonstration, not a defect.

Of the three image sources in v1.2, only `imageURL` ships its asset with the document.
`imageName` and `systemImage` resolve against the host application and the platform
respectively, so a document that must render identically everywhere should prefer `imageURL`.

## Files

- `screen.json` — the JUN document
