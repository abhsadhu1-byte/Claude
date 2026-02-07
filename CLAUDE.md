# CLAUDE.md

This file provides guidance for AI assistants (including Claude Code) working in this repository.

## Repository Overview

- **Name:** Claude
- **Owner:** abhsadhu1-byte
- **Status:** New repository — initial setup phase
- **Remote:** `github.com/abhsadhu1-byte/Claude`

## Project Structure

This is a freshly initialized repository. As the project grows, update this section to reflect the directory layout:

```
Claude/
├── CLAUDE.md                       # AI assistant guidance (this file)
├── image-editing-skill.md          # Image editing, enhancement & appeal skill
└── stock-market-research-skill.md  # Comprehensive stock market research skill
```

## Development Workflow

### Getting Started

1. Clone the repository
2. Check out or create your working branch
3. Install dependencies (once a package manager is configured)

### Branch Conventions

- `main` — stable, production-ready code
- `claude/*` — branches created by Claude Code sessions
- Feature branches should use descriptive names (e.g., `feature/add-auth`, `fix/login-bug`)

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in imperative mood (e.g., "Add", "Fix", "Update", "Remove")
- Keep the subject line under 72 characters
- Add a body for non-trivial changes explaining *why*, not just *what*

### Code Quality

When build tooling is added, document the following commands here:

- **Lint:** `(to be configured)`
- **Format:** `(to be configured)`
- **Test:** `(to be configured)`
- **Build:** `(to be configured)`

## Conventions for AI Assistants

### General Rules

- Read files before modifying them — never assume content
- Prefer editing existing files over creating new ones
- Keep changes minimal and focused on the task at hand
- Do not add unnecessary abstractions, comments, or features beyond what is requested
- Do not introduce security vulnerabilities (injection, XSS, etc.)

### When Adding Dependencies

- Prefer well-maintained, widely-used packages
- Document why a dependency was added
- Avoid adding dependencies for trivial functionality

### When Writing Code

- Follow existing patterns and conventions in the codebase
- Write self-documenting code; add comments only where logic is non-obvious
- Include error handling at system boundaries (user input, external APIs)
- Write tests for new functionality when a test framework is available

### File Organization

- Group related files together
- Use clear, descriptive file and directory names
- Keep configuration files at the project root

## Updating This File

This CLAUDE.md should be kept up to date as the project evolves. When making significant changes to the project structure, build system, or conventions, update the relevant sections here.
