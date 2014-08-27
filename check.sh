FILE="README.md" # file output from program is written to 
PID=1 # process id can be found using 'ps -fu user'  


# search for string in file 
myString="finished"
finished=`grep $myString $FILE`

if [[ -n $finished ]]; then 
	kill $PID 
fi 


