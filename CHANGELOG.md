# Changelog

All notable changes to the JUN specification are documented here.

JUN follows semantic versioning: major for breaking changes, minor for backward-compatible
additions, patch for clarifications.

## [1.2.0] — 2026-08-08

### Added

- **`imageName` and `systemImage`** as alternatives to `imageURL`, for assets owned by the
  host application and by the platform respectively. Exactly one image source is required.
- **Structured actions.** `action` accepts either a string or
  `{ "name": ..., "params": { ... } }`. Parameter values are JSON scalars. The string form is
  shorthand for an action with no parameters, and both forms are canonical.
- **Reserved action namespace.** Action names containing a dot are reserved for future
  specification-defined actions; implementations must forward unrecognised ones to the host
  rather than erroring, so later versions can add standard actions without a break.
- **Error Handling and Conformance** section, distinguishing forward-compatibility failures
  (which must degrade) from malformed input (which must be reported with a location), plus
  required resource limits and a conformance checklist.
- **Counter, Remote Images and Font Showcase examples.** The counter demonstrates the action
  format; the README previously linked a counter example that did not exist.

### Changed

- `foregroundColor` is documented as the fill for `rectangle` and `circle`. A shape given
  only `backgroundColor` must be filled with it rather than having it painted behind an
  opaque default fill.
- `padding` is documented as internal to `width` and `height`: a component with `width: 100`
  and `padding: 16` occupies 100 points in total.
- Sizing properties compose. `width`/`height` and `maxWidth`/`maxHeight` may be combined, and
  an implementation must not drop one because another is present.
- Unknown component types must be handled identically whether or not the component carries a
  `properties` object.

### Fixed

- **The JSON Schema omitted `font`.** Because the schema sets `additionalProperties: false`,
  every v1.1 document using the feature v1.1 was released for failed validation. The schema
  was never updated when v1.1 shipped.
- The schema's `$id` still identified itself as v1.0.
- Components with a required property but no `properties` object at all — `{"type": "text"}` —
  passed validation. The requirement is now enforced.

### Notes for implementers

Private aliases for specified properties are non-conformant as of this version. A document
that parses in one implementation and not another is the failure this format exists to
prevent; see the conformance checklist.

## [1.1.0] — 2025-12-03

### Added

- The `font` universal property, for specifying a font family or typeface by name.
- A typography property category.

Backward compatible with 1.0.0. See [spec/jun-v1.1-font-support.md](spec/jun-v1.1-font-support.md)
for the original design note.

## [1.0.0] — 2025-11-30

Initial specification.

- Core component types: `vstack`, `hstack`, `zstack`, `scrollView`, `text`, `image`,
  `button`, `rectangle`, `circle`, `spacer`, `divider`
- Universal property system
- Named and hex color format
- Remote image support

---

**Tagging note:** 1.0.0 and 1.1.0 were published as specification revisions but were never
tagged in git. 1.2.0 is the first tagged release.
