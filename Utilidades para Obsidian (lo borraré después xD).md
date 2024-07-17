$$
\newcommand{\bm}[1]{\boldsymbol{#1}}
$$$$\bm{x} = \begin{bmatrix} r_x & r_y \end{bmatrix}$$Matriz vertical:
$$\begin{bmatrix} a_{11} \\ a_{21} \\ a_{31} \\ \end{bmatrix}$$Matriz horizontal:
$$\begin{bmatrix} a_{11} & a_{12} & a_{13} \end{bmatrix}$$Bloques de código:

```python
a = 10
b = 5
print(a+b)
```

Bloque de pseudocódigo:

```pseudo
    \begin{algorithm}
    \caption{Biseccion}
    \begin{algorithmic}
      \Procedure{Biseccion}{$a, b, f, \text{TOL}$}
        \While{($\frac{b-a}{2} < \text{TOL}$)}
        \EndWhile
      \EndProcedure
      \Procedure{Partition}{$A, p, r$}
        \State $x \gets A[r]$
        \State $i \gets p - 1$
        \For{$j \gets p$ \To $r - 1$}
          \If{$A[j] < x$}
            \State $i \gets i + 1$
            \State exchange
            $A[i]$ with $A[j]$
          \EndIf
        \State exchange $A[i]$ with $A[r]$
        \EndFor
      \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```

