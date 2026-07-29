# Accessibility

This project treats accessibility as a release requirement, not a final audit.

## Current target

- Use WCAG 2.2 Level AA for user-facing web content and interfaces.
- Treat applicable Level AAA criteria as aspirational improvements, not as
  Level AA failures.
- Use the latest stable W3C Recommendation unless a receiving project or legal
  requirement names another version.
- Prefer semantic HTML and platform behaviour before ARIA.
- Require keyboard access, visible focus, sufficient contrast, reflow, clear
  language, and accessible names where applicable.

## Documentation

- Use descriptive headings and link text.
- Explain acronyms on first use where the audience may not know them.
- Do not rely on color, position, or sensory characteristics alone.
- Give text alternatives for meaningful images and diagrams.
- Make tables simple, captioned when useful, and correctly headed.
- Keep instructions usable without a mouse.

## Testing

Use automated testing as evidence, not as a complete conformance decision.
Combine deterministic checks with keyboard review, screen-reader review where
relevant, zoom and reflow testing, and testing with disabled people when impact
or risk warrants it.

Report:

- the affected people and tasks;
- the relevant requirement;
- reproducible steps and environment;
- automated and manual evidence;
- uncertainty and false-positive risk;
- expected behaviour.

The planned accessibility adapter will connect these general contribution
skills to [ACCESSIBILITY.md](https://github.com/mgifford/ACCESSIBILITY.md) and
[accessibility-skills](https://github.com/mgifford/accessibility-skills).
