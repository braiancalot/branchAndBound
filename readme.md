# Branch and Bound

</br><h3> Grupo: Braian dos Santos Calot, João Victor Simões Gonçalves e Igor Fracalossi do Nascimento Lozorio.</h3></br>

## Explicação
<h3> 
    Esse programa foi feito utilizando o algoritmo A* como base. Dada uma matriz onde 0 e -1 são células onde não é possível passar, e 1 ou acima indica uma célula onde é possível passar e o custo para passar por ela. O algoritmo encontra o melhor caminho entre uma célula inicial ( START ) e uma célula final ( GOAL ). Neste caso, o caminho encontrado é o de menor custo.
</h3></br>

## Exemplo
<h3>
    0 &nbsp 5 &nbsp 0 &nbsp 0 &nbsp 0 </br> 
    0 &nbsp 2 &nbsp 3 &nbsp 3 &nbsp 0 </br>
    1 &nbsp 0 &nbsp 2 &nbsp 0 &nbsp 7 </br>
    0 &nbsp 4 &nbsp 0 &nbsp 6 &nbsp 0 </br>
    0 &nbsp 1 &nbsp 2 &nbsp 1 &nbsp 2 </br>
    0 &nbsp 1 &nbsp 1 &nbsp 3 &nbsp 0 </br>
</h3></br>

<h3>
     START: &nbsp ( 0, 1 ) </br>
     GOAL:  &nbsp&nbsp ( 5, 3 )
</h3>

</br>

## Caminho encontrado:</br>
<h3>
    ( 0 , 1 ) &nbsp ( 1 , 1 ) &nbsp ( 2 , 0 ) &nbsp ( 3 , 1 ) &nbsp ( 4 , 2 ) &nbsp ( 5 , 3 )
</h3></br>

<h3> 
    Neste programa é possível utilizar as matrizes já definidas bastando escolher o START e GOAL para executar o algoritmo, ou se preferir, é possível criar sua própria matriz para aplicar o algoritmo. 
</h3>
