# JUN Specification v1.2

**JSON UI Notation** - A declarative format for defining user interfaces

**Status**: Draft
**Version**: 1.2.0
**Author**: Pawel Zgoda-Ferchmin
**Last Updated**: 2026-08-08

---

## Table of Contents

1. [Overview](#overview)
2. [Core Concepts](#core-concepts)
3. [Component Structure](#component-structure)
4. [Component Types](#component-types)
5. [Properties](#properties)
6. [Data Types](#data-types)
7. [Color Format](#color-format)
8. [Actions](#actions)
9. [Examples](#examples)
10. [Implementation Guidelines](#implementation-guidelines)
11. [Error Handling and Conformance](#error-handling-and-conformance)
12. [Versioning](#versioning)

---

## Overview

JUN (JSON UI Notation) provides a standardized way to represent user interfaces as JSON documents. It is designed to be:

- **Platform-agnostic**: Works across iOS, Android, Web, Desktop
- **Human-readable**: Easy to write and understand
- **Machine-parseable**: Strict JSON format
- **Composable**: Recursive component structure
- **Extensible**: Easy to add new component types

## Core Concepts

### 1. Component Model

Every UI element is a **component** with:
- A `type` identifier (string)
- Optional `properties` (object)
- Optional `children` (array of components)

### 2. Recursive Structure

Components can contain other components, forming a tree:

```
VStack
├── Text
├── Image
└── HStack
    ├── Button
    └── Button
```

### 3. Property Inheritance

Properties are either:
- **Universal**: Applicable to all components (padding, colors, sizing)
- **Type-specific**: Only for certain component types (text content, button labels)

---

## Component Structure

### Basic Component Schema

```json
{
  "type": "component_type",
  "properties": {
    "property1": "value1",
    "property2": 123
  },
  "children": [
    { /* child component */ }
  ]
}
```

### Fields

#### `type` (required)
- **Type**: String
- **Description**: Component type identifier
- **Case**: Case-insensitive (recommended: lowercase)
- **Examples**: `"vstack"`, `"text"`, `"button"`

#### `properties` (optional)
- **Type**: Object
- **Description**: Component configuration
- **Default**: Empty object `{}`

#### `children` (optional)
- **Type**: Array of components
- **Description**: Child components (for containers only)
- **Constraints**: Not allowed for leaf components (text, image, button, shapes, spacer, divider)

#### `id` (optional)
- **Type**: String (UUID)
- **Description**: Unique identifier
- **Default**: Auto-generated if not provided

---

## Component Types

### Layout Components

Components that contain and arrange children.

#### `vstack`
Vertical stack layout.

**Properties:**
- `spacing` (number) - Space between children
- `alignment` (string) - Horizontal alignment: `"leading"`, `"center"`, `"trailing"`

**Example:**
```json
{
  "type": "vstack",
  "properties": {
    "spacing": 20,
    "alignment": "center"
  },
  "children": [...]
}
```

#### `hstack`
Horizontal stack layout.

**Properties:**
- `spacing` (number) - Space between children
- `alignment` (string) - Vertical alignment: `"top"`, `"center"`, `"bottom"`

#### `zstack`
Depth stack (overlapping layers).

**Properties:**
- `alignment` (string) - Alignment: `"topLeading"`, `"top"`, `"topTrailing"`, `"leading"`, `"center"`, `"trailing"`, `"bottomLeading"`, `"bottom"`, `"bottomTrailing"`

#### `scrollView`
Scrollable container.

**Properties:**
- `axis` (string) - Scroll direction: `"vertical"`, `"horizontal"`
- `showsIndicators` (boolean) - Show scroll indicators (default: `true`)

**Example:**
```json
{
  "type": "scrollView",
  "properties": {
    "axis": "horizontal",
    "showsIndicators": false
  },
  "children": [...]
}
```

### Content Components

Components that display content.

#### `text`
Text label.

**Properties:**
- `content` (string) - **Required** - Text to display
- `fontSize` (number) - Font size in points
- `fontWeight` (string) - Font weight: `"thin"`, `"light"`, `"regular"`, `"medium"`, `"semibold"`, `"bold"`, `"heavy"`, `"black"`

**Example:**
```json
{
  "type": "text",
  "properties": {
    "content": "Hello World",
    "fontSize": 24,
    "fontWeight": "bold",
    "font": "Helvetica",
    "foregroundColor": "blue"
  }
}
```

#### `image`
Image from a remote URL, a bundled asset, or the platform's system icon set.

**Properties:**
- `imageURL` (string) - URL to image (`http://`, `https://`, or `file://`)
- `imageName` (string) - Name of an image bundled with the host application *(since v1.2)*
- `systemImage` (string) - Name of an icon in the platform's system icon set *(since v1.2)*
- `resizable` (boolean) - Make image resizable (default: `false`)

**Exactly one** of `imageURL`, `imageName` or `systemImage` is **required**. Providing more
than one is invalid.

The three sources differ in who owns the asset:

| Source | Asset owned by | Resolution |
|--------|----------------|------------|
| `imageURL` | The document author | Fetched at render time; implementations show a loading state and a failure placeholder |
| `imageName` | The host application | Looked up in the app's asset catalogue / resource bundle |
| `systemImage` | The platform | Looked up in the platform icon set (SF Symbols on Apple platforms, Material Symbols on Android, and the equivalent elsewhere) |

Because `imageName` and `systemImage` resolve against assets the *document* cannot ship,
their names are inherently platform- and application-specific. A document that must render
identically everywhere should prefer `imageURL`.

**Example:**
```json
{
  "type": "image",
  "properties": {
    "imageURL": "https://example.com/image.jpg",
    "resizable": true,
    "contentMode": "fill",
    "width": 300,
    "height": 200,
    "cornerRadius": 12
  }
}
```

```json
{
  "type": "image",
  "properties": {
    "systemImage": "star.fill",
    "foregroundColor": "yellow",
    "width": 24,
    "height": 24
  }
}
```

#### `button`
Interactive button.

**Properties:**
- `label` (string) - **Required** - Button text
- `action` (string | object) - Action dispatched when the button is activated. See [Actions](#actions).

**Example:**
```json
{
  "type": "button",
  "properties": {
    "label": "Click Me",
    "action": "submit",
    "backgroundColor": "blue",
    "foregroundColor": "white",
    "padding": 12,
    "cornerRadius": 8
  }
}
```

### Shape Components

#### `rectangle`
Rectangular shape.

**Example:**
```json
{
  "type": "rectangle",
  "properties": {
    "width": 100,
    "height": 100,
    "backgroundColor": "red",
    "cornerRadius": 12
  }
}
```

#### `circle`
Circular shape.

**Example:**
```json
{
  "type": "circle",
  "properties": {
    "width": 80,
    "height": 80,
    "backgroundColor": "blue"
  }
}
```

### Utility Components

#### `spacer`
Flexible space that expands to fill available space.

**Properties:** None

**Example:**
```json
{
  "type": "spacer"
}
```

#### `divider`
Visual separator line.

**Properties:** None

**Example:**
```json
{
  "type": "divider"
}
```

---

## Properties

### Universal Properties

These properties can be applied to **any component**:

#### Layout Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `padding` | number | Internal padding | `16` |
| `width` | number | Fixed width | `100` |
| `height` | number | Fixed height | `50` |
| `maxWidth` | number | Maximum width | `500` |
| `maxHeight` | number | Maximum height | `300` |

**Padding is internal.** `padding` is applied *inside* `width` and `height`: a component with
`width: 100` and `padding: 16` occupies 100 points in total, of which 68 are available to its
content. `backgroundColor` extends under the padding.

**Sizing properties compose.** `width`/`height` and `maxWidth`/`maxHeight` may be combined
freely; an implementation must not silently drop one because another is present.

#### Visual Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `foregroundColor` | string | Text/icon color, and fill color for shapes | `"blue"`, `"#FF5733"` |
| `backgroundColor` | string | Background color, painted behind the component | `"red"`, `"#00FF00"` |
| `cornerRadius` | number | Corner rounding | `12` |
| `clipped` | boolean | Clip content to bounds | `true` |

**Shape fill.** For `rectangle` and `circle`, `foregroundColor` is the fill. When a shape
specifies `backgroundColor` but no `foregroundColor`, implementations **must** fill the shape
with the background color rather than painting it behind an opaque default fill — otherwise
the most natural way to write a coloured shape produces an invisible one.

#### Typography Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `font` | string | Custom font name | `"Helvetica"`, `"Courier"` |

#### Image Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `aspectRatio` | number | Width/height ratio | `1.5`, `0.75` |
| `contentMode` | string | Scaling mode: `"fit"` or `"fill"` | `"fill"` |

**Note:** For ScrollView, `clipped: false` should disable scroll clipping.

### Type-Specific Properties

Properties only applicable to specific component types.

#### VStack, HStack, ZStack

- `spacing` (number) - Space between children
- `alignment` (string) - Child alignment (varies by layout type)

#### ScrollView

- `axis` (string) - `"vertical"` or `"horizontal"`
- `showsIndicators` (boolean) - Show scroll indicators

#### Text

- `content` (string) - **Required** - Text content
- `fontSize` (number) - Font size
- `fontWeight` (string) - Font weight

#### Image

- `imageURL` (string) - Image URL
- `imageName` (string) - Bundled asset name
- `systemImage` (string) - Platform icon name
- `resizable` (boolean) - Make image resizable

Exactly one of `imageURL`, `imageName`, `systemImage` is required.

#### Button

- `label` (string) - **Required** - Button text
- `action` (string | object) - Dispatched on activation; see [Actions](#actions)

---

## Data Types

### Primitive Types

| Type | JSON Type | Example | Description |
|------|-----------|---------|-------------|
| String | `string` | `"hello"` | Text value |
| Number | `number` | `42`, `3.14` | Numeric value (int or float) |
| Boolean | `boolean` | `true`, `false` | True/false value |

### Complex Types

| Type | JSON Type | Description |
|------|-----------|-------------|
| Component | `object` | Nested component with type, properties, children |
| Array | `array` | List of components (for children) |
| Object | `object` | Key-value pairs (for properties) |

---

## Color Format

Colors can be specified as:

### Named Colors

Standard color names (case-insensitive):
- `"red"`, `"blue"`, `"green"`, `"yellow"`, `"orange"`, `"purple"`
- `"pink"`, `"gray"`, `"black"`, `"white"`
- `"primary"`, `"secondary"` (theme colors)

### Hex Colors

- **6-digit RGB**: `"#FF5733"` (red: FF, green: 57, blue: 33)
- **8-digit RGBA**: `"#FF5733AA"` (includes alpha channel)

**Format Rules:**
- Must start with `#`
- Case-insensitive hex digits (0-9, A-F)
- No shorthand notation (#RGB)

---

## Actions

*Since v1.2.*

An action expresses **what the document wants to happen**, not how it happens. A JUN
document can only *name* an intent; nothing occurs unless the host application implements
that name. This is deliberate — a document arriving from a server must never be able to make
an application act on its own.

Currently only `button` carries an action.

### Format

An action is either a string or an object.

```json
{ "type": "button", "properties": { "label": "Check out", "action": "checkout" } }
```

```json
{
  "type": "button",
  "properties": {
    "label": "Add to cart",
    "action": {
      "name": "addToCart",
      "params": { "productId": "SKU-42", "quantity": 1 }
    }
  }
}
```

The string form is shorthand: `"checkout"` is exactly equivalent to
`{ "name": "checkout", "params": {} }`. Both forms are canonical — use the string when there
are no parameters.

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | **Required.** Non-empty action identifier |
| `params` | object | Optional parameters passed through to the host |

### Parameter values

`params` values **must be JSON scalars**: string, number, boolean, or null. Nested objects
and arrays are not permitted in v1.2.

This restriction is intentional. It keeps the parameter type trivial to express in every
target language, keeps host-side unpacking free of schema guesswork, and can be relaxed in a
later version without breaking existing documents — whereas the reverse could not be done.

### Reserved names

Action names containing a dot (`.`) are **reserved** for future specification-defined
actions. Applications must not define their own dotted names.

No dotted actions are defined in v1.2. Implementations encountering one **must** forward it
to the host application unchanged rather than treating it as an error, so that a future
version can define standard actions without breaking older implementations.

### Dispatch

Implementations must:

1. Deliver the action to a host-supplied handler, with `name` and `params` intact.
2. Do nothing when no handler is supplied. An implementation must not invent a default
   behaviour for any action name, and must not log to standard output in release builds.
3. Never interpret `params` as instructions — parameters are opaque data for the host.

---

## Examples

### Minimal Component

```json
{
  "type": "text",
  "properties": {
    "content": "Hello"
  }
}
```

### Nested Layout

```json
{
  "type": "vstack",
  "properties": {
    "spacing": 16,
    "padding": 20
  },
  "children": [
    {
      "type": "text",
      "properties": {
        "content": "Title",
        "fontSize": 24,
        "fontWeight": "bold"
      }
    },
    {
      "type": "text",
      "properties": {
        "content": "Subtitle",
        "fontSize": 16,
        "foregroundColor": "gray"
      }
    }
  ]
}
```

### Image with URL

```json
{
  "type": "image",
  "properties": {
    "imageURL": "https://picsum.photos/300/200",
    "resizable": true,
    "contentMode": "fill",
    "width": 300,
    "height": 200,
    "cornerRadius": 12,
    "clipped": true
  }
}
```

### Complete Screen

See [examples/](../examples/) directory for full examples.

---

## Implementation Guidelines

### For Implementers

When creating a JUN implementation for a platform:

#### 1. Parser Requirements

- Must parse valid JSON conforming to this spec
- Must validate component `type` field
- Should provide helpful error messages for invalid JSON
- May generate IDs if not provided

#### 2. Component Rendering

- Must support all core component types
- Must respect universal properties
- Should handle missing optional properties gracefully
- May provide platform-specific extensions

#### 3. Property Handling

- Required properties must be validated
- Optional properties should have sensible defaults
- Unknown properties should be ignored (forward compatibility)

#### 4. Error Handling

Implementations should handle:
- Invalid JSON syntax
- Unknown component types
- Missing required properties
- Invalid property values
- Circular references

#### 5. Extensions

Implementations may add:
- Platform-specific component types (prefix with platform: `"ios.tabView"`)
- Additional properties (document in implementation)
- Custom color names (theme support)

### Compatibility

- **MUST** support all component types in this spec
- **SHOULD** ignore unknown properties (forward compat)
- **MAY** add platform-specific extensions
- **MUST NOT** break on future spec additions

---

## Error Handling and Conformance

*Since v1.2.*

Two kinds of thing go wrong when parsing a JUN document, and they have opposite correct
responses. Conflating them is the most common implementation mistake.

### Forward-compatibility failures — degrade

An unknown component type, an unknown property, or a value from a later version of the
specification means **the producer is ahead of the client**. Implementations **must**
degrade rather than fail:

- Unknown component type → skip the component, keep rendering its siblings and ancestors.
- Unknown property → ignore it.
- Unknown enum value (`alignment`, `fontWeight`, `contentMode`, `axis`) → use the default.

This is not a nicety. A client that rejects a document because it contains one unfamiliar
component forces every server-side addition to wait for a coordinated client release, which
defeats the purpose of describing interfaces as data.

Behaviour must not depend on incidental document shape. In particular, an unknown component
type must be handled the same way whether or not it happens to carry a `properties` object.

### Malformed input — report

A value of the wrong JSON type, a missing required property, or malformed JSON means **the
producer has a bug**. Implementations **must not** discard these silently.

- The implementation **should** still render everything it could parse.
- It **must** make the failures available to the host application, each identified by its
  location in the document (for example `children[3].properties.imageURL`) and a description
  of the problem.
- A malformed component **must not** remove its siblings. Implementations parsing a
  `children` array must handle each element independently.
- Implementations **should** offer a strict mode that fails on the first such problem, for
  use in tests and build pipelines.

The distinction matters most in production: a lenient parser that reports nothing turns a
producer-side bug into a blank screen with no diagnosis, while a strict parser turns a
harmless unknown property into an outage.

### Resource limits

Documents may arrive from untrusted sources. Implementations **must** bound their parsing:

- A maximum nesting depth (recommended: 64).
- A maximum total component count (recommended: 10,000).

Exceeding a limit is a hard failure, not a degradation — the document is rejected. This also
discharges the circular-reference concern, since JSON documents cannot contain cycles but
generated ones can be arbitrarily deep.

### Conformance checklist

An implementation conforms to JUN v1.2 if it:

1. Renders every component type in [Component Types](#component-types).
2. Applies every universal property in [Properties](#properties), with the padding, sizing
   and shape-fill semantics stated there.
3. Accepts both action forms and dispatches them per [Actions](#actions).
4. Degrades on unknown types, properties and enum values.
5. Reports malformed input with a location, and isolates malformed siblings.
6. Enforces depth and node limits.
7. Accepts only the property names in this specification. Implementations must not accept
   private aliases for specified properties: a document that parses in one implementation and
   not another is the failure mode this format exists to prevent.

---

## Versioning

JUN follows semantic versioning:

- **Major**: Breaking changes to spec
- **Minor**: New components/properties (backward compatible)
- **Patch**: Clarifications, bug fixes

Current version: **1.2.0**

### Version History

#### v1.2.0 (2026-08-08)
- Added `imageName` and `systemImage` as alternatives to `imageURL`
- Added the structured action format, `params`, and the reserved dotted-name namespace
- Added [Error Handling and Conformance](#error-handling-and-conformance)
- Clarified that `padding` is internal to `width`/`height`, that sizing properties compose,
  and that `foregroundColor` fills shapes
- Corrected the JSON Schema, which had omitted the v1.1 `font` property
- Backward compatible with v1.1.0

#### v1.1.0 (2025-12-03)
- Added `font` universal property for custom font names
- Typography properties category
- Enhanced text rendering capabilities
- Backward compatible with v1.0.0

#### v1.0.0 (2025-11-30)
- Initial specification
- Core component types (vstack, hstack, zstack, scrollView, text, image, button, rectangle, circle, spacer, divider)
- Universal properties system
- Color format definition

---

## Future Considerations

### Planned for v1.3

- A conformance fixture suite, so implementations can be checked against the specification
  rather than against each other
- Specification-defined actions under the reserved dotted namespace — `jun.openURL`,
  `jun.navigate`, `jun.dismiss` — together with the host-veto model they require. These
  differ in kind from application-defined actions: they would let a document cause an effect
  without any application code, so they need a security design, not just a schema entry
- Navigation components (navigationLink, sheet), which depend on the above

### Under Discussion

- Data binding with template variables `{{var}}`
- List iteration with `forEach`
- Animation properties
- Gesture recognizers, and whether `action` should extend beyond `button`
- Conditional rendering
- State management
- Form components (textField, picker, toggle, slider)
- Custom component registration
- Nested values in action `params`

---

## Appendix A: Complete Property Reference

### Universal Properties

```typescript
{
  // Layout
  padding?: number
  width?: number
  height?: number
  maxWidth?: number
  maxHeight?: number

  // Visual
  foregroundColor?: string
  backgroundColor?: string
  cornerRadius?: number
  clipped?: boolean

  // Typography
  font?: string

  // Image
  aspectRatio?: number
  contentMode?: "fit" | "fill"
}
```

### Component-Specific Properties

**VStack/HStack/ZStack:**
```typescript
{
  spacing?: number
  alignment?: string
}
```

**ScrollView:**
```typescript
{
  axis?: "vertical" | "horizontal"
  showsIndicators?: boolean
}
```

**Text:**
```typescript
{
  content: string  // required
  fontSize?: number
  fontWeight?: "thin" | "light" | "regular" | "medium" | "semibold" | "bold" | "heavy" | "black"
}
```

**Image:**
```typescript
{
  // exactly one of:
  imageURL?: string
  imageName?: string
  systemImage?: string

  resizable?: boolean
}
```

**Button:**
```typescript
{
  label: string  // required
  action?: string | {
    name: string
    params?: { [key: string]: string | number | boolean | null }
  }
}
```

---

## Appendix B: Validation Rules

### Required Fields

- Component must have `type` field
- Text must have `content` property
- Image must have exactly one of `imageURL`, `imageName`, `systemImage`
- Button must have `label` property

### Optional Fields

- All other properties are optional
- `children` only valid for container components

### Type Constraints

- `type`: non-empty string
- `spacing`, `padding`, `fontSize`, `width`, `height`: non-negative numbers
- `cornerRadius`: non-negative number
- `alignment`: string from allowed values
- `foregroundColor`, `backgroundColor`: valid color string
- `imageURL`: valid URL string
- `resizable`, `showsIndicators`, `clipped`: boolean

### Nesting Rules

**Can have children:**
- `vstack`, `hstack`, `zstack`, `scrollView`

**Cannot have children:**
- `text`, `image`, `button`, `rectangle`, `circle`, `spacer`, `divider`

---

## License

This specification is released under the MIT License.

Copyright (c) 2025 Pawel Zgoda-Ferchmin
