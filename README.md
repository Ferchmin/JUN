# JUN - JSON UI Notation

A declarative JSON format for defining user interfaces across platforms.

**Created by**: Pawel Zgoda-Ferchmin
**Version**: 1.2.0
**License**: MIT

---

## What is JUN?

**JUN (JSON UI Notation)** is a platform-agnostic specification for describing user interfaces in JSON. It enables:

- 🤖 **AI-Generated Interfaces** - LLMs can generate structured UI definitions
- 🚀 **Server-Driven UI** - Update interfaces without app deployments
- 🔄 **Cross-Platform** - Write once, render on iOS, Android, Web, Desktop
- ⚡ **Rapid Prototyping** - Design interfaces declaratively without compilation

## Platform Implementations

### Official Implementations

- **[JUNSwiftUI](https://github.com/ferchmin/JUNSwiftUI)** - iOS/macOS implementation using SwiftUI

### Community Implementations

- Submit yours via PR!

## Quick Example

```json
{
  "type": "vstack",
  "properties": {
    "spacing": 20,
    "padding": 16
  },
  "children": [
    {
      "type": "text",
      "properties": {
        "content": "Hello, JUN!",
        "fontSize": 28,
        "fontWeight": "bold",
        "foregroundColor": "blue"
      }
    },
    {
      "type": "button",
      "properties": {
        "label": "Get Started",
        "backgroundColor": "blue",
        "foregroundColor": "white",
        "padding": 12,
        "cornerRadius": 8
      }
    }
  ]
}
```

## Documentation

### Core Specification
- [JUN Specification v1.2](spec/jun-spec.md) - Complete format reference
- [JSON Schema](schemas/jun.schema.json) - For validation
- [Changelog](CHANGELOG.md) - Version history

### Examples

Every example validates against the JSON Schema on each commit.

- [Simple Layout](examples/simple-layout/) - Basic welcome screen
- [Counter](examples/counter/) - Interactive counter demonstrating the action format
- [Product List](examples/product-list/) - Scrollable catalog with cards
- [Horizontal Scroll](examples/horizontal-scroll/) - Image gallery with remote URLs
- [Remote Images](examples/remote-images/) - Loading, sizing and clipping remote images
- [Font Showcase](examples/font-showcase/) - The `font` property across several typefaces

## Core Concepts

### 1. Component Structure

Every JUN component has:
- `type` (required) - Component type identifier
- `properties` (optional) - Component-specific and universal properties
- `children` (optional) - Array of child components

### 2. Universal Properties

All components support common properties:
- Layout: `width`, `height`, `maxWidth`, `maxHeight`, `padding`
- Visual: `backgroundColor`, `foregroundColor`, `cornerRadius`, `clipped`
- Typography: `font`
- Image: `aspectRatio`, `contentMode`

### 3. Component Types

**Layouts**: `vstack`, `hstack`, `zstack`, `scrollView`
**Content**: `text`, `image`, `button`
**Shapes**: `rectangle`, `circle`
**Utilities**: `spacer`, `divider`

### 4. Actions

Buttons name an intent; the host application decides what it means. A document can never
cause an effect on its own.

```json
{
  "type": "button",
  "properties": {
    "label": "Add to cart",
    "action": { "name": "addToCart", "params": { "productId": "SKU-42" } }
  }
}
```

## Design Principles

1. **Declarative** - Describe what, not how
2. **Composable** - Components nest recursively
3. **Type-safe** - Properties validated by schema
4. **Platform-agnostic** - No platform-specific APIs
5. **Extensible** - Easy to add new component types

## Use Cases

### Server-Driven UI

```swift
// Fetch UI from server
let response = try await api.get("/ui/home-screen")
let component = try parse(response)
render(component)
```

### A/B Testing

```json
// Variant A
{ "type": "vstack", "children": [...] }

// Variant B
{ "type": "hstack", "children": [...] }
```

### AI-Generated UI

```
Prompt: "Create a user profile card with avatar, name, and bio"

LLM Output: { "type": "hstack", ... }
```

## Version History

- **v1.2.0** - Local and system images, structured actions, error-handling and conformance
  rules, and a corrected JSON Schema
- **v1.1.0** - The `font` universal property
- **v1.0.0** - Initial release: core component types, universal properties, remote images

See [CHANGELOG.md](CHANGELOG.md) for detail.

## Roadmap

- [ ] Conformance fixture suite
- [ ] Specification-defined actions (`jun.openURL`, `jun.navigate`, `jun.dismiss`) and the
      host-veto model they require
- [ ] Navigation support (push, sheet, fullscreen)
- [ ] Data binding with template variables `{{var}}`
- [ ] List iteration (`forEach`)
- [ ] Conditional rendering
- [ ] Form components (textfield, picker, toggle)
- [ ] State management

## Contributing

We welcome:
- New platform implementations
- Specification improvements
- Bug reports and feature requests
- Documentation enhancements

See [spec/jun-spec.md](spec/jun-spec.md) for implementation guidelines.

## License

MIT License - See [LICENSE](LICENSE) file

Copyright (c) 2025 Pawel Zgoda-Ferchmin

---
