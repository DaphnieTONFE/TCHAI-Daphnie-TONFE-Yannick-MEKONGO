#!/bin/sh

$data = get-content bd.txt | %{$_ -replace "434","43"}
echo $data > bd.txt