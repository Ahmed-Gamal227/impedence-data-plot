import numpy as np
import matplotlib.pyplot as plt

# Function to load data from the .dat file
def load_data(file_path):
    try:
        # Skip the header row
        data = np.loadtxt(file_path, skiprows=1)
        frequency = data[:, 0]  # First column: Frequency
        real_impedance = data[:, 1]  # Second column: Real Impedance (Z')
        imag_impedance = data[:, 2]  # Third column: Imaginary Impedance (Z'')
        return frequency, real_impedance, imag_impedance
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None, None

# Function to plot Nyquist plot
def plot_nyquist(real, imag):
    plt.figure("Nyquist Plot")
    plt.plot(real, -imag, 'o-', label='Nyquist Plot')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.xlabel(r"Real Impedance ($Z'$) [$\Omega$]")
    plt.ylabel(r"Imaginary Impedance ($-Z''$) [$\Omega$]")
    plt.title("Nyquist Plot")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.axis('equal')

# Function to plot Bode magnitude plot
def plot_bode_magnitude(frequency, real, imag):
    magnitude = np.sqrt(real**2 + imag**2)
    plt.figure("Bode Plot - Magnitude")
    plt.semilogx(frequency, 20 * np.log10(magnitude), 'o-', label='Magnitude')
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude [dB]")
    plt.title("Bode Plot - Magnitude")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

# Function to plot Bode phase plot
def plot_bode_phase(frequency, real, imag):
    phase = np.arctan2(imag, real) * 180 / np.pi
    plt.figure("Bode Plot - Phase")
    plt.semilogx(frequency, phase, 'o-', label='Phase', color='orange')
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Phase [Degrees]")
    plt.title("Bode Plot - Phase")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

# Main script
file_path = r"d:\MyProjects\Vs-Code\Python\imp.dat"  # Full path to your file

# Load data from the file
frequency, real_impedance, imag_impedance = load_data(file_path)

if frequency is not None:
    # Create all three plots
    plot_nyquist(real_impedance, imag_impedance)
    plot_bode_magnitude(frequency, real_impedance, imag_impedance)
    plot_bode_phase(frequency, real_impedance, imag_impedance)
    
    # Display all plots
    plt.show()
else:
    print("Could not load data. Please check the file format.")
