### Env

### Create venv
```
python3 -m venv my_env_name
```

### Definir no interpreter do PyCharm como o env criado
> Settings > Project > Python Interpreter > Add Interpreter
> Select Existing > find folder my_env_name

### Habilitar o env no terminal
```
$ source my_env_name/bin/activate
```

### Instalar dependências somente no ENV selecionado
```
$ pip install -r requirements.txt
```

### Sair do env
```
$ deactivate
```

