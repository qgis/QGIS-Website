# List available recipes
default:
    @just --list

# Alter tailor swatches
alter:
    @tailor alter

# Check what tailor would change and measure
measure:
    @tailor baste
    @tailor measure
