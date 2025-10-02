#!/bin/bash

# NB-2 Project Startup Script
# This script helps you quickly start the entire NB-2 project stack

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if Docker is running
check_docker() {
    print_status "Checking Docker..."
    if ! docker info >/dev/null 2>&1; then
        print_error "Docker is not running. Please start Docker and try again."
        exit 1
    fi
    print_success "Docker is running"
}

# Function to check if docker-compose is available
check_docker_compose() {
    print_status "Checking Docker Compose..."
    if ! command -v docker-compose >/dev/null 2>&1; then
        print_error "Docker Compose is not installed. Please install Docker Compose and try again."
        exit 1
    fi
    print_success "Docker Compose is available"
}

# Function to setup environment file
setup_env() {
    print_status "Setting up environment..."
    if [ ! -f .env ]; then
        print_warning ".env file not found. Creating from template..."
        cp .env.template .env
        print_warning "Please edit .env file with your API keys before proceeding"
        print_warning "Required: OPENAI_API_KEY and/or GEMINI_API_KEY"
        read -p "Press Enter to continue after editing .env file, or Ctrl+C to exit..."
    else
        print_success "Found existing .env file"
    fi
}

# Function to start core services
start_core_services() {
    print_status "Starting core services (database, server, frontend, telemetry)..."
    docker-compose up -d database server frontend telemetry
    
    print_status "Waiting for services to be healthy..."
    sleep 10
    
    # Check service health
    if docker-compose ps | grep -q "unhealthy"; then
        print_warning "Some services may not be healthy yet. Checking status..."
        docker-compose ps
    else
        print_success "Core services are starting up"
    fi
}

# Function to start optional services
start_ollama() {
    print_status "Starting Ollama service for local LLM inference..."
    docker-compose --profile ollama up -d ollama
    print_success "Ollama service started"
}

# Function to show service URLs
show_urls() {
    echo ""
    print_success "Services are starting up! Access them at:"
    echo ""
    echo -e "  ${BLUE}Frontend (Open WebUI):${NC}     http://localhost:3000"
    echo -e "  ${BLUE}Backend API:${NC}               http://localhost:8000"
    echo -e "  ${BLUE}API Documentation:${NC}        http://localhost:8000/docs"
    echo -e "  ${BLUE}Telemetry (Phoenix):${NC}      http://localhost:6006"
    echo -e "  ${BLUE}Database:${NC}                 localhost:5432"
    if docker-compose ps | grep -q ollama; then
        echo -e "  ${BLUE}Ollama:${NC}                   http://localhost:11434"
    fi
    echo ""
}

# Function to show logs
show_logs() {
    print_status "Showing service logs (Press Ctrl+C to exit log view)..."
    docker-compose logs -f
}

# Function to run tests
run_tests() {
    print_status "Running Ragas evaluation tests..."
    docker-compose --profile testing run --rm testing
    print_success "Tests completed. Check results in testing/results/"
}

# Function to stop all services
stop_services() {
    print_status "Stopping all services..."
    docker-compose down
    print_success "All services stopped"
}

# Function to show status
show_status() {
    print_status "Service status:"
    docker-compose ps
}

# Main menu
show_menu() {
    echo ""
    echo -e "${BLUE}NB-2 Project Management${NC}"
    echo "=========================="
    echo "1. Start core services (database, server, frontend, telemetry)"
    echo "2. Start core services + Ollama"
    echo "3. Show service status"
    echo "4. Show service logs"
    echo "5. Run evaluation tests"
    echo "6. Stop all services"
    echo "7. Exit"
    echo ""
}

# Parse command line arguments
case "${1:-menu}" in
    "start")
        check_docker
        check_docker_compose
        setup_env
        start_core_services
        show_urls
        ;;
    "start-ollama")
        check_docker
        check_docker_compose
        setup_env
        start_core_services
        start_ollama
        show_urls
        ;;
    "test")
        check_docker
        check_docker_compose
        run_tests
        ;;
    "stop")
        stop_services
        ;;
    "status")
        show_status
        ;;
    "logs")
        show_logs
        ;;
    "menu"|*)
        # Interactive menu
        while true; do
            show_menu
            read -p "Choose an option [1-7]: " choice
            case $choice in
                1)
                    check_docker
                    check_docker_compose
                    setup_env
                    start_core_services
                    show_urls
                    ;;
                2)
                    check_docker
                    check_docker_compose
                    setup_env
                    start_core_services
                    start_ollama
                    show_urls
                    ;;
                3)
                    show_status
                    ;;
                4)
                    show_logs
                    ;;
                5)
                    check_docker
                    check_docker_compose
                    run_tests
                    ;;
                6)
                    stop_services
                    ;;
                7)
                    print_success "Goodbye!"
                    exit 0
                    ;;
                *)
                    print_error "Invalid option. Please choose 1-7."
                    ;;
            esac
            echo ""
            read -p "Press Enter to continue..."
        done
        ;;
esac