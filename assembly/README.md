* Last Name: Wong
* First Name: Tiffany

## Async Work #1
- Convert from numeric into mnemonic code: <br>
`901` `INP` <br>
`399` `STA 99` <br>
`901` `INP` <br>
`199` `ADD 99` <br>
`399` `STA 99` <br>
`901` `INP` <br>
`299` `SUB 99` <br>
`902` `OUT` <br>
`000` `HLT` <br>

- Identify what's wrong with the program. <br>
The program solicits for an input value, stores it in memory cell #99, solicits for another input, but doesn't store the second input value anywhere. Instead, the input stored in #99 is added to the accumulator, then the next command is to store that in #99, which doesn't make sense.

- Code to make program work correctly: <br>
`INP` <br>
`STA 90` <br>
`INP` <br>
`STA 91` <br>
`INP` <br>
`STA 92` <br>
`LDA 90` <br>
`ADD 91` <br>
`SUB 92` <br>
`OUT` <br>
`HLT` <br>

## Async Work #2 Mild Version
Write an LMC program that takes two inputs and produces the larger of the two values as an output. <br>

`INP` <br>
`STA 90` <br>
`INP` <br>
`STA 91` <br>
`LDA 90` <br>
`SUB 91` <br>
`BRP 12` <br>
`LDA 91` <br>
`SUB 90` <br>
`LDA 91` <br>
`OUT` <br>
`HLT` <br>
`LDA 90` <br>
`OUT` <br>
`HLT` <br>

## Async Work #2 Medium Version
Write a Little Man program that accepts three values as input and returns the largest of the 3. <br> *Hint*: The pseudo code for this might look as follows:
- read input into addresses M0, M1, M2
- if M1 > M2, replace value in M2 with value in M1
- if M0 > M2, replace value in M2 with value in M0
- output M2<br>

`INP` <br>
`STA 90` <br>
`INP` <br>
`STA 91` <br>
`INP` <br>
`STA 92` <br>
`LDA 90` <br>
`SUB 91` <br>
`BRP 23` <br>
`LDA 92` <br>
`SUB 90` <br>
`BRP 16` <br>
`HLT` <br>
`LDA 92` <br>
`OUT` <br>
`HLT` <br>
`LDA 91` <br>
`SUB 92` <br>
`BRP 27` <br>
`BRA 12` <br>
`LDA 91` <br>
`OUT` <br>
`HLT` <br>
`LDA 90` <br>
`SUB 92` <br>
`BRP 34` <br>
`BRA 9` <br>
`LDA 90` <br>
`OUT` <br>
`HLT` <br>