---
layout: page
title: Jekyll Dev Container Setup
nav_exclude: true
---

# Jekyll Dev Container Setup Guide

This guide explains how to use the Dev Container setup for local development of this Jekyll site. A dev container provides a consistent development environment with all the necessary dependencies pre-configured.

## What's Configured

The development container has:

- **Ruby 2.5.9** on Debian Buster
- **Jekyll 3.3.1** with necessary dependencies
- **Bundler 1.17.3** for gem management
- Development tools (git, build-essential, libssl-dev)
- Port forwarding for Jekyll (4000) and LiveReload (35729)

## Using the Dev Container

### Prerequisites

1. [VS Code](https://code.visualstudio.com/)
2. [Docker Desktop](https://www.docker.com/products/docker-desktop)
3. [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) VS Code extension

### Opening the Project in a Dev Container

1. Open this project folder in VS Code
2. VS Code should detect the `.devcontainer/devcontainer.json` file and prompt you to "Reopen in Container"
3. If not prompted, press `F1`, type "Remote-Containers: Reopen in Container" and select it
4. Wait for the container to build (it may take a few minutes the first time)

### Running Jekyll Server

Once inside the dev container:

1. Open a terminal in VS Code (`Terminal > New Terminal`)
2. Run:
   ```bash
   bundle _1.17.3_ exec jekyll serve --livereload
   ```
3. Open your browser to http://localhost:4000

## Dev Container Configuration

The container is configured in the `.devcontainer/devcontainer.json` file. Key components:

```jsonc
{
    "name": "Jekyll (Ruby 2.5 on Buster)",
    "image": "ruby:2.5.9-slim-buster",
    "forwardPorts": [4000, 35729],
    "postCreateCommand": "apt-get update && apt-get install -y git build-essential libssl-dev --no-install-recommends && gem update --system 3.3.26 --no-document && gem install bundler -v 1.17.3 --no-document && gem install public_suffix -v 4.0.7 --no-document && gem install jekyll -v 3.3.1 --no-document && bundle _1.17.3_ install",
    "customizations": {
        "vscode": {
            "extensions": [
                "rebornix.Ruby"
            ]
        }
    }
}
```

## Troubleshooting

### Common Issues

1. **Error about missing kramdown-parser-gfm**:
   Add it to your `massively_jekyll_theme.gemspec` file:
   ```ruby
   spec.add_runtime_dependency "kramdown-parser-gfm", "~> 1.1.0"
   ```
   Then run `bundle _1.17.3_ install` in the container.

2. **Native gem compilation errors**:
   The container should already include `build-essential` and `libssl-dev`. If you add gems with other native dependencies, you may need to install additional libraries.

3. **Port already in use**:
   If port 4000 is already in use on your host machine, modify the Jekyll command to use a different port:
   ```bash
   bundle _1.17.3_ exec jekyll serve --livereload --port 4001
   ```

## Creating/Updating the Dev Container

If you need to create or update the dev container configuration:

1. Create a `.devcontainer` folder in the project root if it doesn't exist
2. Create a `devcontainer.json` file there with the configuration
3. Use VS Code Command Palette (`F1`) and select "Remote-Containers: Rebuild Container"

## Why Use a Dev Container?

- **Consistency**: Ensures the same development environment for everyone
- **Isolation**: Keeps Ruby/Jekyll dependencies separate from your system
- **Portability**: Works the same on any machine with VS Code and Docker
- **Simplicity**: Eliminates "it works on my machine" problems

---

*Note: This setup specifically targets the older Jekyll 3.3.1 version used by this site, which requires specific compatibility considerations.*