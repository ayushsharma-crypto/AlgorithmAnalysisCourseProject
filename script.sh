#!/bin/bash

arr=(1.Introduction 2.Tic-Tac-Toe 3.Crime-Detection 4.MST 5.Compression 6.Face-Recog) 
list=(1.Slides 2.Program)
v1=1
v2=2
while [ "1" ]; do
	for i in ${arr[@]};do
		echo $i
	done
	read inp
	clear
	if [ $inp -eq $v1 ]
	then
		xdg-open ./Slides/Introduction.pptx
		continue
	elif [ $inp -ge 7 ]
	then
		echo "Incorrect option, try again"
		continue
	fi
	for i in ${list[@]};do
                echo $i
        done
	read inpsub
	clear
	case $inp in
		2) if [ $inpsub -eq $v1 ]
		then
			xdg-open ./Slides/TTT.pptx
		elif [ $inpsub -eq $v2 ]
		then
			python3 Tic-Tac-Toe/ttt.py
		else
			echo "incorrect option, try again"
		fi
			;;
		3)	if [ $inpsub -eq $v1 ]
		then
			xdg-open ./Slides/CrimeAlgo.pptx
		elif [ $inpsub -eq $v2 ]
		then
			python3 Crime-Algo/suspect_v1.py
		else
			echo "incorrect option, try again"
		fi
			;;
		4)	if [ $inpsub -eq $v1 ]
		then
			xdg-open ./Slides/MST.pptx
		elif [ $inpsub -eq $v2 ]
		then
			python3 MST/mst.py
		else
			echo "incorrect option, try again"
		fi
			;;
		5) if [ $inpsub -eq $v1 ]
		then
			xdg-open ./Slides/Compression.pptx
		elif [ $inpsub -eq $v2 ]
		then
			cd Compression/LZW-Compressor-in-Python
			ls -l
			python3 encoder.py sampleIn
			python3 decoder.py sampleIn.lzw
			ls -l
			diff -s sampleIn sampleIn_decoded.txt
			cd ../../
		else
			echo "incorrect option, try again"
		fi
			;;
		6) if [ $inpsub -eq $v1 ]
		then
			xdg-open ./Slides/FaceRec.pptx
		elif [ $inpsub -eq $v2 ]
		then
			cd FaceRec
			python3 faces-train.py 
			python3 faces.py 
			cd ../
		else
			echo "incorrect option, try again"
		fi
			;;
		*)
			echo "invalid option, try again"
			;;
	esac
done
	
		

