# Photo Viewer Pro

A Python 3 application for viewing and processing images using OpenCV, with Docker development environment.

## Features

- Python 3.11 with OpenCV
- Docker development environment
- Live code reloading with volume mapping
- Jupyter notebook support
- Web interface capabilities (Flask)

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Development Setup

1. **Clone and navigate to the project:**
   ```bash
   git clone <your-repo-url>
   cd photo-viewer-pro
   ```

2. **Build and start the development environment:**
   ```bash
   docker-compose up --build
   ```

3. **Access the development container:**
   ```bash
   docker-compose exec photo-viewer-dev bash
   ```

4. **Run the application:**
   ```bash
   # Inside the container
   python src/main.py
   ```

### Development Workflow

The `src/` directory is mapped to the container, so any changes you make to files in `src/` will be immediately reflected in the container.

#### Running Jupyter Notebook

```bash
# Inside the container
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

Then open `http://localhost:8888` in your browser.

#### Running a Web Server

```bash
# Inside the container
python -m flask run --host=0.0.0.0 --port=8000
```

Then open `http://localhost:8000` in your browser.

### Project Structure

```
photo-viewer-pro/
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Development environment
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── src/                   # Source code (mapped to container)
    ├── __init__.py
    └── main.py            # Main application entry point
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

```bash
# Build the container
docker-compose build

# Start the development environment
docker-compose up

# Run in background
docker-compose up -d

# Stop the environment
docker-compose down

# Rebuild and start
docker-compose up --build

# Access container shell
docker-compose exec photo-viewer-dev bash

# Run Python scripts
docker-compose exec photo-viewer-dev python src/main.py

# Install new packages
docker-compose exec photo-viewer-dev pip install <package-name>
```

### Adding New Dependencies

1. Add the package to `requirements.txt`
2. Rebuild the container: `docker-compose up --build`

### Troubleshooting

- If you encounter permission issues, make sure Docker has proper permissions
- If the container doesn't start, check the logs: `docker-compose logs`
- For OpenCV GUI issues, ensure you're running with proper display forwarding if needed

## Contributing

1. Make your changes in the `src/` directory
2. Test your changes in the Docker environment
3. Commit and push your changes

The development environment ensures consistency across different machines and makes it easy to onboard new developers.
