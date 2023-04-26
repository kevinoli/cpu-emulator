from kevASSEMBLER import assemble
from kevCPUEMU import cpuEmulator


def main():
    # Assemble the asm file
    assemble("kevASM.asm")
    # Run CPU emulation on binary file
    cpuEmulator("kevMC.bin")

main()