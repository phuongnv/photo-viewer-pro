# Photo Viewer Pro

A Python 3 application for viewing and processing images using OpenCV, with a VS Code Dev Container environment.

## Features

- Python 3.11 with OpenCV
- VS Code Dev Container environment (no docker-compose required)
- Live code mapping via devcontainer mounts (src, requirements.txt, README.md)
- Jupyter notebook support
- Web interface capabilities (Flask)

## Quick Start

### Prerequisites

- Docker
- VS Code + Dev Containers extension

### Development Setup (VS Code Dev Containers)

1. **Clone and open in VS Code:**
   ```bash
   git clone <your-repo-url>
   cd photo-viewer-pro
   ```
2. **Reopen in container:**
   - In VS Code, press `Cmd+Shift+P` (macOS) / `Ctrl+Shift+P` (Windows/Linux)
   - Choose: `Dev Containers: Reopen in Container`
3. **Run the application:**
   ```bash
   # Inside the container terminal
   python src/main.py
   ```

### Development Workflow

The following are bind-mounted into the container:

- `src/` → `/app/src`
- `requirements.txt` → `/app/requirements.txt`
- `README.md` → `/app/README.md`

Changes on the host reflect immediately inside the container.

#### Running a Web Server

```bash
# Inside the container
python -m flask run --host=0.0.0.0 --port=8000
```

Then open `http://localhost:8000` in your browser.

### Project Structure

```
photo-viewer-pro/
├── .devcontainer/
│   ├── Dockerfile          # Image for dev container
│   └── devcontainer.json   # Dev container config (mounts, ports, extensions)
├── requirements.txt        # Python dependencies (mounted)
├── README.md               # This file (mounted)
├── .gitignore
└── src/                    # Source code (mounted)
    ├── __init__.py
    └── main.py
```

### Available Services

- **Port 8000**: Web server (Flask)
- **Port 8888**: Jupyter notebook

### Dependencies

- OpenCV 4.8.1
- NumPy 1.24.3
- Pillow 10.0.1
- Flask 2.3.3 (for web interface)
- Jupyter (for notebook development)
- Matplotlib & Seaborn (for plotting)

### Development Commands

Using VS Code Dev Containers:

```bash
# Open Command Palette (in VS Code): Dev Containers: Reopen in Container
# Rebuild after changing devcontainer.json or Dockerfile
# Command Palette: Dev Containers: Rebuild Container
```

Inside the container terminal:

```bash
# Run the app
python src/main.py

# Install new packages after editing requirements.txt
pip install -r requirements.txt
```

### Adding New Dependencies

1. Add the package to `requirements.txt`
2. Inside the container, run: `pip install -r requirements.txt`
3. If base image changes are needed, use Command Palette: `Dev Containers: Rebuild Container`

### Troubleshooting

- If you encounter permission issues, ensure Docker Desktop is running and VS Code has access
- To rebuild after config changes, use: `Dev Containers: Rebuild Container`
- For OpenCV GUI issues, ensure proper display forwarding if needed

## Contributing

1. Make your changes in the `src/` directory
2. Test your changes in the Docker environment
3. Commit and push your changes

The development environment ensures consistency across different machines and makes it easy to onboard new developers.
