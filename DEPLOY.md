# Deploy Shreyash's GitHub Profile V4 (dynamic statistics)

The account is **Yashuuuu02**. The whole repository ZIP is intended for a public repository named `Yashuuuu02/Yashuuuu02`.

## Publish

1. Create that public profile repository if it does not exist. Use **main** as the default branch.
2. Upload **README.md**, the whole `assets/` directory, `scripts/`, and `.github/workflows/`. **Do not omit hidden `.github`!**
3. Commit to `main` and visit https://github.com/Yashuuuu02.
4. The large stats, language, streak and activity-graph cards in README use live SVG URLs: **no setup or API keys required**. They request this user's actual public GitHub data and use provider caches.
5. For reliable **self-hosted backup cards**, the supplied Actions workflow runs on this README's first push (if `main` is default), twice daily and on demand. In **Actions → Refresh GitHub profile statistics**, you can choose **Run workflow** manually.
6. If the workflow is blocked from committing, in **Settings → Actions → General → Workflow permissions** grant read/write if your GitHub policy permits it, or adjust repo rules. You may have to enable Actions first.

## What updates automatically?

| Component | Origin | Refresh |
| --- | --- | --- |
| GitHub stats (commits, stars, PRs, issues) | GitHub Stats Extended + GitHub API | Whenever fetched after provider cache expires |
| Top languages | GitHub Stats Extended + GitHub API | Provider-cached; subject to upstream data refresh |
| Streaks / contribution totals | Streak Stats + GitHub contribution graph | Provider-cached |
| Contribution activity graph | github-readme-activity-graph + GitHub activity | Provider-cached |
| `assets/github-stats.svg` and `assets/top-langs.svg` | GitHub Stats Extended Action + GitHub API | Push to main / 03:23 & 15:23 UTC daily / manual |
| `assets/metrics.svg` | GitHub REST public repo data | Same GitHub Actions workflow |

## Important limits

- **No numbers are manually set in live widgets**; the username is the only identity input. Old screenshots/previews cannot animate or retrieve new data.
- GitHub README Markdown is static. Live SVG widgets query GitHub behind the scenes; they can be cached, rate-limited or briefly offline. They are *not instantaneous* on every page load.
- `include_all_commits=true` attempts all-time author commits on public data. **Commit count is not the same as total contributions** and can differ from GitHub's account dashboard due to authorship rules, API scopes and caches.
- The hosted widgets and default workflow show public data. To include private repo stats, you need an appropriately scoped personal access token configured privately; do not commit any token in README, asset URLs, or code.
- Top languages are **estimated repository code volume**, not personal skills; org-owned repositories generally are not in owned-language totals.
- The backup SVGs initially read 'SYNC PENDING'. This is intentional and *not a fake metric*. When the Actions workflow completes, they are replaced with actual API-generated cards.
- The main card provider is the actively maintained GitHub Stats Extended successor; it supersedes the old github-readme-stats Vercel instance.

## Sources / providers

- https://github.com/stats-organization/github-stats-extended
- https://github.com/stats-organization/github-readme-stats-action
- https://github.com/DenverCoder1/github-readme-streak-stats
- https://github.com/Ashutosh00710/github-readme-activity-graph

All other project artwork is stored under `assets/` and remains independent of third-party services.
