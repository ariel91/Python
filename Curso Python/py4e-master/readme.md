COMO CREAR UN PROYECTO EN GITHUB

1. Crea tu usuario en GITHUB
2. Inicia un nuevo proyecto en GITHUB
	2.1 Cree un nuevo repositorio. github.con/new
	Al continuar, sadran una serie de codigos y un link para el escritorio.
	
	COMO CREAR UN NUEVO REPOSITORIO CON CODIGO EN LA LINEA DE COMANDOS
	echo "# cursoSql" >> README.md
	git init
	git add README.md
	git commit -m "first commit"
	git remote add origin https://github.com/ariel91/cursoSql.git
	git push -u origin master
	
	Empujar un repositorio existende desde la linea de comandos.
	…or push an existing repository from the command line
	git remote add origin https://github.com/ariel91/cursoSql.git
	git push -u origin master
	
	…or import code from another repository
	You can initialize this repository with code from a Subversion, Mercurial, or TFS project.
		
	…or create a new repository on the command line
	echo "# cursoSql" >> README.md
	git init
	git remote add origin https://gitlab.com/ariel91/elearningJava.git
	git add README.md
	git commit -m "first commit"
	git remote add origin git@github.com:ariel91/cursoSql.git
	git push -u origin master
	
	…or push an existing repository from the command line
	git remote add origin git@github.com:ariel91/cursoSql.git
	git push -u origin master
	
	…or import code from another repositorygit 
	You can initialize this repository with code from a Subversion, Mercurial, or TFS project.
	
	Iniciar REPOSITORIO
	==============
	git init
	
	Agregar archivos al Staging Area
	==========================
	git add .
	
	Agregar usuario a configuracion de git
	
	git config --global user.email "arielchitay91@gmail.com"
	git config --global user.name "ariel91"
	
	Hacer commit
	============
	git commit -m "Inicializacion del repositorio (siempre agregar comentario)"
	
	Regresar documentos atras
	===========================
	git checkout + nombreDocumento.extension
	
	Agregar a github desde la linea de comandos.
	git remote add origin https://github.com/ariel91/cursoSql.git
	
	COMO AGREGAR DIRECTAMENTE
	++========================================
	commit -a -m "Actualizar archivo"
	
	git remote add origin https://gitlab.com/ariel91/protocoloTesis.git
	
	RESUMEN PARA ACTUALIZAR
	git init
	git add .
	git remote add origin https://gitlab.com/ariel91/Php.git
	git status
	git commit -a -m "Comentario descriptivo"
	git remote add origin https://gitlab.com/ariel91/elearningJava.git
	git push -u origin master
	Ingreso de usuario y contrasena
	
	link php
    https://gitlab.com/ariel91/Php.git
    
    link protocoloTesis
    git remote add origin https://gitlab.com/ariel91/protocoloTesis.git
    