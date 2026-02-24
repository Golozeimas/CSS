from shutil import make_archive

pasta_para_zipar = input("Coloque o caminho da pasta ou do arquivo (caminho relativo): ")

make_archive("Html_projeto2","zip",pasta_para_zipar) # mais fácil zipar assim com o make_archive do shuti