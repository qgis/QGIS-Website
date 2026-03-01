# OSGeo Hugo Website

This is the official website for the Open Source Geospatial Foundation (OSGeo), built with Hugo using the hugo-bulma-blocks-theme.

## About OSGeo

The Open Source Geospatial Foundation (OSGeo) is a not-for-profit organization whose mission is to foster global adoption of open geospatial technology by being an inclusive software foundation devoted to an open philosophy and participatory community-driven development.

## Development

### Prerequisites

- Hugo Extended (v0.139.0 or later)
- Nix (recommended for development environment)

### Using Nix

Enter the development environment:

```bash
nix develop
```

### Running Locally

Start the development server:

```bash
hugo server
```

Or using the Makefile:

```bash
make hugo-run-dev
```

Visit http://localhost:1313 to see the site.

### Building

Build the site:

```bash
hugo
```

For production build:

```bash
hugo --config config.toml,config/config.prod.toml
```

## Project Structure

```plaintext
OSGEO-hugo/
├── config.toml           # Main Hugo configuration
├── config/               # Environment-specific configs
├── content/              # Markdown content
│   ├── about/           # About OSGeo pages
│   ├── projects/        # OSGeo project listings
│   ├── community/       # Community pages
│   ├── initiatives/     # FOSS4G, Geo for All, etc.
│   ├── resources/       # Documentation and resources
│   ├── membership/      # Membership information
│   ├── local-chapters/  # Local chapter listings
│   ├── donate/          # Donation page
│   └── sponsors/        # Sponsor listings
├── static/              # Static assets
│   └── img/
│       └── osgeo/       # OSGeo logos and branding
├── themes/              # Hugo theme
│   └── hugo-bulma-blocks-theme/
└── data/                # Data files (JSON, YAML)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for more detailed guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Brand Guidelines

This site uses OSGeo's official branding:

- **Primary Color**: Light Green #4DB05B (Pantone 361 U)
- **Secondary Color**: Dark Teal #003A40 (Pantone 330 U)
- **Fonts**: Miriam Libre (headings), Sintony (body text)

For more information about OSGeo branding, see the [OSGeo Branding Materials](https://www.osgeo.org/about/branding-material/).

## Have Questions?

Have questions or feedback? Feel free to open an issue or submit a Pull Request!

---

Based on the QGIS-Hugo website architecture by Tim Sutton (@timlinux).
