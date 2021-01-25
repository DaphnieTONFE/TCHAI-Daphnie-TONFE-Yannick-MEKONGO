#!/bin/sh

$data = get-content bd.txt | %{$_ -replace "123","100"}
echo $data > tZ.txt