# Coffee Gold original design plan

This plan records the design proposed on 13 November 2026, before implementation and release. See the [README](README.md) for current modes, requirements and installation.

Search keywords: Obsidian theme, coffee, brown, gold accents, cream text, warm dark mode.

## Who this is for

People who prefer coffee and brown palettes over blue, purple or black themes.

## User need and evidence

A user explicitly requested a coffee/brown theme with gold accents. This is a narrower demand signal than the recurring readability and mobile complaints.

- [Direct coffee and gold palette request](https://www.reddit.com/r/ObsidianMD/comments/1us4sr1/theme_wants/)

The Reddit post was a qualitative signal from the original idea research.

## Planned appearance and features

- Use espresso and warm brown surfaces with clearly separated panels.
- Use cream body text and muted gold for key accents.
- Use complementary restrained colours for links, warnings and code syntax.
- Keep menus, settings, tabs and file navigation consistent with the palette.
- Avoid textured backgrounds and decoration that competes with notes.

## Mode scope

Warm dark mode is primary. A cream light companion is optional future scope.

## Future implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references for later implementation:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

## Acceptance checklist for later implementation

- [ ] Check contrast on brown surfaces, including gold links and small labels.
- [ ] Verify that hover, focus and selected states remain easy to identify.
- [ ] Review code syntax and warnings so gold is not overloaded with conflicting meanings.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Original planning scope

The initial task covered repository creation and this plan. Implementation and submission were deferred.
