@echo off
set/p f1="First File:"
set/p f2="Second File:"
set/p merged="Name of Merged File:"
type %f1% %f2% > %merged%
pause