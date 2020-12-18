#!/bin/bash

for SAMPLE in 09 11 23 24 27 31 35 39 62 62
do
  bwa mem -t 4 -R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" -o ${SAMPLE}.sam sacCer3.fa A01_${SAMPLE}.fastq
  samtools sort -o ${SAMPLE}_sorted.bam ${SAMPLE}.sam
done
