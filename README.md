# Wei-Yao Wang — Academic Website

Personal academic website built with [HugoBlox Academic CV](https://github.com/HugoBlox/hugo-theme-academic-cv) (Hugo).

Live site: https://wywyWang.github.io

## Local preview

Requirements: [Hugo Extended](https://gohugo.io/installation/) (≥ 0.162), Node.js ≥ 22.15 (22.17 recommended), pnpm.

```bash
pnpm install
hugo server
```

Open http://localhost:1313/

GitHub Actions builds and deploys on every push to `master` (Hugo 0.162 + Node 22.17).

## Edit content

| What | Where |
| --- | --- |
| Bio, education, experience, awards | [`data/authors/me.yaml`](data/authors/me.yaml) |
| Homepage sections | [`content/_index.md`](content/_index.md) |
| Experience page | [`content/experience.md`](content/experience.md) |
| Publications | [`content/publications/*/index.md`](content/publications/) |
| Avatar | [`assets/media/authors/me.png`](assets/media/authors/me.png) |
| Site identity / theme | [`config/_default/params.yaml`](config/_default/params.yaml) |

To regenerate publication stubs from the helper script:

```bash
python3 scripts/generate_publications.py
```

## Deploy (GitHub Pages)

Pushes to `master` (or `main`) trigger [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

One-time GitHub repo setting:

1. **Settings → Pages → Build and deployment → Source**: GitHub Actions

The old Jekyll site is preserved on branch `jekyll-archive`.
