
#!/bin/bash
for ((i=1;i<=100;i++)); do
    if ! ((i%15)); then
        echo AVAAMO
    elif ! ((i%3)); then
        echo AVA
    elif ! ((i%5)); then
        echo AMO
    else
        echo $i
    fi;
done

