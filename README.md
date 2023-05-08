# homemade-CPU
Designed a CPU for fun (and to learn by doing it)

This is an 8-bit CPU, but my goal is to eventually implement RISC-V RV32I CPU. I'm also developing an OS for it. Why am I doing this? I really like to know how all this stuff works, and I've noticed that "learning by doing" is (at least for me) the best way to truly understand something. So when I want to know how something works, I recreate it.

**Current state**:  
It's fully implemented and connected to the virtual TTY and keyboard. With a shell-like joke program hardcoded into the ROM.

# CPU architecture
A simple 8-bit Harvard architecture with 12-bit instructions, 8-bit data-path, 2x8-bit input interface and 2x8-bit output registers. Connected to the TTY and keyboard with a simple interactive "shell-like" program loaded into ROM. Currently has 13 instructions that were the bare minimum to implement the "shell-like" program. There is room in the instruction decoder for 3 more instructions, which I may or may not add in the future.

The CPU does not have an adder. Instead, it just has NAND instruction for doing NAND operation on two registers.

The CPU is designed and simulated with a digital design tool called Logisim:
http://www.cburch.com/logisim/

# How to use it

1. Download the Logisim -> http://www.cburch.com/logisim/download.html
2. Open Logisim and load the file "CPU_design.circ"
3. In the "Simulate" menu click on "Tics enabled" (this will start the clock signal of the CPU)
4. Click on "Keyboard" element bellow the "Keyboard input" label
5. Type "help" and press enter. On TTY you will see the response from the code in ROM that is being executed by CPU

#### The diagram:
![Schematic](/CPU_schematic.png "Schematic")

# TODO
* Would like to implement an assembler for this ISA
* Replace some builtin Logisim components with discrete logic
* Maybe extend ROM addressing for few more bits for executing more than 256 instruction (leave that for the next CPU design?)
