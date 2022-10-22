# homemade-CPU
Designing CPU for fun. A simple 8-bit harvard architecture with 12-bit instructions, 8-bit datapath, 2x8-bit input interface and 2x8-bit output registers. Connected to the TTY and keyboard with a simple interactive "shell-like" program loaded into ROM. Currently has 13 instructions that were the bare minimum to implement the "shell-like" program. There is a room in instruction decoder for 3 more instruction, which I may or may not add in the future.

**Current state**: It's fully implemented. With a shell-like joke program hardcoded into the ROM.

# How to use it
The CPU is designed and simulated with a digital design tool called Logisim:
http://www.cburch.com/logisim/


#### The diagram:
![Schematic](/CPU_schematic.png "Schematic")

# TODO
* Would like to implement an assembler for this ISA
* Replace some builtin Logisim components with discrete logic
* Maybe extend ROM adressing for few more bits for executing more than 256 instruction (leave that for the next CPU design?)
