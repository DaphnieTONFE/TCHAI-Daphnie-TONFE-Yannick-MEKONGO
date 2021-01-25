#!/bin/sh

$data = get-content bd.txt | %{$_ -replace "123","replace"} 
echo $data > tZ.txt