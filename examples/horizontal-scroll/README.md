# Horizontal Scroll Example

A photo gallery with horizontal scrolling demonstrating remote image loading.

## Features Demonstrated

- ScrollView with horizontal axis
- Remote image loading from URLs
- Image sizing and content modes
- VStack and HStack composition
- Clipping behavior control
- Text labels with styling

## Component Breakdown

### Structure

```
VStack (main container)
├── Text (title - "Photo Gallery")
├── Text (subtitle - "Swipe to explore")
├── ScrollView (horizontal)
│   └── HStack (image container)
│       ├── VStack (image card 1)
│       │   ├── Image (remote URL - Sunset)
│       │   └── Text (label)
│       ├── VStack (image card 2)
│       │   ├── Image (remote URL - Ocean)
│       │   └── Text (label)
│       ├── VStack (image card 3)
│       │   ├── Image (remote URL - Forest)
│       │   └── Text (label)
│       └── VStack (image card 4)
│           ├── Image (remote URL - Mountains)
│           └── Text (label)
├── Divider
└── VStack (info box)
    ├── Text (title)
    └── Text (description)
```

## Key Properties

### ScrollView Configuration

```json
{
  "axis": "horizontal",
  "showsIndicators": false,
  "clipped": false
}
```

- `axis: "horizontal"` - Enables horizontal scrolling
- `showsIndicators: false` - Hides scroll bars
- `clipped: false` - Disables scroll clipping for better UX

### Image Configuration

```json
{
  "imageURL": "https://picsum.photos/seed/sunset/200/150",
  "resizable": true,
  "contentMode": "fill",
  "width": 200,
  "height": 150,
  "cornerRadius": 12,
  "clipped": true
}
```

- `imageURL` - Uses Lorem Picsum for demo images with seeded URLs
- `resizable: true` - Makes image scalable
- `contentMode: "fill"` - Scales to fill frame (may crop)
- `width/height` - Fixed dimensions for consistency
- `cornerRadius: 12` - Rounded corners
- `clipped: true` - Clips image to frame bounds

## Remote Image URLs

This example uses Lorem Picsum (https://picsum.photos) for demo images:

- `https://picsum.photos/seed/sunset/200/150` - Seeded random image
- `https://picsum.photos/seed/ocean/200/150`
- `https://picsum.photos/seed/forest/200/150`
- `https://picsum.photos/seed/mountains/200/150`

The `/seed/{name}/{width}/{height}` pattern ensures consistent images across loads.

## Implementation Notes

### Image Loading Behavior

Implementations should:
1. Show loading indicator while fetching remote images
2. Display image when loaded successfully
3. Show error state if loading fails
4. Support both remote (http/https) and local (file://) URLs

### Clipping Behavior

- `clipped: false` on ScrollView → Use platform's scroll clip disabled feature
- `clipped: true` on Image → Clip image content to frame bounds

## Preview

When rendered, this creates:
- A header with title and subtitle
- A horizontally scrollable gallery of 4 images
- Each image has a label underneath
- A footer with information about the components used

## Design Pattern

This example demonstrates the **horizontal card gallery** pattern, commonly used for:
- Photo galleries
- Product carousels
- Featured content
- Story-style feeds
- Category browsing
