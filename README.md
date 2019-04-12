# Multifunction Calculator
This project was made for the course of Design and Analysis of Algorithms in the Federal Universtity of Alagoas

Members:  
  Luiz Antônio  
  Jonathas Silva  
  Nilson Sales  


### Functionalities

This calculator can handle numeric and matrix opperations.

For numeric opperations, we support the following opperations:
- Sum of big numbers
- Subtraction of big numbers
- Multiplication of big numbers
- Division of big numbers
- nth root of a number (non linear)
- Exponentiation (non linear)

For matrices:
- Matrix chain multiplication

### Running

Run the Main funcion
```console
$ python Main.py
```

Choose the type of operation:
- Numeric
- Matrix

#### Numeric:  

Fo numeric opperations, the input must have the following structure:  
first_number **opperator** second_number

You can see the list of opperators bellow

|  opperators | function  |
|:-:|:-:|
| +  | addition  |
| -  | subtration  |
| *  | multiplication  |
| /  | division  |
|root| nth root  |
| ^  |  exponentiation |

P.S.: '64 root 2' means the square root of 64.

#### Matrix opperation:  

For matrix multiplication, it'll ask for some informations before you enter the actual matrix.  

1st - Enter the numer of matrices to multiply
2nd - Enter the size of the matrix: lines[space]columns (Ex: 3 4)
3rd - Enter the matrix, line by line, with the elements split by space (Ex: 1 2 3 4)

### Examples:
- inputs:  
1  
1234567890 + 98764321  
1  
450 ^ 12  
1  
64 root 3  

- outputs:  
1333332211  
68952523554931640625000000000000  
4.0  


- inputs:  
2  
3  
1 2  
7 8  
2 3  
1 2 3  
4 5 6  
3 4  
4 3 2 1  
6 5 4 3  
7 6 5 4  

- outputs:  

