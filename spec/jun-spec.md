# JUN Specification v1.1

**JSON UI Notation** - A declarative format for defining user interfaces

**Status**: Draft
**Version**: 1.1.0
**Author**: Pawel Zgoda-Ferchmin
**Last Updated**: 2025-12-03

---

## Table of Contents

1. [Overview](#overview)
2. [Core Concepts](#core-concepts)
3. [Component Structure](#component-structure)
4. [Component Types](#component-types)
5. [Properties](#properties)
6. [Data Types](#data-types)
7. [Color Format](#color-format)
8. [Examples](#examples)
9. [Implementation Guidelines](#implementation-guidelines)
10. [Versioning](#versioning)

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
Image from URL.

**Properties:**
- `imageURL` (string) - **Required** - URL to image (http://, https://, or file://)
- `resizable` (boolean) - Make image resizable (default: `false`)

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

#### `button`
Interactive button.

**Properties:**
- `label` (string) - **Required** - Button text
- `action` (string) - Action identifier

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

#### Visual Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `foregroundColor` | string | Text/icon color | `"blue"`, `"#FF5733"` |
| `backgroundColor` | string | Background color | `"red"`, `"#00FF00"` |
| `cornerRadius` | number | Corner rounding | `12` |
| `clipped` | boolean | Clip content to bounds | `true` |

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

- `imageURL` (string) - **Required** - Image URL
- `resizable` (boolean) - Make image resizable

#### Button

- `label` (string) - **Required** - Button text
- `action` (string) - Action identifier

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

## Versioning

JUN follows semantic versioning:

- **Major**: Breaking changes to spec
- **Minor**: New components/properties (backward compatible)
- **Patch**: Clarifications, bug fixes

Current version: **1.1.0**

### Version History

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

### Planned for v1.2

- Navigation components (navigationLink, sheet)
- Data binding with template variables `{{var}}`
- List iteration with `forEach`

### Under Discussion

- Animation properties
- Gesture recognizers
- Conditional rendering
- State management
- Form components (textField, picker, toggle, slider)
- Custom component registration

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
  imageURL: string  // required
  resizable?: boolean
}
```

**Button:**
```typescript
{
  label: string  // required
  action?: string
}
```

---

## Appendix B: Validation Rules

### Required Fields

- Component must have `type` field
- Text must have `content` property
- Image must have `imageURL` property
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
