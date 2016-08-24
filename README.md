py-petridish
========

sandbox for composing and simulating spatial environments with evolving cells that must consume resources to survive and reproduce

## Description

I am working on completing a first useful prototype. A simple animation of random-behavior cells can be seen in 'randomCells.py'.

The aim of this project is to allow construction of highly composable spatial environments and cells that react to said environments such that the cells naturally evolve. The basic ingredients I hope to implement for such an environment are resource consumption, cell reproduction, and cell death. Also, cells need some mechanism of mutating their offspring and reacting to stimulus.

At some point, I would like to implement a cell with a neural network. I also want to parallelize cells' reactions so that multiple cells can make decisions simultaneously.

## Dependencies

matplotlib - graphing library, only needed to run visual demos

## License

The MIT License (MIT)
Copyright (c) 2016 Chase Bowers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
