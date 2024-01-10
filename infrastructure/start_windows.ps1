# Check if docker-compose is installed
if (-not (Test-Path "$env:ProgramFiles\Docker\docker-compose.exe")) {
    Write-Error "Error: docker-compose is not installed. Please install it before running this script."
    exit 1
}

# Run docker-compose up
& "$env:ProgramFiles\Docker\docker-compose.exe" up -d