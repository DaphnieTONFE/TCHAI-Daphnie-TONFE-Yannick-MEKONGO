#!/bin/sh

$data = get-content bd.txt | %{$_ -replace "222","434"} 
echo $data > bd.txt