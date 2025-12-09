load LampController.hdl,
output-file LampController.out,
output-list A%B1.1.1 B%B1.1.1 C%B1.1.1 ONOFF%B3.1.3;
set A 0,
set B 0,
set C 0,
eval,
output;

set A 0,
set B 0,
set C 1,
eval,
output;

set A 0,
set B 1,
set C 0,
eval,
output;

set A 0,
set B 1,
set C 1,
eval,
output;

set A 1,
set B 0,
set C 0,
eval,
output;

set A 1,
set B 0,
set C 1,
eval,
output;

set A 1,
set B 1,
set C 0,
eval,
output;

set A 1,
set B 1,
set C 1,
eval,
output;