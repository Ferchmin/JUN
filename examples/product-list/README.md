# Product List Example

A scrollable product catalog demonstrating complex nested layouts and repeated patterns.

## Features Demonstrated

- ScrollView with vertical scrolling
- Nested VStack and HStack layouts
- Product card pattern (repeated structure)
- Shape components as placeholders
- Text hierarchy (title, description, price)
- Multiple buttons in a row
- Divider for section separation

## Component Breakdown

### Structure

```
ScrollView (vertical)
└── VStack (main container)
    ├── Text (page title)
    ├── Text (page subtitle)
    ├── VStack (product list)
    │   ├── HStack (product card 1)
    │   │   ├── Rectangle (image placeholder - blue)
    │   │   ├── VStack (product info)
    │   │   │   ├── Text (name)
    │   │   │   ├── Text (description)
    │   │   │   └── Text (price)
    │   │   └── Spacer
    │   ├── HStack (product card 2)
    │   │   ├── Rectangle (image placeholder - purple)
    │   │   └── VStack (product info)
    │   └── HStack (product card 3)
    │       ├── Circle (image placeholder - orange)
    │       └── VStack (product info)
    ├── Divider
    └── HStack (action buttons)
        ├── Button ("View All")
        └── Button ("Cart")
```

## Key Properties

### Product Card Pattern

Each product card uses this repeatable structure:

```json
{
  "type": "hstack",
  "properties": {
    "spacing": 12,
    "padding": 12,
    "backgroundColor": "#F5F5F5",
    "cornerRadius": 12
  },
  "children": [
    {
      "type": "rectangle",
      "properties": {
        "width": 80,
        "height": 80,
        "backgroundColor": "blue",
        "cornerRadius": 8
      }
    },
    {
      "type": "vstack",
      "properties": {
        "spacing": 4,
        "alignment": "leading"
      },
      "children": [
        { "type": "text", "properties": { "content": "Product Name" } },
        { "type": "text", "properties": { "content": "Description" } },
        { "type": "text", "properties": { "content": "Price" } }
      ]
    },
    {
      "type": "spacer"
    }
  ]
}
```

### Design Choices

**Shape placeholders**: Uses Rectangle and Circle as image placeholders with solid colors. In a real app, these would be replaced with `image` components using `imageURL`.

**Text hierarchy**:
- Product name: 18pt, semibold
- Description: 14pt, gray
- Price: 16pt, bold, color-coded

**Spacing**:
- Between cards: 15pt
- Within cards: 12pt
- Within product info: 4pt

## Scrolling Behavior

```json
{
  "type": "scrollView",
  "properties": {
    "axis": "vertical",
    "showsIndicators": true
  }
}
```

- `axis: "vertical"` - Enables vertical scrolling
- `showsIndicators: true` - Shows scroll bars

## Action Buttons

Two buttons at the bottom:
- **"View All"** - Primary action (blue)
- **"Cart"** - Secondary action (gray)

## Design Pattern

This example demonstrates the **product list** pattern, commonly used for:
- E-commerce catalogs
- Item listings
- Feed-style content
- Scrollable cards
- Search results

## Implementation Notes

### Future Enhancement: Data Binding

In v1.1+, this could use data iteration:

```json
{
  "type": "vstack",
  "forEach": "products",
  "children": [
    {
      "type": "text",
      "properties": {
        "content": "{{item.name}}"
      }
    }
  ]
}
```

For now, each product is manually defined.

## Complexity: Intermediate

This example shows:
- Multiple levels of nesting
- Repeated component patterns
- Mixed layout types (VStack + HStack)
- Shape variety (Rectangle + Circle)
- Proper use of Spacer
