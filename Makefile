hello:
	~ echo "hello world"

migrate:
	~ python practice/manage.py makemigrations practice
	~ python practice/manage.py migrate
