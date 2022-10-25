

. ./vars.sh

name="Champ"
age=41
surname="Pitts"


every() {

	all=($name $age $surname)

	for i in ${all[@]}
	do
		echo $i
	done
}


every


echo $HOSTN
echo $NAME
echo $kernel
