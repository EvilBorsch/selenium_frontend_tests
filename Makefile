run: # Предварительно засовываем в env пароль (export PASSWORD=твой пароль export LOGIN=твой логин)
	sh node.sh&
	sleep 1
	python run_tests.py

install:
	source ./login_password
	sh grid.sh&