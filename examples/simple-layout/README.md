# Simple Layout Example

A basic welcome screen demonstrating fundamental JUN components and properties.

## Features Demonstrated

- VStack layout with alignment
- Text components with different styles
- HStack for horizontal composition
- Shape components (Circle)
- Spacer for flexible layouts
- Button with styling
- Divider for visual separation

## Component Breakdown

### Structure

```
VStack (centered, padded container)
├── Text (title - "Welcome to JUN")
├── Text (subtitle)
├── Divider
├── HStack (featured badge)
│   ├── Circle (yellow dot)
│   └── Text (label)
├── Spacer (pushes button to bottom)
└── Button ("Get Started")
```

## Properties Used

### Layout Properties
- `spacing: 20` - Vertical space between elements
- `alignment: "center"` - Center-align all children
- `padding: 20` - Internal padding around VStack

### Text Styling
- `fontSize: 28` - Large title
- `fontWeight: "bold"` - Bold text
- `foregroundColor: "blue"` - Colored text

### Button Styling
- `backgroundColor: "blue"` - Blue background
- `foregroundColor: "white"` - White text
- `padding: 15` - Internal button padding
- `cornerRadius: 10` - Rounded corners

### Shape Usage
- `Circle` with fixed `width: 40, height: 40`
- `backgroundColor: "yellow"` - Solid yellow fill

## Design Pattern

This example demonstrates the **welcome screen** pattern:
- Centered content with title and subtitle
- A featured badge or indicator
- Flexible spacer to push CTA to bottom
- Prominent action button

Common uses:
- Onboarding screens
- Landing pages
- Empty states
- Welcome messages

## Complexity: Beginner

This is the simplest JUN example, perfect for:
- Learning the basic component structure
- Understanding property application
- Seeing how layouts compose
- First-time implementations
