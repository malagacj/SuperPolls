#! /bin/bash

# Variables definition
env="env"
root_folder=`dirname $(dirname $(realpath $0))`

if [ "$1" == "" ]
then
	env_folder=`dirname $root_folder`
	environ=""
else
	env_folder=$root_folder
	environ="$1"
fi


# Functions
removing_old () {
	cd $root_folder
	echo "Getting database name"
	rm db.* */migrations/0*
	rm -rf static media
}

making_migrations () {
	cd $root_folder
	python manage.py makemigrations
}

running_tests () {
	if [ "$environ" == "" ] # Executes in Local only
	then
		cd $root_folder
		python manage.py test
		if [ $? != 0 ]
		then
			echo
			echo TESTS NOT PASSED, STOPING PIPELINE
			exit $?
		fi
	fi
}

initial_setup () {
	cd $root_folder
	#python manage.py import_allergens initial_data/allergens/allergens.csv
	#python manage.py import_dishes initial_data/dishes/dishes.csv

	if [ "$environ" == "" ] || [ "$environ" == "dev" ] # Executes in Local only
	then
		imports="
		from django.contrib.auth import get_user_model;
		User = get_user_model();
		"

		admin=adm
		password=adm
		shell_comd="
		$imports
		user = User.objects.create_superuser(email='admin@admin.com', username='$admin', password='$password');
		user = User.objects.create_superuser(email='plokoon1987@gmail.com', username='froylan', password='froylan');
		"

		cd $root_folder
		echo $shell_comd | python manage.py shell
	fi
}

static_files () {
	cd $root_folder
	scripts/get_static.sh
	if [ "$environ" != "" ] # Executes in other than Local only
	then
		if [ ! -e PiedrasNegras/static ]
		then
			mkdir PiedrasNegras/static
		fi
		python manage.py collectstatic --noinput
	fi
}

. $env_folder/env/bin/activate

removing_old
making_migrations
running_tests
python manage.py migrate
initial_setup
static_files
if [ "$environ" == "" ] # Executes in Local only
then
	python manage.py runserver
fi
