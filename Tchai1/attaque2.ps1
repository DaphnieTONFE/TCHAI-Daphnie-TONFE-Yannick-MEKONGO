#!/bin/sh

$lines= get-content bd.txt
$first = $lines[2]
$lines | where {$_ -ne $first } | Set-Content bd.txt